# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:56:33 2017

@author: Ana
"""
from numpy import *

"""
Random number guessing game
"""
#a = random.randint(1,9)
#
#counter = 1
#user_1 = ((input("Guess what the number is: ")))
#
#while user_1 != "exit":
#      
#    
#    if user_1 == "exit":
#        break
#    
#    user_1 = int(user_1)
#    
#    if user_1 > a:
#        print ("Too high")
#    elif user_1 < a:
#        print ("Too low")
#    else:
#        print ("You're correct!", 'counter',counter)
#        break
#    
#    counter = counter +1 
#    user_1 = ((input("Guess what the number is: ")))

"""   
List Overlap Comprehensions/ similar in 2 lists
"""
#a = random.randint(1,12,8)
#b = random.randint(1,14,6)
#
#c = [a for a in b if a not in c]
#
#print('a',a,'b',b,'c', c)
 
"""
Prime number checker
"""   
#def getnumber(prompt):
#
#    return int(input(prompt))
#    
#def is_prime(number):
#    #edge cases
#    if number == 1:
#        prime = False
#    elif number == 2:
#        prime = True
#    
#    #All other cases
#    else:
#        prime = True
#        for check_number in range(2,int(number/2)+1):
#            if number % check_number == 0:
#                prime = False
#                break
#    return prime
#    
#def print_prime(number):
#    prime = is_prime(number)
#    if prime:
#        descriptor = ""
#    else:
#        descriptor = "not "
#    
#    print(number, " is ", descriptor , "prime.", sep= "", end =  "\n\n")
#    
#        
#while 1 == 1:
#    print_prime(getnumber("enter a number to check. escape to exit."))

"""
list ends (gathering info)
"""
#a = random.randint(1,10,5)
#
#c = [a[0],a[-1]]
#print (c)

"""
Fibonacci
"""
#Better way to imrpove this in terms of efficency
#is to think about edge limits
#and results that can have simple outputs
#then doing the fomulation
#def how_many(prompt):
#    return (int(input(prompt)))
#    
#def fibonacci(number):
#    a = zeros(number)
#    a[0] = a[1] = 1
#
#    for n in range(2,number):
#        a[n] =  a[n-1] + a[n-2]
#        
#    return a
#    
#print(fibonacci(how_many("How many Fibonnaci numbers to generate? ")))

"""
List remove duplicates
"""
#a = list(random.randint(1,13,7))
#
#def sort(a):
#    b = set(a)
#    
#    return b
#    
#def sort_2(a):
#    c = []    
#    for i in a:
#        if i not in c:
#            c.append(i)
#    return c
#    
#print('a',a,sort(a),sort_2(a))

"""
Reverse word order
"""
#def statement(prompt):
#    return(str(input(prompt)))
#    
#def backwards_statement(string):
#    y = string.split()
#    y = y[::-1]
#    x = " ".join(y)
#    return x
#    
#print(backwards_statement(statement("Please enter text here: ")))

"""
Password generator
"""
#need to make such numpy isnt all imported
#np.random.sdample() != random.sample()
#import numpy as np
#import random
#
#def password_strength(prompt):
#    return (str(input(prompt)))
#    
#def password (value):
#    weak_words = ["free","string","trust","yahoo","mingle","opposite"]
#    numbers = np.random.randint(1,5,4)
#    letters_symbols = "thequickbrownfoxjumpsoverlazydog£$%&@#?!"
#
#    y = value.casefold()
#    passlen = 8
#    
#    if y == "weak":
#        password = weak_words[(numbers[0])]+str(numbers[0])+weak_words[(numbers[1])]
#    
#    elif y == "medium":
#        randIndex = random.sample(letters_symbols,passlen)
#        password = "".join(randIndex)
#    
#    elif y == "strong":
#        randIndex = random.sample(letters_symbols,passlen)
#        for i in range(0,len(randIndex)):
#            if randIndex[i].isalpha()==True and i%numbers[2]==0:
#                randIndex[i] = randIndex[i].capitalize()
#        password = "".join(randIndex)
#
#    return password
#    
#print(password(password_strength("How strong do you want your password: \
#weak, medium or strong? = ")))
"""
Decode A Web Page (exercise 17)
"""
"""
exercise 18
"""
"""
Decode A Web Page 2 (exercise 19)
"""
"""
Element Search (exercise 20) look over
"""
#a = random.randint(1,10,8)
#
#def sort(a):
#    return a.sort()
    
#def user_input(prompt):
#    return int(input(prompt))
#    
#def isinlist (a,b):
#    counter = 0
#    for i in a:
#        if i == b:
#            counter += 1

#    print (b, " is in list %d times" %counter, a)
#  
### same thing but using binary search: 


#def binary_search(a,b):
###doesn't work unless number is list XD
#    a = sort(a)
#    print(a)
#    while True:
#        middle = len(a)//2
#        print("middle",middle, "a", a[middle])
#        if middle < 0 or middle > (len(a)-1):
#            print("not in list")
#            break
#            
#        
#        if a[(middle-1)] == b:
#            print (b, " is in list")
#            break
#        elif a[(middle-1)] > b :
#            a = a[0:(middle-1)]
#            
#        elif a[(middle-1)] < b :
#            a = a[(middle-1):-1]
#        else:
#            print ("not in list motherfucker!")
#            
#    return
#            
#    
##
##print(isinlist(a,user_input("What number do you think is in this list?: ")))
#
#print(binary_search(a,user_input("What number do you think is in this list?: ")))
#



    
