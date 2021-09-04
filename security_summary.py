#!/usr/bin/env python
# coding: utf-8

# In[ ]:


stock_p = float(input("Stock Purchace Price: "))
stock_s = float(input("Stock Selling Price: "))
shares = int(input("Shares: "))
print(f'Purchace amount: ${shares*stock_p:.2f}')
print(f'Selling amount:  ${shares*stock_s:.2f}')
print(f'Comission cost:  ${(shares*stock_s)*.015:.2f}')
print(f'Profit/Loss:     ${(shares*stock_s) - (shares*stock_p) - ((shares*stock_s)*.015):.2f}')

