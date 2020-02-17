import sys
import csv

filename="file"
with open(fileName) as user_list: 
    reader=csv.reader(user_list,delimiter=",")
    line_count=0

