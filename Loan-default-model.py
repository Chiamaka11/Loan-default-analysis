#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import pyodbc


# In[3]:


conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=LAPTOP-VD12GVOR\SQLEXPRESS;'
    'DATABASE=LoanDB;'
    'Trusted_Connection=yes;'
)


# In[4]:


query = """
SELECT 
    [Age],
    [Income],
    [LoanAmount],
    [CreditScore],
    [MonthsEmployed],
    [NumCreditLines],
    [InterestRate],
    [LoanTerm],
    [DTIRatio],
    [Education],
    [EmploymentType],
    [MaritalStatus],
    [HasMortgage],
    [HasDependents],
    [LoanPurpose],
    [HasCoSigner],
    [Default],
    -- Calculated columns
    (LoanAmount / LoanTerm) AS Installment_per_Month,
    ROUND((MonthsEmployed / 12.0), 2) AS YearsEmployed,
    ROUND(((LoanAmount / LoanTerm) / Income), 2) AS Installment_to_IncomeRatio,
    ROUND(((MonthsEmployed / 12.0) / Age), 2) AS EmployabilityStability
FROM Loan_default
"""
df = pd.read_sql(query, conn)


# In[5]:


print(df)


# In[6]:


#data cleaning and preprocessing
#Remove duplicates 
df = df.drop_duplicates()

#Handle missing values
df = df.dropna()


# In[7]:


print(df)


# In[8]:


print(df['Default'].unique())



# In[9]:


#converting values
#Marital Status: Single = 1, Married= 2, Divorced = 3
df['MaritalStatus'] = df['MaritalStatus'].map({'Single': 1, 'Married': 2, 'Divorced': 3})

df['Default'] = df['Default'].map({True: 1, False: 0})
df['HasCoSigner'] = df['HasCoSigner'].map({True: 1, False: 0})
df['HasDependents'] = df['HasDependents'].map({True: 1, False: 0})
df['HasMortgage'] = df['HasMortgage'].map({True: 1, False: 0})


# In[10]:


print(df.head(10))


# #MODEL 

# In[13]:


print(df.columns)


# In[14]:


target_variable =  ['Default']

features = ['Age', 'Income', 'LoanAmount', 'CreditScore', 'MonthsEmployed',
       'NumCreditLines', 'InterestRate', 'LoanTerm', 'DTIRatio', 'Education',
       'EmploymentType', 'MaritalStatus', 'HasMortgage', 'HasDependents',
       'LoanPurpose', 'HasCoSigner', 'Default', 'Installment_per_Month',
       'YearsEmployed', 'Installment_to_IncomeRatio',
       'EmployabilityStability']


# In[16]:


#Splitting the model into train and testing
from sklearn.model_selection import train_test_split

X = df[features]
y = df[target_variable]

# Drop rows with NaNs in either features or target
X = X.dropna()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[ ]:




