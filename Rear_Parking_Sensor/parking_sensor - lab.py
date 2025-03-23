import RPi.GPIO as GPIO
import time
import threading



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

second = 1
distance = 1000
TRIG = 23
ECHO = 24

def get_distance():

    GPIO.output(TRIG, False)
    time.sleep(0.1)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        start = time.time()

    while GPIO.input(ECHO)==1:
        end = time.time()

    return (end - start) * 17015



def job():
    while True:
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17,False)
        if distance <=10:
            #second = 500
            time.sleep(0.05)
            GPIO.output(17,True)
            time.sleep(0.05)
        elif distance <=20:
            #second = 1000
            time.sleep(0.1)
            GPIO.output(17,True)
            time.sleep(0.1)
        elif distance <=30:
            #second = 20000
            time.sleep(0.2)
            GPIO.output(17,True)
            time.sleep(0.2)
    

t =threading.Thread(target = job)

t.start()


while True:
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.IN)
    print (get_distance())
    distance = get_distance()
    
    
    #set different condition here
    

        

    


GPIO.cleanup()
