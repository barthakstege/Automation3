#!/bin/bash

# De lijst met dependencies (zie GitHub)
DEPENDENCIES=(python3 ansible docker docker-compose systemctl bash)

# Loop door dependencies 
for DEPENDENCY in "${DEPENDENCIES[@]}"
do
	# Test aanwezigheid van dependency met which en redirect output naar /dev/null
	which $DEPENDENCY > /dev/null 2>&1
	
	# Laat gebruiker weten of dependency aanwezig is
	if [ $? -eq 1 ]; then
		echo -e "\e[31m$DEPENDENCY [X]\e[0m"
	else
		echo -e "\e[32m$DEPENDENCY [OK]\e[0m"
	fi
done
