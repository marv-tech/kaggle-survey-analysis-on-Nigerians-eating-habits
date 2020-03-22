#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
df=pd.read_csv('../Adaaaa/Downloads/fast-food-habit/FastFood_Habits_Questionnaire.csv')
df
new_df = df[['Which is your gender?', 'How often do you eat from fast foods each month?', 
             'When it comes to ordering, which do you prefer the most?',
             'What about a fast food restaurant endears you to them? [Value for your money]',
             'What about a fast food restaurant endears you to them? [Price]',
             'What about a fast food restaurant endears you to them? [Excellent service]',
             'What about a fast food restaurant endears you to them? [Convenience]',
             'What about a fast food restaurant endears you to them? [Social media savviness]',
             'What about a fast food restaurant endears you to them? [The quality]']]
new_df.to_csv('project one on food choices.csv')


# In[ ]:





# In[ ]:




