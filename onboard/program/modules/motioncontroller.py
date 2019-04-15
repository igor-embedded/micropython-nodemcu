from program.drivers.motorcontroller import PhysMotor
from program.drivers.imu import Compass
# import uasyncio as asyncio
# from uasyncio.synchro import Lock
import time


LEFT_MOTOR = PhysMotor.MOTOR_A
RIGHT_MOTOR = PhysMotor.MOTOR_B
STOP = 0
FORWARD = 1
BACKWARD = 2
LEFT = 0
RIGHT = 1


class Motor():
    def __init__(self, board, index, inverted=False):
        self.__motorcontroller = board.motorcontroller
        self.__index = index
        if inverted:
            self.__directions = [PhysMotor.DIR_STOP, PhysMotor.DIR_CCW,
                                 PhysMotor.DIR_CW]
        else:
            self.__directions = [PhysMotor.DIR_STOP, PhysMotor.DIR_CW,
                                 PhysMotor.DIR_CCW]

    def move(self, movement, pwm=None):
        self.__movement = movement
        self.__pwm = pwm
        self.__motorcontroller.update(self.__index,
                                      self.__directions[movement], pwm)

    def stop(self):
        self.move(STOP)


class MotionController():
    def __init__(self, controller):
        self.__motors = [None, None]
        self.__motors[LEFT_MOTOR] = Motor(controller.board,
                                          PhysMotor.MOTOR_A, inverted=False)
        self.__motors[RIGHT_MOTOR] = Motor(controller.board,
                                           PhysMotor.MOTOR_B, inverted=True)
#        loop = asyncio.get_event_loop()
#        loop.create_task(motor_task())

    def move(self, left_dir, left_pwm, right_dir, right_pwm):
        self.__motors[LEFT_MOTOR].move(left_dir, left_pwm)
        self.__motors[RIGHT_MOTOR].move(right_dir, right_pwm)

    def stop(self):
        self.__motors[LEFT_MOTOR].stop()
        self.__motors[RIGHT_MOTOR].stop()

    def test(self):
        self.move(FORWARD, 0xfff, FORWARD, 0xfff)
        time.sleep(3)
        self.move(BACKWARD, 0xfff, BACKWARD, 0xfff)
        time.sleep(3)
        self.move(FORWARD, 0xfff, FORWARD, 0xfff)
        time.sleep(3)
        self.stop()

#    async def motor_task(self, event):
#        while True:
#            if self.__index is None:
#                await event.wait()
#            if self.__index >= len(self.__commands):
#                self.__index = None
#                continue
#            await asyncio.sleep()
