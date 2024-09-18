# operator
# arithmethic operatore
a=10
b=5
c=a+b,a-b,a*b,a%b,a/b,a**b,a//b
print(c)

# comparsion operator
a=6
b=10
c=a==b,a!=b,a<b,a>b,a<=b,a>=b
print(c)

# assingment operator(+=,-=,*=,%=,/=,&=,//=,**=)
a=5
a&=3

print(a)

# logical operator(And,Or,Not)
x=int(input("Enter the value:"))
if (x>=50 and x<=100):
    print("yes")
else:
    print("no")

x=int(input())
if not (x>=1 and x<5):
    print("yes")
else:
    print("no")

# identity operator(is, isnot)

a=(1,2,3,4,5)
b=(1,2,3,4)

print(a is b)
print(a is not b)


x=4
if (x>5):
    print("x is greater than y"  )
else:
    print("x is lesser than y")

# membership operator
a="python is very easy language"

print("python "in a)

# bitwise operator
