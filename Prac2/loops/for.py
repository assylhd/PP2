#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#loop over sequence(list)

for x in "banana":
  print(x)

  #loop over string

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#apple, banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

  #apple

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  #apple cherry

for x in range(6):
  print(x)


#loop over range(0,1,2,3,4,5)

for x in range(2, 6):
  print(x)

#start parameter, starts from 2(inclusive) amd ends at 6(exclusive) 2,3,4,5

for x in range(2, 30, 3):
  print(x)

#start, end, step

for x in range(6):
  print(x)
else:
  print("Finally finished!")

  #1 2 3 4 5 finally finished

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

  #0 1 2

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

'''red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry'''

for x in [0, 1, 2]:
  pass

#


