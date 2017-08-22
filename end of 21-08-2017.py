import os
import glob
flist=[]
flist=glob.glob('newfolder\\*')
print(flist)




fo=open(flist[0],"r")
str=fo.read()
str=str.lower()
st1=""
for i in str:
	if(97<=ord(i)<=122 or 48<=ord(i)<=57):
		st1=st1+i
	else:
		st1=st1+' '
print(st1)
data = st1.split() #split string into a list
dict={}
for i in data:
	if i not in dict:
		dict[i]=1
	else:
		dict[i]=dict[i]+1
print(dict)
f1=open(flist[1],"r")
st=f1.read()
st=st.lower()
st2=""
for i in st:

	if(97<=ord(i)<=122 or 48<=ord(i)<=57):
		st2=st2+i
	else:
		
		st2=st2+' '
print(st2)		
data1=st2.split()
dict1={}
for word in data1:
	if word not in dict1:
		dict1[word]=1
	else:
		dict1[word]=dict1[word]+1
l=[]
print(dict1)
for i in dict:
	for j in dict1:
		if(i==j):
			l.append(dict[i]*dict1[j])
tot=0
for i in l:
	tot=tot+i
sum=0
for i in dict.values():
	sum=sum+i**2
v=sum**(1/2)
sum=0
for j in dict1.values():
	sum=sum+j**2
k=sum**(1/2)
g=v*k
prod=((tot)/g)*100
print("copied percentage is:",prod)
