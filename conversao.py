#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install forex_python


# In[3]:


from forex_python.converter import CurrencyRates


# In[7]:


c = CurrencyRates()
quantidade = int(input("Entre com algum valor:"))
from_moeda = input("Qual moeda quer converter:").upper()
to_conversao = input("Moeda convertido:").upper()

print(from_moeda, "para", to_conversao, quantidade)
resultado = c.convert(from_moeda, to_conversao, quantidade)
print(resultado)


# In[ ]:




