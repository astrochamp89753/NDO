#!/bin/bash
source ~/simastro/venv/bin/activate
jupyter-book build ~/simastro/jupyter-book

#Kopiraj html datoteke za statični del
sudo rm -rf /var/www/simastro/jupyter-book/*
sudo cp -a ~/simastro/jupyter-book/_build/html/* /var/www/simastro/jupyter-book/

#Kopiraj konfiguracijsko datoteko - to zaenkrat ni treba, saj še ne vemo kako točno deluje
#sudo rm -rf /var/www/simastro/jupyter-hub/*
#sudo cp -a ~/simastro/jupyterhub_config.py /var/www/simastro/jupyter-hub/