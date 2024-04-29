#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


print("Tuhin Chakraborty")


# In[4]:


print("What's up")


# In[6]:


x=2
y=3
print(x*y)


# In[7]:


a=5
b=7
print(a+b)


# In[3]:


a=int(input("Enter the value:" ))
b=int(input("Enter the value:" ))
if(a<b):
    print(b," is bigger")
elif(a>b):
    print(a," is bigger")
else:
    print("Both the values are same")


# In[7]:


#nested if
a=int(input("Enter the value:" ))
b=int(input("Enter the value:" ))
if(a!=b):
    if(a<b):
        print(b," is bigger")
    else:
        print(a," is bigger")
else:
    print("Both the given values are same")


# In[1]:


i=0
while i<3:
    print("Hello")
    i+=1


# In[2]:


i=0
while i<4:
    i+=1
    print(i)
else:
    print("No break\n")


# In[4]:


i=0
while i<10:
    i+=1
    print(i)


# In[1]:


n=int(input("Enter any number: "))
count=0
while(n>0):
    count=count+1
    n=n//10
print("Count of digits: ",count)


# In[2]:


n=int(input("Enter the value of n: "))
for i in range(1,n+1):
    print(i,end=' ')


# In[2]:


n=int(input("Enter a number: "))
i=0
while i<n:
    i+=1
    print(i)


# In[5]:


#break & continue
for i in range(1,10):
    if(i==5):
        break
    print(i)


# In[6]:


#break & continue
for i in range(1,10):
    if(i==5):
        continue
    print(i)


# In[9]:


mylist=[1, "a", 69.69]
print(mylist)


# In[10]:


len(mylist)


# In[12]:


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
newlist = list1 + list2
print(newlist)


# In[13]:


list1*3


# In[14]:


list3 = []
print(list3)


# In[15]:


list4 = list()
print(list4)


# In[16]:


primes = [2, 3, 5, 7, 11, 13, 17]
primes[1]


# In[17]:


primes[3:]


# In[18]:


primes[:4]


# In[19]:


primes[2:4]


# In[20]:


primes[::-1]


# In[21]:


mylist[1] = "e"
print(mylist)


# In[22]:


mylist = ["a", "b"]
mylist.append("c")
print(mylist)


# In[23]:


mylist.extend(["d", "e", "f"])
print(mylist)


# In[24]:


mylist.insert(0, "z")
print(mylist)


# In[25]:


mylist.pop()
print(mylist)


# In[28]:


mylist.remove("z")
print(mylist)


# In[29]:


fib = [1, 1, 2, 3, 4, 5, 6,]
fib.count(1)


# In[32]:


fib.index(5)


# In[33]:


letters = ["a", "b", "c"]
letters.reverse()
print(letters)


# In[34]:


#numbers are sorted without affecting the original list
numbers = [2, 10, 45, 86, 5, 69]
print(sorted(numbers))


# In[35]:


#list gets updated
numbers.sort()
print(numbers)


# In[36]:


sorted(numbers, reverse=True)


# In[37]:


#max & min in a list
numbers = [2, 5, 42, 10, 69]
print(min(numbers), max(numbers))


# In[1]:


#a list of Squares
squares=[x**2 for x in range(10)]
print(squares)


# In[2]:


even_squares=[x**2 for x in range (10) if x%2==0]
print(even_squares)


# In[ ]:




