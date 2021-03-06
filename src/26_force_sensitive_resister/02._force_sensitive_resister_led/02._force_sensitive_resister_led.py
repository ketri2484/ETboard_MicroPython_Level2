# ******************************************************************************************
# FileName     : 02._force_sensitive_resister_led
# Description  : 압력 센서의 값에 따라 LED를 순차적으로 켜보기
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 주석 수정, 소스 크린징 
# ******************************************************************************************


# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *


# global variable
sensor = ADC(Pin(A3))                 # 압력센서 핀 지정

led_led = Pin(D2)                     # 빨강 LED 핀 지정
led_blue = Pin(D3)                    # 파랑 LED 핀 지정
led_green = Pin(D4)                   # 초록 LED 핀 지정
led_yellow = Pin(D5)                  # 노랑 LED 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)

    led_led.init(Pin.OUT)             # D2를 LED 출력모드 설정
    led_blue.init(Pin.OUT)            # D3를 LED 출력모드 설정
    led_green.init(Pin.OUT)           # D4를 LED 출력모드 설정
    led_yellow.init(Pin.OUT)          # D5를 LED 출력모드 설정


# main loop
def loop():
    sensor_result = sensor.read()
    
    led_led.value(LOW)                # 빨강 LED 끔
    led_blue.value(LOW)               # 파랑 LED 끔
    led_green.value(LOW)              # 초록 LED 끔
    led_yellow.value(LOW)             # 노랑 LED 끔
    
    if sensor_result > 1000:          # 압력 센서의 값이 1000초과라면  빨강 LED 켜기
        led_led.value(HIGH)
        
    if sensor_result > 1100:          # 압력 센서의 값이 1100초과라면  파랑 LED 켜기
        led_blue.value(HIGH)
        
    if sensor_result > 1200:          # 압력 센서의 값이 1200초과라면  노랑 LED 켜기
        led_green.value(HIGH)
        
    if sensor_result > 1300:          # 압력 센서의 값이 1300초과라면  초록 LED 켜기
        led_yellow.value(HIGH)
    
    time.sleep(0.1)                   # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
