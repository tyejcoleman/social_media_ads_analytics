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

income_bins = [0, 30000, 69999, 99999, float('inf')]
income_labels = ['Less than $30,000', '$30,000- $69,999', '$70,000- $99,999', '$100,000+']

data['IncomeBracket'] = pd.cut(data['EstimatedSalary'], bins=income_bins, labels=income_labels, right=False)

income_purchase_rate = data.groupby(['IncomeBracket', 'Gender']).agg(
    Purchase_Count=('Purchased', 'sum'),
    Total_Count=('Purchased', 'count')
)
income_purchase_rate['Purchase_Rate'] = (income_purchase_rate['Purchase_Count'] / income_purchase_rate['Total_Count']) * 100  # in percentage

income_purchase_rate = income_purchase_rate[income_purchase_rate['Purchase_Count'] > 0]

income_purchase_rate = income_purchase_rate.reset_index()

output_folder_path = '../output/'
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
output_dir = os.path.join(project_dir, 'output')

if not os.path.exists(output_dir):
    os.makedirs(output_dir)


output_file_path = os.path.join(output_dir, 'income_analysis.csv')
income_purchase_rate.to_csv(output_file_path, index=False)


