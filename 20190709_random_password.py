# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:06:42 2019

HOMEWORK EXERCISE

Create a random password of length 5 to 8 characters with the requirements:
    - 1 special character, drawing from characters like "~!@#$%^&*()_-+="
    - At least 2 numerical digits (0-9)
    - At least 1 capital letter A-Z
    - At least 1 lowercase letter a-z
    
@author: James Richardson
"""

#REFERENCE FOR APPLICATIONS OF randint TO RANDOMIZE VARIOUS CHARACTER CLASSES

#We can reference this dictionary of ASCII characters to find corresponding
#characters when applying the chr() function: 

ascii_dict = {k : chr(k) for k in range(200)}

#Shows with minimal space, but visually crowded in the console:
print(ascii_dict)

#A longer, but cleaner view of the dictionary:
ascii_dict

#NOTES ON PATTERNS OF ASCII CHARACTERS WITH CORRESPONDING ASSIGNMENT FUNCTIONS

#NUMERIC (0-9):
#   48-57
#   10 characters
#For x in range(10), we define the assignment function:
def numeric(x):
    return chr(x+48)

#UPPERCASE ALPHABET (A-Z):
#   65-90
#   26 characters    
#For x in range(26), we define the assignment function:
def alpha_upper(x):
    return chr(x+65)

#LOWERCASE ALPHABET (a-z):
#   97-122
#   26 characters    
#For x in range(26), we define the assignment function:
def alpha_lower(x):
    return chr(x+97)    

#FULL RANGE OF ALPHANUMERIC CHARACTERS COMBINED WITH SPECIAL CHARACTERS:
#   33-126
#   94 characters    
#For x in range(94), we define the assignment function:
def all_char(x):
    return chr(x+33)

#FULL RANGE OF ALPHANUMERIC CHARACTERS (WITHOUT SPECIAL CHARACTERS):
#   48-57, 65-90, 97-122 
#   10 + 26 + 26 = 62 characters    
#For x in range(62), we define the assignment function:
def alpha_num(x):
    if x < 10:
        return chr(x+48)
    elif x >= 10 and x < 36:
        return chr(x-10+65)
    else:
        return chr(x-36+97)

#SPECIAL CHARACTERS:
#   33-47, 58-64, 91-96, 123-126
#   15 + 7 + 6 + 4 = 32 characters
#For x in range(32), we define the assignment function:   
def special(x):
    if x < 15:
        return chr(x+33)
    elif x >= 15 and x < 22:
        return chr(x-15+58)
    elif x >= 22 and x < 28:
        return chr(x-22+91)
    else:
        return chr(x-28+123)
        

#PASSWORD RANDOMIZATION CODE BEGINS HERE:

import random as r

#Define a function to generate passwords at least 5 characters in length:
def generate_pw(n=8,min=5,crazy=False):

    #Randomize the length from min>=5 to n>=8, where n=8 and min=5 are default values. 
    #Note that the range for the function randint is inclusive.
    length = r.randint(min,n)

    #Initialize a list to store each random character appended in the for loop:
    pass_list = []

    for k in range(length):
        #Choose 2 numeric characters (0-9):
        if k == 0 or k == 1:
            pass_list.append(numeric(r.randint(0, 9)))
        #Choose 1 capital letter (A-Z):
        elif k == 2:
            pass_list.append(alpha_upper(r.randint(0, 25)))
        #Choose 1 lowercase letter (a-z):
        elif k == 3:
            pass_list.append(alpha_lower(r.randint(0, 25)))
        #Choose 1 special character:
        elif k == 4:
            pass_list.append(special(r.randint(0, 31)))
        elif k >= 5:
            #For the default setting, characters beyond 5 are randomly selected
            #from alphanumeric characters, not including special characters:
            if crazy==False:
                pass_list.append(alpha_num(r.randint(0, 61)))    
            #If you like crazy passwords with more than one special character, I included a
            #"crazy" option to include random special characters beyond 5:
            else:
                pass_list.append(all_char(r.randint(0, 93)))
        
    #Now randomize the order of the list using the shuffle function:
    r.shuffle(pass_list)

    #Join the elements of the list to create the password as a string:
    password = ''.join(pass_list)
    
    return password

#The default version of the function yields exactly one special character with 
#total character length between 5 and 8:
print(generate_pw())

#If you are feeling wild, you can generate long passwords with many special characters:
print(generate_pw(n=100, min=50, crazy=True))


#CALCULATING THE CARDINALITY OF ALL POSSIBLE GENERATED PASSWORDS 

#The difficulty in calculating all the possible combinations with pen and paper
#is that when we introduce the larger character classes with alphanumeric or
#alphanumeric with special, the other classes are subclasses that overlap.
#To avoid redundancy, we can divide these superclasses into their distinct subclasses
#for all possible cases (numeric, lowercase, uppercase, and special) but this
#can be especially tedious. Fortunately, we have for loops to do this dirty work!

from math import factorial as fa

#We follow the same parameter constraints of the function generate_pw (n>=min>=5).
def pw_combinations(n=8,min=5,crazy=False):
    count=0
    #For the crazy case, the number of special characters can be greater than one.
    if crazy==True:
        for k in range(min, n+1):
            #j is number of numerical characters (j>=2):
            for j in range(2,k):
                #s is number of special characters (s>=1):
                for s in range(1,k):
                    #l is the number of lowercase characters (l>=1):
                    for l in range(1,k):
                        #u is the number of uppercase characters (u>=1):
                        for u in range(1,k):
                            #We require the sum to be k for counting purposes:
                            if j+s+l+u==k:
                                #We apply combinatorial arguments for each distinct possible case,
                                #using factorials to count distinct orders of character classes.                              
                                count+=(10**j)*(32**s)*(26**(l+u))*(fa(k))/(fa(j)*fa(s)*fa(l)*fa(u))
        return count
    #For the false case, we simply require s=1:
    elif crazy==False:
        for k in range(min, n+1):
            #j is number of numerical characters (j>=2):
            for j in range(2,k):
                #l is the number of lowercase characters (l>=1):
                for l in range(1,k):
                    #u is the number of uppercase characters (u>=1):
                    for u in range(1,k):
                        #We require the sum to be k for counting purposes:
                        if j+1+l+u==k:
                            #Same as above with s=1:
                            count+=(10**j)*32*(26**(l+u))*(fa(k))/(fa(j)*fa(l)*fa(u))
        return count
    
pw_combinations()
#261812052736000.0

pw_combinations(crazy=True)
#884615676672000.0

pw_combinations(n=9, min=9)
#2.26642362605568e+16       
#Already Python is running out of space with the allocated significant digits...       
        
                                
                                
        
        

    
    
        

