import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
#cleaning the data

df = df.dropna(subset = ['type' ,'duration' , 'country' , 'rating' , 'release_year'])

#Bar graph showing NUMBER OF MOVIES VS TV SHOWS
type_counts = df['type'].value_counts()
plt.figure(figsize = (6,4))
plt.bar(type_counts.index , type_counts.values , color = ['orange' , 'skyblue'])
plt.title("MOVIES VS TV SHOWS")
plt.xlabel('TYPE')
plt.ylabel('COUNT')
plt.tight_layout()
plt.savefig("movies_vs_tv_shows.jpg")
plt.show()

#PIE CHART SHOWING % RATING
df = df.dropna(subset = ['type' ,'duration' , 'country' , 'rating' , 'release_year'])
rating_counts = df['rating'].value_counts()
plt.figure(figsize =(6,4))
plt.pie(rating_counts , labels = rating_counts.index , autopct = '%1.1f%%' , startangle = 90)
plt.title(" Percentage of ratings ")
plt.tight_layout()
plt.savefig("PERCENT_RATING.png")
plt.show()

#GRAPH SHOWING TOP 10 COUNTRIES MAKING RELEASES:
df = df.dropna(subset = ['type' ,'duration' , 'country' , 'rating' , 'release_year'])
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize= (8,6))
plt.barh(country_counts.index , country_counts.values , color = 'teal')
plt.title("top 10 countries")
plt.xlabel("Number of shows")
plt.ylabel("country")
plt.savefig("top10_countries.jpg")
plt.show()

#RELEASE YEAR SCATTER : 
df = df.dropna(subset = ['type' ,'duration' , 'country' , 'rating' , 'release_year'])
release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize = (10,6))
plt.scatter(release_count.index , release_count.values , color = 'red')
plt.title("Release year vs no. of shows")
plt.xlabel("YEAR")
plt.ylabel("Number of shows")
plt.savefig("RELEASE YEAR SCATTER.jpg")
plt.show()

# PER YEAR RELEASE COMPARISON OF MOVIES AND TV SHOWS ON SAME PLOT:
content_by_year = df.groupby(['release_year' , 'type']).size().unstack().fillna(0)
fig , ax = plt.subplots(1,2,figsize = (12,5))
#subplot for movies
ax[0].plot(content_by_year.index , content_by_year['Movie'] , color = 'blue')
ax[0].set_title("Movie")
ax[0].set_xlabel('year')
ax[0].set_ylabel("no. of movies")

ax[0].plot(content_by_year.index , content_by_year['TV Show'] , color = 'orange')
ax[0].set_title("tv shows")
ax[0].set_xlabel('year')
ax[0].set_ylabel("no. of movies")

fig.suptitle('comparision of movies vs tv shows per year')
plt.tight_layout()
plt.savefig("movies_tv_comparision.png")
plt.show()

#HISTOGRAM SHOWING DURATION OF MOVIES :
df = df.dropna(subset = ['type' ,'duration' , 'country' , 'rating' , 'release_year'])
movie_df = df[df['type']=='Movie'].copy()
# I instructed the python to access the csv file and there further access type column and give only movies 
movie_df['duration_int'] = movie_df['duration'].str.replace('min', '', regex=False).astype(int)

# Now because duration column in movie is in string form ... so i am instructing python to replace min from the numbers and express it in the form of aa str(.astype())

plt.figure(figsize = (8,6))
plt.hist(movie_df['duration_int'] , bins = 30 , color = 'purple' , edgecolor ='black')
plt.title('Distribution of movie duration')
plt.xlabel("duration (minutes)")
plt.ylabel("number of movies")
plt.tight_layout()
plt.savefig("duration of movies in minutes.png")
plt.show()
