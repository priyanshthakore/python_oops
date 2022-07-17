class pushpop():
    def __init__(self,max):
        self.max = max
        self.inner_list = []

    def push(self,string_value):
        self.inner_list.append(string_value)
        if len(self.inner_list) > self.max:
            self.inner_list.pop(0)
    
    def get_list(self):
        return self.inner_list

a = pushpop(3)
b = pushpop(1)

a.push("hey")
a.push("hi")
a.push("lets")
a.push("go")

b.push("hey")
b.push("hi")
b.push("lets")
b.push("go")

print(a.get_list())
print(b.get_list())

