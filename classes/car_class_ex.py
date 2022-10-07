#!/usr/bin/python3

class car():
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def horn(self):
        print("Horn OK")
    def get_speed(self):
        return self.speed
    def set_speed(self,value):
        try:
            val = int(value)
        except ValueError:
            return
        self.speed = value

num1 = car(10,"nissan")
num2 = car(20,"mercedes")
print(num1.get_speed())
num1.set_speed(50)
print(num1.get_speed())
print("Done")