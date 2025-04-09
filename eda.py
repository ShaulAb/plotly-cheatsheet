import pandas as pd
import plotly.express as px
import os

# Create plots directory if it doesn't exist
os.makedirs('plots', exist_ok=True)

# Load the Titanic dataset
df = pd.read_csv('data/titanic.csv')

# Univariate Analysis
# Continuous Variables
fig = px.histogram(df, x='Age', title='Age Distribution')
fig.write_image('plots/age_distribution.png')
print('Age distribution plot saved as age_distribution.png')

fig = px.box(df, y='Fare', title='Fare Distribution')
fig.write_image('plots/fare_distribution.png')
print('Fare distribution plot saved as fare_distribution.png')

# Discrete Variables
fig = px.histogram(df, x='Pclass', title='Passenger Class Distribution')
fig.write_image('plots/pclass_distribution.png')
print('Passenger class distribution plot saved as pclass_distribution.png')

fig = px.pie(df, names='Sex', title='Gender Distribution')
fig.write_image('plots/gender_distribution.png')
print('Gender distribution plot saved as gender_distribution.png')

# Bivariate Analysis
# Continuous vs. Continuous
fig = px.scatter(df, x='Age', y='Fare', title='Age vs Fare')
fig.write_image('plots/age_vs_fare.png')
print('Age vs Fare plot saved as age_vs_fare.png')

# Continuous vs. Discrete
fig = px.box(df, x='Pclass', y='Age', title='Age by Passenger Class')
fig.write_image('plots/age_by_pclass.png')
print('Age by Passenger Class plot saved as age_by_pclass.png')

# Discrete vs. Discrete
fig = px.bar(df, x='Pclass', color='Survived', barmode='group', title='Survival by Passenger Class')
fig.write_image('plots/survival_by_pclass.png')
print('Survival by Passenger Class plot saved as survival_by_pclass.png')

# Multivariate Analysis
fig = px.scatter(df, x='Age', y='Fare', color='Survived', size='Pclass', title='Age vs Fare by Survival and Class')
fig.write_image('plots/age_fare_survival_class.png')
print('Age vs Fare by Survival and Class plot saved as age_fare_survival_class.png')