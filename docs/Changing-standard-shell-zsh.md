### Intall zsh

Well everybody say that zsh is the better shell to use together Git and Python. I'm starting to use too.

As a pre-requisite, ensure that the following tools are installed; git, wget, curl

> sudo apt-get install wget curl git

Installing zsh:
> sudo apt install zsh

Check installation:
> zsh --version
zsh 5.4.2 (x86_64-ubuntu-linux-gnu)

Configure zsh:
> chsh -s $(which zsh

Install Oh-my-zsh:
> sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

Configure Oh-my-zsh:

The main configuration file for Zsh is located under $HOME/.zshrc while the Oh-my-Zsh configuration files are located under $HOME/.oh-my-zsh/ directory.

If more details is necessary I can make a search in Google webpages like:
> https://kifarunix.com/how-to-install-and-setup-zsh-and-oh-my-zsh-on-ubuntu-18-04/
>
> https://casparwre.de/blog/zsh-in-ubuntu-1804/
>

Check the shell active:
> echo "$SHELL"

or

> ps -p $$

Check how many shell were installed:
> cat /etc/shells

More commands about shell are available on:
> https://www.cyberciti.biz/tips/how-do-i-find-out-what-shell-im-using.html





