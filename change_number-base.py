# convert postive decimal numbers to other base 2-10
# Author: Roxana Haghgoo

# get base from user
run = True
while run:
    base = input(">>> Please enter the 'base' you want to convert to: ")
    try:
        base = int(base)
        if base >= 0 and base < 11:
            run = False
        else:
            print("\n> please type a number in range(2-10)! \n")
    except:
        print("\n> please type a number! \n")


# lists of powers of base numbers
list1 = [base ** i for i in range(50)]
list1.sort(reverse=True)
list2 = list1.copy()
indexs = []


# get a decimal number from user
run = True
while run:
    decimal = input('>>> Please enter a decimal number:  ')
    try:
        decimal = int(decimal)
        if decimal >  0:
            run = False
        else:
            print("\n> please type a postive number \n")
    except:
        print("\n> please type a number! \n")
num = decimal

# find decimal number position between power numbers and replace it, and subtract main number
for i in list1:
    if num >= i:
        indexs.append(list1.index(i))
        list2[list1.index(i)] = num // i
        num = num % i
        continue

# replace numbers that didnt change with 0
for i in range(len(list2)):
    if i not in indexs:
        list2[i] = 0


# convert number to string 
def not_zero():
    for i in list2:
        if i != 0 :
            return list2.index(i)
# display
new = list2[not_zero()::]
new = map(str, new)
res = ''.join(new)
print(f'>>> The {base}-base form of {decimal} is: >>> {res}')


# -----------------------------------------------------------------------------------------------------
# old code 

# # get base from user
# base = int(input("Please enter the base you want to convert to: "))

# # lists of powers of base numbers
# list1 = [base ** i for i in range(30)]
# list2 = [base ** i for i in range(30)]
# list1.sort(reverse=True)
# list2.sort(reverse=True)
# indexs = []


# # get a decimal number from user
# decimal = int(input('Please enter a decimal number:  '))
# num = decimal

# # find decimal number position between power numbers and replace it, and subtract main number
# for i in list1:
#     if num >= i:
#         indexs.append(list1.index(i))
#         list2[list1.index(i)] = num // i
#         num = num % i
#         continue


# # replace numbers that doesnt change with 0
# for i in range(len(list2)):
#     if i not in indexs:
#         list2[i] = 0


# # convert number to string to display
# def not_zero():
#     for i in list2:
#         if i != 0 :
#             return list2.index(i)

# new = list2[not_zero()::]
# new = map(str, new)
# res = ''.join(new)
# print(f'The {base}-base form of {decimal} is: >>> {res}')





