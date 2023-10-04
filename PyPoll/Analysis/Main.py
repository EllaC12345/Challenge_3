#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


election_data = os.path.join('/Users/ellandalla/Desktop/Challenge_3/PyPoll/Resources/election_data.csv')


# In[3]:


#Read CSV File and transform into a listelection = []
election = []
with open (election_data, encoding = 'utf=8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #print(next(csvreader))
    for row in csvreader:
        election.append(row)
    print(election[:10])


# In[4]:


## Determine the total number of votes:
votes = []
for row in election[1:]:
    votes.append(row[0])

Total_votes = (len(votes))
print(Total_votes)


# In[5]:


## List of Candidates who received votes 
candidates = []
for row in election[1:]:
    if row[0] is not None:
        candidates.append(row[2])
print (candidates[-11:])

    


# In[6]:


## list of unique candidates
unique_candidates = list(set(candidates))
print (unique_candidates)


# In[7]:


## The percentage of votes each candidates won - Charles Casper Stockham
# Total votes obatined by Charles Casper Stockham
CCS_Vote = 0
for candidate in candidates:
    if candidate == 'Charles Casper Stockham':
        CCS_Vote += 1
print (CCS_Vote)

# Percentage votes 
CCS_percentage_vote = ("{:.2%}".format(CCS_Vote/Total_votes))
print(f"Charles Casper Stockham:{CCS_percentage_vote} or ({CCS_Vote}) votes")



# In[8]:


## The percentage of votes each candidates won - Raymon Anthony Doane
# Total votes obatined by Raymon Anthony Doane
RAD_Vote = 0
for candidate in candidates:
    if candidate == 'Raymon Anthony Doane':
        RAD_Vote += 1
print (RAD_Vote)
# Percentage votes 
RAD_percentage_vote = ("{:.2%}".format(RAD_Vote/Total_votes))
print(f"Raymon Anthony Doane:{RAD_percentage_vote} or ({RAD_Vote}) votes")


# In[9]:


## The percentage of votes each candidates won - Diana DeGette
# Total votes obatined by Diana DeGette
DG_Vote = 0
for candidate in candidates:
    if candidate == 'Diana DeGette':
        DG_Vote += 1
print (DG_Vote)
# Percentage votes 
DG_percentage_vote = ("{:.2%}".format(DG_Vote/Total_votes))
print(f"Diana DeGette:{DG_percentage_vote} or {DG_Vote} votes")


# In[10]:


## Create a function to find the candidate with the maximum number of votes then return the name of that cnadidate
def winner():
    CCS_Vote = 0
    RAD_Vote = 0
    DG_Vote = 0
    candidates_votes = []
    for candidate in candidates:
        if candidate == 'Charles Casper Stockham':
            CCS_Vote += 1
            candidates_votes.append(CCS_Vote)
        elif candidate == 'Raymon Anthony Doane':
            RAD_Vote += 1
            candidates_votes.append(RAD_Vote)
        elif candidate == 'Diana DeGette':
            DG_Vote += 1
            candidates_votes.append(DG_Vote)
# find the maximum votes
    max_votes = max(candidates_votes)
    for candidate, vote in zip(candidates, candidates_votes):
        if vote == max_votes:
            return (candidate)
candidate_winner = winner()
print("winner:", candidate_winner)


# In[13]:


results = ('/Users/ellandalla/Desktop/Challenge_3/PyPoll/Analysis/Main.py')
# Saving the results into a jupiter notebook
file_path = "main.txt"

with open(file_path, 'w') as file:
    file.write(results)


# In[ ]:




