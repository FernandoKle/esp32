import dht, machine

d = dht.DHT22(machine.Pin(13))
print(d.measure())
print("Temperatura:", d.temperature())
print("Humedad:", d.humidity())