import random

class myclass():
    def dothis(self):
        self.random_num = random.randint(1,10)

obj = myclass()
obj.dothis()
print(obj.random_num)