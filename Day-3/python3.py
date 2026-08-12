name="Krishna"
def student():
    print(name)
    student()
    print(name)
def student():
    age=27
    print(age)
student()

name="Krishna"
def display():
    age=20
    print(age)
    print(name)
display()

name="Krishna"
def display():
    name="Radha"
    print(name)
display()
print(name)

name="Radha"
name="Krishna"
def display():
    name="Shree"
    name="Nivasa"
    print(name)
display()
print(name)
print(name)

def square():
    num=int(input("Enter the square of a number:"))
    print(num*num)
square()

square=lambda x:x*x
print(square(2))

large=lambda x,y:x if x>y else y
print(large(10,20))

def countdown(n):
    if n==0:
        return
    print(n)
    countdown(n-1)
countdown(5)

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(6))

def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print(power(2,4))


def even_odd():
    num=int(input("Enter a number:"))
    if num%2==0:
        print("Even")
    else:
        print("Odd")
even_odd()