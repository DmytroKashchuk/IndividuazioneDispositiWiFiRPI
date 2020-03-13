# DetectionWifiDevice
Individuazione dei dispositivi Wi-Fi usando Raspberry PI

## Set-up
Collegare l'antenna al Raspberry PI.
Impostare l'antenna in modalità promiscua:
```python
sudo ifconfig wlan1 down
sudo iwconfig wlan1 mode monitor
sudo ifconfig wlan1 up
```
Una volta dentro la cartella dell'applicazione, bisgona eseguire il server e l'applicazione per individuazione dei dispositivi.
Eseguire il Web Server: eseguire il file server.py
```python
sudo python3 server.py
```
Eseguire l'applicazione: eseguire il file webSocket_server.py
```python
sudo python3 webSocket_server.py
```
A questo punto si può passare all'utilizzo dell'applicazione, per fare questo bisogna dal browser digitare l'indirizzo del server, che è quello del raspberry.
