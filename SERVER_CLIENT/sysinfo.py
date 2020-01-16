# Importeer modules die systeeminfo opvragen

from psutil import cpu_percent, virtual_memory, disk_usage
from time import sleep

# rawCPU geeft alleen het percentage gebruikte CPU (input voor matplotlib?)
def rawCPU():
    load = cpu_percent(percpu=False, interval = 1)
    return load

# rawDISK geeft het percentage gebruikte disk space weer (input voor matplotlib)
def rawDISK():
    usage = disk_usage("/")
    return usage[3]

# ramCheck() print het percentage RAM dat in gebruik is
def ramCheck():
    while True:
        # Dit koppelt de output van virtual_memory aan een variabele
        virtualMem = virtual_memory()
        # Dit print het percentage beschikbare RAM
        print("Er wordt momenteel " + str(virtualMem[2]) + "% RAM gebruikt")
        # Slaap 1 seconde om de output in de hand te houden
        sleep(1)

# rawRAM geeft alleen het percentage gebruikte RAM (voor matplotlib?)
def rawRAM():
    virtualMem = virtual_memory()
    return str(virtualMem[2])

## OOP class om eventueel later te gebruiken
#class Data:
#	def __init__(self, hostname, cpu, ram, disk):
#		self.hostname = hostname
#		self.cpu = cpu
#		self.ram = ram
#		self.disk = disk
#	
#client = Data("client", 14.6, 12.1, 54.2)
