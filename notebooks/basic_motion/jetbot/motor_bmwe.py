import time
import board
import busio
from adafruit_motor import motor
from adafruit_motorkit import MotorKit


i2c=busio.I2C(board.SCL,board.SDA)
kit=MotorKit(i2c=i2c)

kit.motor1.throttle =0.5
kit.motor2.throttle =0.5
time.sleep(2)
kit.motor1.throttle =0
kit.motor2.throttle =0