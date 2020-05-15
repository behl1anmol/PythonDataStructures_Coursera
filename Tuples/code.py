"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name,"r")

s=""
dic={}

for line in handle:
    line=line.rstrip()
    s=line.split(" ")
    if s[0] !="From":
        continue
    for i in s:
        if ":" in i:
            j=i.split(":")
            temp=j[0]
            if temp in dic:
                dic[temp]+=1
            else:
                dic[temp]=1
lst = list()

for key, value in dic.items():
    lst.append( (key,value) )
lst.sort()

for hour, counts in lst:
    print(hour, counts)
