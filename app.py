from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load data and keep only the top 7000 rows to save memory
df = pd.read_csv('anime_data.csv').head(7000) 
df['genres'] = df['genres'].fillna('')

# Initialize engine with limited features
cv = CountVectorizer(max_features=1000) # Further saves memory
count_matrix = cv.fit_transform(df['genres'])
similarity = cosine_similarity(count_matrix)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form.get('anime_name')
    try:
        # Match using the 'name' column from your Excel sheet
        idx = df[df['name'].str.contains(user_input, case=False)].index[0]
        distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
        
        results = []
        for i in distances[1:13]: # Get 12 for your 'Load More' feature
            results.append({
                'title': df.iloc[i[0]]['name'],
                'image': df.iloc[i[0]]['image_url'],
                'genres': df.iloc[i[0]]['genres']
            })
        return render_template('index.html', suggestions=results, original=user_input)
    except Exception as e:
        return render_template('index.html', error="Anime not found!")

if __name__ == "__main__":
    app.run()