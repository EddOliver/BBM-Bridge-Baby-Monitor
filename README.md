# BBM: Bridge-Baby-Monitor

<img src="https://i.ibb.co/TR9vzWw/BBMLogo.png" width="500">

Intelligent IoT Edge solution for structural monitoring, based on the analysis of natural frequencies in bridges. 

<img src="https://i.ibb.co/y0FNfCq/Fisicoa.jpg">

# Table of contents
* [Introduction](#introduction)
* [Problematic](#problematic)
* [Our Solution](#our-solution)
* [Ultra96 Setup](#ultra96-setup)
* [Accelerometer configuration for Arduino Curie](#accelerometer-configuration-in-the-arduino-curie)
* [Configuration of the Raspberry Pi Zero](#configure-the-raspberry-pi-zero)
* [Connection diagrams for all the devices](#connection-diagrams-of-all-the-devices)
* [Time to perform the first test](#time-to-perform-the-first-test)
* [Create your Dashboard](#create-your-dashboard)
* [Tests](#tests)
* [Results](#results)
* [How to make your own FPGA developments in the Ultra96](#how-to-make-your-own-fpga-developments-in-the-ultra96)
* [Future Rollout](#future-rollout)
* [References](#references)

## Introduction:

According to the 2017 Infrastructure Report Card published by the American Society of Civil Engineers (ASCE), almost 40 percent of the 614,387 bridges in the United States are at least a half century old. Almost 10 percent were structurally deficient in 2016. On average, 188 million vehicles cross structurally deficient bridges each day. People who manage them are constantly looking for more cost-effective ways to keep them in good repair.

Perhaps the biggest issue affecting people who maintain bridges today is that they are forced into being reactive in how they approach their work, rather than proactive. They must repair the worst damage to structures rather than use limited resources to keep them in good shape. As with most things, being reactive is never as effective as planning ahead.

A “worst first” approach is not a cost-effective way to keep bridges healthy. It evolves into a vicious cycle where more and more budget dollars go toward emergency repairs. This underfunds proactive maintenance projects that could keep bridges out of the deficient category entirely.

According to ASCE, the current cost to rehabilitate the nation’s bridges is more than $120 billion.
As with most things earthquakes and other disasters also can suddenly pass and if there's not a precise monitoring, issues could be fatal.

This is quite important for our team as he had to live this predicament in 2017. On September the 7th of 2017 there was an earthquake in Mexico City. At about 8.1 in the Richter scale it caused structural damage to several buildings around the city and a couple pedestrian bridges in the authors' University. And then we had a big earthquake in September 19th that decimated these damaged structures, and in the case of our University this was the result. 

Video: Click on the image

[![TERREMOTO 7.1 | 19 DE SEPTIEMBRE 2017 | CDMX TEC DE MONTERREY](https://image.flaticon.com/icons/png/128/44/44431.png)](https://www.youtube.com/watch?v=47jqaRRaQAM)

With better monitoring and alert systems we could have probably spotted on these failures and prevented the crisis, or maybe acted on it faster.

## Problematic:

<img src="https://bridgemastersinc.com/wp-content/uploads/2016/06/I-35W-Mississippi-River-Bridge-collapse.jpg" width="800">

The main problematic is the little monitoring that bridges have, and the structural damage that they can have over time and as the lack of preventive maintenance can cause a partial or total failure of the bridge.

The main problems by which a bridge can fail and fall are:

- Infrastructure failure.
- Structrural collapse
- Lack of good maintainance
- Wear and Tear
- Floods.
- Unexpected events
- A combination of issues.

If we could notice a failure in the structure beforehand this would cut costs of maintenance and also prevent any disaster, therefore that is the main problem we want to fight with our solution.

Other forms of predictive solutions in bridges do not provide accurate data, or require a technician to go directly to the place to check manually.

## Our Solution:

Our solution in placing a pair of vibration sensors strategically in bridges to perform a continuous monitoring. And through AI and Machine Learning we will generate predictive models for the wear and tear of the bridge, and to recommend the user scheduling for preventive maintenance. We will use these algorithms and then accelerate them via the potent FPGA on top of the Ultra96 for maximum performance.

Bill of materials.

- Ultra96 Board .
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

Optional (Our own testing platform):
- Arduino UNO.
- USB Type A Male to USB Type B Male (Arduino Cable).
- Arduino Motor Shield (for Servos).
- 2x small Servo motors.
- Power Bank 5v (Another).

Code Flowchart.

<img src="https://i.ibb.co/b78TxQr/Blank-Diagram-1.png">

Several Universities are already performing this type of census in structures using strain gauges such as: http://livinglabs.curtin.edu.au/#/, this shows us that structural sensing is indispensable for Industry 4.0.

## Ultra96 Setup:

1. The most important part, for this solution, will be the use of the Ultra96 which is Xilinx and 96 boards' latest board. In this project we will take maximum advantage of the board in addition to its linux operating system, to perform software acceleration by creating hardware modules on the Ultra96's FPGA.

1.1. Download the operating system for the Ultra96:
The operating system that comes by default in the SD card of the Ultra96, is a system based on PetaLinux. It caused many problems for us due to its inability to install packages using the "apt-get" command. The command was essential for the correct installation of some packages that we would be using later, therefore we settled to use another operating system that Xilinx offers from its official sources: Pynq. And here it is:

- Link: http://avnet.me/ultra96_pynq_sd_image
- Link: Documents in the Wiki: D.

1.2. Flashing the operating system on an SD card.
To Flash the operating system in the SD card, we recommend a minimum size of SD of 16 GB.
We recommend the following software which works in any operating system, but you can use your preferred one:

- Link: https://www.balena.io/etcher/
- Remember that before Flashing the operating system you have to format the SD.

1.3. Once the operating system is flashed, place the SD card in the correct slot of the Ultra96, connect a microUSB cable to the laptop, also the power cable, and press the power button as shown in the following diagram.

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
- Already in the interface you can see folders and a Jupyter Notebook, the board has by default installed Python 3 for Notebooks.

1.7. Access the files on the card.

- To access the files on the card, through the smb connection according to the OS you will have to go to the file browser and put in the address bar.
    - \\ 192.168.3.1 \ xilinx (for Windows, tested on Windows 10).
    - smb: //192.168.3.1/xilinx (for Linux, tested on Ubuntu 18.04)
    - On the Mac, it is not possible to connect correctly due to the USB Ethernet PCI connection protocol. I recommend that you use another operating system to be able to configure the board (maybe you can use a virtual machine with linux)

1.8. Download and save the necessary files on the board.
Download the files from the github repository.

- Link: https://github.com/EddOliver/BBM-Bridge-Baby-Monitor/
- Copy and paste the folder called "Hackster" in the path "/xilinx/jupyter_notebooks".
- Copy and paste the contents of the "FPGA" folder in the following path "/xilinx/pynq/overlays".

1.9. Now we will make the configuration of the Ultra96 installing the corresponding packages so that our code runs without problems.

- For the initial configuration inside the "Hackster" folder you have to open the notebook called "First_Setup.ipynb".
- Once inside the Notebook, run the command in point 1.
- This command configures the WiFi network on the board, in order to download the packages.
- If it is connected correctly, the text "WiFi Ready" will be printed.
- When it finishes executing we will run the command of subsection 2 which downloads the necessary packages for the board to work.
- This process will take between 5 and 15 min depending on the speed of the internet.
- If all this process goes well, a sign that says "All the Packages was installed correctly" will be printed on the bottom of the console.

When this process is finished, execute the command in part 3 to obtain the IP of the board. **THIS PROCESS IS VERY IMPORTANT SINCE THE IP WILL BE USED LATER FOR THE COMMUNICATION OF THE RASPBERRY AND THE ARDUINO BY MQTT.**

1.10. Congratulations! We have made the corresponding configurations in the Ultra96 for now.

## Accelerometer configuration in the Arduino Curie:

2. For this project this sensor was used because it was the sensor that we had at hand, it is also more interesting to show the integration of an Arduino Curie also called Arduino 101 to a solution of this type.

**PD.It is also possible to use any other Accelerometer and connect it directly to the Raspberry Pi Zero W that we will configure later.**

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


## Configure the Raspberry Pi Zero:

3. For this point it is also possible to use instead of the Arduino Curie and the Raspberry Pi Zero, an ESP32 or an ESP8266 with an accelerometer, connecting it through MQTT.

3.1. Download the operating system of the Raspberry Pi Zero.

- To download the operating system of the Raspberry enter the following link:
- Link: https://downloads.raspberrypi.org/raspbian_lite_latest
- The version that we will download will be the lite version to not load work to the raspberry.

3.2. Flash in the SD operating system as shown in point 1.2 but with raspbian.

- Flash with Etcher the raspberry operating system but DO NOT put it on the raspberry yet.

3.3. Create a wpa_supplicant for the connection of the raspberry to the internet.

- Since we have the operating system flashed, we copy and paste the files from the "RaspberryPi" folder directly into the SD card.
- Once we open the "wpa_supplicant.conf" file with a text editor
- In between the quotes of ssid write your wifi network and the psk the network key.

        country = us
        update_config = 1
        ctrl_interface =/var/run/wpa_supplicant

        network =
        {
        scan_ssid = 1
        ssid = "yourwifi"
        psk = "yourpassword"
        }


- We save the changes and remove the SD from the PC.

3.4. We place the SD in the raspberry and connect it to its power source.

- The power source of a Raspberry Pi Zero is recommended to be from 5 volts to 1A minimum.

3.5. Once the raspberry has already started, we need to access it through SSH or with a keyboard and a monitor.

- If you want to access it through SSH we need your IP.
- In order to analyze your network and obtain the number we will have to use one of the following programs.
- Advanced IP Scanner (Windows) or Angry IP Scanner program (Windows, Mac and Linux).
- We can see in the screenshot below how we got the Raspberry IP.

<img src="https://i.ibb.co/KLThvst/AngryIP.png"> 

3.6. Copy the program inside the "RaspberrySoft" folder using FileZilla to the raspberry.

- To pass the file via wifi to the raspberry we have to download another program called "FileZilla".
- Link: https://filezilla-project.org/download.php?type=client
- Once we have the program, we open it and put the data in the upper bar to access the raspberry.

Host: RASPBERRYIP              Username:pi           Password:raspberry             port:22

<img src="https://i.ibb.co/4Y80V96/filezilla.png"> 

- Press Quickconnect.
- Once we enter the Raspberry, we copy the file "exe.py" in the folder "/home/pi".

3.7. Since we have the file in the raspberry we will have to connect the raspberry with ssh.

- To connect using ssh to the raspberry we need the Putty program.
- Link: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
- This program will let us access the command console of the raspberry.
- In Linux, just open the terminal and put the following command.

        ssh pi@RASPBERRYIP

<img src="https://i.ibb.co/PxP86Xz/terminal.png">

- Password: “raspberry”

<img src="https://i.ibb.co/NthRqRc/terminal2.png">

3.8. First, we will install the necessary libraries for our program to work.

- For it to work we just have to put the following command.

      sudo apt-get update && sudo apt-get install -y python-pip && pip install pyserial paho-mqtt

- This command will install the pyserial and paho-mqtt libraries

3.9. Once the console is open, we will edit the file that we passed in the previous paragraph to configure the IP of the Ultra96.

- In the terminal of the raspberry we will write the following command.
     
    sudo nano exe.py

<img src="https://i.ibb.co/JCpSFDJ/terminalcomand.png">

- The command will open the text editor where we can go through the file "exe.py".
- We go down to the part shown in the image and instead of the text "ULTRA96IP" we will put the IP that we obtained in subsection 1.9.

<img src="https://i.ibb.co/gwmdqyZ/Putty.png">

- Since we change that text we will save the changes made by pressing "ctrl + o" and enter, and to exit the editor press "ctrl + c".

3.10. Put the program that runs whenever you turn on the raspberry.
In order for the program to start together with raspbian and we no longer have to execute it, we will write the following command.

    sudo nano /etc/rc.local

<img src="https://i.ibb.co/t46LWqc/start.png">

- Inside the file we will have to write the following as shown in the image.

      sudo python /home/pi/exe.py
      
<img src="https://i.ibb.co/177pdcd/start2.png">

- As we add that text we will save the changes made by pressing "ctrl + o" and enter, and to exit the editor press "ctrl + c".

3.11. Once we finish editing this file we are ready to connect everything and run our program in the Ultra96.
Before proceeding, disconnect the raspberry and the arduino from their sources because we are going to connect them to each other.

## Connection diagrams of all the devices:

4.1. Schematic:

<img src="https://i.ibb.co/QXBvKQV/Ultra-Conections.png" width="400"><img src="https://i.ibb.co/wYhBXRr/RPIEsquema.png" width="400">

4.2. Real connections:

- The black box below the raspberry is a power bank of 5v - 10000mA.

<img src="https://i.ibb.co/y0FNfCq/Fisicoa.jpg">

## Time to perform the first test:

5.1. Connect the Ultra96 to the network and activate Mosquitto.

- For this first test we will connect the Ultra96 first as shown in the diagram of point 4. and we will turn it on.
- We will access the web interface where the Jupyter Notebooks are.
- We will enter the Hackster folder.
- We opened the "Bridges.ipynb" and "Wifi_Mosquitto.ipynb" notebook.
- We entered the "Wifi_Mosquitto.ipynb" notebook.
- We put our data of SSID and PSW.
- We give run to run the program to connect to our WiFi network and activate the Mosquitto broker.

5.2. Connection to the Ultra96 broker.

- Once it connects correctly, we enter the "Bridges.ipynb" notebook.
- We execute the main code, if everything goes well we will notice as it says "Connected to broker" meaning that there is a correct connection.

5.3. Connect the sensor module.

- Connect your power supply to the raspberry and go!
5.4. Check that the data reaches the board.

- If the data is arriving correctly, according to the sampling specifications that we have programmed, we will receive these notifications that the frequencies are being saved in a CSV file.

<img src="https://i.ibb.co/cyTPBrJ/Results.png">

5.5. Once all the data samples have been made, the system will take the stored data and load them into the machine learning model so that it learns in each iteration and becomes more precise, this being a model of continuous learning.

<img src="https://i.ibb.co/Q9nnM3N/results1.png">

## Create your Dashboard:

//////////////////////TRADUCIR////////////////

6. Para finalizar debemos realizar un dashboard con Watson IoT Cloud para visualizar los datos en tiempo real.

- En el codigo principal estamos posteando en Watson IoT, el como crear la credenciales ya esta en otro de nuestros repositorios.

- How Create a Cloudant instance (Change the credential in the "Bridges" code for your credentials).

https://console.bluemix.net/docs/services/Cloudant/tutorials/create_service.html#creating-an-ibm-cloudant-instance-on-ibm-cloud

- Your API for pushetta is in this link (You need to create an account first, its free :3).

http://www.pushetta.com/my/dashboard/

- How Create a Watson IoT application.

https://github.com/altaga/The-Ultimate-IBM-Watson-IoT-Platform-Guide

- Para este caso vamos a ir a la esquina superior a la seccion de "Boards".

<img src="https://i.ibb.co/hmBx1pK/1png.png">

- Una vez en esta seccion creamos una nueva board.

<img src="https://i.ibb.co/ZY5DYdY/2.png">

- A la board le ponemos cualquier nombre.

<img src="https://i.ibb.co/JjT202v/3.png">

- En la esquina superior derecha creamos dos nuevas cards (Una "Line chart" y una "Value").

<img src="https://i.ibb.co/n8Pjmwk/4.png">

- Para cada card debemos seleccionar el dispositivo.

<img src="https://i.ibb.co/wRT5w2v/5.png">

- Para la Line chart usaremos la siguiente configuracion de events and properties, esta grafica va a mostrar los valores de riesgo en XYZ en tiempo real.

<img src="https://i.ibb.co/NC6ktjx/6.png" width="400"><img src="https://i.ibb.co/qpsvRGG/7.png" width="400">

- Por ultimo en la card de "Value" usaremos la siguiente configuracion.

<img src="https://i.ibb.co/XLsrZj1/8.png">

- Una vez hemos terminado esta configuracion ya tendremos nuestro dashboard.

///////////////////////TRADUCIR/////////////////

## Tests:

7. Since the project was made, it was time to test it on a platform where we could recreate an oscillatory movement that the sensors could capture.

7.1. Test platform with Arduino.

A platform with an arduino system and a shield of motors was realized, which served to recreate a harmonic abdnormal movement with the motors and in addition to make it portable it was decided to use a Power Bank.

<img src="https://i.ibb.co/L8R6m8N/Platform.jpg">

- Once the platform works, we put the sensor on the platform so that we could get an abnormal answer.

Video: Click on the image

[![BBM Test Platform](https://cdn.iconscout.com/icon/premium/png-256-thumb/bridge-199-673478.png)](https://youtu.be/KuoN3N4PJSM)

- The results showed how the notification of the bridge when maintenance is required was sent correctly when the sensor measures an excessive amplitude over an X frequency.

7.2. Actual test on pedestrian bridge.

- For the final test it was decided to take the system to a pedestrian bridge in our university, we monitoring every so often to verify that the system works correctly.

Video: Click on the image:

[![BBM - Demo](https://i.ibb.co/TR9vzWw/BBMLogo.png)](https://youtu.be/4BNzPV9-NgQ)

## Results:

8.1. The results of the tests in the simulator and the tests in the field were the expected ones, the effective reaction system and the stimuli generated. When analyzing the data of the field tests, the following results were obtained.

<img src="https://i.ibb.co/pQnbj4t/Frecuencia.png">

8.2. We obtained that the greatest amplitude in the bridge was generated at 0.33 Hz. This being the natural frequency of the bridge, the objective of the model we obtain will be to analyze if the bridge through maintenance is decreasing that amplitude in its natural frequency.

Useful guides:

- How Create a Watson IoT application.

https://github.com/altaga/The-Ultimate-IBM-Watson-IoT-Platform-Guide

- How create a Cloudant client:
https://console.bluemix.net/docs/services/Cloudant/tutorials/create_database.html#creating-and-populating-a-simple-ibm-cloudant-database-on-ibm-cloud

## How to make your own FPGA developments in the Ultra96:

9. For this part of the tutorial I will show you how to make your own custom modules for the FPGA in a simple way using the two softwares provided by Xilinx, which they are.

- Vivado Design Suite - HLx Editions and Vivado High-Level Synthesis (Included in the Suite)
- Direct Download: https://www.xilinx.com/member/forms/download/xef-vivado.html?filename=Xilinx_Vivado_SDK_2018.2_0614_1954.tar.gz

9.1. Development of module with Vivado code High-Level Synthesis.

- We enter Vivado High-Level Synthesis, where the following options menu will appear and where we will select "Create New Project"

<img src="https://i.ibb.co/g9PYkm0/1.png">

- In the "Project name" type the name you want.
- In the route where it will be saved, I recommend it to be a personalized route where you know it is going to be saved (Note this route because it will serve later).

<img src="https://i.ibb.co/QNMn5QH/1-1.png">

- In "Top Function" write the name of the function, I recommend that it be a simple name and that you remember it for later.

<img src="https://i.ibb.co/f1FCBkw/3.png">

- We will go to the "New File" button and create a new file as shown in the image.

<img src="https://i.ibb.co/RTr6QXB/4.png">

- When we finish creating the file and add it, we will give it "Next" twice and a screen like the following one will appear, where we will select "Part Selection" to choose the part that has the Ultra96.

<img src="https://i.ibb.co/FXpYrvB/5-5.png">

- The part of the Ultra96 is an "xczu3eg-sbva484-1-e"

<img src="https://i.ibb.co/fkNHkkT/5.png">

- Once this process is finished we will go to the upper left of the project and open the tab that says "Source" and we will double click on our module to open it.

<img src="https://i.ibb.co/S58QCgF/7.png">

- Within our module we will write the following code.

        // DONT MODIFY
        #include "ap_axi_sdata.h"
        #include "ap_int.h"

        // DONT MODIFY
        typedef ap_axiu<32,1,1,1> stream_type;


        // MODIFY
        float YOUR_OUTPUT=0;
        float IN_NUMBER=0;

        // DONT MODIFY
        void YOUR_MODULE_NAME(stream_type* in_data, stream_type* out_data) {
        #pragma HLS INTERFACE ap_ctrl_none port=return
        #pragma HLS INTERFACE axis port=in_data
        #pragma HLS INTERFACE axis port=out_data

        // MODIFY
        // Your code structure in c goes from here

        //This variable is the entry of the data sent by the DMA number by number.
        IN_NUMBER = in_data->data;

        // This is my structure to always get the highest number that has entered at the exit.
        if(YOUR_OUTPUT < IN_NUMBER)
        {
            YOUR_OUTPUT = IN_NUMBER;
        }

        /*
        I will send to this structure a series
        of data within an array and therefore
        send me the maximum value found in the array.
        */

        // To here


        // This is the declaration of the exit ports necessary to operate the DMA.

        // DONT MODIFY
        out_data->data = YOUR_OUTPUT;
        out_data->dest = in_data->dest;
        out_data->id = in_data->id;
        out_data->keep = in_data->keep;
        out_data->last = in_data->last;
        out_data->strb = in_data->strb;
        out_data->user = in_data->user;
        }

- The code is commented on what parts you should write and what not, this in order to create a code based on the data transfer by DMA, which is the fastest hardware way to move data and also be able to implement any structure in C that is required, which is very useful.

- Once the writing of the code is finished, we will go to the top of the window to the synthesis button to compile the code.

<img src="https://i.ibb.co/rZncmdM/8.png">

- If everything went well the code will be compiled and it will allow us to create our RTL, which is the file that we will import to Vivado Design Suite - HLx Editions to put it in our design to blocks of the FPGA.

<img src="https://i.ibb.co/B6BF4pS/9.png">

8.2. Development of overlay with blocks in Vivado Design Suite - HLx Editions.

- First when opening the program we will have to create a new project.

<img src="https://i.ibb.co/f8gWx42/10.png">

- We create the name of the project with "ANY_NAME"

<img src="https://i.ibb.co/XDXbTsn/11.png">

- In this option we put "do not specify sources at this time"

<img src="https://i.ibb.co/hf1PVQr/12.png">

- We selected the Ultra96 in the selection of boards.

<img src="https://i.ibb.co/TRWm0P1/13.png">

- Already in the project we select the option "Create Block Diagram".

<img src="https://i.ibb.co/pLFGTWB/14.png">

- We press the Add IP button.

<img src="https://i.ibb.co/FKMTKBt/15.png">

- In the search menu we type "Ultra" and select the option of the image to add the FPGA that has the Ultra96.

<img src="https://i.ibb.co/DQthvMf/16.png">

- It will open a module like this.

<img src="https://i.ibb.co/V9M1PkK/17.png">

- In the part above we press this button so that the block is configured.

<img src="https://i.ibb.co/sRhnFwj/18.png">

- We add a DMA module.

<img src="https://i.ibb.co/cyPZzzY/19.png">

- We double-click on the module and remove the "Enable Scatter Gather Engine" option.

<img src="https://i.ibb.co/s3f8YwP/21.png">

- We go to Tools - Settings - IP - Respository.

<img src="https://i.ibb.co/6HYwYjv/23.png">

- In the IP Repositories option, we click on Add.

<img src="https://i.ibb.co/r6fCCfh/24.png">

- We select the folder where we store our module.

<img src="https://i.ibb.co/w46JWFg/25.png">

- Select your module and add it to your design.

<img src="https://i.ibb.co/PmvgG84/26.png">

- Since we have both DMA modules and your module we connect them as follows.

<img src="https://i.ibb.co/mGCGZtd/29.png">

- We double click on the Ultra module where you will see this menu.

<img src="https://i.ibb.co/V3BFs7s/30.png">

- We leave the PS-LS Configuration section and add the following port.

<img src="https://i.ibb.co/rfppp5H/31.png">

- Once we have finished our designs, we press the next button to automatically connect everything, this process we will do as many times as this button appears so that the connections are finished.

<img src="https://i.ibb.co/k6Z8hk8/32.png">

- Once it is finished, we will have a module similar to this one.

<img src="https://i.ibb.co/yqLSx8p/33.png">

- To make reference in the python code we will have to change the name of the DMA module in the Block Properties menu as seen in the image.

<img src="https://i.ibb.co/zmnRg9J/34.png">

- Once this is over we go to the Sources tab and in our block we give "Create HDL Wrapper", remember well where you save it because it will be an important file for our project, also give it a simple name like "model.tcl".

<img src="https://i.ibb.co/grnYc4M/35.png">

Once the process is finished, we will press the "Generate Bitstream" button.

<img src="https://i.ibb.co/LdR8v7V/36.png">

- The file was created in the path where the project ~ / vivado / ANY_NAME / ANY_NAME.runs / impl_1 / design_1_wrapper.bit was saved

- That file you copy and paste it into the folder where you saved the tcl and you will also give them both the same name.

- Once this is done we will paste both files in the Overlays folder of the Ultra96 as we did in subsection 1.8.

9.3. How to call our FPGA module in Python.

- Copy this code to a jupyter notebook for the module to work.

        from pynq import Overlay
        from pynq import DefaultIP
        import pynq.lib.dma
        from pynq import Xlnk

        xlnk = Xlnk()

        # Change this path with the path of your bitstream.

        overlay = Overlay('/home/xilinx/pynq/overlays/model.bit')

        # Write the name of your module as shown in the tutorial.

        dma = overlay.MY_DMA

        # Here you have to put the length of the arrangement that you will send to the module.

        in_buffer = xlnk.cma_array(shape=(YOUR_ARRAY_SIZE,), dtype=np.float32)
        out_buffer = xlnk.cma_array(shape=(YOUR_ARRAY_SIZE,), dtype=np.float32)

        # Copy your array data in in_buffer before run this part

        dma.sendchannel.transfer(in_buffer)
        dma.recvchannel.transfer(out_buffer)
        dma.sendchannel.wait()
        dma.recvchannel.wait()

        # After this, the data was in your out_buffer

9.4. Here we show some results where we show that using FPGA designs is an advantage.

<img src="https://i.ibb.co/HtLYmg0/estadistica.png">

## Future Rollout

DOKI

## References:

All the information about the technology used and direct references are in our wiki:

Wiki: https://github.com/EddOliver/BBM-Bridge-Baby-Monitor/wiki

Top

* [Table of Contents](#table-of-contents)
