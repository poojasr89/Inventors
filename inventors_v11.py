#Which field is California and Massachusetts encouraging its people in
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('table_2b.csv')

california_data = data[(data.state == 'California')].groupby('year')

california_grantees = california_data[['grantee','grantee_cat_1','grantee_cat_2','grantee_cat_3','grantee_cat_4','grantee_cat_5','grantee_cat_6','grantee_cat_7']].sum()

Massachusetts_data = data[(data.state == 'Massachusetts')].groupby('year')

Massachusetts_grantees = Massachusetts_data[['grantee','grantee_cat_1','grantee_cat_2','grantee_cat_3','grantee_cat_4','grantee_cat_5','grantee_cat_6','grantee_cat_7']].sum()

Patent_categories = ['Chemical', 'Computers', 'Medical', 'Electronic', 'Mechanical', 'Others', 'Industry'] 
# https://www.nber.org/patents/subcategories.txt

fig, axes = plt.subplots(2,4, figsize=(20,20));

handle = california_grantees['grantee'].plot(ax = axes[0,0], color='blue'); axes[0,0].set_title('Total Patent Grantees'); 
Massachusetts_grantees['grantee'].plot(ax = axes[0,0], color='orange'); axes[0,0].set_xlabel('');axes[0,0].set_ylabel('Percentage of population');

california_grantees['grantee_cat_1'].plot(ax = axes[0,1], color='blue'); axes[0,1].set_title('Chemical'); 
Massachusetts_grantees['grantee_cat_1'].plot(ax = axes[0,1], color='orange'); axes[0,1].set_xlabel('');

california_grantees['grantee_cat_2'].plot(ax = axes[0,2], color='blue'); axes[0,2].set_title('Computers'); 
Massachusetts_grantees['grantee_cat_2'].plot(ax = axes[0,2], color='orange'); axes[0,2].set_xlabel('');

california_grantees['grantee_cat_3'].plot(ax = axes[0,3], color='blue'); axes[0,3].set_title('Drugs/Medical'); 
Massachusetts_grantees['grantee_cat_3'].plot(ax = axes[0,3], color='orange'); axes[0,3].set_xlabel('');

california_grantees['grantee_cat_4'].plot(ax = axes[1,0], color='blue'); axes[1,0].set_title('Electronics'); 
Massachusetts_grantees['grantee_cat_4'].plot(ax = axes[1,0], color='orange');axes[1,0].set_ylabel('Percentage of population');

california_grantees['grantee_cat_5'].plot(ax = axes[1,1], color='blue'); axes[1,1].set_title('Mechanical'); 
Massachusetts_grantees['grantee_cat_5'].plot(ax = axes[1,1], color='orange');

california_grantees['grantee_cat_6'].plot(ax = axes[1,2], color='blue'); axes[1,2].set_title('Other'); 
Massachusetts_grantees['grantee_cat_6'].plot(ax = axes[1,2], color='orange');

california_grantees['grantee_cat_7'].plot(ax = axes[1,3], color='blue'); axes[1,3].set_title('Design/Plant'); 
Massachusetts_grantees['grantee_cat_7'].plot(ax = axes[1,3], color='orange');

handle.legend(['Blue CA', 'Orange MA'])

plt.show()





