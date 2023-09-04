import requests
import json

body = {"coordinates": [[8.681495, 49.41461], [
    8.686507, 49.41943], [8.687872, 49.420318]]}

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '5b3ce3597851110001cf6248270d5b828ec94d80832f7a8259b16571',
    'Content-Type': 'application/json; charset=utf-8'
}
call = requests.post(
    'https://api.openrouteservice.org/v2/directions/cycling-road', json=body, headers=headers)

print(call.status_code, call.reason)
print(call.json()["routes"][0]["summary"]["distance"])
