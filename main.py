import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

nobel = pd.read_csv('datasets/nobel.csv')

# Taking a look at the first several winners
print(nobel.head(n=6))

# Display the number of (possibly shared) Nobel Prizes handed
# out between 1901 and 2016
print(len(nobel))

# Display the number of prizes won by male and female recipients.
print(nobel['sex'].value_counts())

# Display the number of prizes won by the top 10 nationalities.
print(nobel['birth_country'].value_counts().head(10))

# Calculating the proportion of USA born winners per decade
nobel['usa_born_winner'] = nobel['birth_country'] == "United States of America"
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype('int64')
prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()

# Display the proportions of USA born winners per decade
print(prop_usa_winners)

# Setting the plotting theme
sns.set()

# and setting the size of all plots.
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners
ax = sns.lineplot(x='decade', y='usa_born_winner', data=prop_usa_winners)

# Adding %-formatting to the y-axis
ax.yaxis.set_major_formatter(PercentFormatter(1.0))

plt.show()

# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel['sex'] == 'Female'
prop_female_winners = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()

# Plotting female winners with % winners on the y-axis
ax = sns.lineplot(x='decade', y='female_winner', hue='category', data=prop_female_winners)
ax.yaxis.set_major_formatter(PercentFormatter(1.0))

plt.show()

# Picking out the first woman to win a Nobel Prize
print(nobel[nobel.sex == 'Female'].nsmallest(1, 'year'))

# Selecting the laureates that have received 2 or more prizes.
print(nobel.groupby('full_name').filter(lambda group: len(group) >= 2))

# Converting birth_date from String to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])

# Calculating the age of Nobel Prize winners
nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year

sns.lineplot(x='year', y='age', data=nobel)
plt.show()

# Plotting the age of Nobel Prize winners
sns.lmplot(x='year', y='age', data=nobel, lowess=True, aspect=2, line_kws={'color' : 'black'})
plt.show()

# Same plot as above, but separate plots for each type of Nobel Prize
sns.lmplot(x='year', y='age', data=nobel, row='category', lowess=True, aspect=2, line_kws={'color' : 'black'})
plt.show()

# The oldest winner of a Nobel Prize as of 2016
print(nobel.nlargest(1, 'age'))

# The youngest winner of a Nobel Prize as of 2016
print(nobel.nsmallest(1, 'age'))

# The name of the youngest winner of a Nobel Prize as of 2016
youngest_winner = 'Malala Yousafzai'
print(youngest_winner)