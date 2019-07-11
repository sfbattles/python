#!/usr/bin/env python3.7
import os

my_name = "POTTER=DAVID=LOUIS"
my_list = my_name.split("=")
lastname_list = [my_list[0]]
firstname_list = my_list[1:] 
display_list = firstname_list + lastname_list

# print(*display_list, sep = " ")

# s ='hello'
# print(s[::-1])

# list4 = [5,3,4,6,1]
# list4.sort()
# print(f'he is the list {list4}')

# d = {'simple_key':'hello'}
# # Grab 'hello'
# print(f"say {d['simple_key']} ")

# d = {'k1':{'k2':'hello'}}
# # Grab 'hello'
# print(f" this is {d['k1']['k2']}")

# Getting a little tricker
os.system('clear')
# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# print(f"this is {d['k1'][0]['nest_key'][1]} ")


#Grab hello
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(f"this is {d['k1'][2]['k2'][1]['tough'][2]} ")
print(3.0 == 3)

with open('test.txt', mode='w') as filename:
    filename.write('Hello World')

st = 'Print only the words that start with s in this sentence'
sentence = st.split(" ")
for loop in range(len(sentence)):
    if sentence[loop][0] == 's':
        print(f'{sentence[loop]}')

st = 'Print every word in this sentence that has an even number of letters'
sentence = st.split()
print(sentence)
for loop in range(len(sentence)):
    if len(sentence[loop]) % 2 ==0:
        print(sentence[loop])

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for loop in range(1,101):
    if loop % 15 == 0:
        print("FizzBuzz")
    elif loop % 5 == 0:
        print('Buzz')
    elif loop % 3 == 0:
        print("Fizz")  
    else:
        print(loop)

#Code in this cell
st = 'Create a list of the first letters of every word in this string'
sentence = st.split(" ")
thelist = []
for loop in range(len(sentence)):
    thelist.append(sentence[loop][0])
print(f'{thelist}')        


class Car:
    def __init__(self, year,make,model):
        self.year = year
        self.make = make
        self.model = model

    def age(self, year):
        self.year=2019
        return self.year


abc=Car("2019","Hyundai","Accent")

print (abc.year)
print (abc.make)
print (abc.model)


shoes=["Spizikes","Air force1","Curry2", "Melo5"]
for shoe in shoes:
    print(shoe)  