#!/usr/bin/env python3

import argparse
import subprocess

# Colours
greenColour = "\033[1;32m"
endColour = "\033[0m"
redColour = "\033[1;31m"
blueColour = "\033[1;34m"
yellowColour = "\033[1;33m"
purpleColour = "\033[1;35m"
turquoiseColour = "\033[1;36m"
grayColour = "\033[1;37m"


def mostrar_discos():
    print("Particiones de discos: ")
    subprocess.run(["sudo", "fdisk", "-l"])


def mostrar_ultimo_reinicio():
    print("Información sobre el último reinicio del sistema: ")
    subprocess.run(["last", "reboot"])


def mostrar_disco_actual():
    print("Datos sobre memoria RAM y swap usada y libre: ")
    subprocess.run(["free", "-h"])


def mostrar_sistema_operativo():
    print("Información sobre el sistema operativo: ")
    subprocess.run(["uname", "-a"])


def mostrar_version_sistema_operativo():
    print("Versión del sistema operativo: ")
    subprocess.run(["lsb_release", "-a"])


def mostrar_memoria_ram():
    print("Memoria RAM: ")
    subprocess.run(["grep", "MemTotal", "/proc/meminfo"])


def main():
    parser = argparse.ArgumentParser(
        description="Script para mostrar información del sistema.")
    parser.add_argument(
        "-a", "--discos", help="Mostrar particiones de discos", action="store_true")
    parser.add_argument("-b", "-j", "--ultimo-reinicio",
                        help="Mostrar información sobre el último reinicio del sistema", action="store_true")
    parser.add_argument("-c", "--sistema-operativo",
                        help="Mostrar información sobre el sistema operativo", action="store_true")
    parser.add_argument("-d", "--version-sistema-operativo",
                        help="Mostrar la versión del sistema operativo", action="store_true")
    parser.add_argument("-e", "--memoria-ram",
                        help="Mostrar información sobre la memoria RAM", action="store_true")
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        return

    if args.discos:
        mostrar_discos()

    if args.ultimo_reinicio:
        mostrar_ultimo_reinicio()

    if args.sistema_operativo:
        mostrar_sistema_operativo()

    if args.version_sistema_operativo:
        mostrar_version_sistema_operativo()

    if args.memoria_ram:
        mostrar_memoria_ram()


if __name__ == "__main__":
    main()


# Este script se puede ejecutar en la línea de comandos utilizando los siguientes argumentos:

#     -a o - -discos para mostrar las particiones de discos
#     -b o - j o - -ultimo-reinicio para mostrar información sobre el último reinicio del sistema
#     -c o - -sistema-operativo para mostrar información sobre el sistema operativo
#     -d o - -version-sistema-operativo para mostrar la versión del sistema operativo
#     -e o - -memoria-ram para mostrar información sobre la memoria RAM

# Si se ejecuta el script sin ningún argumento, se imprimirá el mensaje de ayuda.
