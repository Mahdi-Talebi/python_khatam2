#!/usr/bin/env python
# coding: utf-8

# # 1. Classify each of the following as either a legal or illegal Python identifier:
# 1. fred
# 2. if
# 3. 2x
# 4. -4
# 5. sum_total
# 6. sumTotal
# 7. sum-total
# 8. sum total
# 9. sumtotal
# 10. While
# 11. x2
# 12. Private
# 13. public
# 14. $16
# 15. xTwo
# 16. _static
# 17. _4
# 18. `___`
# 19. 10%
# 20. a27834
# 21. wilma’s

# In[15]:


# leagal: 1, 5, 6, 9, 11, 12, 13, 15, 16, 17, 20 
#illegal: 2, 3, 4, 7, 8, 10, 14, 18, 19, 21


# # 2. What is wrong with the following statement that attempts to assign the value ten to variable x?
# > 10 = x

# In[16]:


# in python we cannot use digit at start of each variable. in this case we should move 10 & x same as below to assign value 10 to variable x:
x=10 
print (x)


# # 3. Is "i" a string literal or variable?

# In[17]:


type ("i")


# # 4. Indicate what each of the following Python statements would print:
# > x = 2
# 1. print("x") 
# 2. print(’x’)
# 3. print(x)
# 4. print("x + 1")
# 5. print(’x’ + 1)
# 6. print(x + 1)

# In[23]:


# 1. x
# 2. invalid character
# 3. 2
# 4. x+1
# 5. invalid character
# 6. 3


# # 5. Given the following assignments:
# i1 = 2
# i2 = 5
# i3 = -3
# d1 = 2.0
# d2 = 5.0
# d3 = -0.5;
# # Evaluate each of the following Python expressions.
# 1. i1 + i2
# 2. i1 / i2
# 3. i1 // i2
# 4. i2 / i1
# 5. i2 // i1
# 6. i1 * i3
# 7. d1 + d2
# 8. d1 / d2
# 9. d2 / d1
# 10. d3 * d1
# 11. d1 + i2
# 12. i1 / d2
# 13. d2 / i1
# 14. i2 / d1
# 15. i1/i2*d1
# 16. d1*i1/i2
# 17. d1/d2*i1
# 18. i1*d1/d2
# 19. i2/i1*d1
# 20. d1*i2/i1
# 21. d2/d1*i1
# 22. i1*d2/d1

# In[28]:


# 1. 7.0
# 2. 0.4
# 3. 0.0
# 4. 2.5
# 5. 2.0
# 6. -6.0
# 7. 7.0
# 8. 0.4
# 9. 2.5
# 10. -1.0
# 11. 7.0
# 12. 0.4
# 13. 2.5
# 14. 2.5
# 15. 0.8
# 16. 0.8
# 17. 0.8
# 18. 0.8
# 19. 5.0
# 20. 5.0
# 21. 5.0
# 22. 5.0


# # 6. Write the shortest way to express each of the following statements.
# 1. x = x + 1
# 2. x = x / 2
# 3. x = x - 1
# 4. x = x + y
# 5. x = x - (y + 7)
# 6. x = 2*x
# 7. number_of_closed_cases = number_of_closed_cases + 2*ncc

# In[61]:


# 1. x+=x
# 2. x/=x
# 3. x-=x
# 4. x+=y
# 5. x-=(y+7)
# 6. x*=2
# 7. number_of_closed_cases += 2*ncc


# # 7. Is the value -16 interpreted as True or False?

# In[30]:


x=-16
x<0


# # 8. Given the following definitions:
# x, y, z = 3, 5, 7
# evaluate the following Boolean expressions:
# 1. x == 3
# 2. x < y
# 3. x >= y
# 4. x <= y
# 5. x != y - 2
# 6. x < 10
# 7. x >= 0 and x < 10
# 8. x < 0 and x < 10
# 9. x >= 0 and x < 2
# 10. x < 0 or x < 10
# 11. x > 0 or x < 10
# 12. x < 0 or x > 10

# In[ ]:


# 1. True
# 2. True
# 3. False
# 4. True
# 5. False
# 6. True
# 7. True
# 8. False
# 9. False
# 10. True
# 11. True
# 12. False


# # 8. Write a Python program that requests an integer value from the user.
# * If the value is between 1 and 100 inclusive, print ”OK;” otherwise, do not print anything.

# In[64]:


x = int(input("please enter your weight"))

if 0<x<100:
    print ("OK")
else:
    print ()


# # 9. Write a Python program that requests an integer value from the user.
# * If the value is between 1 and 100 inclusive, print ”OK;” otherwise, print ”Out of range.”

# In[65]:


x = int(input("please enter your weight"))

if 0<x<100:
    print ("OK")
else:
    print ("Out of range")


# # 10. Write a Python program that:
# * requests five integer values from the user.
# * It then prints the maximum and minimum values entered.
# * If the user enters the values 3, 2, 5, 0, and 1, the program would indicate that 5 is the maximum and 0 is the minimum.
# * Your program should handle ties properly; for example, if the user enters 2, 4 2, 3 and 3, the program should report 2 as the minimum and 4 as maximum.

# In[68]:


list3 = []
counter = 0
while counter < 5:
    number = int(input("Please enter a number: "))
    counter += 1
    list3.append(number)

print(max(list3),'is the maximum and',min(list3),' is the minimum.') 


# In[ ]:




