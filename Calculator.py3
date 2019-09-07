# For choice 
print("1. Addition  ")
print("1. Subtract  ") 
print("3. Multiply  ")
print("4. Division  ")
ch=int(input("Enter Your Choice  "))
if ch==1 :
	a=int(input("Enter First Number  "))
	b=int(input("Enter Second Number  "))
	c=a+b
	print("Answer is  ",c)
elif ch==2 :
	d=int(input("Enter First Number  "))
	e=int(input("Enter Second Number  "))
	f=d-e
	print("Answer is  ",f)
elif ch==3 :
	g=int(input("Enter First Number  "))
	h=int(input("Enter Second Number  "))
	i=g*h
	print("Answer is  ",i)
elif ch==4 :
	j=int(input("Enter First Number  "))
	k=int(input("Enter Second Number  "))
	l=j/k
	print("Answer is  ",l)
else :
	print("Enter A Wrong Choice  ")	