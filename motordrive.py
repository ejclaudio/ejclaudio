import RPI.GPIO as GPIO
import time

class MotorDriver(object):

    def __init__(self):

        self.PWMA1=19
        self.PWMA2=16
        self.PWMB1=21
        self.PWMB2=26
        self.D1=13
        self.D2=20

        self.PWM = 50

        GPIO.setmode(GPIO.BCM)
        GPIO.setwanings(False)
        GPIO.setup(self.PWMA1, GPIO.OUT)
        GPIO.setup(self.PWMA2, GPIO.OUT)
        GPIO.setup(self.PWMB1, GPIO.OUT)
        GPIO.setup(self.PWMB2, GPIO.OUT)
        GPIO.setup(self.D1, GPIO.OUT)
        GPIO.setup(self.D2, GPIO.OUT)
        self.p1 = GPIO.PWM(self.D1, 500)
        self.p2 = GPIO.PWM(self.D2, 500)
        self.p1.start(50)
        self.p2.start(50)

    def set_motor(self, A1, A2, B1, B2):
        GPIO.output(self.PWMA1, A1)
        GPIO.output(self.PWMA2, A2)
        GPIO.output(self.PWMB1, B1)
        GPIO.output(self.PWMB2, B2)

    def forward(self):
        self.set_motor(1, 0, 1, 0)

    def stop(self):
        self.set_motor(0, 0, 0, 0)

    def reverse(self):
        self.set_motor(0, 1, 0, 1)

def motor_driver_test():

    motor= MotorDriver()
    motor.stop()
    time.sleep(0.5)

    motor.forward()
    time.sleep(2.0)

    motor.reverse()
    time.sleep(2.0)

def motor_driver_test_basic(PWM_VALUE):

    motor = MotorDriver()

    motor.PWM = PWM.VALUE
    motor.p1.ChangeDutyCycle(motor.PWM)
    motor.p2.ChangeDutyCycle(motor.PWM)
    print(srt(motor.PWM))

    motor.reverse()
    time.sleep(2.0)

    motor.forward()
    time.sleep(2.0)

if __name__ == "__main__":
    print('Starting motor driver test')
    pwm_value = 50
    while True:
        motor_driver_test_basic(pwm_value)
        pwm_value +=10
    GPIO.cleanup()
    print("Starting MOTOR driver test...End")
