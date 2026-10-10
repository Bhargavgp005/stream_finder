import requests

BASE_URL = "https://api.tmdb.org/3"

def search_media(query: str, api_key: str):
    """Searches for movies and TV shows."""
    if api_key.lower() == "demo":
        # Provide a mock search result
        return [
            {
                "id": 19995,
                "media_type": "movie",
                "title": "Avatar (Demo)",
                "poster_path": "/jRXYjXNqcgCSKpY042K9pU7X4K8.jpg"
            },
            {
                "id": 1396,
                "media_type": "tv",
                "name": "Breaking Bad (Demo)",
                "poster_path": "/3xnWaLQjelJDDF7LT1WBo6f4BRe.jpg"
            }
        ]

    url = f"{BASE_URL}/search/multi"
    params = {
        "api_key": api_key,
        "query": query,
        "page": 1,
        "include_adult": "false"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    results = response.json().get("results", [])
    
    # Filter only movies and TV shows
    filtered_results = [
        item for item in results 
        if item.get("media_type") in ["movie", "tv"]
    ]
    return filtered_results

def get_watch_providers(media_id: int, media_type: str, api_key: str, region: str = "IN"):
    """Gets the streaming providers for a specific region (Default: India 'IN')."""
    if api_key.lower() == "demo":
        if media_id == 19995: # Avatar
            return {
                "link": "https://www.hotstar.com/in/movies/avatar/1770000147",
                "flatrate": [{"provider_name": "Hotstar"}]
            }
        elif media_id == 1396: # Breaking Bad
            return {
                "link": "https://www.netflix.com/in/title/70143836",
                "flatrate": [{"provider_name": "Netflix"}, {"provider_name": "ZEE5"}]
            }
        return {}

    url = f"{BASE_URL}/{media_type}/{media_id}/watch/providers"
    params = {
        "api_key": api_key
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    results = response.json().get("results", {})
    
    # Get the data for the specific region
    region_data = results.get(region, {})
    return region_data
