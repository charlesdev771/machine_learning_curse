from pandas.core.internals import base
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.naive_bayes import GaussianNB
import pickle

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

#base_credit.isnull().sum()
#base_credit.loc[pd.isnull(base_credit['age'])]
#base_credit['age'].fillna(base_credit['age'].mean(), inplace = True)
#base_credit.loc[pd.isnull(base_credit['age'])]

#L20

x_credit = base_credit.iloc[:, 1:4].values
y_credit = base_credit.iloc[:, 4].values

#L21

#x_credit[:, 0].min()
#x_credit[:, 0].max()

scaler_credit = StandardScaler()

#x_credit = scaler_credit.fit_transform(x_credit)
#x_credit

#L22

#with open('credit.pkl', mode = 'wb') as f:
 # pickle.dump(x_credit)


#ALG naive bayes

risk = pd.read_csv("/content/risco_credito.csv")

x_risk = risk.iloc[:, 0:4].values
y_risk = risk.iloc[:, 4].values


label_encouder_hist = LabelEncoder()
label_encouder_divi = LabelEncoder()
label_encouder_garant = LabelEncoder()
label_encouder_rend = LabelEncoder()

x_risk[:, 0] = label_encouder_hist.fit_transform(x_risk[:, 0])
x_risk[:, 1] = label_encouder_divi.fit_transform(x_risk[:, 1])
x_risk[:, 2] = label_encouder_garant.fit_transform(x_risk[:, 2])
x_risk[:, 3] = label_encouder_rend.fit_transform(x_risk[:, 3])

x_risk

import pickle 
with open('Risk.pkl', 'wb') as f:
  pickle.dump([x_risk, y_risk], f)

naiv_risk_credit = GaussianNB()
naiv_risk_credit.fit(x_risk, y_risk)

prev = naiv_risk_credit.predict([[0,0,1,2], [2,0,0,0]])

prev

