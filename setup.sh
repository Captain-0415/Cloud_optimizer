#!/bin/bash

###Get required parameters ###
#Fresh installation command: bash setup.sh -i <ip> Y
#Upgrade command: bash setup.sh -i <ip> N <path-of-old-cloud-optimiser>
answer=$3
old_path=$4
######## Verify details ########

echo "Values provided are : 1. Machine ip: "$2
echo "2.Fresh installation :" $answer

if [["$answer" =="N" || "$answer"=="n" ]]; then
	echo "Path of existing directory : " $old_path
	while [[! -e $old_path/version.txt ]]
	 	do
	 		echo "version.txt not found. Enter correct path"
	 		read old_path
	 	done
fi

read -p "Please confirm the above details. Do you want to continue?(yes/no) " choice

if [["$choice"=="no" || "$choice"=="No" || "$choice"=="NO"]];then
	echo "Installation aborted!"
	exit 1
fi

#!/bin/bash
while getopts ":i:" opt; do
	case $opt in
		i) ip="$OPTARG"
		;;
		\?)echo "Inavlid option -$OPTARG" >&2
		exit 1
		;;
	esac
	
	case $OPTARG in
		-*)echo "Option $opt needs a valid argument"
		exit 1
		;;
	esac
done

###############################

backend_server_port=8080
ng_server_port=8081

##$PWD
setup_path=$PWD
venv_name='venv_py3'

sudo -n true
test $? -eq 0 || exit 1 "You should have sudo priveleges"


#############################

ufw status
ufw disable

echo "---------------------------------"
echo "Installing required packages."
echo "---------------------------------"

sudo apt update

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | sudo tree /etc/apt/sources.list.d/pgdg.list

sudo apt update
sudo apt -y install vim bash-completion wget
sudo apt -y upgrade
packages=( postgresql-12 postgresql-client-12 gcc-c++ make python3 python3-venv pip curl)

for package_name in "${packages[@]}"
do
	sudo apt-get -y install $package_name ;
done

curl -ksL https://deb.nodesource.com/setup_16.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt update
sudo apt -y install nodejs
npm config set registry http://registry.npmjs.org/

echo N | sudo npm install -g @angular/cli


echo "-------------------------------------------"
echo "Installing virtual environment and activating it "
echo "-------------------------------------------"

echo "Setup path"
echo $setup_path
cd $setup_path

pip3 install -U pip
pip3 install -U setuptools
sudo apt-get -y install libpq-dev

python3 -m venv $venv_name
source $venv_name/bin/activate

echo "-------------------------------------------------"
echo PIP - Install Python requirements
echo "-------------------------------------------------"

#Delete
sed -i '/local	all		all				peer/d' /etc/postreqsql/12/main/pg_hba.conf
sed -i '/host	all		all		127.0.0.1/\32		md5/d' /etc/postgresql/12/main/pg_hba.conf
sed -i '/host	all		all		::1/\128		md5/d' /etc/postgresql/12/main/pg_hba.conf

#Insert
echo 'host	all		all		127.0.0.1/32		trust' /etc/postreqsql/12/main/pg_hba.conf
echo 'local	all		all				trust' /etc/postgresql/12/main/pg_hba.conf
echo 'host	all		all		::1/128		trust' /etc/postgresql/12/main/pg_hba.conf

cd $setup_path
pip3 install -r requirements.txt
pip3 install djangoframework-jwt
