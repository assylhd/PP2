"""Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!"""

"""To open the file, use the built-in open() function.
The open() function returns a file object, which has a read() method for reading the content of the file:"""

f = open("demofile.txt")
print(f.read())

#If the file is located in a different location, you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt")
print(f.read())

#You can also use the with statement when opening a file:
with open("demofile.txt") as f:
  print(f.read())

#Close the file when you are finished with it:
f = open("demofile.txt")
print(f.readline())
f.close()

#Return the 5 first characters of the file:
with open("demofile.txt") as f:
  print(f.read(5))

#Loop through the file line by line:
with open("demofile.txt") as f:
  for x in f:
    print(x)