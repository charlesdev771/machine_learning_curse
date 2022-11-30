import pandas as pd
import numpy as nṕ
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def my_main():
    
    base_credit = pd.read_csv("credit_data.csv")
    print(base_credit)
    #print(base_credit.tail())
    #print(base_credit.describe())
    print(base_credit[base_credit['income'] >= 7378.833599])




my_main()
