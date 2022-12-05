<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="artwork/smartCamera.png" alt="Project logo"></a>
</p>

<h3 align="center">SmartQuadCamera</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()


</div>

---


<p align="center"> SmartQuadCamera
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#deployment)
- [Installation and Config](#Installation_and_Config)
- [Test](#test)
- [Circuit](#circuit)
- [Dashboard](#dashboard)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This repo contains circuit, firmware and backend for SmartQuadCamera Project.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites <a name = "Prerequisites"></a>

What things you need to install the software and how to install them.

```
- Raspberry Pi Model 4 (8GB)
```

## Installation and Configuration <a name = "Installation_and_Config"></a>

A step by step series that covers how to get the Firmware running.

### Raspberry Pi Firmware Pre-Reqs

1.  Download and install the latest Raspberry Pi OS Desktop image to your SD card
2.  Open the terminal and execute the following command
    ```sudo raspi-config```
3. Then follow the following pictures to enable I2C bus on you raspberry pi

* ![R1](artwork/r1.png)
* ![R2](artwork/r2.png)
* ![R3](artwork/r3.png)
* ![R4](artwork/r4.png)
* ![R5](artwork/r5.png)

* Then do the same for Serial(UART)

* ![R2](artwork/r2_2.jpg)

* And same for SPI, SSH and Camera

### Configuring Raspberry Pi and Running the UI
  1.  Copy FirmwareRPi folder to the desktop of your Raspberry Pi, open the terminal of your Raspberry Pi and execute the following commands

```bash
  - sudo apt-get update
  - sudo apt-get upgrade
  - sudo apt install python3-pip
  - pip3 install paho-mqtt
  - sudo adduser $USER dialout
  - sudo cp siSensor.service /lib/systemd/system/
  
```

Once done, import `flows.json` to the nodered, form `dashboard` folder.
### Installing and Configuring Node-RED on Raspberry Pi

Conifguring NodeRED, MQTT is required only one time.

Open the terminal and execute the following commands

```
- sudo apt install ufw
- sudo ufw enable
- sudo ufw allow tcp http https 1883 8883 1880 80 8080 443
```
##### Installing MQTT(Mosquitto)
Open the terminal and execute the following commands

```
- sudo apt install -y mosquitto mosquitto-clients
- sudo systemctl enable mosquitto.service
- mosquitto -v
```
##### Installing and Configuring NodeRED
Open the terminal and execute the following commands

```
- bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
- sudo systemctl enable nodered.service
- npm install node-red-dashboard 
- sudo npm install node-red-dashboard
- sudo systemctl restart nodered.service
```
Then open NodeRED in your raspberry pi or using any other device which is connected to the same network
as your Raspberry Pi is.
In the browser you can type http://raspberrypi.local:1880 to open the node-red

- Once node-red is opened, click on the menu button on the top left corner of the app and click on import.
- Click on `select file to import` and select flows.json present in the `dashboard` directory of this repo.
- After flows are imported, click on Deploy button on the top of the screen to save the changes.
- You can access the Dashboard using http://raspberrypi.local:1880/ui



1.  To run the program just restart the raspberry pi.

This program make use of MQTT to communicate with the webapp.

  ```diff
  + broker used is mosquitto, deployed on the Raspberry Pi.
  + vending can be done by publishing an ammount to mdb/invoke topic
  ```


## ⛏️ Testing <a name = "test"></a>

1.  The Firmware can be tested on Raspberry Pi 3B, 3B+ or 4B with the following modifications
  1.  Connect the sensor as shown in the Circuit Diagram section below.

## 🔌 Circuit Diagram <a name = "circuit"></a>

![GPIOsRPi](Circuit/Circuit.png)


* RPi 3,4 GPIOs Pinout

![GPIOsRPi](Circuit/rpi34.jpg)



### Circuit



```http
Pins connections
```

| Si7021 | Raspberry Pi |
| :--- | :--- |
| `SDA` | `2` | 
| `GND` | `GND` |
| `3V3` | `3V3` | 
| `SCL` | `3` | 

| Relay Pins | Raspberry Pi |
| :--- | :--- |
| `VCC` | `5V` | 
| `GND` | `GND` | 
| `P1` | `29` | 
| `P2` | `31` | 
| `P2` | `33` | 
| `P2` | `35` | 



## Dashboard <a name = "dashboard"></a>

You can use the dashboard with the link below:

[]()

<!-- ![dash](artwork/db1.png) -->


  ```diff
  - The dashboard is running on Raspberry Pi. 
  ```

  <!-- ![db1](artwork/db1.png)
  ![db2](artwork/db2.png)
  ![db3](artwork/db3.png)
  ![db4](artwork/db4.png)
  ![db5](artwork/db5.png) -->


## Components Used

1.  [Raspberry Pi](https://www.amazon.co.uk/SANOOV-Raspberry-Pi-Motherboard-Screwdiver/dp/B0BF58GQD4/ref=sr_1_1_sspa?crid=2BHVW7XD7RENW&keywords=raspberry+pi+4&qid=1667034192&qu=eyJxc2MiOiI1LjUxIiwicXNhIjoiNS41MCIsInFzcCI6IjQuNjgifQ%3D%3D&sprefix=raspberry+pi+4%2Caps%2C100&sr=8-1-spons&psc=1)
2. [Quad Camera Kit](https://www.arducam.com/product/64mp-quad-camera-kit/)
3. [GPS Module](https://www.amazon.co.uk/FUQUANDIAN-GY-NEO6MV2-Flight-Controller-Raspberry/dp/B09ND9SX8J/ref=sr_1_12?crid=1ETIQ6V4XZW3L&keywords=raspberry+pi+gps+module&qid=1667034390&qu=eyJxc2MiOiIzLjQ5IiwicXNhIjoiMy4yOSIsInFzcCI6IjEuNTkifQ%3D%3D&sprefix=gps+module+ras%2Caps%2C92&sr=8-12)
4. [4G LTE USB Dongle](https://www.waveshare.com/sim7600g-h-4g-dongle.htm)
5. [Raspberry Pi UPS - Pi Sugar 3](https://www.amazon.co.uk/Portable-Platform-Raspberry-Accessories-Handhold/dp/B09QRS666Y/ref=sr_1_2?crid=3HWT3GFC18CCK&keywords=pisugars+plus&qid=1667036487&sprefix=pisugar+s+plus+%2Caps%2C84&sr=8-2)

## ⛏️ Built Using <a name = "built_using"></a>

- [Python3](https://www.python.org/) - Raspberry Pi FW
- [Node-RED](https://nodered.org/) - Platform for creating dashbaords and backend logic
- Bash

## ✍️ Authors <a name = "authors"></a>

- [@Nauman3S](https://github.com/Nauman3S) - Development and Deployment
