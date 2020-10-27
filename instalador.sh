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




echo “Instalação finalizada”
