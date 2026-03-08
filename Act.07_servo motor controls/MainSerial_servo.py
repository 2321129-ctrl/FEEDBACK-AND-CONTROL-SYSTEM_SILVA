import serial
import time

def run_servo_controller(port, baud_rate=9600):
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connecting to Arduino on {port}...")
        
        # Wait for Arduino to reset
        time.sleep(2) 
        ser.reset_input_buffer() 
        print("Connection established. Type 'exit' to quit.")

        while True:
            user_input = input("\nEnter angle (0-180): ").strip().lower()
            if user_input == 'exit':
                break
                
            try:
                angle = int(user_input)
                if 0 <= angle <= 180:
                    ser.write(f"{angle}\n".encode('utf-8'))
                    
                    # INCREASED DELAY: Give the Arduino time to process and reply
                    # 0.1s is often too fast; 0.2s or 0.3s is more reliable
                    time.sleep(0.3) 
                    
                    # Check for the response from the Arduino
                    if ser.in_waiting > 0:
                        feedback = ser.readline().decode('utf-8').strip()
                        
                        # SUCCESS PRINT: This displays the Arduino's confirmation
                        print(feedback) 
                    else:
                        print("Waiting for Arduino response...")
                else:
                    print("Error: Range is 0-180.")
            except ValueError:
                print("Error: Please enter a valid number.")

    except serial.SerialException as e:
        print(f"Serial Error: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Port closed.")

if __name__ == "__main__":
    run_servo_controller(port="COM4")