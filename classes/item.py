import glob, os

class Item:
    def __init__(self, ):
        self.value = "I"
    def __str__(self):
        return self.value
    def __repr__(self):
        return self.__str__()
