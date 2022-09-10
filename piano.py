#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2019, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# paino_buzzer.py
# Make the buzzer sound like a piano
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
BUZZER_PIN = 7
BTN_PIN_0 = 11
BTN_PIN_1 = 12
BTN_PIN_2 = 13
BTN_PIN_3 = 15
BTN_PIN_4 = 16
BTN_PIN_5 = 18
BTN_PIN_6 = 22

MELODY_DO = 523
MELODY_RE = 587
MELODY_ME = 659
MELODY_FA = 698
MELODY_SO = 784
MELODY_LA = 880
MELODY_SI = 988

WAIT_TIME = 200
DURATION = 0.2

GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(BTN_PIN_0,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
#########################
#Setup GPIO here
#########################

def buzz(pitch) :
    period = 1.0 / pitch
    half_period = period / 2
    cycles = int(DURATION * pitch)

    for i in range(cycles) :
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(half_period)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(half_period)

def mycallback(channel):
    print("Button pressed @:", channel, time.ctime())

    if channel == BTN_PIN_0:
        buzz(MELODY_DO)
#################################
#add melody settings here
#################################

try:
    GPIO.add_event_detect(BTN_PIN_0, GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)
#################################
#detect event here
#################################


    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()          
