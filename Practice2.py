# q1 Find the largest element in a list. 

lis1=[25,42,54,29,65]
greatest=0
for el in lis1:
    if el>greatest:
        greatest=el
print(greatest)

#  Check if a number is even or odd. 

num=int(input("Enter the number:"))
if(num%2==0):
    print(f"{num}is even")
else:
    print(f"{num} is odd")
 
# Reverse a string (without slicing).

str=input("enter the string:")
rev=""
for i in str:
    rev=i+rev
print(rev)

# Count vowels in a string. 

str=input("enter the string:")
count=0
for ch in str:
    if ch in "AEIOUaeiou":
        count+=1
print(count)

# Find the sum of digits of a number. 
num=int(input("Enter the number:"))
sum=0
while(num>0):
    dig=num%10
    sum+=dig
    num//=10
print(sum)

# Check if a string is a palindrome.

str=input("Enter the string:")
if str==str[::-1]:
    print("Palindrome")
else:
    print("not a palindorme")

# Print Fibonacci series up to N terms. 
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Enter number of terms: "))
fibonacci(n)

# Swap two variables without a third variable. 
a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
a,b=b,a
print(a,b)

# Count words in a sentence. 

str=input("enter the word:")
word=str.split()
count=len(word)
print(count)

# Find minimum and maximum in a list 
lis1=[10,20,30,35,45,25,95]
max=lis1[0]
min=lis1[0]
for i in lis1:
    if i<min:
        min=i
    if i>max:
        max=i
print(max)
print(min)

# Find the second largest number in a list. 
l = [10, 20, 4, 45, 99]
print(sorted(l)[-2])

# Remove duplicates from a list (without set). 

l = [1,2,2,3,4,4]
res = []
for i in l:
    if i not in res:
        res.append(i)
print(res)

# Count frequency of elements in a list. 
l = [1,2,2,3,3,3]
d = {}
for i in l:
    d[i] = d.get(i,0)+1
print(d)

#Q14:Merge two sorted lists.
a=[1,3,5]; b=[2,4,6]
print(sorted(a+b))


#Q15:Find the intersection of two lists.
l1=[1,2,3,4]
l2=[3,4,5,6]
intersection=[]
for i in l1:
    if i in l2:
        intersection.append(i)
print(intersection)


#Q16:Rotate a list by k positions.
l1=[1,2,3,4,5]
k=2
rotated=l1[k:]+l1[:k]
print(rotated)


#Q17:Check if two strings are anagrams.
s1="listen"
s2="silent"
if sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")


#Q18:Find the first non-repeating character.
s="aabbcdde"
for i in s:
    if s.count(i)==1:
        print(i); break


#Q19:Flatten a nested list.
nested=[1,2,[3,4],5]
flat=[]
for i in nested:
    if isinstance(i,list):
        flat.extend(i)
    else:
        flat.append(i)
print(flat)


#Q20:Find all pairs with a given sum.
l1=[1,2,3,4,5]
target=5
pairs=[]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]+l1[j]==target:
            pairs.append((l1[i],l1[j]))
print(pairs)


#Q21:Print a right triangle pattern.
n=5
for i in range(1,n+1):
    print("*"*i)


#Q22:Print a pyramid pattern.
n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
    
    
#Q23:Print all prime numbers in a range.
start=10
end=50
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=" ")


#Q24:Check if a number is Armstrong.
num=int(input("Enter a number: "))
org=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**org
    temp//=10
if num==sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
