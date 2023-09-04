from chkrutasGPX import ChkRutasGPS
from chkrutasTest import RutaGenerator


def conv_metros_a_kilometros(metros):
    return "{:.2f}".format(metros / 1000)


def genera_fichero_ruta(gpx_file_path, intervalo_metros=2000, add_last=True):
    # gpx_file_path = "NK-FI-01.gpx"
    # intervalo_metros = 2000  # Cambia esto al intervalo deseado
    import os
    # output_file_path = os.path.splitext(gpx_file_path)[0] + ".ruta"
    output_file_path = os.path.splitext(
        os.path.basename(gpx_file_path))[0] + ".ruta"

    gpx_track = ChkRutasGPS.read_gpx_file(gpx_file_path)
    distancia_total = ChkRutasGPS.create_ruta_json(
        gpx_track, intervalo_metros, output_file_path)
    print(
        f"Archivo .ruta.json generado: {output_file_path} con un intervalo de {intervalo_metros} metros -> distancia {distancia_total}")


def chequea_ruta(fichero):
    distancia_gps = ChkRutasGPS.get_distancia_ruta(fichero)
    distancia_ruta = RutaGenerator.get_distancia_ruta(fichero)
    print(
        f"La distancia del fichero gpx es {conv_metros_a_kilometros(distancia_gps)} y la de la ruta es {conv_metros_a_kilometros(distancia_ruta)}")
    return distancia_gps
