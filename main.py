#!/usr/bin/env pybricks-micropython
        

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more informati


# Create your objects here.
# ev3 = EV3Brick()


# Write your program here.
# Motor(Port.C).run(500)
# 모터C가 500의 속도로
# Motor(Port.B).run(500)
# 모터B가 500의 속도로
# wait(1000)

# 모터가 500의 속도로 1.000초동안 이동하는것.
# Motor(Port.C).stop(Stop.HOLD)
# Motor(Port.B).stop(Stop.HOLD)
# 모터가 멈추는 것이다.
# HOLD:강제유지 정지
# COAST:부드럽게 정지
# BRAKE:강제 정지
# wait(200)

# B=Motor(Port.B)
# B는 Motor(Port.B)와 같다
# C=Motor(Port.C)
# C는 Motor(Port.C)와 같다
# B.run(500)
# B.run(500)=Motor(Port.B).run(500)이다
# C.run(500)
# B.run(500)=Motor(Port.B).run(500)이다
# wait(2000)

# B=Motor(Port.B)
# C= Motor(Port.C)
# B.run_time(500,2000)
# run_time(1~,2~)에서 1~= 속도2~=시간과 같다
# C.run_time(500,2000)


# box=input("아무거나 입력하세요")

# if box == '바보':
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")
# 아무거나 입력하세요 일때
# 바보가 box면 택시를 타고 가라 라고 말함
# 바보가 box가 아니면 걸어가라 라고 말함

# a = 0
# while a<10:
#     print('배고파')
#     a=a+1
# a=0일때,
# a가 10 보다 작을때 배고파를 말하다.
# 그 다음 a에 1을 더한다
# 그 다음 다시 실행한다(반복)

# for i in range(10):
#     print (i)
# 0~9까지 순서대로 보여준다

# a = ['one','two','three']
# for i in a:
#     print (i)
# 순서대로 a에 있는 one,two.three를 순서대로 보여준다
# (i를 꼭 넣어야 한다)


# for i in range(3):
#     Motor(Port.C).run(500)
#     Motor(Port.B).run(500)
#     wait(1000)
# "500의 속도로 포트CB가 1.000초로 이동한다"가 3번 반복

# def Turn_Left():
#     Motor(Port.B).run(500)
    
#     wait(800)
#     Motor(Port.B).run(-300)
#     Motor(Port.C).run(300)
#     wait(400)
# Turn_Left()

# for i in range(4):
#     Motor(Port.B).run(500)
#     wait(800)
#     Motor(Port.B).run(300)
#     Motor(Port.C).run(-300)
#     wait(400) Motor(Port.C).run(500)

# TS=TouchSensor(Port.S1)
# while a.pressed() == 0:
#     Motor(Port.B).run(300)
#     Motor(Port.C).run(300)
#     wait(1000)
# 터치 센서를 눌르지 않으면 앞으로 갔다가 멈추는 것을 반복하고 터치 센서를 눌르면 프로그램 종료
# 터치 센서가 눌러 있지 않으면 (참)반복
# 이므로 눌르면 프로그램 종료 
#TS= 포트 1(S1)에 있는터치 센서 선언



# while True:
#     Motor(Port.B).run(500)
#     Motor(Port.C).run(500)

    # if b.distance() <= 500:
#         Motor(Port.B).stop(Stop.BRAKE)
#         Motor(Port.C).stop(Stop.BRAKE)

# CS = ColorSensor(Port.S2)



# while True:
#     brick.display.text()
#     wait(5000)
# # 컬러센서로 색을 측정하는 프로그램

# while True:
#     if s4.color() == Color.BLACK:
#         Motor(Port.C).run(500)
#         Motor(Port.B).run(400)
#     if s4.color() == color.
#         Motor(Port.C).run(400)
#         Motor(Port.B).run(500)

# s4=UltrasonicSensor(Port.S4)
# # B = Motor(Port.B)
# # C = Motor(Port.C)
#s3 = GyroSensor(Port.S3)

# B = Motor(Port.B)
# C = Motor(Port.C)

# for i in range(10):
#     while i % 2 == 0:
#         B.run(500)
#         C.run(500)
#         wait(1000)
#         B.stop(Stop.BRAKE)
#         C.stop(Stop.BRAKE)
#         wait(200)

# while True:
#     if us.distance() > 100:
#         B.run(300)
#         C.run(300)
#     elif us.distance() < 80:
#         B.run(-300)
#         C.run(-300)
#     else:
#         B.stop(Stop.BRAKE)
#         C.stop(Stop.BRAKE)

# while True:
#     ev3.screen.print(ev3.buttons.pressed())

# while True:
#     if ev3.buttons.pressed() == [Button.UP]:
#         B.run(300)
#         C.run(300)
# else:
#     C.stop(Stop.BRAKE)
#     B.stop(Stop.BRAKE)


# ev3.speaker.say('')

# robot = DriveBase(B, C, wheel_diameter=55.5, axle_track=104)

# robot.straight(1000)
# ev3.sspeaker.beep()

# while True:
#     B.run(200)
#     C.run(200)
#     if s1.pressed() == 1:
#         break
#     B.run(-200)
#     C.run(-200)
#     wait(1000)
#     while True:
#     robot.turn(90)
#     B.run(200)
#     C.run(200)
#     if s2.color() == Color.BLACK:
#         robot.turn(-100)
#         Motor(Port.C).run(500)
#         Motor(Port.B).run(400)
#     if s2.color() == Color.WHITE:
#         Motor(Port.C).run(400)
#         Motor(Port.B).run(500)
#         if s4.distance() > 200:
#             break
# robot.turn(3600)
# while True:
    # if CS.color() == Color.GREEN:
    #     B.run(480)
    #     C.run(680)
    # elif CS.color() == Color.YELLOW:
    #     B.run(680)
    #     C.run(480)
# B.run(300)
# C.run(300)
# wait(1600)
# B.run(300)
# C.run(-300)
# wait(590)
# B.run(300)
# C.run(300)
# wait(2800)
# B.run(-300)
# C.run(300)
# wait(560)
# while True:
#     if CS.color() == Color.BLACK:
#         B.run(300)
#         C.run(500)
#     elif CS.color() == Color.WHITE:
#         B.run(500)
#         C.run(300)
# while True:
#     if CS.color() == Color.RED:
        # ev3.speaker.set_volume(5000)
#         ev3.speaker.say('RED')
#     if CS.color() == Color.YELLOW:
#         ev3.speaker.say('YELLOW')
#     if CS.color() == Color.BLUE:
#         ev3.speaker.say('BLUE')
#     if CS.color() == Color.GREEN:
#         ev3.speaker.say('GREEN')
# while True:
#     B.run(500)
#     C.run(500)
#     if TS.pressed() == 1:
#         ev3.speaker.set_volume(10000)
#         ev3.speaker.say('멈춰')
# B.run(500)
# C.run(300)
# wait(1600)
# B.run(300)
# C.run(-300)
# wait(590)
# B.run(300)
# C.run(300)
# wait(2800)
# B.run(-300)
# C.run(300)
# wait(520)
# B.run(300)
# C.run(300)
# wait(2650)
# B.run(240)
# C.run(-240)
# wait(560)
# if CS.color() == Color.YELLOW:
#     ev3.speaker.say('YELLOW'

