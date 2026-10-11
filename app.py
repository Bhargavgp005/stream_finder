import streamlit as st
import os
from dotenv import load_dotenv
from utils.tmdb_client import (
    search_media, 
    get_trending, 
    discover_by_language, 
    get_watch_providers,
    LANG_MAP
)
from utils.curated_data import CURATED_MOVIES

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="StreamFinder 🍿 | Universal Streaming Guide",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
    }

    /* Hero Banner */
    .hero-container {
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 30px;
        background: linear-gradient(180deg, rgba(11,15,25,0.2) 0%, rgba(11,15,25,0.95) 100%),
                    url('https://image.tmdb.org/t/p/original/m0Ob5uFqO9gB4Y55Z2V1o5u5g6y.jpg') center/cover;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 40px rgba(0,0,0,0.6);
        padding: 40px 35px 30px 35px;
    }
    .hero-tag {
        display: inline-block;
        background: linear-gradient(90deg, #E50914, #ff5b00);
        color: white;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 15px;
    }
    .hero-title {
        font-size: 38px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 10px;
        line-height: 1.2;
        text-shadow: 0 2px 10px rgba(0,0,0,0.8);
    }
    .hero-meta {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 14px;
        color: #cbd5e1;
        margin-bottom: 12px;
    }
    .hero-meta .rating {
        color: #f59e0b;
        font-weight: 700;
    }
    .hero-desc {
        font-size: 15px;
        color: #94a3b8;
        max-width: 650px;
        line-height: 1.5;
        margin-bottom: 20px;
    }

    /* Movie Cards */
    .movie-card {
        background: rgba(18, 24, 38, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        overflow: hidden;
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        margin-bottom: 24px;
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    .movie-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 30px rgba(0, 0, 0, 0.7);
        border-color: rgba(99, 102, 241, 0.4);
    }
    .poster-container {
        position: relative;
        width: 100%;
        padding-top: 145%;
        background-color: #1e293b;
        overflow: hidden;
    }
    .poster-img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .rating-badge {
        position: absolute;
        top: 10px;
        right: 10px;
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(8px);
        color: #f59e0b;
        font-size: 12px;
        font-weight: 700;
        padding: 4px 8px;
        border-radius: 8px;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }
    .lang-badge {
        position: absolute;
        top: 10px;
        left: 10px;
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(8px);
        color: #e2e8f0;
        font-size: 11px;
        font-weight: 600;
        padding: 4px 8px;
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .card-body {
        padding: 16px;
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }
    .card-title {
        font-size: 16px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 4px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .card-meta {
        font-size: 12px;
        color: #94a3b8;
        margin-bottom: 12px;
    }
    
    /* Platform Badges */
    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: auto;
        padding-top: 8px;
    }
    .platform-btn {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        font-size: 11px;
        font-weight: 600;
        padding: 5px 10px;
        border-radius: 8px;
        color: white;
        text-decoration: none;
        transition: transform 0.15s ease, opacity 0.15s ease;
        border: 1px solid rgba(255,255,255,0.15);
    }
    .platform-btn:hover {
        transform: scale(1.05);
        color: white;
        text-decoration: none;
        opacity: 0.95;
    }
    .btn-netflix { background: #E50914; }
    .btn-amazon { background: #00A8E1; color: #ffffff !important; }
    .btn-hotstar { background: #032541; border: 1px solid #FFD700; color: #FFD700 !important; }
    .btn-zee5 { background: #8230C6; }
    .btn-jiocinema { background: #E5007D; }
    .btn-sonyliv { background: #FF5B00; }
    .btn-aha { background: #FF4500; }
    .btn-sunnxt { background: #E51937; }
    .btn-appletv { background: #1f2937; }
    .btn-youtube { background: #CC0000; }
    .btn-other { background: #334155; }

    /* Custom Input */
    .stTextInput>div>div>input {
        background-color: #131b2e !important;
        color: #ffffff !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 15px !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.25) !important;
    }

    /* Section Headers */
    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
        margin-top: 15px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR CONFIGURATION -----------------
with st.sidebar:
    st.markdown("### 🍿 StreamFinder")
    st.caption("Universal OTT Availability Guide for India & Global")
    st.markdown("---")
    
    # API Key Handling (Reads from env or user input)
    default_key = os.getenv("TMDB_API_KEY", "")
    if "api_key" not in st.session_state:
        st.session_state.api_key = default_key
        
    api_key_input = st.text_input(
        "🔑 TMDB API Key",
        value=st.session_state.api_key,
        type="password",
        placeholder="Enter key or leave blank for Curated Mode",
        help="Get a free key from themoviedb.org. If left empty, app runs in instant Curated Mode with 20+ top Indian & Hollywood hits!"
    )
    st.session_state.api_key = api_key_input.strip()

    if not st.session_state.api_key:
        st.info("💡 **Curated Catalog Active**: Enjoy instant access to blockbuster movies and shows across Netflix, Prime, Hotstar, and Zee5!")
    else:
        st.success("✅ **Live TMDB API Connected**: Searching over 1,000,000+ movies and TV series!")

    st.markdown("---")
    st.markdown("### 🌍 Streaming Country")
    regions = {
        "India (IN) 🇮🇳": "IN",
        "United States (US) 🇺🇸": "US",
        "United Kingdom (GB) 🇬🇧": "GB",
        "Canada (CA) 🇨🇦": "CA",
        "Australia (AU) 🇦🇺": "AU",
        "Japan (JP) 🇯🇵": "JP",
        "South Korea (KR) 🇰🇷": "KR"
    }
    selected_region_label = st.selectbox("Select Country:", list(regions.keys()), index=0)
    selected_region_code = regions[selected_region_label]

    st.markdown("---")
    st.markdown("### 📱 Direct Launch Platforms")
    st.markdown("""
    - 🔴 **Netflix India**
    - 🔵 **Amazon Prime Video**
    - ⭐ **Disney+ Hotstar**
    - 🟣 **ZEE5**
    - 🌸 **JioCinema**
    - 🟠 **SonyLIV**
    - 🟧 **Aha (Telugu/Tamil)**
    - 🟡 **Sun NXT**
    - 📺 **YouTube Movies**
    """)
    st.markdown("---")
    st.caption("Built with Streamlit & TMDB JustWatch API")


# ----------------- FEATURED HERO BANNER -----------------
st.markdown("""
<div class="hero-container">
    <div class="hero-tag">🔥 Featured Indian Blockbuster</div>
    <div class="hero-title">RRR (Rise Roar Revolt)</div>
    <div class="hero-meta">
        <span class="rating">⭐ 8.1 / 10</span>
        <span>•</span>
        <span>2022</span>
        <span>•</span>
        <span>Telugu, Hindi, Tamil, Malayalam</span>
        <span>•</span>
        <span>Action, Drama</span>
    </div>
    <div class="hero-desc">
        A fearless revolutionary and an officer in the British force decide to join forces and chart out a path towards independence against the British Raj.
    </div>
    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="https://www.netflix.com/title/81476453" target="_blank" class="platform-btn btn-netflix" style="padding: 10px 18px; font-size: 13px;">
            🔴 Watch Hindi on Netflix
        </a>
        <a href="https://www.zee5.com/movies/details/rrr/0-0-1z5154378" target="_blank" class="platform-btn btn-zee5" style="padding: 10px 18px; font-size: 13px;">
            🟣 Watch Telugu on ZEE5
        </a>
        <a href="https://www.hotstar.com/in/explore?search_query=RRR" target="_blank" class="platform-btn btn-hotstar" style="padding: 10px 18px; font-size: 13px;">
            ⭐ Watch Tamil/Malayalam on Hotstar
        </a>
    </div>
</div>
""", unsafe_allow_html=True)


# ----------------- NAVIGATION & FILTERS -----------------
main_tab, trending_tab, regional_tab, platform_tab = st.tabs([
    "🔍 Search & Discover", 
    "🔥 Trending This Week", 
    "🇮🇳 Regional Indian Cinema", 
    "📺 Browse by OTT Platform"
])


def render_movie_grid(movie_list, active_api_key, region_code):
    """Renders a grid of realistic movie cards with provider buttons and detailed drawers."""
    if not movie_list:
        st.warning("No titles found matching your criteria. Try adjusting your search or filters.")
        return

    # Render in 4 responsive columns
    cols = st.columns(4)
    for idx, movie in enumerate(movie_list):
        with cols[idx % 4]:
            poster_path = movie.get("poster_path")
            if poster_path:
                if poster_path.startswith("http"):
                    poster_url = poster_path
                else:
                    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            else:
                poster_url = "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=500&auto=format&fit=crop&q=80"

            rating = movie.get("rating", 0.0)
            year = movie.get("year", "")
            title = movie.get("title", "Untitled")
            lang = movie.get("language", "All")
            m_type = "🎬 Movie" if movie.get("media_type") == "movie" else "📺 Series"
            
            # Fetch providers
            providers = get_watch_providers(
                movie["id"], 
                movie.get("media_type", "movie"), 
                active_api_key, 
                region=region_code,
                title=title
            )

            # Render Card HTML
            st.markdown(f"""
            <div class="movie-card">
                <div class="poster-container">
                    <img class="poster-img" src="{poster_url}" alt="{title}" loading="lazy">
                    <div class="rating-badge">⭐ {rating}</div>
                    <div class="lang-badge">{lang}</div>
                </div>
                <div class="card-body">
                    <div class="card-title" title="{title}">{title}</div>
                    <div class="card-meta">{year} • {m_type}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Streaming Availability Accordion / Expander
            with st.expander(f"🍿 Where to Watch: {title[:20]}...", expanded=False):
                st.write(f"**Plot Synopsis:** {movie.get('overview', 'No summary.')}")
                
                # Subscription Platforms
                flatrate = providers.get("flatrate", [])
                if flatrate:
                    st.markdown("**📺 Stream on Subscription:**")
                    badge_html = "<div class='badge-container'>"
                    for p in flatrate:
                        name = p["provider_name"]
                        url = p.get("url", "#")
                        b_class = f"btn-{p.get('logo_class', 'other')}"
                        badge_html += f"<a href='{url}' target='_blank' class='platform-btn {b_class}'>{name} ↗</a>"
                    badge_html += "</div>"
                    st.markdown(badge_html, unsafe_allow_html=True)
                
                # Free / Ad-Supported Platforms
                free_streams = providers.get("free", []) + providers.get("ads", [])
                if free_streams:
                    st.markdown("<div style='margin-top: 10px;'><b>🆓 Watch Free / With Ads:</b></div>", unsafe_allow_html=True)
                    badge_html = "<div class='badge-container'>"
                    for p in free_streams:
                        name = p["provider_name"]
                        url = p.get("url", "#")
                        b_class = f"btn-{p.get('logo_class', 'other')}"
                        badge_html += f"<a href='{url}' target='_blank' class='platform-btn {b_class}'>🆓 {name} ↗</a>"
                    badge_html += "</div>"
                    st.markdown(badge_html, unsafe_allow_html=True)

                # Universal Direct Quick Search buttons
                quick_links = providers.get("quick_links", [])
                if quick_links:
                    st.markdown("<div style='margin-top: 10px;'><b>🔍 Open Directly In:</b></div>", unsafe_allow_html=True)
                    badge_html = "<div class='badge-container'>"
                    for q in quick_links:
                        badge_html += f"<a href='{q['url']}' target='_blank' class='platform-btn btn-other'>{q['icon']} {q['provider_name']} ↗</a>"
                    badge_html += "</div>"
                    st.markdown(badge_html, unsafe_allow_html=True)

                # Rent / Buy
                rent_buy = providers.get("rent", [])
                if rent_buy:
                    st.markdown("<div style='margin-top: 8px;'><b>🎟️ Available to Rent:</b></div>", unsafe_allow_html=True)
                    badge_html = "<div class='badge-container'>"
                    for r in rent_buy:
                        badge_html += f"<a href='{r.get('url', '#')}' target='_blank' class='platform-btn btn-other'>{r['provider_name']} ↗</a>"
                    badge_html += "</div>"
                    st.markdown(badge_html, unsafe_allow_html=True)

                justwatch = providers.get("justwatch_link")
                if justwatch:
                    st.markdown(f"<div style='margin-top: 10px;'><a href='{justwatch}' target='_blank' style='font-size: 12px; color: #94a3b8;'>🔗 Verify on JustWatch Database</a></div>", unsafe_allow_html=True)

            st.write("") # Spacer between rows


# ----------------- TAB 1: SEARCH & DISCOVER -----------------
with main_tab:
    st.markdown('<div class="section-title">🔍 Search Any Movie or Series Worldwide</div>', unsafe_allow_html=True)
    
    col_search, col_lang, col_type = st.columns([3, 1, 1])
    with col_search:
        search_query = st.text_input(
            "Search Title", 
            placeholder="Type any movie or show (e.g. Kalki 2898 AD, Salaar, Stranger Things, Mirzapur, Inception)...",
            label_visibility="collapsed"
        )
    with col_lang:
        lang_filter = st.selectbox(
            "Filter Language", 
            ["All", "Telugu", "Hindi", "Tamil", "Malayalam", "English", "Korean"],
            label_visibility="collapsed"
        )
    with col_type:
        type_filter = st.selectbox(
            "Filter Type", 
            ["All", "Movies Only", "TV Shows Only"],
            label_visibility="collapsed"
        )
    
    m_type_arg = "all"
    if type_filter == "Movies Only": m_type_arg = "movie"
    elif type_filter == "TV Shows Only": m_type_arg = "tv"

    if search_query:
        with st.spinner(f"Searching streaming availability for '{search_query}'..."):
            results = search_media(
                search_query, 
                st.session_state.api_key, 
                media_type=m_type_arg, 
                language_filter=lang_filter
            )
            st.markdown(f"**Found {len(results)} results for '{search_query}'**")
            render_movie_grid(results, st.session_state.api_key, selected_region_code)
    else:
        st.markdown('<div class="section-title">🍿 Popular Right Now Across Platforms</div>', unsafe_allow_html=True)
        # Show curated or trending collection by default so page is NEVER blank
        default_items = CURATED_MOVIES
        if lang_filter != "All":
            default_items = [m for m in default_items if m.get("language") == lang_filter]
        render_movie_grid(default_items, st.session_state.api_key, selected_region_code)


# ----------------- TAB 2: TRENDING THIS WEEK -----------------
with trending_tab:
    st.markdown('<div class="section-title">🔥 What Everyone is Watching This Week</div>', unsafe_allow_html=True)
    with st.spinner("Fetching trending movies and series..."):
        trending_items = get_trending(st.session_state.api_key)
        render_movie_grid(trending_items, st.session_state.api_key, selected_region_code)


# ----------------- TAB 3: REGIONAL INDIAN CINEMA -----------------
with regional_tab:
    st.markdown('<div class="section-title">🇮🇳 Discover South Indian & Bollywood Cinema</div>', unsafe_allow_html=True)
    
    selected_ind_lang = st.radio(
        "Choose Industry:",
        ["Telugu (Tollywood)", "Hindi (Bollywood)", "Tamil (Kollywood)", "Malayalam (Mollywood)"],
        horizontal=True
    )
    
    code_map = {
        "Telugu (Tollywood)": "te",
        "Hindi (Bollywood)": "hi",
        "Tamil (Kollywood)": "ta",
        "Malayalam (Mollywood)": "ml"
    }
    target_code = code_map[selected_ind_lang]
    
    with st.spinner(f"Loading top {selected_ind_lang} titles..."):
        regional_items = discover_by_language(st.session_state.api_key, target_code)
        render_movie_grid(regional_items, st.session_state.api_key, selected_region_code)


# ----------------- TAB 4: BROWSE BY OTT PLATFORM -----------------
with platform_tab:
    st.markdown('<div class="section-title">📺 Select Your Streaming Subscription</div>', unsafe_allow_html=True)
    
    selected_platform = st.selectbox(
        "Choose Platform to view catalog:",
        ["Netflix", "Amazon Prime Video", "Disney+ Hotstar", "ZEE5", "JioCinema", "Aha"]
    )
    
    platform_results = []
    for item in CURATED_MOVIES:
        prov_dict = item.get("providers", {})
        all_provs = []
        for p_list in prov_dict.values():
            for p in p_list:
                all_provs.append(p.get("provider_name", "").lower())
        if any(selected_platform.lower() in p for p in all_provs):
            platform_results.append(item)
            
    st.markdown(f"**Showing top movies & series streaming on {selected_platform} in India:**")
    render_movie_grid(platform_results, st.session_state.api_key, selected_region_code)
