import asyncio
import websockets
import random
import sys
import socket
from scapy.all import *
from scapy.layers.dot11 import Dot11
from math import log10

#Set up of application
#########################################################
ipAddress = socket.gethostbyname(socket.gethostname())
interface = "en0"
port = 8888
#########################################################

#Debug
#########################################################
print(f"IP Address: {str(ipAddress)}")
print(f"Interface: {str(interface)}")
print(f"Port: {str(port)}")
#########################################################


devices = set()
dev = set()
bannedDevices = set()
'''
Classe che identifica un dispositivi wifi
'''
class WifiDevice:
    def __init__(self,macAddr, dbm):
        self.macAddr = macAddr
        self.dbm = dbm

'''
Funzione di debug che individia i pacchetti IP
'''			
def PacketHandlerIP(pkt):
    #print("Strat scanning")
    #pkt.show()
    if pkt.haslayer('IP'):
        print("IP LAYER")
        k = pkt.getlayer('IP')
        print(k.src)

        dev.add(WifiDevice(k.src,str(-20)))

'''
Funzione che analizza i pacchetti, verifica che il pacchetto ricevuto sia di probeReq,
nel casso fosse cosi, ne estrae l'indirizzo MAC e la potenza del segnale e li salva nella
lista dei dispositivi trovati
'''		
def PacketHandler(pkt):
    if pkt.haslayer(Dot11ProbeReq):

        print(pkt.dBm_AntSignal)
        dot11_layer = pkt.getlayer(Dot11)
                            
        if dot11_layer.addr2 and (dot11_layer.addr2 not in devices):
            devices.add(dot11_layer.addr2)
            dev.add(WifiDevice(dot11_layer.addr2,str(pkt.dBm_AntSignal)))



'''
Quetsa funzionde è responsabole della ricezione, invio ed elaborazione dei messaggi
con il client
'''	
async def echo(websocket, path):
   
    #mes = await websocket.recv()
    
    #print message riceved from client
    #print(f"From client: {mes}")
            
    async for message in websocket:
        print(f"[From client]: {message}")
        protocol = message.split("-")[0]
        attributes = message.split("-")[1]
        if protocol == "$scan":
            t = AsyncSniffer(iface = interface, prn = PacketHandler)
            t.start()
            tempo = int(attributes)
            time.sleep(tempo)
            print(f"[scanning for]: {str(tempo)} seconds")
            t.stop()
            #print(t)                    

            await websocket.send("numDev$"+str(len(dev)))
            for d in dev:
                print(f"To client:" + "dev$"+d.macAddr+ "---"+d.dbm)
                await websocket.send("dev$"+d.macAddr+ "---"+d.dbm)

        if protocol == "$cleanCache":
            print("---> Set of devices has been cleaned")
            dev.clear()
            await websocket.send("Server cleaned devices")


# sniff(iface = "wlan1", count = 5, prn = PacketHandler)
asyncio.get_event_loop().run_until_complete(websockets.serve(echo, ipAddress, port))
asyncio.get_event_loop().run_forever()
