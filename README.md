# Embedded Complex Acquirer and Transmitter - ecat

ECAT is an embedded system controlled by a Beaglebone Black which measures atmospheric variables from different devices transmitting the data in real time to a computer.

# Devices

Transmitter
------------

* Controller: Beaglebone Black - http://beagleboard.org/BLACK
* Barometer: BMP180 - http://www.adafruit.com/products/1603
* Compass: HMC6352 - https://www.sparkfun.com/products/retired/7915
* Gyroscope: LISY300AL - https://www.sparkfun.com/products/retired/8955
* Accelerometer: ADXL335 - https://www.sparkfun.com/products/9269
* GPS: ADAFRUIT ULTIMATE GPS BREAKOUT - https://www.adafruit.com/products/746

Receiver
------------

* Controller: Arduino Uno - http://www.arduino.cc/en/Main/ArduinoBoardUno

# Installation

As root execute the following lines:

------

    $ apt-get install update
    $ apt-get install upgrade
    $ apt-get install $(cat dependencies.txt)
    $ pip install -r requirements.txt
    $ reboot
    $ ./setup.sh

# References

* https://learn.adafruit.com/downloads/pdf/using-the-bmp085-with-raspberry-pi.pdf
* http://blog.initialstate.com/beaglebone-black-gps-mobile/
* http://randymxj.com/?p=491
* http://andrewdai.co/beaglecar/sensors-and-interfaces.html


# License
Pygram uses the [MIT](http://opensource.org/licenses/MIT) license.
The dependencies used by Pygram are subject to their respective licenses.

