# BBM: Bridge-Baby-Monitor

<img src="https://i.ibb.co/zJTPRqk/bbm.png">

Intelligent solution for structural monitoring based on the analysis of natural frequencies in bridges.

(INSERTAR BUENA IMAGEN DEL DISPOSITIVO)
<img src="https://i.ibb.co/zJTPRqk/bbm.png">

# Table of contents
* [Introduction](#introduction)
* [Problematic](#problematic)
* [Our Solution](#our-solution)
* [Where should I start?](#where-should-i-start)
* [Future Rollout](#future-rollout)
* [References](#references)

## Introduction:

The little monitoring that bridges have in the world and the structural damage that they can have over time and as the lack of preventive maintenance can cause a partial or total failure of the bridge.

The main problems by which a bridge can fail and fall are:

- Infrastructure failure.
- Structrural collapse
- Lack of good maintainance
- Wear and Tear
- Floods.
- Unexpected events
- A combination of issues.

Do not believe me ?, look what happened to the pedestrian bridges of my university.

Video: Click on the image

[![TERREMOTO 7.1 | 19 DE SEPTIEMBRE 2017 | CDMX TEC DE MONTERREY](https://image.flaticon.com/icons/png/128/44/44431.png)](https://www.youtube.com/watch?v=47jqaRRaQAM)

If we could notice a failure in the structure beforehand this would cut costs of maintenance and also prevent any disaster, therefore it is the main problem we want to fight with our solution.

## Problematic:

<img src="https://image.ibb.co/nc9HYo/farmer_7591.jpg" width="800">

Let's take a look at some FACTS:

• The population in Mexico (Both of the author's own country) and in the world will grow.

• By 2050 the production of food will have to DOUBLE to feed this population.

• The amount of arable Land will not increase.

• The amount of Water available will be decreasing.

• Sustainable Disruption is needed.

• Current methods are insufficient for this.

• Infrastructure is costly.

• Most fields are in remote areas.

• Urban agriculture needs a cheap and readily available solution, for it to be sustainable.

If only there was a way to monitor the field through a network of sustainable sensors, which could be monitored in real time 365 days a year, performing data analytics in the cloud and taking weather predictions to generate models. Taking all this information to manage resources such as water, in order to save most of them, and above all being powered by solar panels ....... oh wait, there is Aggrofox!

## Our Solution:

The solution would be to place a pair of vibration sensors strategically in the bridge to perform a continuous monitoring of the data and through AI and Machine Learning generate predictive models for the wear of the bridge, and preventive maintenance schedules for them.

Bill of materials.

- Board Ultra96.
- SD card, 16 GB, Class 10 (Ultra96).
- Power Source, 5v 2.5 A, Jack, (Ultra96)
- Arduino 101 (Arduino Curie).
- Raspberry Pi Zero W.
- SD card, 16 GB, Class 10 (Raspberry Pi Zero W).
- Power Source, 5v 2.5 A, micro-USB (Raspberry Pi Zero W).
- Micro-USB to USB OTG adapter.
- Micro-USB cable (Raspberry Pi Cable).
- USB Type A Male to USB Type B Male (Arduino Cable).
- Power Bank 5v.

Optional:
- Arduino UNO.
- USB Type A Male to USB Type B Male (Arduino Cable).
- Arduino Motor Shield.
- 2x Angle Servo.
- Power Bank 5v (Another).

Code Flowchart.

<img src="https://i.ibb.co/b78TxQr/Blank-Diagram-1.png">

There are already universities in the world that make this type of census of bridges using strain gauges as they do in http://livinglabs.curtin.edu.au/#/, this shows us that the part of bridges sensing and obtaining the data is indispensable.

# Ultra96 Setup.

1. For this solution the most important part will be the use of the Ultra96 which is the last board of Xilinx for the contest Create Intelligence at the Edge of the Hackster page, in this project we will take advantage of the board in addition to have a linux operating system, we can perform acceleration of software processes by creating hardware modules on an FPGA.

1.1. Download the operating system that the Ultra96 will use
The operating system that comes by default in the SD card that comes with the Ultra96 is a system based on PetaLinux, which to start carrying out this project caused many problems due to not being able to install packages using the "apt-get" command. which was essential for the correct installation of some packages that we will use later, therefore it was decided to change to the other operating system that Xilinx offers from its official sources.

    - Link: http://avnet.me/ultra96_pynq_sd_image
    - Link: Documents in the Wiki: D.

1.2. Flash the operating system on an SD card.
To Flash the operating system in the SD, I recommend a minimum size for the SD of 16 GB.
I recommend using the following software which works in any operating system, but you can use the program that you like the most.

    - Link: https://www.balena.io/etcher/
    - Remember that before Flash the operating system you have to format the SD.

1.3. Once the operating system is flashed, place the SD card in the correct slot of the Ultra96, connect a microUSB cable to the laptop, the power cable and press the power button as shown in the following diagram.

    - Remember that the minimum power the card can have is 12 Volts at 2 A.

<img src="https://i.ibb.co/QXBvKQV/Ultra-Conections.png">

1.4. If the Flashing of the operating system and the power supply is correct, the board will turn on as follows.


Video: Click on the image

[![Ultra96 Correct Boot](https://ultra96-pynq.readthedocs.io/en/latest/_images/ultra96.png)](https://www.youtube.com/watch?v=pf8QWeNk9lU)

1.5. Once we have connected the card, we will notice that the connected memory will appear on our connected USB devices.

    - The Ultra96 creates an Ethernet PCI connection and when we see that USB memory connected it means that we are ready to start working.

<img src="https://i.ibb.co/k42JcTZ/USB.png">

1.6. Enter the web interface.

    - To access the web interface we will enter the following IP "192.168.3.1".
    - The board will ask us for an access code, the key is "xilinx".
Already in the interface you can see folders and a Jupyter Notebook, the board has by default installed Python 3 for Notebooks.

1.7. Access the files on the card.

    - To access the files on the card, through the smb connection according to the OS you will have to go to the file browser and put in the address bar.
        - \\ 192.168.3.1 \ xilinx (for Windows, tested on Windows 10).
        - smb: //192.168.3.1/xilinx (for Linux, tested on Ubuntu 18.04)
        - On the Mac, it is not possible to connect correctly due to the USB Ethernet PCI connection protocol. I recommend that you use another operating system to be able to configure the board (maybe you can use a virtual machine with linux)
1.8. Download and save the necessary files on the board.
Download the files from the github repository.

    - Link: https://github.com/EddOliver/BBM-Bridge-Baby-Monitor/
    - Copy and paste the folder called "Hackster" in the path "/ xilinx / jupyter_notebooks".
    - Copy and paste the contents of the "FPGA" folder in the following path "/ xilinx / pynq / overlays".


1.9. Now we will make the configuration of the Ultra96 installing the corresponding packages so that our code runs without problems.

    - For the initial configuration inside the "Hackster" folder you have to open the notebook called "First_Setup.ipynb".
    - Once inside the Notebook, run the command in point 1.
    - This command configures the WiFi network on the board, in order to download the packages.
    - If it is connected correctly, the text "WiFi Ready" will be printed.
    - When it finishes executing we will run the command of subsection 2 which downloads the necessary packages for the board to work.
    - This process will take between 5 and 15 min depending on the speed of the internet.
    - If all this process goes well, a sign that says "All the Packages was installed correctly" will be printed on the bottom of the console.

When this process is finished, execute the command in part 3 to obtain the IP of the board. THIS PROCESS IS VERY IMPORTANT SINCE THE IP WILL BE USED LATER FOR THE COMMUNICATION OF THE RASPBERRY AND THE ARDUINO BY MQTT.

1.10. Congratulations! We have made the corresponding configurations in the Ultra96 for now.

# Accelerometer configuration in the Arduino Curie.

2. For this project this sensor was used because it was the sensor that we had at hand, it is also more interesting to show the integration of an Arduino Curie also called Arduino 101 to a solution of this type.

PD.It is also possible to use any other Accelerometer and connect it directly to the Raspberry Pi Zero W that we will configure later.

2.1. Arduino curie configuration on the PC.
    - For this step you have two options:
        - Use the Arduino WebEditor with which you do not have to install anything, but you have to have an account in the arduino page to access, create it is free: 3
        - Link: https://create.arduino.cc/

    - If you prefer to use the editor in the Arduino IDE Desktop Editor, read the official Arduino 101 documentation for information on how to install the arduino curie according to your operating system.
        - Link: https://www.arduino.cc/en/Guide/Arduino101


2.2.  Program the Arduino Curie with the code provided.

    - If you chose to use the WebEditor:
    - The code link: https://create.arduino.cc/editor/Altaga/88928a34-3c20-4968-96a6-6413fe2f357b/preview
    - If you chose to use the Desktop Editor:
    - In the github folder called "AccelerometerCurie" you will find the .ino that you have to program in the Arduino Curie.








1.- Using temperature with humidity, soil moisture and soil temperature sensors, we used a Pycom FiPy dev board with Sigfox technology to obtain sensor data every 6 min. Sigfox chosen because the characteristics of long range and low power are excellent for remote areas.

- Each batch of sensing is done at this frequency to send 120 data per day and not pass the data quota of Sigfox which is 140 data packets per day.

- For this system it was decided to use an Arduino board to obtain the data from the sensors (using the vast array of libraries from Arduino) and send them through Serial at 9600 baud rate to the Pycom FiPy board.

- Once on the Pycom board we receive the data from the sensors and through Sigfox we send them to the Sigfox Backend platform.

<img src="https://image.ibb.co/bGNtpT/chacala3.png">

On the image above you can see at: A)The main sensor circuit, with the Pycom FiPy with Sigfox and the sensors connected, also the solar power management. B) The irrigation system circuit that uses a Particle Photon and a Solenoid Valve. And C) an implementation of the system.

<img src="https://image.ibb.co/h5drR8/Whats_App_Image_2018_07_29_at_01_22_33.jpg" width="600">

This other image shows the finished Hardware product, with the irrigation system on the left and the sensor system with its solar panel on the right.

2.- Once the data is in the Sigfox Backend, we send the data through a callback to the Thingspeak website through its API (more information in the link below).

Link: https://github.com/EddOliver/AggroFox/tree/master/Sigfox%20Configuration/Aggrofox%20Conf

3.- Once we have the data at Thingspeak, through the Thingspeak API we send the data to IBM Bluemix.

- On the Bluemix platform, we made it possible to develop almost any application with the obtained data. (All the applications are based on Node Red to make the prototyping easier).

- Examples of these applications:

    Generate databases of our crops and their conditions.

    Do data analysis to obtain predictive models in the long term.

    Water automation systems with the data obtained (as we do in this project).
    
    Crop yield analysis.

3.1- We made a Dashboard with the data obtained for the complete and simple visualization of the data.

<img src="https://image.ibb.co/hGifKT/68747470733a2f2f696d6167652e6962622e636f2f656a6e7934542f6e6f6465646173682e6a7067.jpg">

In this image you can see the Node-RED flow and the Dashboard we made.

<img src="https://image.ibb.co/k0baOo/EFDF60_E8_0_E94_4802_8_D96_2_DF7_F35331_FA.jpg">

<img src="https://image.ibb.co/m7yKDo/Whats_App_Image_2018_07_29_at_01_22_13.jpg" width="300"> <img src="https://image.ibb.co/j3kczT/Whats_App_Image_2018_07_29_at_01_22_14.jpg" width="300">

These other images above show the Web Desktop Dashboard and some screenshots of the mobile version.

- For the application, we made a data crossing with the OpenWeatherMap API, to perform the control of an electrovalve connected to a Particle Photon microcontroller.

- The crossing of data obtained is used to check if that day is going to rain and thus not use irrigation water in crops.

- Also if the system detects that water is needed in the field by the humidity sensors, the irrigation system is turned on.

- In turn once a day an email will be sent to the farmer with the general information of his field or he can check anytime on his dashboard.

- Also everytime the irrigation system is online, a notification will be sent.

# Here are some images of the solution implemented on various crops:

<img src="https://image.ibb.co/dre1B8/Whats_App_Image_2018_07_29_at_21_23_06_1.jpg" width="300"> <img src="https://image.ibb.co/iS4CJo/Whats_App_Image_2018_07_29_at_21_23_09_1.jpg" width="300"> <img src="https://image.ibb.co/gqfmdo/Whats_App_Image_2018_07_29_at_21_23_06.jpg" width="300">

In the images you can see an Hydroponic Chili,an Onion Culture and the implementation on a Fig Tree

# Here is a Video of AggroFox in action!, click on the image:

[![AggroFox VIDEO!](https://image.ibb.co/n84O68/agrofox_Recuperado.png)](https://www.youtube.com/watch?v=7SUabreZY28& "AggroFox")


## Where should I start:

1.-Do the first configuration for your board.

Link: https://github.com/EddOliver/AggroFox/tree/master/Sigfox%20Configuration/First%20Configuration

2.- Enter the following folder: AggroFox Configuration, and complete all the steps to perform the corresponding configuration.

Link: https://github.com/EddOliver/AggroFox/tree/master/Sigfox%20Configuration/Aggrofox%20Conf

3.- Do the Arduino configuration.

Link: https://github.com/EddOliver/AggroFox/tree/master/Arduino%20Code

4.- Do the Pycom configuration.

Link: https://github.com/EddOliver/AggroFox/tree/master/Pycom%20Code

5.- Make the circuits:

Link: https://github.com/EddOliver/AggroFox/tree/master/Circuit

6.- Link it to IBM IoT Cloud for amazing dashboards, data storage and access to other cloud services.

Link: https://github.com/EddOliver/AggroFox/tree/master/IBM%20cloud%20AggroFox

7.- Automation of irrigation via IBM cloud with weather forecast.

Link: https://github.com/EddOliver/AggroFox/tree/master/Irrigation%20System

8.- Going Green (Add a Solar panel to your sensor module).

Link: https://github.com/EddOliver/AggroFox/tree/master/Solar%20Power

Enjoy!!


# Future Rollout

• Adding a water fluxometer to know exactly how much water we use.

• Custom PCB for all the hardware components.

• Maybe migrate to the SiPy version of the Pycom Board.

• Get the data to a SQL database for long term predictive ML models.

• Expand to the use of several other clouds such as AWS and Google cloud which we already dominate.

• Replace the Particle Photon with Sigfox for the actuators so it uses only one communication platform.


# References:

All the information about the technology used and direct references are in our wiki:

Wiki: https://github.com/EddOliver/AggroFox/wiki

Top

* [Table of Contents](#table-of-contents)
