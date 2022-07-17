## while calling a method in a classes the first argument we pass is the instance 
## so self is the instance object

class newclass():
    def firstmethod(self):
        print("first Method")
        print(self)

obj = newclass()
obj.firstmethod()
print(obj)