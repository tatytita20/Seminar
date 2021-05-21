#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import json
import matplotlib.pyplot as plt
import numpy as np
Datos = []
for x in range(1000): 
    numbers = random.randint(0,100)
    Datos.append(numbers)
    plt.barh(x,numbers)
    plt.title("Bar plot")   
    plt.xlabel("Range")
    plt.ylabel("Random")
    
    data = { 
        'aleatorios' : Datos
    }
    with open('data.json', 'w') as outfile:
        json.dump(data,outfile)


# In[ ]:




