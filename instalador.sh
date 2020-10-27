#!/bin/bash

RED='\033[0;31m'
GRE='\033[0;32m'
NC='\033[0m' # No Color

printf "\n${NC}Atualizando repositórios...\n\n"
if ! apt-get update
then
    printf "\n${RED}Não foi possível atualizar os repositórios. Verifique seu arquivo /etc/apt/sources.list\n\n"
    exit 1
fi
printf "\n${GRE}Atualização feita com sucesso\n\n"


printf "\n${NC}Atualizando pacotes já instalados\n\n"
if ! apt-get upgrade
then
    printf "\n${RED}Não foi possível atualizar pacotes.\n\n"
    exit 1
fi
printf "\n${GRE}Atualização de pacotes feita com sucesso.\n\n"


printf "\n${NC}Instalando Flask-Ask\n\n"
if ! python3 -m pip install Flask-Ask
then
    printf "\n${RED}Não foi possível instalar o Flask-Ask.\n\n"
    exit 1
fi
printf "\n${GRE}Flask-Ask instalado com sucesso.\n\n"


printf "\n${NC}Atualizando o setuptools do pip3\n\n"
if ! pip3 install --upgrade setuptools
then
    printf "\n${RED}Não foi possível atualizar o pacote setuptools do pip3.\n\n"
    exit 1
fi
printf "\n${GRE}pip3 setuptools atualizado com sucesso.\n\n"


printf "\n${NC}Instalando Cryptography\n\n"
if ! pip3 install 'cryptography<2.2'
then
    printf "\n${RED}Não foi possível instalar o cryptography.\n\n"
    exit 1
fi
printf "\n${GRE}Cryptography instalado com sucesso.\n\n"


printf "\n${NC}Baixando Ngrok zip\n\n"
if ! wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
then
    printf "\n${RED}Não foi possível baixar o Ngrok.\n\n"
    exit 1
fi
printf "\n${GRE}Ngrok baixado com sucesso.\n\n"


printf "\n${NC}Unziping Ngrok\n\n"
if ! unzip ngrok-stable-linux-arm.zip
then
    printf "\n${RED}Unziping Ngrok failed.\n\n"
    exit 1
fi
printf "\n${GRE}Ngrok unziped sucessfully.\n\n"




echo “Instalação finalizada”
