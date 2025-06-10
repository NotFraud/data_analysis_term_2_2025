import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# # Filter for female athletes only
# female_athletes = df[df['Sex'] == 'F']
# print(female_athletes.head())

# # Filter for athletes older than 35
# older_athletes = df[df['Age'] > 35]
# print(older_athletes[['Name', 'Age', 'Sport']].head())


# print(f'The lengths {len(female_athletes)}, {len(older_athletes)}')

# #which had most female athletes?
# sport_by_female_athletes = df[df('Sex')['Female']].groupby('Sport')
# # print(medals_by_team.sort_values(ascending=False).head())
# most_frequent_sport = df[df['Sex'] == 'F']['Sport'].value_counts().idxmax()

# print(most_frequent_sport)
median_age_by_year = df.groupby('Sex')['Weight'].median()
print(median_age_by_year)