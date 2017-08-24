st='to be or not to be'
n=len(st)
st1=""
l=[]
for i in range(len(st)):
	st1=""
	for j in range(i,len(st)):
		st1=st1+st[j]
		l.append(st1)
print(l)
st2='doubt truth to be a liar'
n1=len(st2) 
st3=""
l1=[]
for i in range(len(st2)):
	st3=""
	for j in range(i,len(st2)):
 		st3=st3+st2[j]
	 	l1.append(st3)
print(l1)
l2=[]
for i in l:
 	if i in l1:
 			l2.append(i)
print(l2)
k=[]
p=0
j=0
for i in range(0,len(l2)):
	if(len(l2[i])>p):
		p=len(l2[i])
		#print(p)
		j=i

print(l2[j])

		
print(n+n1)
print(p)
r=(p*2)/(n+n1)
print (r*100)
