
#If you want to connect the ESP32 to an existing newtork:
import network
from machine import Pin
 
import esp
esp.osdebug(None)
 
import gc
gc.collect()
 
ssid = 'YOUR NETWORK NAME'
password = 'YOUR NETWORK PASSWORD'

station = network.WLAN(network.STA_IF)
 
station.active(True)
station.connect(ssid, password)
# 
while station.isconnected() == False:
  pass
 
print('Connection successful')
print(station.ifconfig())


from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v


import machine
import time
led = machine.Pin(2,machine.Pin.OUT)
led.on()

from machine import Pin
import dht
sensor = dht.DHT11(Pin(14))

# ************************
# Configure the socket connection
# over TCP/IP
import socket

def read_ph():
  global ph
  ph = 0
  try:
    gpioVal = 0
    pot_value = pot.read()
    for i in range(0, 10):
      gpioVal += pot_value
      sleep(0.01)
    voltage = 5 / 4095 * gpioVal/10
    ph =  ((2.5 + voltage) / 0.020)-300
    return(ph)
   
  except OSError as e:
    return('Failed to read sensor.')
  
def web_page():
  html = """<!DOCTYPE HTML><html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
    html {
     font-family: Arial;
     display: inline-block;
     margin: 0px auto;
     text-align: center;
    }
    h2 { font-size: 3.0rem; }
    p { font-size: 3.0rem; }
    .units { font-size: 1.2rem; }
    .dht-labels{
      font-size: 1.5rem;
      vertical-align:middle;
      padding-bottom: 15px;
    }
    </style>
     </head>
    <body>
    <h1>Yuri's pH monitoring system</h1>
    <p>
    <i class="fas fa-tint" style="color:#00add6;"></i> 
    <span class="dht-labels">pH value</span>
    <span>"""+str(read_ph())+"""</span>
    <sup class="units"></sup>
    </p>
    </body>
    </html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))

  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
