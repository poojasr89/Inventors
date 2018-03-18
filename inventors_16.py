import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('table_2b.csv');

data_by_state = data.groupby('stateabbrv');

fig, axes = plt.subplots(2,1, figsize=(6,6))


handle_population = pd.concat([data_by_state['count_g_m'].sum(),data_by_state['count_g_f'].sum()], axis = 1).plot.bar(stacked=True, ax = axes[0]);

axes[0].set_xlabel(''); axes[0].set_ylabel('Population');

handle_population.legend(['Male','Female'])

handle_population.text(40,3e8,'US population')


handle_grantee = pd.concat([data_by_state['grantee_g_m'].sum(),data_by_state['grantee_g_f'].sum()], axis = 1).plot.bar(stacked=True, ax = axes[1]);

axes[1].set_xlabel('State'); axes[1].set_ylabel('Percentage');

handle_grantee.legend(['Male','Female'])

handle_grantee.text(30,2.5,'Patent Grantees as percentage of population')

plt.show()