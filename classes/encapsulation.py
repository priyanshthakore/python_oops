#!/usr/bin/python3
class myinteger():
    def set_value(self,value):
        try:
            val = int(value)
        except ValueError:
            return
        self.val = val 

    def get_value(self):
        return self.val

    def increment_value(self):
        self.val = self.val + 1

obj = myinteger()
obj.set_value(5)
obj.increment_value()
print(obj.val)
