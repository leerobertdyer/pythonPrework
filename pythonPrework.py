# Question 1
# Write a function to print “hello_USERNAME!” 
# USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name)

# My Test:
# hello_name('lee robert dyer')

        
# Question 2
# Write a python function, 
# first_odds that prints the odd numbers 
# from 1-100 and returns nothing

def first_odds():
    x = range(2, 102, 2)
    for num in x:
        print(num)

# My Test:
# first_odds()


# Question 3
# Please write a Python function, 
# max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.


def max_num_in_list(a_list):
    x = 0
    for num in a_list:
        if num > x:
            x = num
    return x

# My Test: 
# print(max_num_in_list([1, 1, 2, 16, 1241, 999, 999999, 1, 234, 1]))

        

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. 
# The return should be boolean Type (true/false).


def is_leap_year(a_year):
    if a_year % 400 == 0:
        if a_year % 4 == 0 and a_year % 100 == 0:
            return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else: return False

# My Tests:
# print(is_leap_year(100))
# print(is_leap_year(2000))
# print(is_leap_year(1200))
# print(is_leap_year(400))



# Question 5
# Write a function to check to see 
# if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    firstNumCheck = a_list[0] - 1
    for num in a_list:
        if num == firstNumCheck + 1:
            firstNumCheck += 1
        else: return False
    return True

# My Tests:
# print(is_consecutive([1, 2, 3]))
# print(is_consecutive([3, 2, 1]))
# print(is_consecutive([1, 2, 3, 5]))