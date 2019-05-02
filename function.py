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

def almost_there(n):
    range_100 = range(90,111)
    range_200 = range(190,211)
    if n in range_100 or n in range_200: 
        return(True)
    else:
        return(False)

print(f"{almost_there(209)}")




