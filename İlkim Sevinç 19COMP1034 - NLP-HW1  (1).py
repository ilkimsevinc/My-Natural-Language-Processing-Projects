#!/usr/bin/env python
# coding: utf-8

# 
# a) find all words which include successive non-numeric and non-alphabetic characters with the length of 3n (n >=1),
# while both sides of this substring (with a length of 3n) are surrounded by any number (greater thanor equal to 1)
# of alphabetic characters. 

# In[37]:


import re
text = ["bo&$#jok", ")))", "yyy$$$$$$F", "H******z", "I&)(oin", "&$#", "yyy$$F", "I6&)(oi5n", "H54O", "H^&^^%K", "g6&(y", "6%%%8", "^^^H"]
print(text)


for i in text:
    m = re.match(r"[a-zA-Z]+(\W\W\W)+[a-zA-Z]", i)
    if m:
        print(m.group())


# In[ ]:





# ##
# part b) all words (including only alphabetic or numeric characters) the length of which, is an even number.

# In[38]:


string1 = ["bebebebk", "Hualalalalbb", "hbe7bhh7ek", "*&^b.", "HHH.", "Aaaa."]
print(string1)

for i in string1:
    m = re.match(r"(?:\w{2})+$", i)
    if m:
        print(m.group())


# In[ ]:




