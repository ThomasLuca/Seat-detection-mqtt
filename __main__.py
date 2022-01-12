import serial
from mqtt_client import MQTTClient

client = MQTTClient()

ser = serial.Serial('/dev/ttyACM0', 115200)
chairId= 0

while True:
  data = str(ser.readline())[2:-3]
  if "Seat-fill" in data:
    fill = float(data.split()[1])
    print("filled: " + str(fill))
    if fill > 0.5:
      client.publish(f"chair{chairId}:Occupied")
    else:
      client.publish(f"chair{chairId}:Empty")