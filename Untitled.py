#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import numpy as np


# In[9]:


x=np.linspace(0,10,100)
y=np.sin(x)


# In[10]:


fig,ax=plt.subplots()

ax.plot(x,y,label='sin(x)')


# In[12]:


ax.set_title('ART')
ax.set_xlabel('x')
ax.set_ylabel('y')


# In[13]:


ax.legend()


# In[21]:


plt.show()


# In[16]:





# In[ ]:




