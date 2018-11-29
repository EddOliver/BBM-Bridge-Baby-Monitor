#include "CurieIMU.h"

float ax, ay, az;         // Acceleration Values
float cx,cy,cz;           // Auto-Calibration

void setup() {
  Serial.begin(115200);   // initialize Serial communication
  while (!Serial);        // wait for the serial port to open

  // initialize device
  Serial.println("Initializing IMU device...");
  CurieIMU.begin();

  // Set the accelerometer range to 2G
  CurieIMU.setAccelerometerRange(2);
  delay(30);                // Delay While the accelerometer start correctly (DONT TOUCH!)
  CurieIMU.readAccelerometerScaled(cx, cy, cz); //We obtain the Auto-Calibration values

}

void loop() {
  CurieIMU.readAccelerometerScaled(ax, ay, az);
  Serial.println("x:"+ String(ax-cx));
  // This delay is 100 data per second 10 miliseconds / 3, 3333 micro seconds per axis data.
  delayMicroseconds(3333);  
  Serial.println("y:"+ String(ay-cy));
  delayMicroseconds(3333);
  Serial.println("z:"+ String(az-cz));
  delayMicroseconds(3333);
}
