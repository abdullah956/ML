#!/usr/bin/env python
# coding: utf-8

# ## Text Classification Using Random Forest Classifier

# #### Importing the necessary libraries

# In[107]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
import re
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.naive_bayes import GaussianNB


# #### Loading the dataset

# In[78]:


df = pd.read_csv('Corona_NLP_train.csv', encoding = 'latin')


# In[79]:


df.head()


# In[80]:


df.columns


# ### Dropping Irrelevant Columns

# In[81]:


df.drop(['UserName', 'ScreenName', 'Location', 'TweetAt'], axis = 1, inplace = True)


# In[82]:


df.head()


# #### Encoding The 'Sentiment' Column Using Label Encoder

# In[83]:


labelEncoder = LabelEncoder()


# In[84]:


df['Sentiment'] = labelEncoder.fit_transform(df['Sentiment'])


# In[85]:


df['Sentiment'].unique()


# ### Preprocess The Text Data

# #### Converting Text To Lower Case

# In[86]:


df['OriginalTweet'] = df['OriginalTweet'].str.lower()


# In[87]:


df['OriginalTweet'].head()


# #### Removing URLs

# In[88]:


df['OriginalTweet'] = df['OriginalTweet'].str.replace(r'https?://\S+|www\.\S+', '', regex = True)


# The 'r' before a string denotes a raw string literal.  
# It is used to indicate that the string should be treated as a raw string, where escape characters are not interpreted

# #### Remove Non - Alphanumeric Characters From The Text 

# In[89]:


df['OriginalTweet'] = df['OriginalTweet'].str.replace("[^a-zA-Z0-9]", " ", regex = True)


# In[90]:


df['OriginalTweet'].head()


# #### Splitting The Text Into Tokens

# In[91]:


df['OriginalTweet'] = df['OriginalTweet'].str.split()


# In[92]:


df['OriginalTweet'].tail()


# #### Removing Stopwords

# In[93]:


wordsEng = stopwords.words('english')


# In[94]:


# df["OriginalTweet"] = [[item for item in tweet if item not in wordsEng] for tweet in df["OriginalTweet"]]

stop_words = set(stopwords.words('english'))

for i in range(len(df['OriginalTweet'])):
    new_tweet = []
    for word in df['OriginalTweet'][i]:
        if word not in stop_words:
            new_tweet.append(word)
    df['OriginalTweet'][i] = new_tweet


# In[95]:


df["OriginalTweet"]


# #### Join The Words Back Into A Sentence

# In[96]:


df['OriginalTweet'] = df['OriginalTweet'].str.join(" ")


# ### Split The Dataset Into Training And Testing Sets

# In[97]:


x = df['OriginalTweet']
y = df['Sentiment']


# In[98]:


xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.3)


# ### Apply TF-IDF Vectorization To The Text Data

# In[99]:


vectorizer = TfidfVectorizer()


# In[100]:


vectorizer.fit(xtrain)


# In[110]:


xtrain = vectorizer.transform(xtrain)
xtest = vectorizer.transform(xtest)


# ### Train The Random Forest Classifier

# In[111]:


rf = RandomForestClassifier()


# In[112]:


rf.fit(xtrain, ytrain)


# In[109]:


nb = GaussianNB()

nb.fit(xtrain, ytrain)


# ### Make Prediction On The Test Set

# In[113]:


pred = rf.predict(xtest)

print(pred)


# In[ ]:




