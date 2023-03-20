#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is 
#the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name.upper()+"!")
    ##in case user puts lower case it will turn to upper##
hello_name("USERNAME")

#Question 2
#Write a python function, first_odds that prints the odd numbers
# from 1-100 and returns nothing


def first_odds():
    for x in range(1, 100):
        if x % 2 == 1:
            print(x, end=" ")

## to get the lists of odd nos in 1-100 do **print(first_odds())**on a new line

#Question 3
#Please write a Python function, max_num_in_list to return
# the max number of a given list. The first line of 
# the code has been defined as below.

def max_num_in_list(a_list):
    max=a_list[0]
    for x in a_list:
        if x > max:
            max = x
    return max

##testing my code
#  a_list=[30,60,90,100]        
##print("The higher price of item is: ",max_num_in_list(a_list))
 
#Question 4
#Write a function to return if the given year is a leap year.
#A leap year is divisible by 4, but not divisible by 100, unless it
# is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    leap=False
    # divided by 100 means century year
    # century year divided by 400 is leap year
    if (a_year % 400 == 0) and (a_year % 100 == 0):  
       # change leap to True
        leap = True
        print(True)
    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (a_year % 4 ==0) and (a_year % 100 != 0):  
        #Change leap to true
        leap = True
        print(True)
    #else not a leap year
    else:      
        pass
    
    return leap    

## Testing my code not part of assignment print(is_leap_year(2022))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] 
#are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))

##Test my code #a_list =[3,4,7,6,5,8]
#print(is_consecutive(a_list))