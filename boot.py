#############################################
# Provide your Wifi connection details here #
#############################################

WIFI_SSID = "My Wireless Network Name"
WIFI_PASSWORD = "password_goes_here"

#############################################

import network
from time import sleep
from machine import Pin
import ntptime

sleep(1)  # Without this, the USB handshake seems to break this script and then fail sometimes.

led = Pin(2, Pin.OUT, value=1)


wlan = network.WLAN(network.STA_IF)
wlan.active(False)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)

while not wlan.isconnected():
    led.value(not bool(led.value()))
    sleep(0.2)

# Set the RTC to the current time

ntptime.settime()

# Solid LED means we're connected and ready to go
led.on()
