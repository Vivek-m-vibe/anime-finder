from flask import Flask, render_template, request, jsonify
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
        searched_anime_image = df.iloc[idx]['image_url']
        # Ensure the image URL is valid
        if pd.isna(searched_anime_image) or searched_anime_image == '' or str(searched_anime_image).strip() == '':
            searched_anime_image = None
        else:
            searched_anime_image = str(searched_anime_image).strip()
        distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
        
        results = []
        for i in distances[1:19]: # Get 18 for your 'Load More' feature (6 initial + 6 + 6)
            results.append({
                'title': df.iloc[i[0]]['name'],
                'image': df.iloc[i[0]]['image_url'],
                'genres': df.iloc[i[0]]['genres'],
                'score': df.iloc[i[0]]['score'] if pd.notna(df.iloc[i[0]]['score']) else None
            })
        return render_template('index.html', suggestions=results, original=user_input, background_image=searched_anime_image)
    except Exception as e:
        return render_template('index.html', error="Anime not found!")

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('q', '').lower()
    if len(query) < 2:
        return jsonify([])
    
    # Get matching anime names (case-insensitive)
    matches = df[df['name'].str.contains(query, case=False, na=False)]['name'].head(10).tolist()
    return jsonify(matches)

if __name__ == "__main__":
    app.run()