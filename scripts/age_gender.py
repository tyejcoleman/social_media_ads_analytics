import pandas as pd
import numpy as np
from scipy import stats
import os

data = pd.read_csv('./sources/Social_Network_Ads.csv')

# clean data
data.fillna(data.mean(numeric_only=True), inplace=True)
data.dropna(inplace=True)
data.fillna(value=0, inplace=True)
data.drop_duplicates(inplace=True)

# find outliers
numeric_cols = ['EstimatedSalary', 'Age']
for col in numeric_cols:
    data = data[(np.abs(stats.zscore(data[col])) < 3)]

# change gender to numerical value
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

age_bins = [18, 29, 49, 64, 100] 
age_labels = ['18-29', '30-49', '50-64', '65+']

data['AgeGroup'] = pd.cut(data['Age'], bins=age_bins, labels=age_labels, right=True)

# Group by AgeGroup, Gender and calculate purchase rate
purchase_rate = data.groupby(['AgeGroup', 'Gender']).agg(
    Purchase_Count=('Purchased', 'sum'),
    Total_Count=('Purchased', 'count')
)
purchase_rate['Purchase_Rate'] = (purchase_rate['Purchase_Count'] / purchase_rate['Total_Count']) * 100  # in percentage

purchase_rate = purchase_rate[purchase_rate['Purchase_Count'] > 0]

purchase_rate = purchase_rate.reset_index()

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
output_dir = os.path.join(project_dir, 'output')

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

age_gender_output_file = os.path.join(output_dir, 'age_gender_analysis.csv')
purchase_rate.to_csv(age_gender_output_file, index=False)


