#!/bin/bash

# Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

export DEBIAN_FRONTEND=noninteractive

trap ctrl_c INT

function ctrl_c(){
    echo -e "\n${yellowColour}[*]${endColour}${grayColour} Saliendo ${endColour}"
    tput cnorm
    exit 0
}

function helpPanel(){
    echo -e "\n${yellowColour}[*]${endColour}${grayColour} Uso: ./Menu12.sh${endColour}"
    echo -e "\n\t${purpleColour}a)${endColour} Introducir ./Menu12.sh -a para mostrar las particiones de discos"
    echo -e "\n\t${purpleColour}b)${endColour} Introducir ./Menu12.sh -j para mostrar información sobre el último reinicio del sistema"

    exit 0
}

function mostrarDiscos(){
    tput civis
    echo "Particiones de discos: "
    sudo fdisk -l

}

function mostrarUltimoReinicio(){
    echo "Información sobre el último reinicio del sistema: "
    last reboot
}

# ///////////////////////////

function mostrarDiscoActual(){
    echo "Datos sobre memoria RAM y swap usada y libre: "
    free -h
}

function mostrarSistemaOperativo(){
    echo "Información sobre el sistema operativo: "
    uname -a
}

function mostrarVersionSistemaOperativo(){
    echo "Versión del sistema operativo: "
    lsb_release -a
}

function mostrarMemoriaRAM(){
    echo "Memoria RAM: "
    grep MemTotal /proc/meminfo
}

# Main Function

if [ "$(id -u)" == "0" ]; then
    declare -i parameter_counter=0
    while getopts ":abcdejh:" arg; do
        case $arg in
            a) mostrarDiscos; let parameter_counter+=1 ;;
            b|j) mostrarUltimoReinicio; let parameter_counter+=1 ;;
            c) mostrarSistemaOperativo; let parameter_counter+=1 ;;
            d) mostrarVersionSistemaOperativo; let parameter_counter+=1 ;;
            e) mostrarMemoriaRAM; let parameter_counter+=1 ;;
            h) helpPanel;;
            *) echo -e "\nOpción inválida. Ejecutar ./Menu12.sh -h para ver las opciones disponibles.\n"; exit 1;;
        esac
    done

    if [ $parameter_counter -eq 0 ]; then
        helpPanel
    fi
    tput cnorm
else
    echo -e "\n${redColour}[*] No soy root${endColour}\n"
fi
