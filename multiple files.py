import os
import glob
flist=[]
flist=glob.glob('newfolder\\*')
print(flist)

def readfile_split(fo):
	st=fo.read()
	st=st.lower()
	st1=""
	for i in st:
		if(97<=ord(i)<=122 or 48<=ord(i)<=57):
			st1=st1+i
		else:
			st1=st1+' '
	print(st1)
	data = st1.split()
	return data
z=[]
for i in range(len(flist)):
	fo=open(flist[i],'r')
	z.append(readfile_split(fo))
print(z)
def frequency(k):
	dict={}
	for i in k:
		if i not in dict:
			dict[i]=1
		else:
			dict[i]=dict[i]+1
	return dict
d=[]
for i in z:
	print(i)
	d.append(frequency(i))
print(d)
def dotproduct(r,h):
	l=[]
	for i in r:
		#print(i)
		for j in h:
			#print(j)
			if(i==j):
				l.append(r[i]*h[j])
	return l
l=[]
for i in range(0,len(d)-1):
	for j in range(0,len(d)):
		if(i<j):
			l.append(dotproduct(d[i],d[j]))
print(l)
def euclidian_form(r):
	sum=0
	for i in r.values():
		sum=sum+i**2
	v=sum**(1/2)
	return v
z1=[]
for i in d:
	z1.append(euclidian_form(i))
print(z1)
def sum_of_dotproduct(l):
	tot=0
	for i in l:
		tot=tot+i
	return tot
z2=[]
for i in l:
	z2.append(sum_of_dotproduct(i))
print(z2)
z3=[]
for i in range(0,len(z1)):
	
	for j in range(0,len(z1)):
		if(i<j):
			z3.append(z1[i]*z1[j])
print(z3)
prod=[]
for i in range(len(z3)):
	prod.append((z2[i])/(z3[i]))
print(prod)







		






	


