"""Query Google Solar API buildingInsights for CLV buildings.

Setup:
  1. console.cloud.google.com -> create project -> enable "Solar API" -> create API key
  2. export GOOGLE_MAPS_API_KEY=...   (never commit the key)
  3. .venv/bin/python solar_api_clv.py

Add one (lat, lng) per CLV building below: right-click the building in
Google Maps -> the coordinates appear at the top of the context menu.
findClosest snaps to the nearest building, so a point anywhere on the
roof works. Duplicate points that snap to the same building are deduped.
"""

import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

# 46 CLV building centers, found by sweeping a ~30 m grid over the village
# bounding polygon and deduplicating buildingInsights responses (2026-07-04).
# Sorted by roof area, largest first.
POINTS = [
    (43.47077, -80.56249), (43.47069, -80.56007), (43.47060, -80.55997),
    (43.46993, -80.56258), (43.46975, -80.56347), (43.47054, -80.56089),
    (43.46985, -80.56188), (43.47050, -80.56150), (43.46931, -80.56304),
    (43.46957, -80.56376), (43.47026, -80.56215), (43.46925, -80.56373),
    (43.47009, -80.56122), (43.47028, -80.56242), (43.47074, -80.56099),
    (43.47044, -80.56146), (43.47011, -80.56273), (43.47071, -80.56114),
    (43.47014, -80.56212), (43.47026, -80.56250), (43.47067, -80.56137),
    (43.46953, -80.56323), (43.47013, -80.56266), (43.46967, -80.56335),
    (43.47006, -80.56201), (43.47029, -80.56072), (43.47069, -80.56121),
    (43.47025, -80.56134), (43.47035, -80.56136), (43.46952, -80.56378),
    (43.46962, -80.56332), (43.46969, -80.56241), (43.47113, -80.56470),
    (43.47138, -80.56354), (43.47038, -80.56082), (43.47127, -80.56416),
    (43.47132, -80.56392), (43.47143, -80.56309), (43.46979, -80.56244),
    (43.47129, -80.56403), (43.47133, -80.56386), (43.47119, -80.56446),
    (43.47122, -80.56435), (43.47117, -80.56490), (43.47115, -80.56463),
    (43.47114, -80.56486),
]

OUT_DIR = Path(__file__).parent / "solar_api_responses"
API = "https://solar.googleapis.com/v1/buildingInsights:findClosest"


def fetch(lat: float, lng: float, key: str) -> dict:
    q = urllib.parse.urlencode({
        "location.latitude": f"{lat:.6f}",
        "location.longitude": f"{lng:.6f}",
        "requiredQuality": "HIGH",
        "key": key,
    })
    with urllib.request.urlopen(f"{API}?{q}", timeout=30) as r:
        return json.load(r)


def main() -> None:
    key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not key:
        sys.exit("Set GOOGLE_MAPS_API_KEY first")

    OUT_DIR.mkdir(exist_ok=True)
    seen = {}
    for lat, lng in POINTS:
        try:
            b = fetch(lat, lng, key)
        except urllib.error.HTTPError as e:
            print(f"({lat}, {lng}): HTTP {e.code} - {e.read().decode()[:200]}")
            continue
        center = b["center"]
        bid = f"{center['latitude']:.6f},{center['longitude']:.6f}"
        if bid in seen:
            print(f"({lat}, {lng}): duplicate of building at {bid}, skipped")
            continue
        seen[bid] = b
        (OUT_DIR / f"building_{bid}.json").write_text(json.dumps(b, indent=2))

    total_area = total_panels = total_kwh = 0.0
    for bid, b in seen.items():
        sp = b["solarPotential"]
        roof = sp["wholeRoofStats"]["areaMeters2"]
        sun = sp["maxSunshineHoursPerYear"]
        panels = sp["maxArrayPanelsCount"]
        best = max(sp["solarPanelConfigs"], key=lambda c: c["panelsCount"])
        kwh = best["yearlyEnergyDcKwh"]
        total_area += roof
        total_panels += panels
        total_kwh += kwh
        print(f"\nBuilding {bid}")
        print(f"  roof area:          {roof:8.0f} m2")
        print(f"  max sunshine:       {sun:8.0f} h/yr")
        print(f"  max panels:         {panels:8d}")
        print(f"  max config yield:   {kwh:8.0f} kWh DC/yr")
        for seg in sp["roofSegmentStats"][:6]:
            print(f"    segment: {seg['stats']['areaMeters2']:6.0f} m2, "
                  f"pitch {seg.get('pitchDegrees', 0):4.1f} deg, "
                  f"azimuth {seg.get('azimuthDegrees', 0):5.1f} deg")

    print(f"\n=== CLV totals ({len(seen)} buildings) ===")
    print(f"  roof area:  {total_area:9.0f} m2")
    print(f"  max panels: {total_panels:9.0f}")
    print(f"  max yield:  {total_kwh:9.0f} kWh DC/yr")
    print(f"\nRaw responses saved to {OUT_DIR}/")


if __name__ == "__main__":
    main()
