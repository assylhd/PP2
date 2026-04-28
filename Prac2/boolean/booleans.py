#Python Booleans
"""
Boolean Values
In programming you often need to know if an expression is True or False.
"""
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#b is not greater


print(bool("Hello")) #True
print(bool(15)) #True

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))