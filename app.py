import streamlit as st
import os
from dotenv import load_dotenv
from utils.tmdb_client import search_media, get_watch_providers

# Load env variables
load_dotenv()

st.set_page_config(
    page_title="StreamFinder 🍿",
    page_icon="🍿",
    layout="wide"
)

# Custom CSS for UI
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
    }
    .platform-badge {
        display: inline-block;
        padding: 5px 10px;
        margin: 2px;
        border-radius: 5px;
        font-size: 12px;
        font-weight: bold;
        color: white;
    }
    .netflix { background-color: #E50914; }
    .amazon { background-color: #00A8E1; }
    .hotstar { background-color: #032541; }
    .zee5 { background-color: #8230C6; }
    .other { background-color: #333333; }
    .movie-title {
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("🍿 StreamFinder: Where is it Streaming?")
st.markdown("Search for any movie or TV show to find out if it's available on **Netflix, Prime Video, Hotstar, Zee5**, or other platforms in India!")

with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input(
        "TMDB API Key", 
        type="password", 
        value=os.getenv("TMDB_API_KEY", ""),
        help="Get your free API key from themoviedb.org"
    )
    
    st.header("🌍 Country")
    regions = {
        "India (IN)": "IN",
        "United States (US)": "US",
        "United Kingdom (GB)": "GB",
        "Canada (CA)": "CA",
        "Australia (AU)": "AU",
        "Japan (JP)": "JP",
        "South Korea (KR)": "KR"
    }
    selected_region_name = st.selectbox("Select Region for Streaming:", list(regions.keys()))
    selected_region_code = regions[selected_region_name]

    st.markdown("---")
    st.markdown("Powered by TMDB & JustWatch")

# Search Bar
query = st.text_input("🔍 Search for a movie or TV show...", placeholder="e.g., Avatar, Breaking Bad, RRR")

if query:
    if not api_key:
        st.warning("Please enter your TMDB API Key in the sidebar to search.")
    else:
        with st.spinner("Searching..."):
            try:
                results = search_media(query, api_key)
                
                if not results:
                    st.info("No results found. Try a different search term.")
                else:
                    # Display results in a grid
                    cols = st.columns(4)
                    
                    for idx, item in enumerate(results[:8]): # Limit to top 8 results
                        with cols[idx % 4]:
                            # Poster
                            if item.get('poster_path'):
                                poster_url = f"https://image.tmdb.org/t/p/w500{item['poster_path']}"
                            else:
                                poster_url = "https://via.placeholder.com/500x750?text=No+Poster"
                            
                            st.image(poster_url, use_container_width=True)
                            
                            # Title
                            title = item.get("title") or item.get("name")
                            st.markdown(f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True)
                            
                            # Get streaming providers
                            providers = get_watch_providers(item["id"], item["media_type"], api_key, region=selected_region_code)
                            
                            if not providers:
                                st.write("❌ Not streaming locally")
                            else:
                                # TMDB provides flatrate (subscription), rent, and buy. We care most about flatrate.
                                streaming_services = providers.get("flatrate", [])
                                watch_link = providers.get("link", "#")
                                
                                if not streaming_services:
                                    st.write("❌ Not on subscription")
                                else:
                                    for service in streaming_services:
                                        name = service["provider_name"]
                                        css_class = "other"
                                        if "Netflix" in name: css_class = "netflix"
                                        elif "Amazon" in name: css_class = "amazon"
                                        elif "Hotstar" in name: css_class = "hotstar"
                                        elif "ZEE5" in name: css_class = "zee5"
                                        
                                        st.markdown(f"<span class='platform-badge {css_class}'>{name}</span>", unsafe_allow_html=True)
                                
                                if watch_link != "#":
                                    st.markdown(f"[▶️ Watch / View Links]({watch_link})")
                            
                            st.markdown("---")
            except Exception as e:
                st.error(f"An error occurred: {e}")
