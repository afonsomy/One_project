##  Solving problem on Vostro 5490 wifi

We needs compile a driver for Intel AC 9462.

The solution was published on https://ubuntuforums.org/showthread.php?t=2431914

1 - Make a folder to new git repository

````
mkdir git
cd git
````

2 - Update system

````
sudo apt update

sudo apt install git build-essential
````

3 - Download the needs files

````
git clone https://git.kernel.org/pub/scm/linux/kernel/git/iwlwifi/backport-iwlwifi.git
````

4 - Execute compiler

````

cd backport-iwlwifi/

make defconfig-iwlwifi-public

````

5 - Makes the configuration files

````
sed -i 's/CPTCFG_IWLMVM_VENDOR_CMDS=y/# CPTCFG_IWLMVM_VENDOR_CMDS is not set/' .config
````

6 - Execute final compiler and install

````
make -j4

sudo make install
````

7 - Reboot

8 - Send changes to iwlwifi file config

````
sudo modprobe iwlwifi
````


