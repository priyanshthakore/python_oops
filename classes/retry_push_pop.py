#!/usr/bin/python3

class MaxSizeList():
    def __init__(self,max):
        self.custom = []
        self.maxvalue = max
    def push(self,string_value):
        self.custom.append(string_value)
        if len(self.custom) > self.maxvalue:
            self.custom.pop(0)

    def get_list(self):
        return self.custom


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())