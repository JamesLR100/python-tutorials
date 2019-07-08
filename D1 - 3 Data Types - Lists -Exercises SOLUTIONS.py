# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:22:10 2019

Solutions by James Richardson

@author: SHAIL
"""
abcd = ['nintendo','Spain', 1, 2, 3]

print(abcd)

# Ex1 - Select the third element of the list and print it
print(abcd[2])
#1


# Ex2 - Type a nested list with the follwing list elements inside list abcd mentioned above and print it

newlist = [54,76]

abcd.append(newlist)
print(abcd)
#['nintendo', 'Spain', 1, 2, 3, [54, 76]]


# Ex3 - Print the 1 and the 4 position element in the following list

nestedlist = ["shail", [11,8, 4, 6], ['toronto'],abcd, "abcd"]

print(nestedlist[1])
#[11, 8, 4, 6]
print(nestedlist[4])
#abcd

# Ex4  - add the following 2 lists and create list3 (remove strings and concatenate) and print 

list1= [10, 20, 'company', 40, 50, 100]

list2 = [100, 200, 300, 'orange', 400, 500,1000]

#Remove the strings
del(list1[2])
del(list2[3])
#Concatenate
list3 = list1 + list2
print(list3)
#[10, 20, 40, 50, 100, 100, 200, 300, 400, 500, 1000]


# Ex 5 - print the lenght of the list3

print(len(list3))
#11

# Ex 6 Add 320 to list 1 and print

list1.append(320)
print(list1)
#[10, 20, 40, 50, 100, 320]


#Ex 7 - Add parts of list1 & 2 by taking first 4 elements from list1 and last 2 elements from list2
print(list1[:4] + list2[-2:])
#[10, 20, 40, 50, 500, 1000]


#ex 8 check if 99 is in list 1 

99 in list1
#False

#ex 9 check if 99 is not in list 1 

99 not in list1
#True

# concatenation (+) and replication (*) operators
#ex 10 - CONCATENANTE  list 1 and ['cool', 1990]

print(list1 + ['cool', 1990])
#[10, 20, 40, 50, 100, 320, 'cool', 1990]

# Ex 11 -  triplicate the list 1
print(list1*3)
#[10, 20, 40, 50, 100, 320, 10, 20, 40, 50, 100, 320, 10, 20, 40, 50, 100, 320]


# ex 12 - find min & max of list2
print(min(list2))
#100
print(max(list2))
#1000


# append & del
# Ex 13 append 'training' to list 1

list1.append('training')
print(list1)
#[10, 20, 40, 50, 100, 320, 'training']


# Ex 14 delete 2nd position element from list 2

del(list2[1])
print(list2)
#[100, 300, 400, 500, 1000]


# Ex 15 - iterate over list1 and print all elements by adding 10 to each element

list1= [10, 65,20, 30,93,  40, 50, 100]

for num in list1:
    print(10 + num)
#20
#75
#30
#40
#103
#50
#60
#110  
    

# for x in list1:
    


#Ex 16 sorting

#sort list1 by ascending order

list1.sort()
print(list1)
#[10, 20, 30, 40, 50, 65, 93, 100]

#sort list1 by reverse order
list1.sort(reverse=True)
print(list1)
#[100, 93, 65, 50, 40, 30, 20, 10]
   

