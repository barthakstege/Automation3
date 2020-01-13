#!/bin/bash
## Gemaakt door Bart :-)
echo "AUTOMATION INSTALL SCRIPT V1.0"

# Verwijder irritante cache folder (kan error geven als directory niet bestaat)
rm -rf /root/SCRIPTS/__pycache__

# Run dependencies.sh en format de output
echo "Runing dependencies.sh to check for installed software ..."
./dependencies.sh | column -t

# Als niet alle dependencies geïnstalleerd zijn moet het script stoppen ...
if  ./dependencies.sh | grep '[X]'; then
	echo "Error, not all dependencies are installed. Exiting script."
	exit
# ... en anders mag het doorgaan
else
	echo "All dependencies are installed, continuing ..."
fi

## Run het Python script dat een script signed.
echo "Sign a script"
/usr/bin/python3 sign.py 

# Run ansible's 'ping' module om te kijken of de client online is
echo "Testing whether ansible client is online ..."

if ansible -m ping all | grep 'pong'; then
	echo "Client is online"
else
	# Exit script als client niet online is.
	echo "Client is not online. Exiting script."
	exit
fi

# Voer de ansible playbooks uit
echo "Installing scripts on client ..."
ansible-playbook /root/SCRIPTS/scripts.yml && ansible-playbook /root/SCRIPTS/sysd.yml
echo "SCRIPTS installed sucessfully"

## Check SHA1 sum op client (over ssh)
#echo "Checking SHA1 sum of scripts on client ..."
#if ssh 192.168.37.210 python3 /root/SCRIPTS/check_sum.py | grep 'failed'; then
#	# Exit als SHA1 sum niet klopt
#	echo "SHA1 sums are not correct. Exiting script."
#	exit
#fi
#echo "SHA1 sums are correct."

# Installeer de listen systemd service
cp monitor-listen.service /etc/systemd/system/ && systemctl daemon-reload && systemctl --now enable monitor-listen.service
if systemctl status monitor-listen | grep -i "active (running)"; then
	echo "Systemd service is running."
else
	# Exit als de service niet runt
	echo "Systemd service is not running. Exiting script."
	exit
fi

# Controleer of docker active is
if systemctl status docker | grep -i "active (running)"; then
	echo "Docker is running, rolling out container ..."
else
	echo "Docker is not running. Exiting script."
	exit
fi
# Change directory naar SCRIPTS/ en start de website met docker-compose
cd /root/SCRIPTS/ && docker-compose up &
echo "System installed successfully. Load 192.168.37.3 in a browser to monitor"
