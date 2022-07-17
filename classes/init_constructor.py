#!/usr/bin/python3

class mynum():
    def __init__(self,value):
        try:
            value = int(value)  
        except ValueError:
            value = 0
        self.value = value

    def increment(self):
        self.value = self.value + 1

aa = mynum('Hi')
bb = mynum(100)
aa.increment()
bb.increment()
print(aa.value)
print(bb.value)

 