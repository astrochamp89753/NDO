#!/bin/bash

source ~/simastro/venv/bin/activate

#~/simastro/venv/bin/jupyterhub -f /var/www/simastro/jupyter-hub/jupyterhub_config.py
~/simastro/venv/bin/jupyterhub -f jupyterhub_config.py &
