#INTRO CONCATINATING

#high level  dynamic typing   makes a testing easy   use simple engish   powerfull   oops
a=input("Enter the first no")
b=input("Enter the second number")
print("The sum of the two numbers are", str(a)+str(b))

f=int(input("Enter the degree in fahrenheit that is tio be converted to celsius"))
ans_c=(f-32)*(5/9)
print("the converted celsius scale temperature is ",ans_c)
c= int(input("Enter the celsius degree to convert it to fahrenheit "))
ans_f=(c*(9/5))+32
print("The converted fahrenheit temperature is ",ans_f)



#SI Calculator
interest=int(input ("Enter the Interest rate"))
timePeriod=int(input ("Enter the time period of the simple interest"))
principalAmount=int(input("Enter the principal amount"))
simpleInterest =(interest*timePeriod*principalAmount)/100
print("The simple interest is ",simpleInterest)

#INBUILD FUNCTIONS

print(max(1,2,3,4,5,6))
print(abs(-20.20))
print(pow(3,2))



#IF CONDITIONS

a=int(input("Enter your marks"))
if (a>90 and a<100):
    print("O+")
elif (a>80 and a<90):
    print("A+")
elif (a>70 and a<80):
    print("A")
else:
    print("Fail")

for i in range(10):
    print("HELLO",sep='')


counter=1
while (counter<=5):
    print(counter)
    counter+=1



#CODE REUSING --->FUNCTION

def repeat():
    input("Enter the name of your favorite fruit")
    for i in range(10):
        print(i)
repeat()



#LOCK SYS
pin=1234
a=int(input("Enter your pin"))
def lock_sys():
    global a
    while a!=pin:
        print("Passcode incorrect")

    else:
        print("Passcode correct")

lock_sys()


def my_world(a,b,c):
    return " ".join([a,b,c])

a=my_world("I","love","adventure")
b=my_world("I","love","DV"
print(a)
print(b)


def add(x, y):
    return x + y
def sub(a,b):
        return a - b
def calc():
    add(1,2)
    sub(3,2)
calc()


def add(a,b):
    return a+b
a=add(3,5)
print(a)



# IMPORT MODULE

from math import pi
print(pi)

#OR

from math import *     ->->->->->->->->->->   *   ->->->->->->all modules


import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())


x = input("Enter the number to find the factorial")
def factorial(x):
    if x<2:
        return 1
    else:
        return x*(factorial(x-1))
fact=factorial(4)
print(fact)

file = open('python.txt','r')

inside the paranthesis specifies the location and the there is a file mode specified
 there are read,append,write,read and write

read=file.read()
reads=file.readline()
readss=file.readlines()
print(read)
print(reads)
print(readss)
file.close()


file = open('python.txt','a')
write=file.write("how is ur life")
print(write)
file = open('python.txt','r')
read=file.read()
print(read)
file.close()

file = open('python.txt','r+')
write=file.write("how is ur life")
print(write)
read=file.read()
print(read)
file.close()


DICTIONARY

it uses CURLY BRACES

#for list =[]   and also we need to know its index value
#but in dictionary ={}   key is to known
# dictionary========specification====== dictionary = {key:value,key:value}

dict={'a':"apple",
      'b':"ball",
      'c':"cat",
      'e':"elephant"}
dict['d']="dog"         #this will automatically append the dictionary
del(dict['e'])          #this statement deletes the the value and the key of 'e'
print(dict)
print('c' in dict)      #checks if the element is in the dictionary
print(dict.keys())      #provides the keys
print(dict.values())    #provides the values
print(dict['a'])
dict.clear()


#LIST
list are used to avoid creation of multiple variables
LISTS are mutable--->changable

list1=[5,6,7,9]
list2=[2,3,4,8]
list2[0]=1
list3=list1+list2
list4=list1*3                 #prints the list number of times
print(list4)
print(list3)
print(list2)


SETS:
unordered
unique elements
defined in a {}

set={0,1,2,3,4,5,6,7}
set1={1,3,5,7,9}
print(set.intersection(set1))
print(set.union(set1))
set.add(8)
set.remove(0)
print(8 in set)
print(set)

STRING FUNCTIONS:

str="P S Shaktivel"
print(str.capitalize())         #capitalize is used to convert the first letter capital
print(str.upper())
print(str.lower())
print(str.isnumeric())


LIST FUNCTION
isnumeric()
isalphabet()
lower()
upper()
capitalize()
insert(place,value)
is()
find()
replace()
startswith()
endswith()
lstrip()
rstrip()
split()
splitlines()
join()
swapcase()
len()
name= "mike"
format()=== print("Hi {} how are u ".format(name())

TUPLES:
tuple is defined in ()
immutable or cannot be changed

numbers=(1,2,3,4,5)
print(numbers[3])
num1=(10,9,8,7,6)
num2=(1,2,3,4,5)
print(num1+num2)                #concating
print(len(num1+num2))
print(numbers.index(5))

CLASS SYNTAX
class(name):
    statements and attributes
    ********pass is a null operator
    it is used in class if there is no attribute then it provides an error so here pass is used********
    .
    here
    .
    .


class shakti:
    character="good"
    gender="male"

var=shakti()
print(var.character)
print(var.gender.capitalize())

'.'--->dot notation is used to store and access the datas
a function in a class is called 'METHOD'

SELF :it is a kind of representation of the current instance of the class 'it must be placed in the first place while declaring the method it can be declared with any name
CONSTRUCTOR :it is placed in the top and
DESTRUCTOR :it is usually called at the last of the program
constructor::::::-----  __init__
destructor:::::::----- __del__

class classname:
    n=0
    def cnt(self):
        self.n=self.n+1
        print("The count is" ,self.n)
c=classname()
c.cnt()

CONSTRUCTOR


class hi:
    def __init__(self,character,gender):
        self.character=character
        self.gender=gender
        print("Constructor")

    def __del__(self):
        print("Destructor")

cd= hi("good","male")
print(cd.character)
print(cd.gender)

print("hi")
class func(hi):
    str = "P S Shaktivel"

    def __init__(self,gender):
        self.gender=gender
        print(gender)

    def __init__(self,i):
            input("Enter the name of your favorite fruit")
            for i in range(10):
                print(i)

cd=func("shaktivel")
print(cd.str)

INHERITANCE is possible by adding the class name in the class named bracket:
--->Example
    class classname1;
        attributes.....
    class classname2(classname1):
    using this we can inherit all the required attributes from another class
    there are different types of inheritance they are
    --->single level inheritance
    --->multi level inheritance
    --->multiple inheritance


SINGLE LEVEL INHERITANCE

class one:
    def state_1(self):
        print("1 Present")
    def state_2(self):
        print("2 Present")
    def state_3(self):
        print("3 Present")
class two(one):
    def state_4(self):
        print("4 Present")
    def state_5(self):
        print("5 Present")

a=two()             ----->in this only two can access the attributes of one and one cannot access the attributes of class two
a.state_1()
a.state_2()
a.state_5()

MULTI LEVEL INHERITANCE

class one:
    def state_1(self):
        print("1 Present")
    def state_2(self):
        print("2 Present")
    def state_3(self):
        print("3 Present")
class two(one):
    def state_4(self):
        print("4 Present")
    def state_5(self):
        print("5 Present")
class three(two):
    def state_6(self):
        print("6 Present")
a=three()           #  ----->in this only two can access the attributes of one and one cannot access the attributes of class two
a.state_1()
a.state_2()
a.state_5()
a.state_6()
 here the class three has access to all the attributes of both one and two this is called multi level inheritance


MULTIPLE INHERITANCE


class one:
    def state_1(self):
        print("1 Present")
    def state_2(self):
        print("2 Present")
    def state_3(self):
        print("3 Present")
class two:
    def state_4(self):
        print("4 Present")
    def state_5(self):
        print("5 Present")
class three(one,two):
    def state_6(self):
        print("6 Present")
a=three()           #  ----->in this only two can access the attributes of one and one cannot access the attributes of class two
a.state_1()
a.state_2()
a.state_5()
a.state_6()


OPERATOR OVERLOADING

a="1"
b="2"
print(a+b)
print(str.__add__("1","2"))

class fruits:
    def __init__(self,apple,mango):
        self.apple=apple
        self.mango=mango
    def __add__(self,other):
        apple=self.apple+other.apple
        mango=self.mango+other.mango
        return fruits(apple,mango)
fruit = fruits(3,2)
fruit1 = fruits(2,3)
fruit2 = fruit+fruit1
print(fruit2)

DATA HIDING

class class1:
    def __init__(self):
        self._val_1=1
        self.val_2=2
    def __a(self):                  #---->private
        print("apple")
    def _b(self):                   #---->protected
        print("banana")
c=class1()
print(c._val_1)
#print(c.__a)
c._class1__a()                      #---->PRIVATE
print(dir(c))                      #---->DIR SHOWS ALL POSSIBLE attributes to be used to avoid errors

REGULAR EXPRESSIONS
it is used to validate the input(String)
here regex --->reg:regular and ex:expressions

import re
pattern ="apple"
if re.match(pattern,"banana"):  ---->it checks if the string is same or no
    print("true")
else:
    print("false")

FINDALL

import re
pattern="apple"
a=re.findall("p",pattern)     #it take 3 arguments they are patterns string and flag   match(patten, string, flags)
print(a)

SEARCH

import re
pattern="apple"
a=re.search("p",pattern,flags=0)     #it take 3 arguments they are patterns string and flag   match(patten, string, flags)
print(a)

import re
str="it is a dog"
pattern="dog"
a=re.sub(pattern,"cat",str,flags=0)
print(a)


CHARACTER AND CHARACTER SEQUENCES
#pattern=(".")
#patterns=("\S")
#pat=("\D")
#print(re.findall(pattern ,str ,flags=0))
#print(re.findall(patterns ,str ,flags=0))
#print(re.findall(pat,str,flags=0))
^ -----> matches the beginning of the line
$ -----> Matches the end of the line
. ----->Matches the character
\d ---->Matches the digit
\D ---->Matches the non digit
\s ---->Matches the whitespace
\S ---->matches the non whitespace

*------>Repeats a character zero or more times
+------>Repeats a character one or more times
(------>Indicates where string extraction is to start
)------>Indicates where string extraction is to end
?------>Matches the expression 0 to 1 times


import re
#str="it is a dog99"
str="shaktivel.prabhakar@gmail.com"
pattern="ha*"                           #--------->thiss * will find the characters from all whole string whereas
patterns="ha+"                          #--------->this + will only validate the input character from a single place if it is found it will not check for the
pat="s.*?"
pats="s.*?"
print(re.findall(pattern,str))
print(re.findall(patterns,str))
print(re.findall(pat,str))
print(re.findall(pats,str))

TKINTER
step 1: import tkinter
step 2: bring the gui interaction
step 3: adding inputs
step 4: main loop

BASIC STRUCTURE

import tkinter
from tkinter import *

window =Tk()                    #this class helps in interaction with the window

inpt=Label(window ,text = "first gui")
inpt.pack()

window.mainloop()
import tkinter
from tkinter import *

window =Tk()

input=Label(window,text="content")


input.pack()

window.title("title")
window.geometry("500x700")
window.config(bg="yellow")

window.mainloop()


import tkinter
from tkinter import *

window = Tk()

#input=Label(window,cursor="dotbox",text="hi all the text to be displayed")
# input.pack()

window.geometry("500x700")
window.config(bg="black")
window.title("Title Name")

#We need to creata a frame
frame1 = Frame(window,bg="green" ,height=100,width=100,cursor="dot")
frame2= Frame(window,bg="yellow",height=300,width=300,cursor="dotbox")
frame2.pack(side=BOTTOM)
button1=Button(frame1,text="BUTTON",bg ="white")
button1.pack()
frame1.pack(side=TOP)

mainloop()


from tkinter import *

window=Tk()

window.geometry("250x50")
label=Label(window,text="BSAT")
label1=Label(window,text="Password")
label2=Label(window,text="Mail")
label.grid(row= 0, column=1)
label1.grid(row=1, column=1)
label2.grid(row=2, column=1)
a = Entry(window,width=40,borderwidth=5)
b = Entry(window,width=40, borderwidth=5)
b.grid(row=1,column=2)
a.grid(row=2, column=2)
window.mainloop()


from tkinter import *

window=Tk()
window.geometry("500x150")
window.title("Window Title")
label2=Label(window,text="BSAT",bg="green",fg="grey",font="bold,12",)
label2.grid(row=0, column=2)
label=Label(window,text="MAIL ADDRESS :")
label.grid(row=1, column=1)
label1=Label(window,text="Password :")
label1.grid(row=2, column=1)
e=Entry(window,width=50 ,borderwidth=10)
e.grid(row=1, column=2)
e1=Entry(window,width=50 ,borderwidth=10)
e1.grid(row=2 , column=2)

def value():
        value1=e.get()
        print(value1)

        value2=e1.get()
        print(value2)
#def butwork():
#    print("New User")

btn=Button(window,text="Update Me",command=value, activebackground="grey",bg="white",font="bold,12   ")
btn.grid(row=3 , column=2)

window.mainloop()


from tkinter import *               #package named messagebox
import tkinter.messagebox
window=Tk()

window.geometry("500x500")
label=Label(window,text="MESSAGE BOX")
label.pack()
window.title("MESSAGE BOX")
tkinter.messagebox.showinfo("info" ,"Invalid Operation")

window.mainloop()


num=[1,2,3,4,5,6,7]
x=2
y=1
del num[x]
del num[y]
for n in num:
    print(n)
