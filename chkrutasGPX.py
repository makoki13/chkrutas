import gpxpy
import gpxpy.gpx
import json


class ChkRutasGPS:
    @staticmethod
    def read_gpx_file(file_path):
        # Lee el archivo GPX y devuelve un objeto GPXTrack
        with open(file_path, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
        return gpx.tracks[0]

    @staticmethod
    def create_ruta_json(gpx_track, intervalo_metros, output_file):
        ruta_data = {
            "file_name": output_file,
            "last_point_distance": 0,
            "points": []
        }

        distancia_acumulada = 0
        distancia_total = 0
        distancia = 0
        datos = {
            "fichero": output_file,
            "distancia": 0,
            "puntos": []
        }
        lista_puntos = []

        for i in range(len(gpx_track.segments)):
            segment = gpx_track.segments[i]
            # print(segment)
            for j in range(len(segment.points)):
                punto = segment.points[j]
                # print(punto.latitude)
                if not lista_puntos:
                    lista_puntos.append(
                        (punto.latitude, punto.longitude))
                    punto_anterior = punto
                else:
                    # Calcula la distancia desde el punto anterior
                    distancia = punto.distance_2d(punto_anterior)
                    distancia_acumulada += distancia
                    # print(f"distancia {distancia_acumulada}")

                # Agrega el primer punto o puntos en el intervalo especificado
                if distancia_acumulada >= intervalo_metros:
                    # print(f"entra")
                    distancia_total += distancia_acumulada
                    # print(
                    #    f"{j} --> {distancia} {distancia_acumulada} {distancia_total}")
                    lista_puntos.append(
                        (punto.latitude, punto.longitude))
                    distancia_acumulada = 0
                punto_anterior = punto

        # Almacena la distancia del último punto
        # ruta_data["last_point_distance"] = distancia_acumulada

        # Escribe los datos en un archivo JSON
        datos["puntos"] = lista_puntos
        datos["distancia"] = distancia_total
        with open(output_file, 'w') as ruta_file:
            json.dump(datos, ruta_file, indent=4)


if __name__ == "__main__":
    gpx_file_path = "NK-FI-01.gpx"
    intervalo_metros = 1000  # Cambia esto al intervalo deseado
    import os
    output_file_path = os.path.splitext(gpx_file_path)[0] + ".ruta"

    gpx_track = ChkRutasGPS.read_gpx_file(gpx_file_path)
    ChkRutasGPS.create_ruta_json(gpx_track, intervalo_metros, output_file_path)
    print(f"Archivo .ruta.json generado: {output_file_path}")
