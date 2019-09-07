# For asending list without sorting
a=[]
n=6
for i in range(n):
    ele=int(input("Enter the Value of Elements  "))
    a.append(ele)
print("The Value of List is  ",a) 
b=len(a)
for i in range (b-1):
    for j in range (b-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("New Value Is  ",a)    
        
