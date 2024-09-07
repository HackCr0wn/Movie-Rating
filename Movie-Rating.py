import requests 
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

#using get() function to make request to IMDb website 
r = requests.get('https://www.imdb.com/chart/top/')
#html parse helps us to extract content from web pages
soup = BeautifulSoup(r.text, 'html.parser')

#extract data from web pages
#helps us to find required data from web pages
movies_table = soup.find('table', {'class': 'chart'})

if movies_table is not None:
    #traversing through each and every row present to find required data   tr --> table row
    rows = movies_table.find_all('tr')

    #storing titles and rating of movies into empty list
    movie_titles = []
    movie_ratings = []

    #storing extracted data into empty lists
    # Iterate over each row in the table
    for row in rows:
        # Find the title and rating for each movie
        movie_titles = row.find('td', {'class': 'titleColumn'})
        movie_ratings = row.find('td', {'class': 'imdbRating'})
        
        # Check if both title and rating are not None
        if movie_titles is not None and movie_ratings is not None:
            # Append the title and rating to the respective lists
            movie_titles.append(movie_titles.a.text)
            movie_ratings.append(float(movie_ratings.text.strip()))

    # creatinf dataframes for titles and ratings for movies
    df = pd.DataFrame({'Titles': movie_titles, 'Ratings': movie_ratings})

    #extracting release year of movies and calulating decade
    df['Decade'] = df['Titles'].str.extract(r'$(\d{4})$').astype(int) // 10*10


    # Calculate the average rating for each decade
    average_ratings = df.groupby('Decade')['Rating'].mean()

    # Find the decade with the highest average rating
    highest_decade = average_ratings.idxmax()

    # Plot the chart
    plt.bar(average_ratings.index, average_ratings.values)
    plt.xlabel('Decade')
    plt.ylabel('Average Rating')
    plt.title('Average Ratings by Decade')
    plt.xticks(rotation=45)
    plt.axvline(highest_decade, color='red', linestyle='--', label='Highest Decade')
    plt.legend()
    plt.show()