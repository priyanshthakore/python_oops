class yourclass():
    classy = 'class value'

dd = yourclass()
print(dd.classy)
dd.classy = "init"
print(dd.classy)
del dd.classy
print(dd.classy)