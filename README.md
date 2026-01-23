# Anime Discovery Engine

A modern, interactive web application that recommends anime based on your favorite shows. Built with Flask, scikit-learn, and a stunning cyberpunk-themed UI.

## Features

✨ **Smart Recommendations**
- Content-based filtering using cosine similarity
- Recommendations based on anime genres
- Fast and accurate results

🎨 **Beautiful UI**
- Dark/Light theme toggle
- Glassmorphism design with neon accents
- Smooth animations and transitions
- Responsive design for all devices

🔍 **Search & Autocomplete**
- Real-time anime autocomplete
- Search from 7000+ anime titles
- Keyboard navigation support

📊 **Rich Results Display**
- Rating badges with star icons
- Genre tags for each anime
- Poster images with hover effects
- Load more functionality for pagination

## Tech Stack

- **Backend**: Flask (Python)
- **ML**: scikit-learn (TF-IDF & Cosine Similarity)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data**: anime_data.csv (7000+ anime)

## Project Structure

```
anim/
├── README.md                 # Project documentation
├── app.py                    # Flask application & recommendation engine
├── anime_data.csv            # Dataset with anime titles, genres, images, scores
├── requirements.txt          # Python dependencies
├── static/
│   └── style.css            # Complete styling with themes & animations
└── templates/
    └── index.html           # HTML template with JavaScript functionality
```

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/anim.git
   cd anim
   ```

2. **Create virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## How It Works

### Recommendation Algorithm
1. User searches for an anime they like
2. App finds matching anime in database
3. Creates content vector based on genres
4. Calculates similarity with all other anime using cosine similarity
5. Returns top 18 most similar anime sorted by similarity score

### Search Features
- **Autocomplete**: Suggests matching anime as you type (min 2 characters)
- **Keyboard Navigation**: Use arrow keys to navigate suggestions
- **Quick Select**: Click or press Enter to select an anime

## Features Explained

### Dark/Light Theme
Click the moon/sun icon in the top-right corner to toggle between themes. Your preference is saved locally.

### Scattered Background Images
The background displays small scattered anime poster images from your search results. Images:
- Update automatically when you search
- Float with smooth animations
- Are semi-transparent to not obstruct content
- Change opacity based on theme

### Anime Display Card
Shows beside the search bar:
- Large poster image of the searched anime
- Hover effects for interactivity
- Responsive sizing on mobile

### Results Grid
Displays recommendations in a responsive grid with:
- Anime poster image
- Rating badge (if available)
- Title and genre tags
- Hover effects for visual feedback
- Load More button to reveal additional recommendations

## API Endpoints

### POST `/recommend`
Searches for anime and returns recommendations.

**Parameters:**
- `anime_name` (string): Name of the anime to search for

**Response:**
```json
{
  "suggestions": [
    {
      "title": "Anime Title",
      "image": "image_url",
      "genres": "Genre1, Genre2, Genre3",
      "score": 8.5
    }
  ],
  "original": "Searched Anime Name",
  "background_image": "searched_anime_image_url"
}
```

### GET `/autocomplete`
Returns autocomplete suggestions for anime search.

**Parameters:**
- `q` (string): Search query (min 2 characters)

**Response:**
```json
["Anime 1", "Anime 2", "Anime 3", ...]
```

## Customization

### Change Theme Colors
Edit CSS variables in style.css:
```css
:root {
    --neon-pink: #ff00ff;
    --neon-blue: #00f2ff;
    --dark-bg: #05050a;
}
```

### Adjust Recommendation Count
In app.py, modify the slicing range:
```python
for i in distances[1:19]:  # Change 19 to desired count + 1
```

### Modify Background Image Opacity
In style.css:
```css
.scattered-image {
    opacity: 0.35;  /* Adjust this value (0-1) */
}
```

## Performance

- **Dataset**: 7000 anime (optimized for performance)
- **TF-IDF**: Limited to 1000 features to save memory
- **Load Time**: Fast recommendations within seconds
- **Browser Support**: All modern browsers (Chrome, Firefox, Safari, Edge)

## Browser Compatibility

- Chrome/Chromium: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Edge: ✅ Full support
- IE11: ⚠️ Limited support (no CSS variables)

## Troubleshooting

### "Anime not found" error
- Check spelling of anime name
- Try partial names (e.g., "Attack" instead of "Attack on Titan")
- Use autocomplete for exact matches

### Recommendations seem irrelevant
- This is a content-based system (uses genres only)
- More similar genres = more similar anime
- Try searching for niche anime with specific genres

### Slow performance
- Clear browser cache
- Reduce number of results with `Load More` button
- Close other heavy applications

## Future Enhancements

- [ ] Collaborative filtering for better recommendations
- [ ] User ratings and preferences
- [ ] Advanced filtering by year, studio, season
- [ ] Watchlist functionality
- [ ] Share recommendations feature
- [ ] Integration with MyAnimeList API

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Credits

- **Dataset**: Anime data sourced from publicly available anime databases
- **Fonts**: Google Fonts (Orbitron, Rajdhani)
- **Icons**: Custom SVG icons

## Contact & Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review the code comments

---

**Last Updated**: January 23, 2026
**Version**: 1.0.0
```