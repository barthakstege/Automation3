# Importeer modules die systeeminfo opvragen

from psutil import cpu_percent, virtual_memory, disk_usage
from time import sleep

# cpuCheck() print gemiddelde CPU gebruik per seconde
def cpuCheck():
    while True:
        # Dit koppelt de output van cpu_percent aan een variabele
        load = cpu_percent(percpu=False, interval = 1)
        # De counter wordt verderop gebruikt voor waarschuwingen
        counter = 0
        # Als er niks aan de hand is wordt hiermee de load geprint
        print("CPU load is op dit moment " + str(load) +"%")
        # Als de load boven de 70% komt wordt de counter opgeteld
        if load > 70 and counter < 5:
            counter += 1
        # Als de load te vaak > 70% is geweest, print het een waarschuwing
        elif load > 70 and counter > 5:
            print("CPU komt regelmatig (al " + str(counter) + " keer) boven 75%")

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

def menu():
    while True:
        keuze = input("Kies optie: [1: RAM, 2:CPU] $ ")
        if keuze == "1":
            ramCheck()
        elif keuze == "2":
            cpuCheck()
        else:
            break

#menu()
#print(rawRAM()) 
#print(rawDISK())
