import pandas as pd
import matplotlib.pyplot as plt 

#Loading JSON data into dataframe
df = pd.read_json('movies.json')

df.rename(columns={'title': 'Title', 'year': 'Year', 'rating': 'Rating'}, inplace=True)

df['Decade'] = (df['Year'] // 10) * 10

#Calulating average ratings
average_ratings = df.groupby('Decade')['Rating'].mean()

#Plotting graph
plt.figure(figsize=(10, 5))
plt.plot(average_ratings.index, average_ratings.values, marker='o')
plt.xlabel('Decade')
plt.ylabel('Average Rating')
plt.title('Average Movie Rating by Decade')
plt.grid(True)
plt.show()