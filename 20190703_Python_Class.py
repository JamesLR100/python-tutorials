# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello World!")

phrase = 'Please split me into HELLO multiple splits using space'

phrase_list = phrase.split()

print(phrase_list)

phrase_comma = phrase.replace(' ', ',')

print(phrase_comma)

phrase_comma_split = phrase_comma.split(',')

print(phrase_comma_split)

p2 = 'Please find the index of HELLO in this string'

idx = p2.find('HELLO')
print(idx)

p3 = 'We are in all state'
p4 = 'You are in good hands'
psum = p3 + p4
print(psum)

print(psum[3:])

print(psum[::-1])

print(psum[::2])

#Replace backslash with forward slash. 
open("C:/Users/James/data01.csv")

#Name the object to store the file.
f=open("C:/Users/James/data01.csv")

#After applying the close method, you cannot read from it but the file is not deleted.
f.close()

#Resets the cursor to read from file again.
f.seek(0)

#Flush method (if you do not want to close)
f.flush()

#read, write, append modes

#Read mode (default)
f=open("C:/Users/James/data01.csv", 'r')

#Write mode
f=open("C:/Users/James/data01.csv", 'w')

#Append mode
f=open("C:/Users/James/data01.csv", 'a')

#Console will show newline marks "\n" in output.
f.read()

#If you wanted to read from the beginning again, call a seek at 0:
f.seek(0)
f.read()

f.seek(10)
f.read(10)

f.seek(10)
g = f.read(10)

print(g)

#Split the file into a list line by line. 
#h is the string resulting from reading the full .csv file.
f.seek(0)
h = f.read()
line_list = h.split("\n")
print(line_list)

#First element of the list (first line of file):
line_list[0]

type(line_list[0])

first_line_list = line_list[0].split(',')
print(first_line_list)

#This applies splits across every line using a for loop.
#Using the list list_of_lists can simplify some searches later.
list_of_lists = []
for line in line_list:
    list_of_lists.append(line.split(','))
print(list_of_lists)

#Convert string to integer:
int('999')

#(5th row, 4th column from end) add 2
int(list_of_lists[4][-4]) + 2
#Result: 139

#ALTERNATE METHOD
#In a direct manner from the string h defined from reading the csv file:
int(h.split('\n')[4].split(',')[-4]) + 2 

#Creates text file with the result of "139".
#Note: We need to convert to string to apply the write method to result.
result = open("C:/Users/James/result.txt", "w")
result.write(str(int(h.split('\n')[4].split(',')[-4]) + 2))
result.close()
#Now the result is saved and we can view the result "139" in the text file.

#EXERCISE
#See print_2nd_line.py
import requests

#Create object r of requests type:
r = requests.get('https://raw.githubusercontent.com/becloudready/snowflake-tutorials/master/dataset/employees01.csv')
#<Response [200]>
r.status_code
#text attribute
get_text = r.text
get_text #This includes \n.
print(get_text) #This does not.

get_list = get_text.split('\n')
get_list[1]

file_text=open("C:/Users/James/text_line.txt", 'w')
file_text.write(get_list[1])
file_text.close()

#Find '177' in the address and then add 2
int(get_list[-2].split(',')[-3][:3]) + 2

#Here is the request through Postman:

#import requests

url = "https://jr-bucket.s3.amazonaws.com/employees01.csv"

headers = {
    'Host': "jr-bucket.s3.amazonaws.com",
    'X-Amz-Content-Sha256': "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    'X-Amz-Date': "20190703T185655Z",
    'Authorization': "AWS4-HMAC-SHA256 Credential=AKIA4HCIUWEI6QHCLHQH/20190703/us-east-1/s3/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=e650f94d3527c17dc19408335a98de7de638afdb9e8b019fb354d1e1c7e92af4",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "1dc66d17-5624-448e-929d-ca5b6083df78,f20fe10d-3b4d-43dd-9d2d-80356fd7613f",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

r_text = response.text

print(r_text)

#int('177') + 2
int(r_text.split('\n')[-2].split(',')[-3][:3]) + 2

import os
print(os.getcwd())

#Find today's date using the package datetime
import datetime
print(datetime.datetime.now())
print(datetime.date.today())
#check about utc

#ddmmyyyy
#strftime
date_today=datetime.date.today()
date_today.strftime("%d%m%Y")
date_today.strftime("%d/%m/%Y")





















