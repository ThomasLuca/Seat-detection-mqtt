# Seat Detection

This repository contains the python code for the [seat detection project](https://github.com/VIVES-AI-edge-computing/seat-detection-team-brugge).  
It reads the output from the SensorTile and publishes it to an MQTT broker.

## Install the necessary modules

### [PySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html)

```zsh
pip install pyserial
```

### [Paho MQTT](https://www.eclipse.org/paho/)

```zsh
pip install paho-mqtt
```

## Run the code

```zsh
python __main__.py
```
