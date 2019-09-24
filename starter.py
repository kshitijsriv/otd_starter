from google.transit import gtfs_realtime_pb2
import requests


API_URL = "https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key=API_KEY"
feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get(API_URL)
feed.ParseFromString(response.content)
for entity in feed.entity:
    vehicle_id = entity.vehicle.vehicle.id
    vehicle_lat = entity.vehicle.position.latitude
    vehicle_lon = entity.vehicle.position.longitude
    vehicle_route_id = entity.vehicle.trip.route_id
    vehicle_timestamp = entity.vehicle.timestamp
    print(entity)