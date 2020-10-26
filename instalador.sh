#!/bin/bash

printf "\nAtualizando repositórios...\n\n"
if ! apt-get update
then
    printf "\nNão foi possível atualizar os repositórios. Verifique seu arquivo /etc/apt/sources.list\n\n"
    exit 1
fi
printf "\nAtualização feita com sucesso\n\n"


printf "\nAtualizando pacotes já instalados\n\n"
if ! apt-get upgrade
then
    printf "\nNão foi possível atualizar pacotes.\n\n"
    exit 1
fi
printf "\nAtualização de pacotes feita com sucesso.\n\n"




echo “Instalação finalizada”
