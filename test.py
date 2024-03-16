a = [1,2,3,4]
b = [5,6]
a.extend(b)

print(a)

def cut():
    global a
    a = a[2:]


cut()
print(a)