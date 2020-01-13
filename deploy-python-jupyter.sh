#!/bin/bash
# Writer: Afonso Massao Yamaguchi
# Created: 2020-01-12
# Last Update Date: 2020-01-12
# This program was made to install Python and Jupyter Notebook and Jupyter Lab
#
#
##### Instaling Python
#
echo "Installing Python 3.7 ..."
#
# Check version:
python --version
#
# Step 1: Update and Refresh Repository Lists
sudo apt update
#
# Step 2: Install Supporting Software
sudo apt install software-properties-common
#
# Step 3: Add Deadsnakes PPA
sudo add-apt-repository ppa:deadsnakes/ppa
#
sudo apt update
#
# Step 4: Install Python 3.7
sudo apt install python3.7
#
python3.7 --version
#
echo "Python 3.7 installed"
#
##### Install PIP
echo "Installing PIP"
sudo apt install -y python3-pip
pip3 install flask
pip3 --version
#
# Install venv tool
echo "Installing and Configuring a environment to Python 3..."
sudo apt install python3-venv
#
# Creating your Python 3 Virtual Environment
python3 -m venv env
#
#  Activating your Python 3 Virtual Environment
source env/bin/activate
echo "Check Installed packages"
pip3 freeze
echo "Virtual Environment as installed"
#
#
##### Installing using pip classical Notebook
#
echo "Installing Jupter Notebook"
pip3 install jupyter
#
###### Installing using pip Jupyter Lab
#
pip3 install jupyterlab
#
# check
jupyter --version
#
echo "Jupyter Installed."
# end