import requests
from google.transit import gtfs_realtime_pb2
import pandas as pd

# METRO Houston's real-time vehicle tracking URL
url = "https://www.ridemetro.org/MetroWebServices/TrainBusPositions.aspx"

# Fetch the real-time bus data
response = requests.get(url)
feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(response.content)

# Process data
bus_data = []
for entity in feed.entity:
    if entity.HasField("vehicle"):
        vehicle = entity.vehicle
        bus_data.append({
            "Route": vehicle.trip.route_id,
            "Latitude": vehicle.position.latitude,
            "Longitude": vehicle.position.longitude,
            "Bearing": vehicle.position.bearing,
            "Speed (m/s)": vehicle.position.speed,
            "Timestamp": vehicle.timestamp
        })

# Convert to DataFrame and show results
df = pd.DataFrame(bus_data)
print(df)
