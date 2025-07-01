import os
import pandas as pd
from google.cloud import bigquery

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/New folder/p2project-460510-57c8b35adc2f.json"

# Create BigQuery client
client = bigquery.Client()

# Load CSV data
df = pd.read_csv("C:/New folder/movie_genre_classification_final.csv")
df.drop_duplicates(inplace=True)

print(df.head(5))

# Adding ID for Director
df_directors = df[['Director']].drop_duplicates().reset_index(drop=True)
df_directors['director_id'] = df_directors.index + 1
df = df.merge(df_directors, on='Director', how='left')

table_id = "p2project-460510.peerisland.Directors"
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
client.load_table_from_dataframe(df_directors, table_id, job_config=job_config).result()

# Add ID for Language
df_language = df[['Language']].drop_duplicates().reset_index(drop=True)
df_language['language_id'] = df_language.index + 1
df = df.merge(df_language, on='Language', how='left')

table_id = "p2project-460510.peerisland.Languages"
df_language = df[['language_id', 'Language']].drop_duplicates().reset_index(drop=True)
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
client.load_table_from_dataframe(df_language, table_id, job_config=job_config).result()

# ----------------------------------------
# Add ID for Genre
df_genre = df[['Genre']].drop_duplicates().reset_index(drop=True)
df_genre['genre_id'] = df_genre.index + 1
df = df.merge(df_genre, on='Genre', how='left')

table_id = "p2project-460510.peerisland.Genres"
df_genre = df[['genre_id', 'Genre']].drop_duplicates().reset_index(drop=True)
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
client.load_table_from_dataframe(df_genre, table_id, job_config=job_config).result()

# ----------------------------------------
# Add ID for Lead Actor
df_lead_actor = df[['Lead_Actor']].drop_duplicates().reset_index(drop=True)
df_lead_actor['lead_actor_id'] = df_lead_actor.index + 1
df = df.merge(df_lead_actor, on='Lead_Actor', how='left')

table_id = "p2project-460510.peerisland.LeadActors"
df_lead_actor = df[['lead_actor_id', 'Lead_Actor']].drop_duplicates().reset_index(drop=True)
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
client.load_table_from_dataframe(df_lead_actor, table_id, job_config=job_config).result()

# ----------------------------------------
# Create final MovieData fact table
df_movie_data = df[[
    'Title', 'Year', 'Duration', 'Rating', 'Votes',
    'Budget_USD', 'BoxOffice_USD', 'Content_Rating',
    'Num_Awards', 'Critic_Reviews',
    'director_id', 'language_id', 'genre_id', 'lead_actor_id'
]]

table_id = "p2project-460510.peerisland.MovieData"
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
client.load_table_from_dataframe(df_movie_data, table_id, job_config=job_config).result()

# print(df.head(5))  # Optional preview
# print("END")

