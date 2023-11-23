import os
import random
import time

# import pygame

# pygame.init()
class snake:
    def __init__(self,item):
        pass


class sub_snake(snake):
    def __init__(self, item,ring):
        super().__init__(item)



a = sub_snake(item=1,ring=3)


class food:
    def __init__(self):
        pass


class player:
    def __init__(self):
        pass


class screenGame:
    def __init__(self,screen):
        screen = pygame.display.set_mode((1280,720))
        screen.fill('purple')


def a():
    print("##########################")
    print("#                        #")
    print("#                        #")
    print("#                        #")
    print("#                        #")
    print("#                        #")
    print("#                        #")
    print("##########################")


def b():
    print("##########################")
    print("#                        #")
    print("#                        #")
    print("#                        #")
    print("#        snake           #")
    print("#                        #")
    print("#                        #")
    print("##########################")


while True:
    os.system("CLS")
    a()
    time.sleep(0.1)
    os.system("CLS")
    b()
    time.sleep(0.1)