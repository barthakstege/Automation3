#!/usr/bin/python3
# enable debugging
from datetime import datetime
import cgitb
import tkinter
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

cgitb.enable()
print("Content-Type: text/html\n")
print("Update succesful, redirecting ...")

# Lees data en voeg toe aan variabele
#dataFile = open("RAM.txt", "r")
#data = dataFile.readlines()
#ram = float(data[0].rstrip())
#cpu = float(data[1].rstrip())
#disk = float(data[2].rstrip())

sqlite_file = "/root/Automation3/SERVER_CLIENT/database.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("SELECT host FROM resources")
host = c.fetchone()[0].rstrip()
print(host)
c.execute("SELECT ram FROM resources")
ram = c.fetchone()[0]
print(ram)
c.execute("SELECT cpu FROM resources")
cpu = c.fetchone()[0]
print(cpu)
c.execute("SELECT disk FROM resources")
disk = c.fetchone()[0]
print(disk)

# Logging: exporteer waardes naar logbestand
with open("/var/www/monitoring.local/logs/log.txt", "a") as log_file:
	date = datetime.now()
	log_file.write(str(date))
	log_file.write(" - ")
	log_file.write("[HOST]: " +str(host))
	log_file.write(" [RAM]: " +str(ram))
	log_file.write(" [CPU]: " +str(cpu))
	log_file.write(" [DISK]: " +str(disk))
	log_file.write("\n")
	

objects = ('RAM', 'CPU', 'DISK')
y_pos = np.arange(1, 4)
performance = (ram, cpu, disk)

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Percent')
now = datetime.now()
plt.title(host)

#plt.show()
plt.savefig("/var/www/monitoring.local/chart.png")

redirectURL = "http://192.168.37.3"
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')

