# ==============================================================
# PYTHON COURSE PRACTICALS – ALL QUESTIONS WITH ANSWERS & COMMENTS
# ==============================================================


# --------------------------------------------------------------
# 1. Write a program that evaluates an expression at run time using eval()
# --------------------------------------------------------------
expr = input("Enter any mathematical expression: ")
result = eval(expr)
print("Result =", result)


# --------------------------------------------------------------
# 2. Menu-driven program for various operations
# --------------------------------------------------------------
def menu():
    print("\n1. Area of Circle")
    print("2. Area of Triangle")
    print("3. Area of Square & Rectangle")
    print("4. Simple Interest")

menu()
choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area of Circle =", area)
elif choice == 2:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * b * h
    print("Area of Triangle =", area)
elif choice == 3:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area of Rectangle =", l * b)
    print("Area of Square =", l * l)
elif choice == 4:
    p = float(input("Enter principal: "))
    r = float(input("Enter rate: "))
    t = float(input("Enter time: "))
    si = (p * r * t) / 100
    print("Simple Interest =", si)
else:
    print("Invalid choice!")


# --------------------------------------------------------------
# 3. Employee module simulation
# --------------------------------------------------------------
def DA(basic):
    return basic * 0.8

def HRA(basic):
    return basic * 0.2

def PF(basic):
    return basic * 0.12

def ITAX(gross):
    return gross * 0.1

basic = float(input("Enter basic salary: "))
gross = basic + DA(basic) + HRA(basic)
net = gross - PF(basic) - ITAX(gross)
print("Gross Salary =", gross)
print("Net Salary =", net)


# --------------------------------------------------------------
# 4. Dictionary for cricket players and scores
# --------------------------------------------------------------
player = {"Virat": 102, "Rohit": 95, "Dhoni": 78}
name = input("Enter player name: ")
print("Runs =", player.get(name, "Not found"))


# --------------------------------------------------------------
# 5. List methods demo
# --------------------------------------------------------------
lst = [10, 20, 30]
lst.insert(1, 15)
print("After insert:", lst)
lst.remove(20)
print("After remove:", lst)
lst.append(50)
print("After append:", lst)
print("Length:", len(lst))
lst.pop()
print("After pop:", lst)
lst.clear()
print("After clear:", lst)


# --------------------------------------------------------------
# 6. Tuple methods demo
# --------------------------------------------------------------
tup = (10, 20, 30)
print("Tuple:", tup)
print("Item in tuple?", 20 in tup)
print("Length:", len(tup))
print("Access item:", tup[1])
# Deleting a tuple
del tup


# --------------------------------------------------------------
# 7. Dictionary methods demo
# --------------------------------------------------------------
d = {1: "A", 2: "B", 3: "C"}
print("Items:", d.items())
print("Access item:", d[2])
print("Get:", d.get(3))
d[2] = "Z"
print("Changed dictionary:", d)
print("Length:", len(d))


# --------------------------------------------------------------
# 8. Menu using functions (Arithmetic operations)
# --------------------------------------------------------------
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

print("\n1.Add  2.Subtract  3.Multiply  4.Divide")
ch = int(input("Enter choice: "))
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if ch == 1:
    print("Sum =", add(x, y))
elif ch == 2:
    print("Difference =", sub(x, y))
elif ch == 3:
    print("Product =", mul(x, y))
elif ch == 4:
    print("Division =", div(x, y))
else:
    print("Invalid choice!")


# --------------------------------------------------------------
# 9. Check positive or negative
# --------------------------------------------------------------
n = int(input("Enter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# --------------------------------------------------------------
# 10. Print date and time for today
# --------------------------------------------------------------
import datetime
print("Today’s date and time:", datetime.datetime.now())


# --------------------------------------------------------------
# 11. Add days to present date
# --------------------------------------------------------------
days = int(input("Enter days to add: "))
future = datetime.date.today() + datetime.timedelta(days)
print("Future date:", future)


# --------------------------------------------------------------
# 12. Grade based on percentage
# --------------------------------------------------------------
p = float(input("Enter percentage: "))
if p >= 90: g = "O"
elif p >= 80: g = "A"
elif p >= 70: g = "B"
elif p >= 60: g = "C"
elif p >= 50: g = "D"
elif p >= 40: g = "E"
else: g = "F"
print("Grade:", g)


# --------------------------------------------------------------
# 13. Maximum among three numbers
# --------------------------------------------------------------
a, b, c = map(int, input("Enter three numbers: ").split())
print("Maximum =", max(a, b, c))


# --------------------------------------------------------------
# 14. Gross salary calculation based on slabs
# --------------------------------------------------------------
basic = float(input("Enter basic salary: "))
if basic <= 10000:
    hra = basic * 0.2; da = basic * 0.8
elif basic <= 20000:
    hra = basic * 0.25; da = basic * 0.9
else:
    hra = basic * 0.3; da = basic * 0.95
gross = basic + hra + da
print("Gross Salary =", gross)


# --------------------------------------------------------------
# 15. Sum of series 1/2 + 1/3 + ... + 1/N
# --------------------------------------------------------------
N = int(input("Enter N: "))
s = 0
for i in range(2, N + 1):
    s += 1 / i
print("Sum of series =", s)


# --------------------------------------------------------------
# 16. Sum of numbers until user enters 0
# --------------------------------------------------------------
total = 0
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Sum =", total)


# --------------------------------------------------------------
# 17. Print numbers 1–1000 not divisible by given primes
# --------------------------------------------------------------
for i in range(1, 1001):
    if all(i % x != 0 for x in [2, 3, 5, 7, 11, 13, 17, 19]):
        print(i, end=" ")


# --------------------------------------------------------------
# 18. Function to find sum of all odd numbers 1 to n
# --------------------------------------------------------------
def sum_of_odds(n):
    s = 0
    for i in range(1, n + 1, 2):
        s += i
    return s

n = int(input("\nEnter n: "))
print("Sum of odd numbers =", sum_of_odds(n))


# --------------------------------------------------------------
# 19. Check palindrome number
# --------------------------------------------------------------
def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter number: "))
print("Palindrome" if is_palindrome(num) else "Not Palindrome")


# --------------------------------------------------------------
# 20. Multiplication table function
# --------------------------------------------------------------
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

table(int(input("Enter number: ")))


# --------------------------------------------------------------
# 21. Fibonacci series
# --------------------------------------------------------------
n = int(input("Enter how many terms: "))
a, b = 0, 1
print(a, b, end=" ")
for _ in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c


# --------------------------------------------------------------
# 22. Digits of number into list
# --------------------------------------------------------------
num = input("\nEnter number: ")
digits = [int(d) for d in num]
print("List =", digits)


# --------------------------------------------------------------
# 23. Second smallest and second largest in list
# --------------------------------------------------------------
lst = [5, 8, 2, 9, 1, 4]
lst.sort()
print("Second Smallest =", lst[1])
print("Second Largest =", lst[-2])


# --------------------------------------------------------------
# 24. Smallest and largest value in dictionary
# --------------------------------------------------------------
D1 = {1:200, 2:3000, 3:100, 5:20}
print("Smallest =", min(D1.values()))
print("Largest =", max(D1.values()))


# --------------------------------------------------------------
# 25. Count vowels in string
# --------------------------------------------------------------
s = input("Enter string: ")
count = sum(1 for ch in s if ch.lower() in "aeiou")
print("Number of vowels =", count)


# --------------------------------------------------------------
# 26. Count occurrence of character (no built-in)
# --------------------------------------------------------------
string = input("Enter string: ")
ch = input("Enter character: ")
count = 0
for c in string:
    if c == ch:
        count += 1
print("Occurrences =", count)


# --------------------------------------------------------------
# 27. Student class with marks and grade
# --------------------------------------------------------------
class Student:
    def __init__(self, sid, name, m1, m2, quiz):
        self.sid = sid
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.quiz = quiz

    def marksList(self):
        total = self.m1 + self.m2 + self.quiz
        if total >= 80: grade = "A"
        elif total >= 60: grade = "B"
        elif total >= 50: grade = "C"
        else: grade = "Fail"
        print(f"ROLL NUMBER: {self.sid}\nNAME: {self.name}\nMID1: {self.m1}\nMID2: {self.m2}\nQUIZ: {self.quiz}\nTOTAL: {total}\nRESULT: {grade}")

s1 = Student(101, "Tirth", 25, 30, 20)
s1.marksList()


# --------------------------------------------------------------
# 28. CAR and FiringCAR class with inheritance
# --------------------------------------------------------------
class Car:
    def __init__(self, model, speed, price):
        self.model = model
        self.speed = speed
        self.price = price

class FiringCar(Car):
    def __init__(self, model, speed, price, bullets):
        super().__init__(model, speed, price)
        self.bullets = bullets

    def fire(self):
        if self.bullets > 0:
            print("Firing bullets!")
            self.bullets -= 1
        else:
            print("Out of bullets!")

car1 = FiringCar("BMW", 200, 5000000, 5)
car1.fire()
car1.fire()


# --------------------------------------------------------------
# 29. Polygon, Triangle, Rectangle, Square classes (OOP)
# --------------------------------------------------------------
class Polygon:
    def __init__(self, sides):
        self.sides = sides
        print(f"Polygon with {sides} sides created.")

    def area(self):
        print("Generic polygon has no formula.")

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, l, b):
        super().__init__(4)
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def area(self):
        return self.l * self.b

t = Triangle(10, 5)
r = Rectangle(8, 4)
s = Square(6)
print("Area of Triangle:", t.area())
print("Area of Rectangle:", r.area())
print("Area of Square:", s.area())
