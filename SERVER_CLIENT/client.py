# Importeer socket en de functies die info opvragen
import socket
from sysinfo import rawRAM, rawCPU, rawDISK

# Instellingen verbinding
host = '192.168.213.142'
port= 9001

class Data:
	# Initializer 
	def __init__(self, case):
		self.case = case

# Wijs data toe aan variabelen
dataHOST = Data(socket.gethostname())
dataRAM = Data(rawRAM())
dataCPU = Data(rawCPU())
dataDISK = Data(rawDISK())

# Zet lijst in data om te vervoeren met behulp van de socket
lijst = [dataHOST,",",str(dataRAM),",",str(dataCPU),",",str(dataDISK)]
data = ''.join(lijst)

# Encode de data
data_bytes = data.encode("utf-8")


# Stel socket in
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))



# Verstuur ASCII string naar server
client.send(data_bytes)
