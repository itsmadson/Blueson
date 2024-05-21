# Blueson

Blueson is a tool for performing DOS attacks on Bluetooth devices. This repository contains all necessary files to run and install Blueson.
![Screenshot_2024-05-21_00_01_45](https://github.com/itsmadson/Blueson/assets/67187216/431d9bf8-97c7-4cdc-9ca2-1a1f418bbe89)

## Features
- Perform DOS attacks on Bluetooth devices
- Play an MP3 file during the attack
- Easy to install and use

## Installation
To install Blueson, run the following command:
```sh
sudo apt install bluez
sudo apt-get install bluez-firmware firmware-atheros
sudo apt-get install bluetooth bluez bluez-tools rfkill rfcomm
sudo apt install mpg123
```
## Usage
```sh
python3 Blueson.py
```
or Run Blueson.desktop 

## Manual

Target ID or MAC: ID or MAC address displayed after scanning.

Package Size: Size of the packages to be sent to the target (600 is optimal).

Threads Count: Number of threads that simultaneously send packages to the target. Optimal value can be found in the provided table.

|  Packages size | Threads count| Ping, ms  | Distance, meters | Time waited, sec  
|:--------------:|:-----: |:------------:|:--------------------:|:----------------:
|  600           | 1       | 9           |0,3                   |           5      
|  600           | 10      | 38          |0,3                   |           5      
|  600           | 20      | 78          |0,3                   |           5      
|  600           | 50      | 229         |0,3                   |           5      
|  600           | 100     | 413         |0,3                   |           5      
|  600           | 200     | 806         |0,3                   |           5      
|  600           | 500     | 1961        |0,3                   |           5      
|  600           | 1000    | 6621        |0,3                   |           5      
|  600           | 1000+   | Couldn't calculate  |0,3           |           5      
