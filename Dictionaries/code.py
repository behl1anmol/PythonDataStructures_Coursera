"""
Write a program to read through the mbox-short.txt and
figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program
creates a Python dictionary that maps the sender's mail
address to a count of the number of times they appear in the file.
 After the dictionary is produced, the program reads through the
 dictionary using a maximum loop to find the most prolific committer.

"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name,"r")

dic=dict()
s=""
for line in handle:
    line=line.rstrip()
    s=line.split(" ")
    if s[0]=="From":
        temp=s[1]        
        if temp in dic:
            dic[temp]+=1
        else:    
			dic[temp]=1
email=''
count=0

for keys in dic:
    if count<dic[keys]:
        count=dic[keys]
        email=keys       
print(email,count)  