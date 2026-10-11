import requests
import urllib.parse
from utils.curated_data import CURATED_MOVIES, search_curated

BASE_URL = "https://api.tmdb.org/3"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

GENRE_MAP = {
    28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy", 80: "Crime",
    99: "Documentary", 18: "Drama", 10751: "Family", 14: "Fantasy", 36: "History",
    27: "Horror", 10402: "Music", 9648: "Mystery", 10749: "Romance", 878: "Sci-Fi",
    10770: "TV Movie", 53: "Thriller", 10752: "War", 37: "Western",
    10759: "Action & Adventure", 10762: "Kids", 10763: "News", 10764: "Reality",
    10765: "Sci-Fi & Fantasy", 10766: "Soap", 10767: "Talk", 10768: "War & Politics"
}

LANG_MAP = {
    "te": "Telugu",
    "ta": "Tamil",
    "hi": "Hindi",
    "ml": "Malayalam",
    "kn": "Kannada",
    "en": "English",
    "ko": "Korean",
    "ja": "Japanese",
    "es": "Spanish",
    "fr": "French"
}

def generate_provider_url(provider_name: str, title: str) -> str:
    """Generates a direct search/watch link for an OTT platform."""
    encoded_title = urllib.parse.quote_plus(title)
    name_lower = provider_name.lower()
    
    if "netflix" in name_lower:
        return f"https://www.netflix.com/search?q={encoded_title}"
    elif "prime" in name_lower or "amazon" in name_lower:
        return f"https://www.primevideo.com/search/ref=atv_nb_sr?phrase={encoded_title}"
    elif "hotstar" in name_lower or "disney" in name_lower:
        return f"https://www.hotstar.com/in/explore?search_query={encoded_title}"
    elif "zee5" in name_lower:
        return f"https://www.zee5.com/search?q={encoded_title}"
    elif "jiocinema" in name_lower or "jio" in name_lower:
        return f"https://www.jiocinema.com/search/{encoded_title}"
    elif "sonyliv" in name_lower:
        return f"https://www.sonyliv.com/search/{encoded_title}"
    elif "aha" in name_lower:
        return f"https://www.aha.video/search?q={encoded_title}"
    elif "sun nxt" in name_lower or "sunnxt" in name_lower:
        return f"https://www.sunnxt.com/search/{encoded_title}"
    elif "apple" in name_lower:
        return f"https://tv.apple.com/search?term={encoded_title}"
    elif "youtube" in name_lower or "google" in name_lower:
        return f"https://www.youtube.com/results?search_query={encoded_title}+full+movie"
    else:
        return f"https://www.google.com/search?q=watch+{encoded_title}+online+on+{urllib.parse.quote_plus(provider_name)}"

def get_provider_badge_style(provider_name: str) -> dict:
    """Returns CSS class, icon, and colors for major Indian and global OTT platforms."""
    name_lower = provider_name.lower()
    if "netflix" in name_lower:
        return {"class": "netflix", "color": "#E50914", "icon": "🔴", "label": "Netflix"}
    elif "prime" in name_lower or "amazon" in name_lower:
        return {"class": "amazon", "color": "#00A8E1", "icon": "🔵", "label": "Prime Video"}
    elif "hotstar" in name_lower or "disney" in name_lower:
        return {"class": "hotstar", "color": "#032541", "border": "#FFD700", "icon": "⭐", "label": "Hotstar"}
    elif "zee5" in name_lower:
        return {"class": "zee5", "color": "#8230C6", "icon": "🟣", "label": "ZEE5"}
    elif "jiocinema" in name_lower or "jio" in name_lower:
        return {"class": "jiocinema", "color": "#E5007D", "icon": "🌸", "label": "JioCinema"}
    elif "sonyliv" in name_lower:
        return {"class": "sonyliv", "color": "#FF5B00", "icon": "🟠", "label": "SonyLIV"}
    elif "aha" in name_lower:
        return {"class": "aha", "color": "#FF4500", "icon": "🟧", "label": "Aha"}
    elif "sun nxt" in name_lower or "sunnxt" in name_lower:
        return {"class": "sunnxt", "color": "#E51937", "icon": "🟡", "label": "Sun NXT"}
    elif "apple" in name_lower:
        return {"class": "appletv", "color": "#333333", "icon": "🍎", "label": "Apple TV"}
    elif "youtube" in name_lower:
        return {"class": "youtube", "color": "#CC0000", "icon": "▶️", "label": "YouTube"}
    else:
        return {"class": "other", "color": "#2c3440", "icon": "📺", "label": provider_name}

def format_media_item(item: dict) -> dict:
    """Formats raw TMDB media item into clean normalized dictionary."""
    media_type = item.get("media_type", "movie")
    title = item.get("title") or item.get("name") or "Untitled"
    release_date = item.get("release_date") or item.get("first_air_date") or ""
    year = release_date[:4] if release_date else ""
    
    genre_ids = item.get("genre_ids", [])
    genres = [GENRE_MAP.get(gid) for gid in genre_ids if gid in GENRE_MAP]
    
    lang_code = item.get("original_language", "")
    language = LANG_MAP.get(lang_code, lang_code.upper() if lang_code else "Unknown")
    
    return {
        "id": item.get("id"),
        "title": title,
        "media_type": media_type,
        "year": year,
        "release_date": release_date,
        "rating": round(item.get("vote_average", 0.0), 1),
        "vote_count": item.get("vote_count", 0),
        "language": language,
        "lang_code": lang_code,
        "genres": genres[:3],
        "poster_path": item.get("poster_path"),
        "backdrop_path": item.get("backdrop_path"),
        "overview": item.get("overview") or "No description available."
    }

def search_media(query: str, api_key: str, media_type: str = "all", page: int = 1, language_filter: str = "All") -> list:
    """
    Searches for movies and TV shows across TMDB.
    Falls back gracefully to curated database if api_key is 'demo' or unavailable.
    """
    if not api_key or api_key.lower() == "demo":
        return search_curated(query, language=language_filter)
        
    endpoint = "/search/multi"
    if media_type == "movie":
        endpoint = "/search/movie"
    elif media_type == "tv":
        endpoint = "/search/tv"
        
    url = f"{BASE_URL}{endpoint}"
    params = {
        "api_key": api_key,
        "query": query,
        "page": page,
        "include_adult": "false"
    }
    
    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=8)
        response.raise_for_status()
        raw_results = response.json().get("results", [])
        
        results = []
        for item in raw_results:
            # If multi-search, ensure it's movie or tv
            m_type = item.get("media_type", media_type if media_type != "all" else "movie")
            if m_type not in ["movie", "tv"]:
                continue
            item["media_type"] = m_type
            formatted = format_media_item(item)
            
            # Apply language filter if requested
            if language_filter != "All" and formatted["language"] != language_filter:
                continue
                
            results.append(formatted)
            
        return results
    except Exception as e:
        print(f"TMDB search failed ({e}), using curated database fallback")
        return search_curated(query, language=language_filter)

def get_trending(api_key: str, time_window: str = "week") -> list:
    """Fetches trending movies and TV shows."""
    if not api_key or api_key.lower() == "demo":
        return CURATED_MOVIES[:8]
        
    url = f"{BASE_URL}/trending/all/{time_window}"
    params = {"api_key": api_key}
    
    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=8)
        response.raise_for_status()
        raw_results = response.json().get("results", [])
        return [format_media_item(item) for item in raw_results if item.get("media_type") in ["movie", "tv"]]
    except Exception as e:
        print(f"TMDB trending failed ({e}), using curated fallback")
        return CURATED_MOVIES[:8]

def discover_by_language(api_key: str, lang_code: str, page: int = 1) -> list:
    """Discovers movies by original language (e.g., 'te' for Telugu, 'hi' for Hindi)."""
    if not api_key or api_key.lower() == "demo":
        return [m for m in CURATED_MOVIES if m.get("lang_code") == lang_code]
        
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": api_key,
        "with_original_language": lang_code,
        "sort_by": "popularity.desc",
        "page": page,
        "include_adult": "false"
    }
    
    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=8)
        response.raise_for_status()
        raw_results = response.json().get("results", [])
        for item in raw_results:
            item["media_type"] = "movie"
        return [format_media_item(item) for item in raw_results]
    except Exception as e:
        print(f"TMDB discover failed ({e}), using curated fallback")
        return [m for m in CURATED_MOVIES if m.get("lang_code") == lang_code]

def get_watch_providers(media_id: int, media_type: str, api_key: str, region: str = "IN", title: str = "") -> dict:
    """
    Fetches streaming availability for a specific region.
    Returns categorized streams: subscription (flatrate), free, ads, rent, buy,
    and includes direct 1-click launch links for each platform!
    """
    # Check if media exists in curated database first for instant offline response
    for m in CURATED_MOVIES:
        if m["id"] == media_id and "providers" in m:
            return m["providers"]
            
    if not api_key or api_key.lower() == "demo":
        # Generate smart direct links based on title even if offline
        clean_title = title or "movie"
        return {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": generate_provider_url("Netflix", clean_title)},
                {"provider_name": "Prime Video", "logo_class": "amazon", "url": generate_provider_url("Amazon Prime Video", clean_title)},
                {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": generate_provider_url("Disney+ Hotstar", clean_title)},
                {"provider_name": "ZEE5", "logo_class": "zee5", "url": generate_provider_url("ZEE5", clean_title)}
            ],
            "free": [
                {"provider_name": "JioCinema", "logo_class": "jiocinema", "url": generate_provider_url("JioCinema", clean_title)}
            ],
            "rent": [],
            "justwatch_link": f"https://www.justwatch.com/in/search?q={urllib.parse.quote_plus(clean_title)}"
        }

    url = f"{BASE_URL}/{media_type}/{media_id}/watch/providers"
    params = {"api_key": api_key}
    
    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=8)
        response.raise_for_status()
        results = response.json().get("results", {})
        
        region_data = results.get(region, {})
        if not region_data and region != "IN":
            region_data = results.get("IN", {})
            
        justwatch_link = region_data.get("link", f"https://www.justwatch.com/in/search?q={urllib.parse.quote_plus(title)}")
        
        def process_list(raw_list):
            out = []
            for item in raw_list:
                p_name = item.get("provider_name", "")
                badge = get_provider_badge_style(p_name)
                out.append({
                    "provider_name": p_name,
                    "logo_class": badge["class"],
                    "icon": badge["icon"],
                    "color": badge["color"],
                    "url": generate_provider_url(p_name, title)
                })
            return out

        categorized = {
            "flatrate": process_list(region_data.get("flatrate", [])),
            "free": process_list(region_data.get("free", [])),
            "ads": process_list(region_data.get("ads", [])),
            "rent": process_list(region_data.get("rent", [])),
            "buy": process_list(region_data.get("buy", [])),
            "justwatch_link": justwatch_link
        }
        
        # If TMDB has no watch providers mapped yet for this title,
        # provide universal quick search links to all top Indian OTTs so user is never blocked!
        if not (categorized["flatrate"] or categorized["free"] or categorized["ads"]):
            categorized["quick_links"] = [
                {"provider_name": "Search on Netflix", "icon": "🔴", "url": generate_provider_url("Netflix", title)},
                {"provider_name": "Search on Prime Video", "icon": "🔵", "url": generate_provider_url("Amazon Prime Video", title)},
                {"provider_name": "Search on Hotstar", "icon": "⭐", "url": generate_provider_url("Disney+ Hotstar", title)},
                {"provider_name": "Search on ZEE5", "icon": "🟣", "url": generate_provider_url("ZEE5", title)},
                {"provider_name": "Search on JioCinema", "icon": "🌸", "url": generate_provider_url("JioCinema", title)}
            ]
            
        return categorized
    except Exception as e:
        print(f"Watch provider lookup failed ({e})")
        return {
            "flatrate": [],
            "free": [],
            "rent": [],
            "quick_links": [
                {"provider_name": "Search on Netflix", "icon": "🔴", "url": generate_provider_url("Netflix", title)},
                {"provider_name": "Search on Prime Video", "icon": "🔵", "url": generate_provider_url("Amazon Prime Video", title)},
                {"provider_name": "Search on Hotstar", "icon": "⭐", "url": generate_provider_url("Disney+ Hotstar", title)},
                {"provider_name": "Search on ZEE5", "icon": "🟣", "url": generate_provider_url("ZEE5", title)}
            ]
        }
