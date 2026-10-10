# StreamFinder 🍿

StreamFinder is a universal streaming guide web application. Search for any movie or TV show and instantly find out if it is available for streaming on platforms like Netflix, Prime Video, Hotstar, and Zee5 in India.

## 🚀 Features
- **Universal Search**: Search the massive TMDB database for any movie or TV show.
- **Streaming Availability**: Instantly see which subscription services host the movie in India.
- **Direct Links**: Click directly through to the JustWatch page to start watching immediately.
- **Beautiful UI**: Simple, color-coded interface powered by Streamlit.

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.9+
- A free [TMDB API Key](https://www.themoviedb.org/settings/api).

### 2. Installation
Clone the repository and install the dependencies:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory and add your API Key:
```env
TMDB_API_KEY=your_actual_api_key_here
```

### 4. Running the App
```bash
streamlit run app.py
```
