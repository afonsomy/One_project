#!/bin/bash
# Writer: Afonso Massao Yamaguchi
# Created: 2020-01-12
# Last Update Date: 2020-01-12
# This program was made to install all Python packges that will used in Projects it will made
#
#
clear
# root of environment
echo "Go to root of environment"
cd ~/projects
# Activating environment
echo "Activate Environment"
source env/bin/activate
# Intalling packges to use in Data Science works
# Needs install wheel to solute a warnning message during the installations.
pip install wheel; ./setup.py bdist_wheel
echo "Installing packges to Data Science stuffs"
pip3 install pandas
pip3 install numpy
pip install matplotlib
pip install seaborn
pip install plotly
pip install cufflinks
pip install -U scikit-learn
#
#
# Install packges using with AWS tools
echo "Installing packges to Data Engineer stuffs"
pip install boto3
pip install awswrangler
#
#
# Installing packages use to automate or other things
echo "Installing miscelaneous packges"
#
#
echo "Package Installed now..."
pip3 freeze
echo "END"
#
#
