import os
import os,time
def main():
	print(logo)
	print(menu)
	
try:
    import rich
except:
    os.system("pip install rich")
    os.system("pkg install espeak")
    import rich

from rich.progress import track

def looood(rs_rocky):
    for i in track(range(500),description=rs_rocky):
        time.sleep(0.002)
	
	
logo = ('''\033[31;1m
                                                           

\x1b[38;5;46m███████ ███████ ████████ ██    ██ ██████  
\x1b[38;5;46m██      ██         ██    ██    ██ ██   ██ 
\x1b[38;5;46m███████ █████      ██    ██    ██ ██████  
\x1b[38;5;46m     ██ ██         ██    ██    ██ ██      
\x1b[38;5;46m███████ ███████    ██     ██████  ██
\033[31;1m═══════════════════════════════════════''')
menu = ("""\033[0;93m[\033[31;1m1\033[0;93m]>BASIC SETUP\n[\033[31;1m2\033[0;93m]>FULL SETUP\n[\033[31;1m4\033[0;93m]>\033[31;1mEXIT""")
def lock():
	os.system('clear')
	#os.system('espeak -a 300 " enter password"')
	option = input("\033[0;93m[🟰]ENTER PASSWORD : ")
	if option=='ROCKY':
		os.system('clear')
		looood("LODGING.......")
		os.system('clear')
	#	os.system('espeak -a 300 " the password is carrect "')
		print("\033[0;93m[✔️] CARRECT PASSWORD")
		rocky()
	else:
		os.system('clear')
		looood("LODGING.......")
		os.system('clear')
	#	os.system('espeak -a 300 " the password is wrong madarcud "')
		print("\033[31;1m[✖️]WRONG PASSWORD")
		os.system('espeak -a 300 " i fuck you"')
		print("[🖕🖕] I FUCK YOU 👉👌")
		
def rocky():	
	looood("STRATING.......")
	os.system('clear')
	print(logo)
	print(menu)
	ab = input("\033[1;97m[®]>CHOICE OPTION:--->>>")
	if ab=='1':
		ai()
	if ab=='2':
		bi()
	if ab=='3':
		ci()
	if ab=='4':
		di()
		
def ai():
	os.system('termux-setup-storage')
	os.system("""clear
apt update
apt upgrade
apt install git
apt install python
apt install python2
pip install requests
pip2 install requests
pip install mechanize
pkg install espeak
pip2 install mechanize 
pip2 install bs4
pip install bs4
clear
print('\033[0;93m[✔️]BASIC SETUP COMPLETE ')""")
def bi():
	os.system('termux-setup-storage')	
	os.system("""clear
pkg update
pkg upgrade
pkg install python
pkg install python2
pkg install python3
pkg install python-pip
pkg install wget
pkg install fish
pkg install ruby
pkg install help
pkg install espeak
pkg install git
pkg install dnsutils  
pkg install php
pkg install perl
pkg install lua
pkg install parallel
pkg install nmap
pkg install bash
pkg install clang
pkg install nano
pkg install w3m
pkg install hydra
pkg install figlet
pkg install cowsay
pkg install curl
pkg install tar
pkg install zip
pkg install unzip
pkg install net-tools
pkg install tor -y
pkg install sudo -y
pkg install wireshark
pkg install wgetrc
pkg install wcalc
pkg install openssl
pkg install openssl-tool
pkg install bmon
pkg install vpn
pkg install unrar
pkg install toilet
pkg install proot
pkg install net-tools
pkg install vim
pkg install vim-python
pkg install ired
pkg install goaccess
pkg install golang
pkg install tar
pkg install kibi
pkg install tsu
pkg install tmux
pkg install mtools
pkg install file
pkg install vis
pkg install pass
pkg install pick
pkg install chroot
termux-chroot
pkg install macchanger
pkg install ninja
pkg install elixir
pkg install swift
pkg install xmlstarlet
pkg install fakeroot
pkg install texinfo
pkg install netcat
pkg install wren
pkg install gatling
pkg install cvs
pkg install ffmpeg
pkg install screen 
pkg install neofetch 
pkg install mariadb
pkg install picolisp
pkg install toilet
pkg install cmatrix
pkg install dropbear
pkg install openssh
pkg install python-pip
pip2 install wget
pip install bs4
pip2 install bs4
pip install requests
pip2 install requests
pip install mechanize
pip2 install mechanize
pip install php
pip2 install php
clear
print('\033[0;93m[✔️]FULL SETUP COMPLETE ')""")
	
def ci():
	os.system('xdg-open https://www.facebook.com/rockykhan4g?mibextid=2JQ9oc')

def di():
	os.system('espeak -a 300 " Thanks for using  tool "')
	os.system('clear')
	looood("EXIT.......")
	os.system('clear')
	
lock()