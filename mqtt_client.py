import random

from paho.mqtt import client as mqtt_client

class MQTTClient:
  def __init__(self):
    self.broker = 'public.mqtthq.com'
    self.port = 1883
    self.topic = "SensorTile"
    self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
    self.client = None
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


  def publish(self, msg):
    self.client.publish(self.topic, msg)


  def run(self):
    self.client = self.connect_mqtt()
    self.client.loop_start()
