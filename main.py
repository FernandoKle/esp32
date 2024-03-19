# Germán Andrés Xander 2023

from machine import Pin
import time

print("esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
contador = 0
sw_flag = True

while True:
    if sw.value() and sw_flag:
        led.value(not led.value())
        sw_flag = False
        contador += 1
        print(contador)
    
    if sw.value() == False and sw_flag == False:
        sw_flag = True
    
    time.sleep_ms(5)