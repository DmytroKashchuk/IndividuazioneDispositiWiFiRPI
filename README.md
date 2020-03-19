# Individuazione dei dispositivi Wi-Fi usando Raspberry PI
Individuazione dei dispositivi Wi-Fi usando Raspberry PI

## Set-up
Assicurarsi che l'interfaccia di rete riesca a lavorare in monitor mode, sulla seguente pagina web ci sono alcune interfacce di rete che riescono a farlo:
https://null-byte.wonderhowto.com/how-to/buy-best-wireless-network-adapter-for-wi-fi-hacking-2019-0178550/
Collegare l'antenna al Raspberry PI e impostare l'antenna in monitor mode.
Individuare prima l'interfaccia di rete usando il comando:
```python
sudo ifconfig
```
Nel nostro caso è wlan1, quindi impostare wlan1 in monitor mode:
```python
sudo ifconfig wlan1 down
sudo iwconfig wlan1 mode monitor
sudo ifconfig wlan1 up
```
Verificare che l'operazione è avvenuta col successo:
```python
sudo iwconfig
```
Affiamo all'interfaccia wlan1 deve essere scrito "mode:monitor"
### Avvio dell'applicazione
Una volta dentro la cartella dell'applicazione, bisgona eseguire il server e l'applicazione per individuazione dei dispositivi.
Eseguire il Web Server: eseguire il file server.py
```python
sudo python3 server.py
```
Eseguire l'applicazione: eseguire il file webSocket_server.py
```python
sudo python3 webSocket_server.py
```
A questo punto si può passare all'utilizzo dell'applicazione, per fare questo bisogna digitare dal browser l'indirizzo del server, che è quello del raspberry.

Nota: al primo avvio potrebbe esserci l'errore d'indirizzo IP, quindi bisognerà cambiarlo nella pagina webSocket_server.py e index.html.
