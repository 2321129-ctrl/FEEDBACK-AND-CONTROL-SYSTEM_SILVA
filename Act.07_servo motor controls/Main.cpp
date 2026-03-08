#include <Servo.h>

Servo myServo;
const int servoPin = 9;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);

  // Reduces the delay when parsing numbers from the serial buffer
  Serial.setTimeout(50); 

  // Initial position
  myServo.write(90); 

  Serial.println("Enter angle (0-180):");
}

void loop() {
  // Wait until data is available in the buffer
  if (Serial.available() > 0) {
    
    // Read the incoming integer
    int angle = Serial.parseInt();

    // Validate the input range
    if (angle >= 0 && angle <= 180) {
      myServo.write(angle);
      
      // Give the motor a moment to physically move
      delay(150); 

      // Send feedback back to the Python/PC script
      Serial.print("Success: Servo moved to ");
      Serial.print(angle);
      Serial.println(" degrees.");
    } 
    else {
      // Handle out-of-bounds numbers
      Serial.print("Error: ");
      Serial.print(angle);
      Serial.println(" is out of range (0-180).");
    }

    // Flush the buffer to remove trailing newlines (\n) or carriage returns (\r)
    while (Serial.available() > 0) {
      Serial.read();
    }
  }
}
