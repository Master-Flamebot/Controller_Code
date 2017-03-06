import requests
import pygame
pygame.init()
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
print ( j.get_name())
def eye():
    while True:
        pygame.event.pump()
        TextV=["1","2","3","4","L1","R1","L2","L2","S1","S2"]   #what is printed
        BV=[0,0,0,0,0,0,0,0,0,0]    #which value will be printed from TextV
        Q=""    #makes it so you can print the values without them combining
        out = [0,0,0,0]
        it = 0
        pygame.event.pump()

        rightvert = j.get_axis(3)
        rightvert = rightvert * -100
        rightvert = int(rightvert)
        #print (rightvert)

        righthorz = j.get_axis(2)
        righthorz = righthorz * -100
        righthorz = int(righthorz)
        #print (righthorz)

        leftvert = j.get_axis(1)
        leftvert = leftvert * -100
        leftvert = int(leftvert)
        #print (leftvert)
        print (rightvert , leftvert , righthorz)

        leftvert = leftvert + 100
        leftvert = leftvert * 180
        leftvert = leftvert / 200
        r = requests.get('http://10.42.0.111:10/left/{}'.format( leftvert ))

        rightvert = rightvert + 100
        rightvert = rightvert * 180
        rightvert = rightvert / 200
        r = requests.get('http://10.42.0.111:10/right/{}'.format( rightvert ))

        righthorz = righthorz + 100
        righthorz = righthorz * 180
        righthorz = righthorz / 200
        r = requests.get('http://10.42.0.111:10/up/{}'.format( righthorz ))
