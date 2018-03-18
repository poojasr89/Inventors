import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('table_2b.csv')



data_ca = data[(data.state == 'California') & (data.age < 30)]

data_ca_year = data_ca.groupby('year')

data_ma = data[(data.state == 'Massachusetts')& (data.age < 30)]

data_ma_year = data_ma.groupby('year')


fig, axes = plt.subplots(2,1)

handle_populus = pd.concat([ data_ca_year['count_g_f'].sum(), data_ma_year['count_g_f'].sum()],axis=1).plot.bar(stacked = True, ax = axes[0])
handle_populus.legend(['California', 'Massachusetts'])
handle_populus.set_ylabel('Population')
handle_populus.set_title('Comparison of population v/s patent grantees in MA and CA - Women 30 years and younger')

handle_grantees = pd.concat([ data_ca_year['grantee_g_f'].sum(), data_ma_year['grantee_g_f'].sum()],axis=1).plot.bar(stacked = True, ax = axes[1])
handle_grantees.legend([])
handle_grantees.set_ylabel('Patent Grantees (% of populs)')

plt.show()