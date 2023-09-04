import argparse
from rutinas import *


def main():
    print(f"chkrutas V1.0 by Makoki Enterprises")
    parser = argparse.ArgumentParser(
        description="***** informacion *************")
    parser.add_argument("-a", metavar="fichero.gpx",
                        help="Analizar y procesar un fichero gpx")
    parser.add_argument("-i", metavar="intervalo", default="2000",
                        help="Intervalo en metros (por ejemplo, 500m)")
    parser.add_argument("-L", action="store_true",
                        help="Incluir el último punto si no coincide con el primer punto de un intervalo")
    parser.add_argument("-t", metavar="fichero.ruta",
                        help="Testear si una ruta está vigente actualmente")
    parser.add_argument("-d", metavar="directorio",
                        help="Testear todos los ficheros .ruta de un directorio")
    parser.add_argument("-x", action="store_true",
                        help="Chequear el fichero de índices")
    parser.add_argument("-s", metavar="mostrar",
                        help="Mostrar los ficheros .ruta de un directorio")

    args = parser.parse_args()

    # parser.print_help()

    if not any(vars(args).values()):
        parser.print_help()
    else:
        parametros = [None] * 5
        parametros[0] = vars(args)['a']
        if parametros[0] is not None:
            # print(f"Hay a -> {parametros[0]}")
            parametros[1] = vars(args)['i']
            intervalo_metros = 1000
            if parametros[1] is not None:
                intervalo_metros = int(parametros[1])
            parametros[2] = vars(args)['L']
            add_last = True
            if parametros[2] is not None:
                add_last = (parametros[2] == 'S')
            genera_fichero_ruta(parametros[0], intervalo_metros, add_last)

        else:
            parametros[3] = vars(args)['t'] 
            if parametros[3] is not None :
                distancia = chequea_ruta(parametros[3])

if __name__ == "__main__":
    main()
