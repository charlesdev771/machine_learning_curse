import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
#from sklearn.preprocessing import StandardScaler, LabelEncoder


def my_main():

  #base_credit = pd.read_csv("credit_data.csv")
  base_census = pd.read_csv("/content/census.csv")
  # print(base_credit)
  # print(base_credit.tail())
  # print(base_credit.describe())

  #print(base_credit[base_credit['income'] >= 7378.833599])
  # print(np.unique(base_credit['income']))

  #print(sns.countplot(x = base_credit['default']));
  #plt.hist(x = base_credit['income'])
  #plt.hist(x = base_credit['loan'])

  #grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color='default')
  # grafico.show()

  #print(base_credit[base_credit['age'] < 0])
  #base_credit2 = base_credit.drop('age', axis = 1)
  # print(base_credit2)
  #base_credit3 = base_credit.drop(base_credit[base_credit['age'] < 0].index)
  # print(base_credit3)
  # print(base_credit['age'].mean())

  # print(base_credit.isnull().sum())
  #base_credit['age'].fillna(base_credit['age'].mean(), inplace = True)
  # print(base_credit.loc[pd.isnull(base_credit['age'])])

  # print(base_census)

  #np.unique(base_census['income'], return_counts=True)
  #sns.countplot(x = base_census['income']);
  #grafico = px.treemap(base_census, path=['workclass', 'age'])
  # grafico.show()

  x_census = base_census.iloc[:, 14].values
  # print(x_census)

  label = LabelEncoder()
  teste = label.fit_transform(x_census)


my_main()
