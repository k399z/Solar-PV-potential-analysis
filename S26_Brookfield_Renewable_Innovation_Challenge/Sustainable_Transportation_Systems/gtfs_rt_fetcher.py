# Fetches real-time GTFS-RT vehicle positions from the Region of Waterloo's open data API for a live snapshot of active transit IDs, route assignments, and GPS coordinates
# pip install gtfs-realtime-bindings protobuf requests
import requests
import ssl
from urllib3.util import create_urllib3_context
from google.transit import gtfs_realtime_pb2
import time

# --- SSL Adapter for Waterloo Region API ---
class LegacySSLAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context()
        context.set_ciphers("DEFAULT@SECLEVEL=1")
        kwargs["ssl_context"] = context
        return super().init_poolmanager(*args, **kwargs)

# --- GTFS-RT VehiclePositions feed ---
URL = "https://webapps.regionofwaterloo.ca/api/grt-routes/api/vehiclepositions"

ION_ROUTE_IDS = {"301", "302"}  # 302 appears occasionally for testing/special service


def fetch_all_transit():
    """Fetches all active GRT buses + ION trains with GPS coordinates."""
    feed = gtfs_realtime_pb2.FeedMessage()
    session = requests.Session()
    session.mount("https://", LegacySSLAdapter())

    try:
        response = session.get(URL, timeout=15)
        response.raise_for_status()
        feed.ParseFromString(response.content)

        global_ts = feed.header.timestamp or int(time.time())
        vehicles = []

        for entity in feed.entity:
            if not entity.HasField("vehicle"):
                continue

            v = entity.vehicle
            route = v.trip.route_id or "N/A"

            # Identify mode
            if route in ION_ROUTE_IDS:
                v_type = "ION Train"
            else:
                v_type = "Bus"

            # Some feeds omit timestamps
            ts = v.timestamp if v.timestamp != 0 else global_ts

            vehicles.append({
                "type": v_type,
                "id": v.vehicle.id,
                "route": route,
                "lat": v.position.latitude,
                "lon": v.position.longitude,
                "bearing": getattr(v.position, "bearing", None),
                "speed": getattr(v.position, "speed", None),
                "ts": ts
            })

        return vehicles

    except Exception as e:
        print(f"Error fetching GTFS-RT: {e}")
        return []


if __name__ == "__main__":
    data = fetch_all_transit()

    print(f"{'TYPE':<10} | {'ID':<6} | {'ROUTE':<6} | {'COORDINATES'}")
    print("-" * 60)

    for v in data:
        print(f"{v['type']:<10} | {v['id']:<6} | {v['route']:<6} | "
              f"({v['lat']:.5f}, {v['lon']:.5f})")

    print(f"\nTotal vehicles tracked: {len(data)}")