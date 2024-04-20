# Include the library files

import RPi.GPIO as GPIO
import time
from smbus import SMBus
import bluetooth
GPIO.setmode(GPIO.BOARD)
bus = SMBus(1)

# Variable Declaration
pir_pin = 8
relay1 = 13
relay2 = 3   
relay3 = 15
relay4 = 18
relay5 = 22
relay6 = 11
relay7 = 29

led = 7
led_pin1 = 3
led_pin2 = 5
x = True

# Pump timimg
Pump1_timing = 44.150
Pump2_timing = 44.150   #change according to liquid product
Pump3_timing = 44.150   #change according to liquid product

motorstatus1 = True
motorstatus2 = True
motorstatus3 = True
motorstatus4 = True
motorstatus5 = True
motorstatus6 = True
motorstatus7 = True
motorstatus8 = True
motorstatus9 = True

GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(pir_pin, GPIO.IN)

#Set the relay pin as output pin
GPIO.setup(relay1,GPIO.OUT)
GPIO.output(relay1,GPIO.HIGH) # Relay1 turns OFF
GPIO.setup(relay2,GPIO.OUT)
GPIO.output(relay2,GPIO.HIGH) # Relay2 turns OFF
GPIO.setup(relay3,GPIO.OUT)
GPIO.output(relay3,GPIO.HIGH) # Relay3 turns OFF
GPIO.setup(relay4,GPIO.OUT)
GPIO.output(relay4,GPIO.HIGH) # Relay4 turns OFF
GPIO.setup(relay5,GPIO.OUT)
GPIO.output(relay5,GPIO.HIGH) # Relay5 turns OFF
GPIO.setup(relay6,GPIO.OUT)
GPIO.output(relay6,GPIO.HIGH) # Relay6 turns OFF
GPIO.setup(relay7,GPIO.OUT)
GPIO.output(relay7,GPIO.HIGH) # Relay7 turns OFF

Stirrer_motor_ON_time  = 20
Stirrer_motor_OFF_time = 10

# Functions
def Calculate_time(quantity,Pump_timing_in_sec):
    val = 0
    if quantity == 1:
        val = 250
    elif quantity == 2:
        val = 500
    elif quantity == 3:
        val = 1000

    x = val/Pump_timing_in_sec
    round_value = round(x,4)
    return round_value

def Check_object_present():
    dist = GPIO.input(pir_pin)
    time.sleep(0.0001)
    if dist == 0:
        return True
    else:
        return False
    
def processing_cycle_for_pump1(v1):
    print("Process started ..... ")
    caltime = Calculate_time(v1,Pump1_timing)
    GPIO.output(relay1,GPIO.LOW)
    print("Motor1   :ON ")
    time.sleep(caltime)
    GPIO.output(relay1,GPIO.HIGH)
    motorstatus1 = False
    x = False

    while True:
        dist = Check_object_present()

        if dist == True and x == False:          
            GPIO.output(led, True)
            time.sleep(0.3)
            GPIO.output(led, False)
            time.sleep(0.3)
        elif(dist == False):
            GPIO.output(led, False)
            break

    GPIO.output(relay4,GPIO.LOW)
    print("Motor4   :ON ")
    time.sleep(30)
    GPIO.output(relay4,GPIO.HIGH)
    motorstatus4 = False
    x = False

def processing_cycle_for_pump2(w1):
    print("Process started ..... ")
    caltime = Calculate_time(w1,Pump2_timing)
    GPIO.output(relay2,GPIO.LOW)
    print("Motor2   :ON ")
    time.sleep(caltime)
    GPIO.output(relay2,GPIO.HIGH)
    motorstatus2 = False
    x = False

    while True:
        dist = Check_object_present()

        if dist == True and x == False:          
            GPIO.output(led, True)
            time.sleep(0.3)
            GPIO.output(led, False)
            time.sleep(0.3)
        elif(dist == False):
            GPIO.output(led, False)
            break
    GPIO.output(relay5,GPIO.LOW)
    print("Motor5   :ON ")
    time.sleep(30)
    GPIO.output(relay5,GPIO.HIGH)
    motorstatus5 = False
    x = False

def processing_cycle_for_pump3(x1):
    print("Process started ..... ")
    caltime = Calculate_time(x1,Pump3_timing)
    GPIO.output(relay3,GPIO.LOW)
    print("Motor3   :ON ")
    time.sleep(caltime)
    GPIO.output(relay3,GPIO.HIGH)
    motorstatus3 = False
    x = False

    while True:
        dist = Check_object_present()

        if dist == True and x == False:          
            GPIO.output(led, True)
            time.sleep(0.3)
            GPIO.output(led, False)
            time.sleep(0.3)
        elif(dist == False):
            GPIO.output(led, False)
            break
        
    GPIO.output(relay6,GPIO.LOW)
    print("Motor6   :ON ")
    time.sleep(30)
    GPIO.output(relay6,GPIO.HIGH)
    motorstatus6 = False
    x = False

def send_data_to_app(client_socket, data):
    try:
        client_socket.send(data.encode("utf-8"))
        print("Data sent successfully to app:", data)
    except Exception as e:
        print("Error sending data to app:", e)

def bluetooth_connection():
    # Bluetooth server setup
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1

    server_socket.bind(("", port))
    server_socket.listen(1)

    print("Waiting for connection on RFCOMM channel", port)

    try:
        client_socket, address = server_socket.accept()
        print("Accepted connection from", address)
        isConnected = True
        return client_socket,isConnected
    except bluetooth.btcommon.BluetoothError as error:
        print("Bluetooth connection error:", error)
        return None

def stirrer_motor(command):
    if command == "start":
        GPIO.output(relay7,GPIO.LOW)
    else:
        GPIO.output(relay7,GPIO.HIGH)
        motorstatus7 = False
        motorstatus8 = False
        motorstatus9 = False
        x = False

client_socket,isConnected = bluetooth_connection()
stirrer_motor("start")
print("Motor   :OFF")
v1,w1,x1 = 0,0,0
while True:
    while client_socket is not None and isConnected:
        try:
            send_data_to_app(client_socket, "B11,B,B")
            data = client_socket.recv(1024).decode("utf-8")
            stirrer_motor("stop")
            print(data)

            v1 = int(data[1])
            w1 = int(data[4])
            x1 = int(data[7])
            print("v1 ", v1, "w1 ", w1, "x1 ", x1)

            if data:
                if x == True:
                    print("Please keep the container below the tap")

                while True:
                    dist = Check_object_present()

                    if x == True and dist == False:
                        GPIO.output(led, True)

                    elif x == True and dist == True:
                        print("Object detected")
                        GPIO.output(led, False)
                        if v1:
                            processing_cycle_for_pump1(v1)
                            print("Process ended successfully ....")
                            break

                        if w1:
                            processing_cycle_for_pump2(w1)
                            print("Process ended successfully ....")
                            break

                        if x1:
                            processing_cycle_for_pump3(x1)
                            print("Process ended successfully ....")
                            break

                        else:
                            print("value not received")
                data =''
            stirrer_motor("start")
        except bluetooth.btcommon.BluetoothError as error:
            client_socket.close()
            break

        except Exception as e:
            print("An error occured: ",e)
            break
    print("\rBluetooth connection not established. Retrying...",end="")
    time.sleep(1)
    
