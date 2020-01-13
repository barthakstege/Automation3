#!/bin/bash
## Gemaakt door Bart :-)

toilet automation | lolcat

CLIENT_IP=$(grep -oPm1 "(?<=<client>)[^<]+" /root/Automation3/INSTALL/config.xml)
ROOT_DIR=$(grep -oPm1 "(?<=<root_path>)[^<]+" /root/Automation3/INSTALL/config.xml)

# Verwijder irritante cache folder (kan error geven als directory niet bestaat)
rm -rf $ROOT_DIR/SERVER_CLIENT/__pycache__

# Run dependencies.sh en format de output
printf "\nRuning dependencies.sh to check for installed software ..."
bash $ROOT_DIR/INSTALL/dependencies.sh | column -t

# Als niet alle dependencies geïnstalleerd zijn moet het script stoppen ...
if  $ROOT_DIR/INSTALL/dependencies.sh | grep '[X]'; then
	printf "Error, not all dependencies are installed. Exiting script."
	exit
# ... en anders mag het doorgaan
else
	printf "\nAll dependencies are installed, continuing ..."
fi

## Run het Python script dat een script signed.
/usr/bin/python3 $ROOT_DIR/SIGNING/create_sum.py 

# Run ansible's 'ping' module om te kijken of de client online is
printf "\Testing whether ansible client is online ..."

if ansible -m ping all | grep 'pong'; then
	printf "\nClient is online"
else
	# Exit script als client niet online is.
	printf "\nClient is not online. Exiting script."
	exit
fi

# Voer de ansible playbooks uit
printf "\nInstalling scripts on client ..."
ansible-playbook $ROOT_DIR/SERVER_CLIENT/scripts.yml && ansible-playbook /root/Automation3/SERVER_CLIENT/sysd.yml
printf "\nSCRIPTS installed sucessfully"

# Check SHA1 sum op client (over ssh)
printf "\nChecking SHA1 sum of scripts on client ..."
if ssh $CLIENT_IP python3 $ROOT_DIR/SIGNING/check_sum.py | grep 'failed'; then
	# Exit als SHA1 sum niet klopt
	printf "SHA1 sums are not correct. Exiting script."
	exit
fi
printf "\nSHA1 sums are correct."

# SIGN SCRIPTS

# Installeer de listen systemd service
cp $ROOT_DIR/SERVER_CLIENT/monitor-listen.service /etc/systemd/system/ && systemctl daemon-reload && systemctl --now enable monitor-listen.service
if systemctl status monitor-listen | grep -i "active (running)"; then
	printf "\nSystemd service is running."
else
	# Exit als de service niet runt
	printf "\nSystemd service is not running. Exiting script."
	exit
fi

# Controleer of docker active is
if systemctl status docker | grep -i "active (running)"; then
	printf "\nDocker is running, rolling out container ..."
else
	printf "\nDocker is not running. Exiting script."
	exit
fi

# Change directory naar SCRIPTS/ en start de website met docker-compose
cd $ROOT_DIR/httpd/Docker && docker-compose up &
printf "\nSystem installed successfully. Load monitoring.local in a browser to monitor"

# Run Selenium
/usr/bin/python3 $ROOT_DIR/TESTING/test.py
