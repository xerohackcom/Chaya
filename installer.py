import argparse
import os

# command runner
def run_cmd(cmd):
    try:
        os.system(cmd)
    except Exception as e:
        raise e


# initialization
def init():
	# start argument parser
    parser = argparse.ArgumentParser(description="Chaya Argument Parser", add_help=True)
    os_group = parser.add_mutually_exclusive_group()
    os_group.add_argument('-ubu','--ubuntu', action='store_true', help="For Ubuntu or Ubuntu based distros")
    os_group.add_argument('-deb', '--debian', action='store_true', help="For Debian or Debian based distros")
    args = parser.parse_args()

    if args.ubuntu:
    	run_cmd("sudo apt install python3-pip && sudo apt install git && pip3 install -r requirements.txt && sudo apt update && sudo apt-add-repository ppa:linuxuprising/libpng12 && sudo apt update && sudo apt install -y libpng12-0")
    elif args.debian:
    	run_cmd("sudo apt install python3-pip && sudo apt install git && pip3 install -r requirements.txt && sudo apt update && sudo apt install build-essential devscripts && cd ~/ && sudo touch /etc/apt/sources.list.d/libpng12.list && echo 'deb https://ppa.launchpadcontent.net/linuxuprising/libpng12/ubuntu hirsute main' | sudo tee -a /etc/apt/sources.list.d/libpng12.list && echo 'deb-src https://ppa.launchpadcontent.net/linuxuprising/libpng12/ubuntu hirsute main' | sudo tee -a /etc/apt/sources.list.d/libpng12.list && sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 1CC3D16E460A94EE17FE581CEA8CACC073C3DB2A && sudo apt update && sudo apt install -y libpng12-0")
    else:
    	print("ERROR: Please select a distro variant! [python3 installer.py --help]")


if __name__ == "__main__":
	init()
