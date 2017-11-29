#!/usr/bin/python
# encoding:utf-8


"""
@author:jiruiqing
contact:ruiqing0706@163.com
@file: PYG02-PygameHelloWorld.py
@time: 2017/11/29 20:05
"""

import pygame,sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame游戏之旅")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()