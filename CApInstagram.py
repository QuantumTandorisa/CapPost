import requests
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import spacy
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import seaborn as sns

nltk.download('punkt')

def get_recent_posts(user_id, access_token):
    url = f"https://graph.instagram.com/{user_id}/media?fields=id,caption,like_count,comments,mentions,location,media_type,timestamp&access_token={access_token}"
    
    try:
        response = requests.get(url)
        posts = response.json()
        return posts
    except requests.exceptions.RequestException as e:
        print("Error getting posts:", e)

# Sentiment Analyzer configuration / Configuración del analizador de opiniones
sia = SentimentIntensityAnalyzer()

# Load spaCy language processing model / Cargue el modelo de procesamiento de lenguaje spaCy
nlp = spacy.load('en_core_web_sm')

# Example usage / Ejemplo de uso
user_id = "YOUR_USER_ID"  # Replace with your User ID / Reemplace con su ID de usuario
access_token = "YOUR_ACCESS_TOKEN"  # Replace with your Access Token / Reemplace con su token de acceso

posts = get_recent_posts(user_id, access_token)
captions = []
likes = []
hashtags = []
interactions = []
locations = []
weekdays = []
hours = []
content_types = []
new_followers = []
lost_followers = []
total_followers = []
posting_frequency = []
user_mentions = []

for post in posts['data']:
    caption = post['caption'] if 'caption' in post else ''
    captions.append(caption)
    likes.append(post['like_count'])
    content_types.append(post['media_type'])
    
    # Extract hashtags from captions / Extraer hashtags de subtítulos
    words = caption.split()
    hashtags.extend([word[1:] for word in words if word.startswith("#")])
    
    # Analyze interactions with other accounts / Analizar interacciones con otras cuentas
    if 'comments' in post:
        comments = post['comments']['data']
        for comment in comments:
            interactions.append(comment['from']['username'])
    if 'mentions' in post:
        mentions = post['mentions']['data']
        for mention in mentions:
            interactions.append(mention['username'])
            user_mentions.append(mention['username'])
    
    # Analyze interactions by location / Analice las interacciones por ubicación
    if 'location' in post:
        locations.append(post['location']['name'])
    
    # Analyze activity by day and hour / Analizar la actividad por día y hora
    timestamp = pd.to_datetime(post['timestamp'])
    weekdays.append(timestamp.day_name())
    hours.append(timestamp.hour)
    
    # Analyze posting frequency / Analizar la frecuencia de publicación
    posting_frequency.append(timestamp.date())

# Tokenization and lemmatization of captions / Tokenización y lematización de subtítulos
tokens_lemmas = []
for caption in captions:
    tokens = nltk.word_tokenize(caption)
    lemmas = [token.lower() for token in tokens if token.isalpha()]
    tokens_lemmas.append(lemmas)

# Extract entities from captions / Extraer entidades de subtítulos
entities = []
for caption in captions:
    doc = nlp(caption)
    entities.append([ent.text for ent in doc.ents])

# Advanced sentiment analysis / Análisis de sentimiento avanzado
sentiments = []
for caption in captions:
    # Perform sentiment analysis using NLTK's SentimentIntensityAnalyzer / Realice un análisis de sentimiento utilizando SentimentIntensityAnalyzer de NLTK
    score = sia.polarity_scores(caption)
    sentiments.append(score['compound'])

# Analyze popularity of hashtags / Analizar la popularidad de los hashtags
popular_hashtags = nltk.FreqDist(hashtags).most_common(10)

# Analyze content diversity / Analizar la diversidad de contenido
content_types_count = nltk.FreqDist(content_types)

# Analyze interaction rate / Analizar la tasa de interacción
interaction_rate = sum(likes) / len(posts)

# Analyze interaction quality / Analizar la calidad de la interacción
interaction_quality = len(set(interactions)) / len(interactions)

# Analyze follower preferences / Analizar las preferencias de los seguidores

# Analyze activity by day and hour / Analizar la actividad por día y hora
df_activity = pd.DataFrame({'Weekday': weekdays, 'Hour': hours})

# Analyze follower evolution / Analizar la evolución de los seguidores
df_followers = pd.DataFrame({'NewFollowers': new_followers, 'LostFollowers': lost_followers, 'TotalFollowers': total_followers})

# Analyze hashtag interactions / Analizar las interacciones de los hashtags
hashtag_interactions = {}

for i, caption in enumerate(captions):
    # Extract hashtags from captions / Extraer hashtags de subtítulos
    words = caption.split()
    post_hashtags = [word[1:] for word in words if word.startswith("#")]

    # Analyze interactions with the hashtags / Analizar las interacciones con los hashtags
    for hashtag in post_hashtags:
        if hashtag not in hashtag_interactions:
            hashtag_interactions[hashtag] = []
        hashtag_interactions[hashtag].extend(interactions)

# Sort hashtags by the number of interactions / Ordenar hashtags por el número de interacciones
sorted_hashtag_interactions = {k: len(v) for k, v in hashtag_interactions.items()}
sorted_hashtag_interactions = {k: v for k, v in sorted(sorted_hashtag_interactions.items(), key=lambda item: item[1], reverse=True)}

# Print the results / Imprime los resultados
for i, caption in enumerate(captions):
    print(f"Caption: {caption}")
    print(f"Likes: {likes[i]}")
    print(f"Sentiment: {sentiments[i]}")
    print(f"Lemmas: {tokens_lemmas[i]}")
    print(f"Entities: {entities[i]}")
    print("-------------------")

print("Popular Hashtags:")
for hashtag, count in popular_hashtags:
    print(f"{hashtag}: {count}")

print("Interactions with other accounts:")
print(interactions)

print("Locations:")
print(locations)

print("Activity by weekday and hour:")
print(df_activity)

print("Follower Evolution:")
print(df_followers)

# Plot activity by weekday / Trazar actividad por día de la semana
plt.figure(figsize=(8, 5))
sns.countplot(x='Weekday', data=df_activity, order=df_activity['Weekday'].value_counts().index)
plt.xlabel('Weekday')
plt.ylabel('Frequency')
plt.title('Activity by Weekday')
plt.show()

# Plot activity by hour of the day / Trazar actividad por día de la semana
plt.figure(figsize=(8, 5))
sns.countplot(x='Hour', data=df_activity, order=df_activity['Hour'].value_counts().index)
plt.xlabel('Hour of the Day')
plt.ylabel('Frequency')
plt.title('Activity by Hour of the Day')
plt.show()

# Plot follower evolution / Trazar actividad por día de la semana
plt.figure(figsize=(10, 5))
plt.plot(df_followers['NewFollowers'], label='New Followers')
plt.plot(df_followers['LostFollowers'], label='Lost Followers')
plt.plot(df_followers['TotalFollowers'], label='Total Followers')
plt.xlabel('Date')
plt.ylabel('Number of Followers')
plt.title('Follower Evolution')
plt.legend()
plt.show()

# Plot interactions by hashtag / Trazar interacciones por hashtag
top_n = 10  # Number of top hashtags to visualize / Número de hashtags principales para visualizar
top_hashtags = list(sorted_hashtag_interactions.keys())[:top_n]
interactions_top = list(sorted_hashtag_interactions.values())[:top_n]

plt.figure(figsize=(10, 5))
sns.barplot(x=top_hashtags, y=interactions_top)
plt.xlabel('Hashtags')
plt.ylabel('Interactions')
plt.title(f'Top {top_n} Hashtags with Highest Interactions')
plt.xticks(rotation=45)
plt.show()

print("Post analysis completed.")
