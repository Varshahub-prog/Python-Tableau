# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:56:25 2024

@author: Varsha
"""
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

# summary of data
data.describe()
# summary of the columns
data.info()

# Counting no.of articles per source
# format of group by: df.groupby(['coulumn_to_group'])['column_to_count'].count())

data.groupby(['source_id'])['article_id'].count()

# no.of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# dropping a column
data = data.drop('engagement_comment_plugin_count', axis = 1)

# functions in python

def thisFunction():
    print('This is my first function!')
thisFunction()

# This is a function with variables

def aboutMe(name,surname,location):
    print('This is '+name+ ' My Surname is '+surname+' Iam from '+location)
    return name,surname,location
a = aboutMe('Varsha', 'Ala','USA')    

# using for loops in functions

def favfood(food):
    for x in food:
       print('top food is '+x)
fastfood = ['burgers','pizza','pie']
favfood(fastfood)

# Creating a keyword flag
Keyword = 'crash'

# lets create a for loop to isolate each title row
# length = len(data)
# Keyword_flag = []
# for x in range(0,length):
#     heading = data['title'][x]
#     if Keyword in heading:
#         flag =1
#     else:
#         flag =0
#     Keyword_flag.append(flag)
    
# creating a function
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:                                        
            if Keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
keywordflag = keywordflag("murder") 
    
# create a new column in data dataframe
data['keyword_flag'] = pd.Series(keywordflag) 


#SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# adding a for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length =len(data)
for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
              
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

# writing the data

data.to_excel('blogme_clean.xlsx',sheet_name = 'blogmedata',index = False)





