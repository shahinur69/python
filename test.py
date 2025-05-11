
age = 21
height = 5.9
name = "Alice"
is_student = True
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
"""
a = 10
b = 3
result = a / b
print("the result of a divided by b is: ", result)
print("Formate to 3 decimal places: %.3f" % result)
age = int(input("Enter an age: "))
print(age)
num1 =  input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1 = int(num1)
num2 = int(num2) 
print("The sum of numbers: ", num1 + num2)
str = "python"
print("Reversed string: ")
print(str[::-1])
part1 = "I love"
part2 = " python"
full = part1 + part2
print("Concatenation of this: ", full)
text = " I love python"
repeated = text * 3
print(repeated)

text = "I love python"
print(text[2:6])
length = len(text)
print(length)
string = "I loVe pyThOn"
print(string.lower())
print(string.upper())
text = "i love Python. Python is fun"
new_text = text.replace("Python", "Java")
print(new_text)
cnt = text.count("Python")
print(cnt)
s = "123456"
print(s.isdigit())
f = "123abc"
print(f.isdigit())
t1 = input("Enter the first string: ")
t2 = input("Enter the second string: ")
combined = t1 + t2
n = int(input("How many times to repeate it: "))
repeated = combined * n
print(repeated)
print(combined)
text = input("Enter the string: ")
length = len(text)
print(length)
print(text[7:])
string = input("Enter a string: ")
words = string.split()
print("Split words: ", words)
join_text = ' '.join(words)
print(join_text)
print("How is the weather today? ")
weather = input()
if(weather == "Sunny"):
    print("We will wear sunglass")

inp = input()
if(inp == "Snowing"):
    print("Wear sweetshirt")
else:
    print("Wear T-shirt")
num = int(input("Take a number: "))
if(num > 0):
    print(num, "is a positive")
elif(num < 0):
    print(num, "is a negative")
else:
    print(num, "is a 0")
    
number = int(input("Take a number: "))
if(number % 5 == 0):
    print("Multiple of 5")
else:
    print("Not multiple of 5")
    
if(weather <= 28):
    print("It's warm")
else:
    print("It's not warm")
    
    
user_name = input("Press the user name: ")
password = int(input("Enter your password: "))
if(user_name == "Admin"):
    if(password == 123456):
        print("Login successful!!")
    else:
        print("Incorrect password")
else:
    print("User name not found") 
    
n = int (input("enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("The sum of numbers: " , total)

total = 0
num = int(input("Enter a number: "))
i = 1
while(i <= num):
    print(i)
    i = i + 1
    total = total + i
print(total)

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n,"x", i,"=", n*i)

n = int(input("Enter a number: "))
i = 1
while(i <= 10):
    print(n,"x", i, "=", n*i)
    i = i + 1

n = int(input("Enter a number: "))
for i in range(2, n + 1, 2):
    print(i)
    
n = int(input("Enter a number: "))
i = 2
while( i <= n):
    print(i)
    i += 2


n = int(input("Enter a number: "))
i = 1
while(i <= n):
    if(i % 5 == 0):
        print(i)
    i += 1


n = int(input("Enter a number: "))
for i in range(1, n + 1):
    squire = i*i
    print(f"{i}^2 = {squire}")
    
    
count = 0
n = int(input("Enter a number (0 to stop): "))
while n != 0:
    if n > 0:
        count += 1
    n = int(input("Enter a number (0 to stop): "))
print("Count of positive numbers:", count)

"""


