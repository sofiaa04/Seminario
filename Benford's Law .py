#!/usr/bin/env python
# coding: utf-8

# In[1]:


from benfordslaw import benfordslaw
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
import sys
import math
from collections import defaultdict


# In[2]:


import pandas as pd
data = pd.read_csv (r'Desktop\SEMINARIO\PROYECTO\HON.csv',sep=';')
data['# CONTAGIOS'].values.tolist()
X=data['# CONTAGIOS'].values


# In[3]:


#Probabilidad del Primer digito segun la Ley de Benford
def prob_digit(d):
    d = int(d)
    prob_d = np.log10(1 + 1/d)
    return prob_d
digits = np.arange(1,10)
digit_probs = np.zeros(len(digits))
for digit in digits:
    digit_probs[digit - 1] = prob_digit(digit)


# In[4]:


# Lista para guardar los primeros digitos
first_digit_set = []
#metodo
def get_leading_digit(number):
    while (int(number) >= 10):
         number = int(number) // 10
    return int(number)


# In[5]:


#Funcion para contar los primeros digitos
def leading_digit_count(numbers):
    digit_dict = { 'digit': np.arange(1,10),
                   'prob' : np.zeros(9),
                   'count': np.zeros(9) }
    for num in numbers:
        first_digit = int(str(num)[:1])
        ind = np.where(digit_dict['digit'] == first_digit)
        digit_dict['count'][ind] =  digit_dict['count'][ind] +1 
    
    digit_dict['prob'] = digit_dict['count'] / len(numbers)
    
    return digit_dict


# In[6]:


#Lista de Primeros digitos en datos de HON
for num in data['# CONTAGIOS']:
   a=get_leading_digit(num)
   first_digit_set.append(a)
#conteo
d=leading_digit_count(first_digit_set)


# In[7]:


print(first_digit_set)
print(X)
print(d)


# In[8]:


#Graficar frecuencias de la Ley de Benford y Datos HON
plt.rc('font', size=12)
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(digits, digit_probs,width = 0.3)
ax.bar(digits+0.25, d['prob'],color='m',width = 0.3)
plt.xticks(digits)
plt.xlabel('Digits')
plt.ylabel('Probability')
plt.title("Benford's Law: Probability of Leading Digits")
ax.legend(labels=['BL', 'HON'])
plt.show()


# In[9]:


#Realizar prueba chi cuadrado
bl = benfordslaw(alpha=0.01)
results = bl.fit(X)


# In[ ]:




