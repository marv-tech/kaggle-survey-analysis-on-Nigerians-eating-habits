#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd
df=pd.read_csv('../Adaaaa/Downloads/fast-food-habit/FastFood_Habits_Questionnaire.csv')
df
new_df = df[['Which is your gender?','What age group do you fall under?', 
             'When it comes to ordering, which do you prefer the most?',
             'What about a fast food restaurant endears you to them? [Value for your money]',
             'What about a fast food restaurant endears you to them? [Price]',
             'What about a fast food restaurant endears you to them? [Excellent service]',
             'What about a fast food restaurant endears you to them? [Convenience]',
             'What about a fast food restaurant endears you to them? [Social media savviness]',
             'What about a fast food restaurant endears you to them? [The quality]']]
df2 = new_df.to_csv('project one on food choices.csv')
pd.read_csv('../Adaaaa/project one on food choices.csv')


# In[15]:


#this answers the question of how many people choose an eatry based on convenience
import pandas as pd
import matplotlib.pyplot as plt 
df1=pd.read_csv('../Adaaaa/project one on food choices.csv')
df2=df1[['What about a fast food restaurant endears you to them? [Convenience]','Which is your gender?']]
df3=df2.replace(to_replace =["Strongly Disagree","Disagree","Indifferent", "Agree", "Strongly Agree"], value =[1,2,3,4,5])
data_set = df3.groupby('What about a fast food restaurant endears you to them? [Convenience]')['Which is your gender?'].count().plot()
data_set.set(title = 'the graph of convenience preference')
plt.show()


# In[5]:


# this answers the question of how many people choose an eatry bases on price
import pandas as pd
import matplotlib.pyplot as plt
df1= pd.read_csv('../Adaaaa/project one on food choices.csv')
df2=df1[['Which is your gender?','What about a fast food restaurant endears you to them? [Price]']]
df2
df3=df2.replace(to_replace =["Strongly Disagree","Disagree","Indifferent", "Agree", "Strongly Agree"], value =[1,2,3,4,5])
df4 = df3.groupby('What about a fast food restaurant endears you to them? [Price]')['Which is your gender?'].count().plot()
df4.set(title='the graph of price preference')
plt.show()


# In[ ]:





# In[12]:


#this shows how many people choose an eatery based on quality
import pandas as pd
import matplotlib.pyplot as plt
df1=pd.read_csv('../Adaaaa/project one on food choices.csv')
df2 =df1 [['What about a fast food restaurant endears you to them? [The quality]','Which is your gender?']]
#this gives values to choices made,ranging from 1 to 5
df3 = df2.replace(to_replace =["Strongly Disagree","Disagree","Indifferent", "Agree", "Strongly Agree"], value =[1,2,3,4,5])
#the groupby clause
data_set=df3.groupby('What about a fast food restaurant endears you to them? [The quality]')['Which is your gender?'].count().plot()
data_set
data_set.set(title='the graph of quality preference')
plt.show()


# In[ ]:





# In[ ]:




