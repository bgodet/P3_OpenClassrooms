import glob, os

class Item:
    def __init__(self, ):
        self.__value = "I"
    def __str__(self):
        return self.__value
    def __repr__(self):
        return self.__str__()
