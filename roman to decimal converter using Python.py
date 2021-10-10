#!/usr/bin/env python
# coding: utf-8

# In[1]:


roman_dict ={'I': 1, 'V': 5,
             'X': 10, 'L': 50,
             'C': 100, 'D': 500,
             'M': 1000}


# In[2]:


def decimal(roman):
    """
    roman: a string or roman numerals.
    Returns the equivalent in decimal numbers (int).
    """
    global roman_dict
    # Analyze string backwards
    roman_back = list(reversed(list(roman)))  
    value = 0
    # To keep track of order
    right_val = roman_dict[roman_back[0]]  
    for numeral in roman_back:
        left_val = roman_dict[numeral]
        # Check for subtraction
        if left_val < right_val:
           value -= left_val
        else:
            value += left_val
        right_val = left_val
    return value


# In[3]:


print(decimal("IX"))


# In[ ]:




