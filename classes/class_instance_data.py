class instance_counter():
    count = 0 
    def __init__(self,val):
        self.val = val
        instance_counter.count += 1

    def get_value(self):
        return self.val

    def set_value(self,value):
        self.val = value

    def get_count(self):
        return instance_counter.count

a = instance_counter(5)
b = instance_counter(10)
c = instance_counter(15)

for obj in (a,b,c):
    print("value of obj %s" % (obj.get_value()))
    print("count is %s" % (obj.count))