# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:44:46 2019

@author: James
"""
import requests
#Create object r of requests type:
r = requests.get('https://raw.githubusercontent.com/becloudready/snowflake-tutorials/master/dataset/employees01.csv')

#text attribute
get_text = r.text

#Make a list of lines from the text:
get_list = get_text.split('\n')

#Open the file text_line.txt with write setting:
file_text=open("C:/Users/James/text_line.txt", 'w')
#Write second line to file:
file_text.write(get_list[1])
#Close to save the write:
file_text.close()