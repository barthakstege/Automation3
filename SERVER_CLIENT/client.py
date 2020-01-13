# Importeer socket en de functies die info opvragen
import socket
from sysinfo import rawRAM, rawCPU, rawDISK


# Instellingen verbinding
host = '192.168.213.142'
port= 9001


# Wijs output rawRAM toe aan variabele 'data' en encode naar ASCII 
dataHOST = socket.gethostname()
dataRAM = rawRAM()
dataCPU = rawCPU()
dataDISK = rawDISK()

#lijst = [dataHOST, "\n", str(dataRAM), "\n", str(dataCPU), "\n", str(dataDISK)]
#data = ''.join(lijst)

lijst = [dataHOST,",",str(dataRAM),",",str(dataCPU),",",str(dataDISK)]
data = ''.join(lijst)

data_bytes = data.encode("utf-8")


# Stel socket in
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))



# Verstuur ASCII string naar server
client.send(data_bytes)


# Sluit verbinding
