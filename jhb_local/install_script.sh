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

# install this repository
pip install -e .

# NOTE: I pulled {labbox-ephys, spikeextractors, spiketoolkit} repos just before running this

#echo "installing labbox-ephys..."
#cd ~/src/labbox-ephys
#pip install -e ./python
#pip install -e jupyterlab/labbox_ephys_widgets_jp
#jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
#jupyter labextension install jupyterlab/labbox_ephys_widgets_jp

# --- new repo for labbox-ephys-widgets-jp
#pip install --upgrade jupyterlab==3  # <<< do this in the environment file
#cd ~/src/labbox-ephys-widgets-jp
#pip install -e .
#jupyter nbextension install --py --symlink --overwrite --sys-prefix labbox_ephys_widgets_jp
#jupyter nbextension enable --py --sys-prefix labbox_ephys_widgets_jp
#jupyter labextension develop --overwrite labbox_ephys_widgets_jp

# no, let's just install using pip
pip install --upgrade labbox-ephys-widgets-jp
jupyter serverextension enable labbox --sys-prefix

exit 0

echo "installing spikeextractors..."
cd ~/src/spikeextractors
pip install -e .
# Install spiketoolkit
cd ~/src/spiketoolkit
pip install -e .
 
