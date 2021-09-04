#!/usr/bin/env python
# coding: utf-8

# In[ ]:


p = float(input("Initial Investment: "))
r = float(input("Annual Interest Rate: "))
t = int(input("Length of Time in Years: "))
n = float(input("Compound Frequency: "))
tr_r = r/100
print(f'${p * (1 + (tr_r/n))**(n*t):,.2f}')

