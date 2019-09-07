# For Inserting Lists
print("Enter the value for lists  ")
a=[]
n=int(input("Enter the Amount for Elements   "))
for i in range(n):
    ele=int(input("Enter the Value of Elements  "))
    a.append(ele)
print(a)    
b=[]
n=int(input("Enter the Amount for Elements   "))
for i in range(n):
    ele1=int(input("Enter the Value of Elements  "))
    b.append(ele1)
print(b)

# For Choice

print("1. Mathematical Function  ")
print("2. Checking ")
print("3. Updating ")
print("4. Sorting ")

# For Input
c=int(input("Enter Your Choice   "))
if c==1 :
    print("1. Concatenate  ")
    print("2. Replication  ")
    print("3. Length  ")
    print("4. Counting  ")
    d=int(input("Enter The Choice  "))
    if d==1 :
        print("1. Append  ")
        print("1. Extend  ")
        print("1. Insert  ")
        e=int(input("Enter Your Choice  "))
        if e==1 :
            f=int(input("Enter The Number To Append  "))
            a.append(e)
            print(a)
            b.append(e)
            print(b)
        elif e==2 :
            g=int(input("Enter The Value To Extend  "))
            a.extend(g)
            print(a)
            b.extend(g)
            print(b)
        elif e==3 :
            h=int(input("Enter The Index Value  "))
            i=int(input("Enter The Value To Insert  "))
            a.insert(g,h)
            print(a)
            b.insert(g,h)
            print(b)
        else :
            print("Entered A Wrong Sub Choice  ")
elif c==2 :
    print("1. In  ")
    print("2. Index  ")
    j=int(input("Enter Your Choice  "))
    if j==1 :
        k=int(input("Enter The Value To Check  "))
        if k in a :
            print("True for List A  ")
        else :
            print("False for List A ")
        if k in b :
            print("True for List B")
        else :
            print("False for List B")
    if j==2 :
        l=int(input("Enter The Position  "))
        m=int(input("Enter The Value  "))
        a.index(l,m)
        print(a)
        b.index(l,m)
        print(b)
elif c==3 :
    print("1. Updating  ")
    print("2. Reversing  ")
    n=int(input("Enter Your Choice  "))
    if n==1 :
        o=int(input("Index Value  "))
        p=int(input("Enter New Value  "))
        a[o]=p
        print(a)
        b[o]=p
        print(b)
    if n==2 :
        a.reverse()
        print(a)
        b.reverse()
        print(b)
elif c==4 :
    a.sort()
    print(a)
    b.sort()
    print(b)
else :
    print("Entered Wromg Choice  ")
