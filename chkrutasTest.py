import requests
import json
import gpxpy
import gpxpy.gpx


class RutaGenerator:
    def __init__(self, ruta_file_path):
        self.ruta_file_path = ruta_file_path

    def load_ruta_points(self):
        # Lee los puntos desde el archivo .ruta
        with open(self.ruta_file_path, 'r') as ruta_file:
            ruta_data = json.load(ruta_file)
            return ruta_data["puntos"]

    def generate_route(self):
        waypoints_string = ""
        n = 0
        ruta_points = self.load_ruta_points()
        for punto in ruta_points:
            # print(punto[0])
            waypoints_string += f"{punto[0]},{punto[1]};"
            '''waypoints = [
            f"{point['latitude']},{point['longitude']}" for point in ruta_points]'''
            n = n+1
            if n == 2:
                break

        # Realiza una solicitud a la API de OpenStreetMap para generar la ruta
        url = f"http://router.project-osrm.org/route/v1/driving/{waypoints_string}"
        print(url[:-1])
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            route_data = response.json()
            return route_data
        else:
            raise Exception(
                "Error al obtener la ruta desde la API de OpenStreetMap")

    def calculate_distance(self):
        route_data = self.generate_route()
        if "routes" in route_data and route_data["routes"]:
            # La distancia se devuelve en metros, convertimos a kilómetros
            distance = route_data["routes"][0]["distance"] / 1000
            return distance
        else:
            raise Exception("No se pudo calcular la distancia")


if __name__ == "__main__":
    ruta_file_path = "NK-FI-01.ruta"
    ruta_generator = RutaGenerator(ruta_file_path)

    try:
        distance = ruta_generator.calculate_distance()
        print(
            f"Distancia desde el último punto hasta el primero: {distance:.2f} km")
    except Exception as e:
        print(f"Error: {str(e)}")
