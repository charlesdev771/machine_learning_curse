from pandas.core.internals import base
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px

##L1
base_credit = pd.read_csv('/content/credit_data.csv')
#print(base_credit['age'])
#print(base_credit.tail())
#print(base_credit.describe())
#print(base_credit['age'] > 50)


##L2
#np.unique(base_credit['age'])
#sns.countplot(x = base_credit['default']);
#plt.hist(x = base_credit['age']);
#plt.hist(x = base_credit['income']);
#plt.hist(x = base_credit['loan']);
#graf = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'])
#graf.show()

#L3

#base_credit.loc[base_credit['age'] <= 0]
#base_credit3 = base_credit.drop(base_credit[base_credit['age'] < 0].index)
#base_credit3


#L4

base_credit.isnull().sum()
base_credit.loc[pd.isnull(base_credit['age'])]
base_credit['age'].fillna(base_credit['age'].mean(), inplace = True)
base_credit.loc[pd.isnull(base_credit['age'])]


