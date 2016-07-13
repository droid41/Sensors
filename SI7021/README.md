Kopiert von
https://github.com/ControlEverythingCommunity/SI7021

# SI7021
SI7021 Humidity and Temperature Sensor

The SI7021 is a Humidity and Temperature Sensor.
This Device is available from ControlEverything.com [SKU: SI7021_I2CS]

https://www.controleverything.com/content/Humidity?sku=SI7021_I2CS

This Sample code can be used with Raspberry pi and Beaglebone Black.

##Java 
Download and install pi4j library on Raspberry pi. Steps to install pi4j are provided at:

http://pi4j.com/install.html

Download (or git pull) the code in pi.

Compile the java program.
```cpp
$> pi4j SI7021.java
```

Run the java program as.
```cpp
$> pi4j SI7021
```

## Arduino
Download and install Arduino Software (IDE) on your machine. Steps to install Arduino are provided at:

https://www.arduino.cc/en/Main/Software

Download (or git pull) the code and double click the file to run the program.

Compile and upload the code on Arduino IDE and see the output on Serial Monitor.

##Python 
Download and install smbus library on Raspberry pi. Steps to install smbus are provided at:

https://pypi.python.org/pypi/smbus-cffi/0.5.1

Download (or git pull) the code in pi. Run the program

```cpp
$> python SI7021.py
```

## C

Download (or git pull) the code in Beaglebone Black.

Compile the c program.
```cpp
$>gcc SI7021.c -o SI7021
```
Run the c program.
```cpp
$>./SI7021
```
The code output is the relative humidity and temperature reading in degree celsius and fahrenheit.
