#!/usr/bin/env python3.7
import math

# def myfunc(*args):
#     total = 0
#     for x in args:
#         total += x
#     return total

# print(f'Total is {myfunc(7,7)}')

# def myfunc(*args):
#     mylist = []
#     for value in args:
#         if (value % 2 == 0):
#             mylist.append(value)
#     return mylist

# print(f'here are the even values {myfunc(-1,2,3,4,5,6,7)}')

# def myfunc(mystr):
#     return_string = ""
#     for loop in range(len(mystr)):
#         if loop % 2 == 0:
#             return_string += mystr[loop].lower()
#         else:
#             return_string += mystr[loop].upper()
#     return return_string

# print(f"{myfunc('this is a long string')}")

# def myfunc(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a < b:
#             return a
#         else:
#             return b
#     else:  #if one is odd
#         if a < b:
#             return b
#         else:
#             return a

# print(f'{myfunc(2,5)}')

# def myfunc(*args):

#     total = 0
#     for x in args:
#         total += x
#     if total == 20 or 20 in args: 
#         return True
#     else:
#         return False   
    
# print(f'{myfunc(20,10)}')

# def old_macdonald(name):
#     return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

# print(f"{old_macdonald('macdonald')}")

# def master_yoda(sent):
#     sentence = sent.split()
#     return ' '.join(sentence[::-1])

# print(f"{master_yoda('We are ready')}")

# def almost_there(n):
#     range_100 = range(90,111)
#     range_200 = range(190,211)
#     if n in range_100 or n in range_200: 
#         return(True)
#     else:
#         return(False)
# print(f"{almost_there(209)}")

# def has_33(*args):
#     search_value = 3
#     index = args.index(search_value) if search_value in args else -1
#     len_args = len(args) - 1
#     print(f'this is index {index}')
#     if index == -1:         #if not in the tuple that comes in this will run
#         return False
#     if index >= 0:
#         while index < len_args: 
#             print(f'Current index is {index} and the length is {len_args}')           
#             if args[index + 1] == search_value and args[index] == search_value:
#                 return True
#             index += 1
#         return False
#     else:      
#         print('does this get used')
#         return False    #this 

# result = has_33(31,2,4,5,31)
# print(f'result is {result}')

# def paper_doll(text):
#     return_string = ""
#     for loop in range(len(text)):
#         return_string += text[loop] * 3
#     return return_string

# result = paper_doll('Mississippi')
# print(f'result is {result}')

# def cal_volume_of_sphere(radius):
#     return (4/3 * math.pi) * (radius** 3)

# print(f'This is the volumen of the sphere {cal_volume_of_sphere(5)}')

# def check_if_in_range(num,low,high):
#     if num in range(low,high):
#         return True
#     else: 
#         return False

# print(f'this is the range to check {check_if_in_range(30,10,30)}')


# def cal_up_and_low_letters(sentence):
#     upper_case_count = 0
#     lower_case_count = 0
#     for loop in range(len(sentence)):        
#         if sentence[loop] == sentence[loop].upper():
#             print(f'{sentence[loop]} checkupper {sentence[loop].upper()}')
#             upper_case_count += 1
#         else:
#             print(f'{sentence[loop]} checklower {sentence[loop].upper()}')
#             lower_case_count += 1
#     return(upper_case_count,lower_case_count)
# result = cal_up_and_low_letters("now is the Time FOR aas")
# print(f'No. of Uppercase Character : {result[0]}\nNo. of lowerCase Character: {result[1]}')

# def unique_list(mylist):
#     return list(set(mylist))

# print(f'this is the unique list {unique_list([1,1,1,1,2,2,3,3,3,3,4,5])}')

# def mutiply(mynumlist):
#     total = 1
#     for loop in range(len(mynumlist)):
#         total *= mynumlist[loop]
#     return total

# print(f' {mutiply([2,3,4,5,6])}')

def palidrome(s):
    forward_string = list(s)
    reverse_string = forward_string[::-1]    
    if (reverse_string == forward_string):
        return True
    else:
        return False

print(f"is it s paladrone {palidrome('heflleh')}")

