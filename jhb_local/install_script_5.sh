#!/bin/bash

# this script has to be sourced, to activate conda environment

cd ~/proj/nwb_datajoint

echo "setting up the environment..."

# set up a new conda environment
ENVNAME="nwb_datajoint5"
conda env create --name $ENVNAME --file=environment.yml

# activate conda environment (this script has to be sourced as well)
source "/home/jhbak/anaconda3/etc/profile.d/conda.sh"
conda activate $ENVNAME 

# install pytest
conda install pytest

# install this repository
pip install -e .


# --- new install for labbox-ephys and widget (after mid-Mar) ---
cd ~/src/labbox-ephys
pip install -e ./src/python/

# labbox-ephys-widgets-jp is now separated
pip install --upgrade labbox-ephys-widgets-jp
jupyter serverextension enable labbox --sys-prefix

