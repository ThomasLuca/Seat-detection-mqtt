import random

from paho.mqtt import client as mqtt_client


class MQTTClient:
  def __init__(self):
    self.broker = 'public.mqtthq.com'
    self.port = 1883
    self.topic = "SensorTile"
    self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
    self.client = None
    self.chairs = []
    self.run()

  # generate client ID with pub prefix randomly
  def connect_mqtt(self):
    def on_connect(client, userdata, flags, rc):
      if rc == 0:
        print("Connected to MQTT Broker!")
      else:
        print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(self.client_id)
    client.on_connect = on_connect
    client.connect(self.broker, self.port)
    return client

  def subscribe(self, client):
    def on_message(client, userdata, msg):
      self.processMessage(msg)
        
    client.subscribe(self.topic)
    client.on_message = on_message
  
  def isUniqueChair(self, chairId):
    if chairId in self.chairs:
      return False
    return True

  def processMessage(self, msg):
    message = msg.payload.decode()
    chair = message.split()[0][:-1]
    if self.isUniqueChair(chair):
      self.chairs.append(chair)
    print(message)
  
  def run(self):
    client = self.connect_mqtt()
    self.subscribe(client)
    client.loop_forever()

client = MQTTClient()