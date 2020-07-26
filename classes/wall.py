import glob, os

class Wall:
    def __init__(self, ):
        self.__value = "X"
    def __str__(self):
        return self.__value
    def __repr__(self):
        return self.__str__()