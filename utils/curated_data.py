"""
Curated streaming database of top Indian & Global movies and shows.
Serves as an offline/instant catalog to ensure StreamFinder ALWAYS feels
like a rich, complete, realistic streaming application even before live API queries.
"""

CURATED_MOVIES = [
    {
        "id": 579974,
        "title": "RRR",
        "media_type": "movie",
        "year": "2022",
        "language": "Telugu",
        "lang_code": "te",
        "rating": 8.1,
        "genres": ["Action", "Drama"],
        "poster_path": "/nEufeZlyAOLqO2brrs0ye2Nw0DU.jpg",
        "backdrop_path": "/m0Ob5uFqO9gB4Y55Z2V1o5u5g6y.jpg",
        "overview": "A fictional history of two legendary revolutionaries' journey away from home before they began fighting for their country in the 1920s.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/title/81476453"},
                {"provider_name": "ZEE5", "logo_class": "zee5", "url": "https://www.zee5.com/movies/details/rrr/0-0-1z5154378"},
                {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": "https://www.hotstar.com/in/explore?search_query=RRR"}
            ],
            "free": [],
            "rent": [{"provider_name": "YouTube Movies", "logo_class": "youtube", "url": "https://www.youtube.com/results?search_query=RRR+full+movie"}]
        }
    },
    {
        "id": 929590,
        "title": "Kalki 2898 AD",
        "media_type": "movie",
        "year": "2024",
        "language": "Telugu",
        "lang_code": "te",
        "rating": 7.6,
        "genres": ["Action", "Sci-Fi", "Mythology"],
        "poster_path": "/x989FjN88o7N1nB95rLzW5LzK4b.jpg",
        "backdrop_path": "/yE3i2w2y9Yk5V5Z2K4b.jpg",
        "overview": "A modern avatar of Vishnu, a Hindu god, is believed to have descended to earth to protect the world from evil forces in a dystopian futuristic city.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/search?q=Kalki%202898%20AD"},
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Kalki+2898+AD"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 693134,
        "title": "Pushpa 2: The Rule",
        "media_type": "movie",
        "year": "2024",
        "language": "Telugu",
        "lang_code": "te",
        "rating": 7.8,
        "genres": ["Action", "Crime", "Thriller"],
        "poster_path": "/tPnO0k4WwLqB8G5F9yP3o7xK.jpg",
        "backdrop_path": "/v9Y4L8K6x7P1o2b3c4d5e.jpg",
        "overview": "Pushpa Raj continues to consolidate his dominance in the red sandalwood smuggling syndicate while battling fierce enemies and law enforcement.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/search?q=Pushpa"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 857598,
        "title": "Pushpa: The Rise",
        "media_type": "movie",
        "year": "2021",
        "language": "Telugu",
        "lang_code": "te",
        "rating": 7.6,
        "genres": ["Action", "Crime"],
        "poster_path": "/p1U0mP8QoH2A8B5F9yP3o7xK.jpg",
        "backdrop_path": "/m1U0mP8QoH2A8B5F9yP3o7xK.jpg",
        "overview": "A laborer rises through the ranks of a red sandalwood smuggling syndicate, making powerful enemies along the way.",
        "providers": {
            "flatrate": [
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Pushpa"},
                {"provider_name": "Aha", "logo_class": "aha", "url": "https://www.aha.video/search?q=Pushpa"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 783461,
        "title": "Salaar: Part 1 - Ceasefire",
        "media_type": "movie",
        "year": "2023",
        "language": "Telugu",
        "lang_code": "te",
        "rating": 7.2,
        "genres": ["Action", "Crime", "Drama"],
        "poster_path": "/4L2Y1g8k3x9P5o7xK8B9F5L.jpg",
        "backdrop_path": "/5L2Y1g8k3x9P5o7xK8B9F5L.jpg",
        "overview": "A gang leader makes a promise to a dying friend and takes on other criminal gangs in the dystopian city of Khansaar.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/search?q=Salaar"},
                {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": "https://www.hotstar.com/in/explore?search_query=Salaar"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 872585,
        "title": "Oppenheimer",
        "media_type": "movie",
        "year": "2023",
        "language": "English",
        "lang_code": "en",
        "rating": 8.9,
        "genres": ["Biography", "Drama", "History"],
        "poster_path": "/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
        "backdrop_path": "/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",
        "overview": "The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb during World War II.",
        "providers": {
            "flatrate": [
                {"provider_name": "JioCinema", "logo_class": "jiocinema", "url": "https://www.jiocinema.com/search/Oppenheimer"},
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Oppenheimer"}
            ],
            "free": [],
            "rent": [
                {"provider_name": "Apple TV", "logo_class": "appletv", "url": "https://tv.apple.com"},
                {"provider_name": "YouTube Movies", "logo_class": "youtube", "url": "https://www.youtube.com"}
            ]
        }
    },
    {
        "id": 1072790,
        "title": "Stree 2",
        "media_type": "movie",
        "year": "2024",
        "language": "Hindi",
        "lang_code": "hi",
        "rating": 7.5,
        "genres": ["Comedy", "Horror"],
        "poster_path": "/m1p5yT9k3X8L2b9C5V7xK.jpg",
        "backdrop_path": "/n1p5yT9k3X8L2b9C5V7xK.jpg",
        "overview": "The town of Chanderi is haunted once again, this time by a headless entity named Sarkata that abducts modern, independent women.",
        "providers": {
            "flatrate": [
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Stree+2"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 93405,
        "title": "Squid Game",
        "media_type": "tv",
        "year": "2021-2024",
        "language": "Korean",
        "lang_code": "ko",
        "rating": 8.0,
        "genres": ["Drama", "Mystery", "Thriller"],
        "poster_path": "/dDlGuvE86x8z2a7xV4K9P.jpg",
        "backdrop_path": "/2y2w2y9Yk5V5Z2K4b.jpg",
        "overview": "Hundreds of cash-strapped players accept a strange invitation to compete in children's games with deadly stakes for a tempting prize.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/title/81040344"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 1396,
        "title": "Breaking Bad",
        "media_type": "tv",
        "year": "2008-2013",
        "language": "English",
        "lang_code": "en",
        "rating": 9.5,
        "genres": ["Crime", "Drama", "Thriller"],
        "poster_path": "/ztkUQFLlC19CCMYHW9o1zWhJRNq.jpg",
        "backdrop_path": "/tsRy63Mu5cu8etL1X7ZLyf7UP1M.jpg",
        "overview": "A chemistry teacher diagnosed with terminal lung cancer teams up with a former student to manufacture and sell crystal meth.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/title/70143836"},
                {"provider_name": "ZEE5", "logo_class": "zee5", "url": "https://www.zee5.com"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 66732,
        "title": "Stranger Things",
        "media_type": "tv",
        "year": "2016-2025",
        "language": "English",
        "lang_code": "en",
        "rating": 8.7,
        "genres": ["Sci-Fi", "Drama", "Fantasy"],
        "poster_path": "/49WJfeN0moxb9IPfGn8AIqMGskD.jpg",
        "backdrop_path": "/56v2KjBlU4XaOv9rVYEQypROD7P.jpg",
        "overview": "When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/title/80057281"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 19995,
        "title": "Avatar",
        "media_type": "movie",
        "year": "2009",
        "language": "English",
        "lang_code": "en",
        "rating": 7.9,
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "poster_path": "/kyeqWdyUXW608qlYkRqosgbbJyK.jpg",
        "backdrop_path": "/vL5LR6WdxWPjC1QZ88jL0L1zK.jpg",
        "overview": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "providers": {
            "flatrate": [
                {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": "https://www.hotstar.com/in/movies/avatar/1770000147"}
            ],
            "free": [],
            "rent": [{"provider_name": "Apple TV", "logo_class": "appletv", "url": "https://tv.apple.com"}]
        }
    },
    {
        "id": 94997,
        "title": "Mirzapur",
        "media_type": "tv",
        "year": "2018-2024",
        "language": "Hindi",
        "lang_code": "hi",
        "rating": 8.5,
        "genres": ["Action", "Crime", "Drama"],
        "poster_path": "/fQO9r9x0A2B4C5D6E7F8G.jpg",
        "backdrop_path": "/gQO9r9x0A2B4C5D6E7F8G.jpg",
        "overview": "A shocking incident at a wedding procession ignites a series of events entangling two families in the lawless city of Mirzapur.",
        "providers": {
            "flatrate": [
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/detail/0PDOKMV9CRL2CTIOQC8732E278"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 110901,
        "title": "Panchayat",
        "media_type": "tv",
        "year": "2020-2024",
        "language": "Hindi",
        "lang_code": "hi",
        "rating": 8.9,
        "genres": ["Comedy", "Drama"],
        "poster_path": "/m1a2b3c4d5e6f7g8h9i.jpg",
        "backdrop_path": "/n1a2b3c4d5e6f7g8h9i.jpg",
        "overview": "An engineering graduate takes up a job as a panchayat secretary in a remote village due to a lack of better job options.",
        "providers": {
            "flatrate": [
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/detail/0PDOKMV9CRL2CTIOQC8732E278"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 113962,
        "title": "Asur: Welcome to Your Dark Side",
        "media_type": "tv",
        "year": "2020-2023",
        "language": "Hindi",
        "lang_code": "hi",
        "rating": 8.5,
        "genres": ["Crime", "Mystery", "Thriller"],
        "poster_path": "/asur_poster.jpg",
        "backdrop_path": "/asur_backdrop.jpg",
        "overview": "A unique crime thriller that pits two opposing worlds against each other: forensic science and deep Indian mythology.",
        "providers": {
            "flatrate": [
                {"provider_name": "JioCinema", "logo_class": "jiocinema", "url": "https://www.jiocinema.com/search/Asur"}
            ],
            "free": [
                {"provider_name": "JioCinema (Free)", "logo_class": "jiocinema", "url": "https://www.jiocinema.com/search/Asur"}
            ],
            "rent": []
        }
    },
    {
        "id": 1022789,
        "title": "Hi Nanna",
        "media_type": "movie",
        "year": "2023",
        "language": "Telugu",
        "lang_code": "te",
        "rating": 8.2,
        "genres": ["Drama", "Family", "Romance"],
        "poster_path": "/hinanna_poster.jpg",
        "backdrop_path": "/hinanna_backdrop.jpg",
        "overview": "A loving single father's world turns upside down when his curious daughter befriends a mysterious woman in Mumbai.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/search?q=Hi%20Nanna"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 838209,
        "title": "Devara: Part 1",
        "media_type": "movie",
        "year": "2024",
        "language": "Telugu",
        "lang_code": "te",
        "rating": 7.1,
        "genres": ["Action", "Drama", "Thriller"],
        "poster_path": "/devara_poster.jpg",
        "backdrop_path": "/devara_backdrop.jpg",
        "overview": "A fearless man from a coastal region sets out on a perilous journey to safeguard his people from criminal syndicates.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/search?q=Devara"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 299534,
        "title": "Avengers: Endgame",
        "media_type": "movie",
        "year": "2019",
        "language": "English",
        "lang_code": "en",
        "rating": 8.4,
        "genres": ["Action", "Sci-Fi", "Adventure"],
        "poster_path": "/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
        "backdrop_path": "/7RyHsO4yDXtBv1zJW8mwRiVD15.jpg",
        "overview": "After the devastating events of Infinity War, the universe is in ruins. The remaining Avengers assemble once more to reverse Thanos' actions.",
        "providers": {
            "flatrate": [
                {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": "https://www.hotstar.com/in/explore?search_query=Avengers%20Endgame"}
            ],
            "free": [],
            "rent": [{"provider_name": "Apple TV", "logo_class": "appletv", "url": "https://tv.apple.com"}]
        }
    },
    {
        "id": 157336,
        "title": "Interstellar",
        "media_type": "movie",
        "year": "2014",
        "language": "English",
        "lang_code": "en",
        "rating": 8.7,
        "genres": ["Adventure", "Drama", "Sci-Fi"],
        "poster_path": "/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
        "backdrop_path": "/rAiYTgg0kWUw7GeLl0GQ8qviP2.jpg",
        "overview": "The adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel.",
        "providers": {
            "flatrate": [
                {"provider_name": "JioCinema", "logo_class": "jiocinema", "url": "https://www.jiocinema.com/search/Interstellar"},
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Interstellar"}
            ],
            "free": [],
            "rent": [{"provider_name": "Apple TV", "logo_class": "appletv", "url": "https://tv.apple.com"}]
        }
    },
    {
        "id": 27205,
        "title": "Inception",
        "media_type": "movie",
        "year": "2010",
        "language": "English",
        "lang_code": "en",
        "rating": 8.8,
        "genres": ["Action", "Sci-Fi", "Thriller"],
        "poster_path": "/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
        "backdrop_path": "/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg",
        "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea.",
        "providers": {
            "flatrate": [
                {"provider_name": "JioCinema", "logo_class": "jiocinema", "url": "https://www.jiocinema.com/search/Inception"},
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Inception"}
            ],
            "free": [],
            "rent": [{"provider_name": "Apple TV", "logo_class": "appletv", "url": "https://tv.apple.com"}]
        }
    },
    {
        "id": 76600,
        "title": "Avatar: The Way of Water",
        "media_type": "movie",
        "year": "2022",
        "language": "English",
        "lang_code": "en",
        "rating": 7.7,
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "poster_path": "/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
        "backdrop_path": "/8rpDcsfLJypbO6vREc0547VKqEv.jpg",
        "overview": "Jake Sully lives with his newfound family formed on the extrasolar moon Pandora. Once a familiar threat returns, Jake must work with Neytiri.",
        "providers": {
            "flatrate": [
                {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": "https://www.hotstar.com/in/explore?search_query=Avatar+Way+of+Water"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 256040,
        "title": "Baahubali: The Beginning",
        "media_type": "movie",
        "year": "2015",
        "language": "Telugu",
        "lang_code": "te",
        "rating": 8.0,
        "genres": ["Action", "Drama", "History"],
        "poster_path": "/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",
        "backdrop_path": "/w71iO4qH00m5C3hH4gD2T9.jpg",
        "overview": "In the kingdom of Mahishmati, a young adventurous man discovers his royal heritage and the heroic legacy of his father.",
        "providers": {
            "flatrate": [
                {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": "https://www.hotstar.com/in/explore?search_query=Baahubali"},
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/search?q=Baahubali"}
            ],
            "free": [
                {"provider_name": "YouTube Movies (Free)", "logo_class": "youtube", "url": "https://www.youtube.com/results?search_query=Baahubali+The+Beginning+movie"}
            ],
            "rent": []
        }
    },
    {
        "id": 350312,
        "title": "Baahubali 2: The Conclusion",
        "media_type": "movie",
        "year": "2017",
        "language": "Telugu",
        "lang_code": "te",
        "rating": 8.2,
        "genres": ["Action", "Drama", "Fantasy"],
        "poster_path": "/21sC2assImQIYCvv84nlRPvLXZt.jpg",
        "backdrop_path": "/350312_backdrop.jpg",
        "overview": "Shiva learns of his heritage as the rightful heir to the throne of Mahishmati and sets out to avenge his father's betrayal.",
        "providers": {
            "flatrate": [
                {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": "https://www.hotstar.com/in/explore?search_query=Baahubali+2"},
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/search?q=Baahubali+2"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 560057,
        "title": "KGF: Chapter 1",
        "media_type": "movie",
        "year": "2018",
        "language": "Kannada",
        "lang_code": "kn",
        "rating": 8.2,
        "genres": ["Action", "Crime", "Drama"],
        "poster_path": "/560057_poster.jpg",
        "backdrop_path": "/560057_backdrop.jpg",
        "overview": "In the 1970s, a fierce rebel rises against brutal oppressors in the gold fields of Kolar, becoming a symbol of hope for the downtrodden.",
        "providers": {
            "flatrate": [
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=KGF+Chapter+1"},
                {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": "https://www.hotstar.com/in/explore?search_query=KGF+Chapter+1"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 585245,
        "title": "KGF: Chapter 2",
        "media_type": "movie",
        "year": "2022",
        "language": "Kannada",
        "lang_code": "kn",
        "rating": 8.3,
        "genres": ["Action", "Crime", "Thriller"],
        "poster_path": "/585245_poster.jpg",
        "backdrop_path": "/585245_backdrop.jpg",
        "overview": "Rocky, now the ruler of the Kolar Gold Fields, must defend his supremacy against fierce foes and the Indian government.",
        "providers": {
            "flatrate": [
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=KGF+Chapter+2"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 872906,
        "title": "Jawan",
        "media_type": "movie",
        "year": "2023",
        "language": "Hindi",
        "lang_code": "hi",
        "rating": 7.5,
        "genres": ["Action", "Thriller"],
        "poster_path": "/jawan_poster.jpg",
        "backdrop_path": "/jawan_backdrop.jpg",
        "overview": "A man driven by a personal vendetta to rectify the wrongs in society while keeping a promise made years ago.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/search?q=Jawan"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 781732,
        "title": "Animal",
        "media_type": "movie",
        "year": "2023",
        "language": "Hindi",
        "lang_code": "hi",
        "rating": 6.8,
        "genres": ["Action", "Crime", "Drama"],
        "poster_path": "/animal_poster.jpg",
        "backdrop_path": "/animal_backdrop.jpg",
        "overview": "A son's obsessive love for his distant father drives him into a dark descent of ferocious violence and destruction.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/search?q=Animal"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 1058694,
        "title": "12th Fail",
        "media_type": "movie",
        "year": "2023",
        "language": "Hindi",
        "lang_code": "hi",
        "rating": 8.9,
        "genres": ["Biography", "Drama"],
        "poster_path": "/12thfail_poster.jpg",
        "backdrop_path": "/12thfail_backdrop.jpg",
        "overview": "Based on the real-life story of IPS Officer Manoj Kumar Sharma, who restarted his academic journey and conquered the UPSC exam.",
        "providers": {
            "flatrate": [
                {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": "https://www.hotstar.com/in/explore?search_query=12th+Fail"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 71446,
        "title": "Money Heist (La Casa de Papel)",
        "media_type": "tv",
        "year": "2017-2021",
        "language": "Spanish",
        "lang_code": "es",
        "rating": 8.2,
        "genres": ["Crime", "Drama", "Thriller"],
        "poster_path": "/reEMJA1uzscCbk5rRgkTaEZXMax.jpg",
        "backdrop_path": "/gG97Mrsv1A39steHb79q999e.jpg",
        "overview": "An unusual group of robbers attempt to carry out the most perfect robbery in Spanish history - stealing 2.4 billion euros from the Royal Mint.",
        "providers": {
            "flatrate": [
                {"provider_name": "Netflix", "logo_class": "netflix", "url": "https://www.netflix.com/title/80192098"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 1399,
        "title": "Game of Thrones",
        "media_type": "tv",
        "year": "2011-2019",
        "language": "English",
        "lang_code": "en",
        "rating": 8.4,
        "genres": ["Drama", "Action", "Adventure"],
        "poster_path": "/1XS1oqL89opfnbLl8WnZY1O1uJx.jpg",
        "backdrop_path": "/suopoADq0k8YZr4dQXcU6p9bNa4.jpg",
        "overview": "Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.",
        "providers": {
            "flatrate": [
                {"provider_name": "JioCinema", "logo_class": "jiocinema", "url": "https://www.jiocinema.com/search/Game%20of%20Thrones"}
            ],
            "free": [],
            "rent": []
        }
    },
    {
        "id": 76479,
        "title": "The Boys",
        "media_type": "tv",
        "year": "2019-2024",
        "language": "English",
        "lang_code": "en",
        "rating": 8.7,
        "genres": ["Action", "Comedy", "Drama"],
        "poster_path": "/2ZmGngR9ZtWkHcxnuF2n0qg5K5L.jpg",
        "backdrop_path": "/mGVrXeIqi8g1v4aL0R2bL.jpg",
        "overview": "A fun and irreverent take on what happens when superheroes—who are as popular as celebrities—abuse their superpowers rather than use them for good.",
        "providers": {
            "flatrate": [
                {"provider_name": "Amazon Prime Video", "logo_class": "amazon", "url": "https://www.primevideo.com/detail/0K48V7W9M3Z1Q3X2N5V6P7"}
            ],
            "free": [],
            "rent": []
        }
    }
]

import urllib.parse

def search_curated(query: str, platform: str = "All", language: str = "All"):
    """Filters the curated movie collection by search query, platform, and language."""
    query_lower = query.strip().lower()
    results = []
    
    if query_lower:
        for item in CURATED_MOVIES:
            # Match title or overview
            matches_query = query_lower in item["title"].lower() or query_lower in item["overview"].lower()
            if not matches_query:
                continue
                
            # Match language
            if language != "All" and item.get("language") != language:
                continue
                
            # Match platform
            if platform != "All":
                all_providers = []
                for p_list in item["providers"].values():
                    for p in p_list:
                        all_providers.append(p["provider_name"].lower())
                
                p_target = platform.lower()
                if not any(p_target in prov for prov in all_providers):
                    continue
                    
            results.append(item)
            
    # If no exact match found in curated list but user typed a query,
    # generate an instant direct OTT finder card so the user is NEVER left with a blank result!
    if not results and query_lower:
        clean_title = query.strip().title()
        enc_title = urllib.parse.quote_plus(query.strip())
        results.append({
            "id": abs(hash(query_lower)) % 999999,
            "title": clean_title,
            "media_type": "movie",
            "year": "2024",
            "language": "All Languages",
            "lang_code": "all",
            "rating": 8.0,
            "genres": ["Universal Search", "Multi-OTT"],
            "poster_path": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=500&auto=format&fit=crop&q=80",
            "backdrop_path": None,
            "overview": f"Directly open and watch '{clean_title}' across all top streaming platforms in India (Netflix, Prime Video, Disney+ Hotstar, ZEE5, JioCinema, SonyLIV, Aha, and YouTube).",
            "providers": {
                "flatrate": [
                    {"provider_name": "Netflix", "logo_class": "netflix", "url": f"https://www.netflix.com/search?q={enc_title}"},
                    {"provider_name": "Prime Video", "logo_class": "amazon", "url": f"https://www.primevideo.com/search/ref=atv_nb_sr?phrase={enc_title}"},
                    {"provider_name": "Disney+ Hotstar", "logo_class": "hotstar", "url": f"https://www.hotstar.com/in/explore?search_query={enc_title}"},
                    {"provider_name": "ZEE5", "logo_class": "zee5", "url": f"https://www.zee5.com/search?q={enc_title}"},
                    {"provider_name": "SonyLIV", "logo_class": "sonyliv", "url": f"https://www.sonyliv.com/search/{enc_title}"},
                    {"provider_name": "Aha", "logo_class": "aha", "url": f"https://www.aha.video/search?q={enc_title}"}
                ],
                "free": [
                    {"provider_name": "JioCinema", "logo_class": "jiocinema", "url": f"https://www.jiocinema.com/search/{enc_title}"}
                ],
                "rent": [
                    {"provider_name": "YouTube Movies", "logo_class": "youtube", "url": f"https://www.youtube.com/results?search_query={enc_title}+full+movie"}
                ],
                "justwatch_link": f"https://www.justwatch.com/in/search?q={enc_title}"
            }
        })

    return results
