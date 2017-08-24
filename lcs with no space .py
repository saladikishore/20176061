fo=open('1.txt','r')
st=fo.read()
st="what is your name"
n=len(st)
st1=""
l=[]
for i in range(len(st)):
	st1=""
	for j in range(i,len(st)):
		st1=st1+st[j]
		l.append(st1)
print(l)
f1=open('2.txt','r')
st2="doubt truth to be liar"
n1=len(st2) 
st3=""
l1=[]
for i in range(len(st2)):
	st3=""
	for j in range(i,len(st2)):
 		st3=st3+st2[j]
	 	l1.append(st3)
l2=[]
for i in l:
 	if i in l1:
 			l2.append(i)

k=[]
p=0
j=0
for i in range(0,len(l2)):
	if(len(l2[i])>p):
		p=len(l2[i])
		j=i


st4=l2[j].strip(' ')
print(st4)
l=len(st4)	
print(l)
print(n)
print(n1)
print(n+n1)
r=(l*2)/(n+n1)
print (r*100)
