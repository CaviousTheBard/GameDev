# -*- coding: utf-8 -*-
'''
Filename: Enity.py
Type: Class
------------------------------
Created By: Donald R. Valverde
'''


class Entity(object):

    def __init__(self, name, xPos, yPos):
        self.__name = 'entity_' + name
        self.__xPos = xPos
        self.__yPos = yPos

    #Entity __name Getter
    def name(self):
        return self.__name

    #Entity __xPos Getters and Setters
    def x_pos(self):
        return self.__xPos

    def set_x_pos(self, num):
        self.__xPos = num

    #Entity __xPos Getters and Setters
    def y_pos(self):
        return self.__yPos

    def set_y_pos(self, num):
        self.__yPos = num