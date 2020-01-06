### Installing Python

The original material is on:

> https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/
>
> https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
>
___

Start by updating the packages list and installing the prerequisites:

> sudo apt update
> sudo apt install software-properties-common

Next, add the deadsnakes PPA to your sources list:

> sudo add-apt-repository ppa:deadsnakes/ppa
When prompted press Enter to continue:
>Press [ENTER] to continue or Ctrl-c to cancel adding it.

Once the repository is enabled, install Python 3.7 with:

> sudo apt install python3.7

At this point, Python 3.7 is installed on your Ubuntu system and ready to be used. You can verify it by typing:

> python3.7 --version

### Installing PIP

For me, first install pip to python 3.6: 
> sudo apt install python3-pip 

After that install Python 3.7:
> sudo apt install python3.7

Finally install pip to Python 3.7:
>python3.7 -m pip install pip

For install packages use:
> sudo python3.7 -m pip install <module>


