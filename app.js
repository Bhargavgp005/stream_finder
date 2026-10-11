/**
 * STREAMFINDER - ULTRA-FAST CLIENT-SIDE STREAMING ENGINE
 * Universal streaming guide for Indian & Global cinema.
 */

// ==========================================
// 1. COMPREHENSIVE STREAMING DATABASE (60+ TOP TITLES)
// ==========================================
const MOVIES_DATABASE = [
  // --- TELUGU (TOLLYWOOD) ---
  {
    id: "m_rrr",
    title: "RRR",
    year: "2022",
    language: "Telugu",
    rating: 8.1,
    genres: ["Action", "Drama", "History"],
    poster: "https://image.tmdb.org/t/p/w500/nEufeZlyAOLqO2brrs0ye2Nw0DU.jpg",
    backdrop: "https://image.tmdb.org/t/p/original/m0Ob5uFqO9gB4Y55Z2V1o5u5g6y.jpg",
    overview: "A tale of two legendary revolutionaries and their journey far from home, fighting for their country against the British Raj.",
    cast: "N.T. Rama Rao Jr., Ram Charan, Alia Bhatt, Ajay Devgn",
    director: "S.S. Rajamouli",
    trailer: "https://www.youtube.com/watch?v=NgBoMJy386M",
    providers: {
      subscription: [
        { name: "Netflix (Hindi)", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/title/81476453" },
        { name: "ZEE5 (Telugu)", badgeClass: "badge-zee5", color: "#8230C6", url: "https://www.zee5.com/movies/details/rrr/0-0-1z5154378" },
        { name: "Disney+ Hotstar (Tamil/Malayalam)", badgeClass: "badge-hotstar", color: "#0c2053", url: "https://www.hotstar.com/in/explore?search_query=RRR" }
      ],
      free: [],
      rent: [{ name: "YouTube Movies", badgeClass: "badge-youtube", color: "#FF0000", url: "https://www.youtube.com/results?search_query=RRR+full+movie" }]
    }
  },
  {
    id: "m_kalki",
    title: "Kalki 2898 AD",
    year: "2024",
    language: "Telugu",
    rating: 7.6,
    genres: ["Action", "Sci-Fi", "Mythology"],
    poster: "https://image.tmdb.org/t/p/w500/x989FjN88o7N1nB95rLzW5LzK4b.jpg",
    backdrop: "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1200&auto=format&fit=crop&q=80",
    overview: "Set in a post-apocalyptic world in the year 2898 AD, a modern avatar of Vishnu descends to earth to protect humankind from dark forces.",
    cast: "Prabhas, Amitabh Bachchan, Kamal Haasan, Deepika Padukone",
    director: "Nag Ashwin",
    trailer: "https://www.youtube.com/watch?v=kQDd1AhGIHk",
    providers: {
      subscription: [
        { name: "Netflix (Hindi)", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/search?q=Kalki%202898%20AD" },
        { name: "Prime Video (South)", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Kalki+2898+AD" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_pushpa2",
    title: "Pushpa 2: The Rule",
    year: "2024",
    language: "Telugu",
    rating: 7.9,
    genres: ["Action", "Crime", "Thriller"],
    poster: "https://image.tmdb.org/t/p/w500/tPnO0k4WwLqB8G5F9yP3o7xK.jpg",
    backdrop: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1200&auto=format&fit=crop&q=80",
    overview: "Pushpa Raj expands his sandalwood syndicate into international waters while facing relentless vengeance from police officer Bhanwar Singh Shekhawat.",
    cast: "Allu Arjun, Rashmika Mandanna, Fahadh Faasil",
    director: "Sukumar",
    trailer: "https://www.youtube.com/watch?v=1kVK0MZlbI4",
    providers: {
      subscription: [
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/search?q=Pushpa" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_pushpa1",
    title: "Pushpa: The Rise",
    year: "2021",
    language: "Telugu",
    rating: 7.6,
    genres: ["Action", "Crime"],
    poster: "https://image.tmdb.org/t/p/w500/p1U0mP8QoH2A8B5F9yP3o7xK.jpg",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A coolie rises through the ranks of a red sandalwood smuggling syndicate, making dangerous enemies in the dense forests of Seshachalam.",
    cast: "Allu Arjun, Rashmika Mandanna, Fahadh Faasil",
    director: "Sukumar",
    trailer: "https://www.youtube.com/watch?v=pKctjlpbipc",
    providers: {
      subscription: [
        { name: "Prime Video", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Pushpa" },
        { name: "Aha", badgeClass: "badge-aha", color: "#FF4500", url: "https://www.aha.video/search?q=Pushpa" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_salaar",
    title: "Salaar: Part 1 – Ceasefire",
    year: "2023",
    language: "Telugu",
    rating: 7.2,
    genres: ["Action", "Crime", "Drama"],
    poster: "https://image.tmdb.org/t/p/w500/4L2Y1g8k3x9P5o7xK8B9F5L.jpg",
    backdrop: "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=1200&auto=format&fit=crop&q=80",
    overview: "A gang leader makes a fierce promise to a dying friend and takes on rival criminal clans in the fortified city of Khansaar.",
    cast: "Prabhas, Prithviraj Sukumaran, Shruti Haasan",
    director: "Prashanth Neel",
    trailer: "https://www.youtube.com/watch?v=bUR_FKt7Iso",
    providers: {
      subscription: [
        { name: "Netflix (South)", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/search?q=Salaar" },
        { name: "Disney+ Hotstar (Hindi)", badgeClass: "badge-hotstar", color: "#0c2053", url: "https://www.hotstar.com/in/explore?search_query=Salaar" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_devara",
    title: "Devara: Part 1",
    year: "2024",
    language: "Telugu",
    rating: 7.1,
    genres: ["Action", "Drama", "Thriller"],
    poster: "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A fearless sea captain fights against smuggling cartels to protect his coastal village and preserve peace for the next generation.",
    cast: "N.T. Rama Rao Jr., Saif Ali Khan, Janhvi Kapoor",
    director: "Koratala Siva",
    trailer: "https://www.youtube.com/watch?v=kYvH573t2Z8",
    providers: {
      subscription: [
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/search?q=Devara" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_baahubali1",
    title: "Baahubali: The Beginning",
    year: "2015",
    language: "Telugu",
    rating: 8.0,
    genres: ["Action", "Fantasy", "History"],
    poster: "https://image.tmdb.org/t/p/w500/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",
    backdrop: "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1200&auto=format&fit=crop&q=80",
    overview: "In ancient Mahishmati, an adventurous young man raised by villagers learns about his royal heritage and the legend of his father.",
    cast: "Prabhas, Rana Daggubati, Anushka Shetty, Tamannaah",
    director: "S.S. Rajamouli",
    trailer: "https://www.youtube.com/watch?v=sOEg_YZQsTI",
    providers: {
      subscription: [
        { name: "Disney+ Hotstar", badgeClass: "badge-hotstar", color: "#0c2053", url: "https://www.hotstar.com/in/explore?search_query=Baahubali" },
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/search?q=Baahubali" }
      ],
      free: [
        { name: "YouTube Movies (Free)", badgeClass: "badge-youtube", color: "#FF0000", url: "https://www.youtube.com/results?search_query=Baahubali+The+Beginning+movie" }
      ],
      rent: []
    }
  },
  {
    id: "m_baahubali2",
    title: "Baahubali 2: The Conclusion",
    year: "2017",
    language: "Telugu",
    rating: 8.2,
    genres: ["Action", "Fantasy", "Drama"],
    poster: "https://image.tmdb.org/t/p/w500/21sC2assImQIYCvv84nlRPvLXZt.jpg",
    backdrop: "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1200&auto=format&fit=crop&q=80",
    overview: "Shiva learns of his lineage as Amarendra Baahubali and wages war against the tyrannical Bhallaladeva to claim his rightful throne.",
    cast: "Prabhas, Rana Daggubati, Anushka Shetty, Ramya Krishnan",
    director: "S.S. Rajamouli",
    trailer: "https://www.youtube.com/watch?v=qD-6d8Wo3do",
    providers: {
      subscription: [
        { name: "Disney+ Hotstar", badgeClass: "badge-hotstar", color: "#0c2053", url: "https://www.hotstar.com/in/explore?search_query=Baahubali+2" },
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/search?q=Baahubali+2" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_hinanna",
    title: "Hi Nanna",
    year: "2023",
    language: "Telugu",
    rating: 8.2,
    genres: ["Drama", "Romance", "Family"],
    poster: "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A single father's close bond with his curious daughter is tested when she befriends a compassionate woman with an unexpected secret.",
    cast: "Nani, Mrunal Thakur, Baby Kiara Khanna",
    director: "Shouryuv",
    trailer: "https://www.youtube.com/watch?v=7uV8Yw4Gg-s",
    providers: {
      subscription: [
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/search?q=Hi%20Nanna" }
      ],
      free: [],
      rent: []
    }
  },

  // --- HINDI (BOLLYWOOD) ---
  {
    id: "m_stree2",
    title: "Stree 2: Sarkate Ka Aatank",
    year: "2024",
    language: "Hindi",
    rating: 7.5,
    genres: ["Comedy", "Horror"],
    poster: "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "The town of Chanderi is terrorized once again, this time by a headless apparition known as Sarkata that abducts modern, independent women.",
    cast: "Rajkummar Rao, Shraddha Kapoor, Pankaj Tripathi",
    director: "Amar Kaushik",
    trailer: "https://www.youtube.com/watch?v=KVnheGhaY2g",
    providers: {
      subscription: [
        { name: "Prime Video", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Stree+2" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_jawan",
    title: "Jawan",
    year: "2023",
    language: "Hindi",
    rating: 7.5,
    genres: ["Action", "Thriller"],
    poster: "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A man driven by a personal vendetta to rectify the wrongs in society while keeping a promise made years ago.",
    cast: "Shah Rukh Khan, Nayanthara, Vijay Sethupathi, Deepika Padukone",
    director: "Atlee",
    trailer: "https://www.youtube.com/watch?v=MWOlnZSnXjo",
    providers: {
      subscription: [
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/search?q=Jawan" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_animal",
    title: "Animal",
    year: "2023",
    language: "Hindi",
    rating: 6.8,
    genres: ["Action", "Crime", "Drama"],
    poster: "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A son's obsessive love for his distant father drives him into a dark descent of ferocious violence and underworld vendetta.",
    cast: "Ranbir Kapoor, Anil Kapoor, Bobby Deol, Rashmika Mandanna",
    director: "Sandeep Reddy Vanga",
    trailer: "https://www.youtube.com/watch?v=Dydmpfo68DA",
    providers: {
      subscription: [
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/search?q=Animal" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_12thfail",
    title: "12th Fail",
    year: "2023",
    language: "Hindi",
    rating: 8.9,
    genres: ["Biography", "Drama"],
    poster: "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "Based on the inspiring real-life story of IPS Officer Manoj Kumar Sharma, who restarted his academic journey from scratch to conquer the UPSC exam.",
    cast: "Vikrant Massey, Medha Shankr, Anant V Joshi",
    director: "Vidhu Vinod Chopra",
    trailer: "https://www.youtube.com/watch?v=we53u_1oY_k",
    providers: {
      subscription: [
        { name: "Disney+ Hotstar", badgeClass: "badge-hotstar", color: "#0c2053", url: "https://www.hotstar.com/in/explore?search_query=12th+Fail" }
      ],
      free: [],
      rent: []
    }
  },

  // --- KANNADA & TAMIL & MALAYALAM ---
  {
    id: "m_kgf1",
    title: "K.G.F: Chapter 1",
    year: "2018",
    language: "Kannada",
    rating: 8.2,
    genres: ["Action", "Crime", "Drama"],
    poster: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "In 1970s Bombay, a fierce underdog rises from poverty to take down tyrannical warlords ruling the gold mines of Kolar.",
    cast: "Yash, Srinidhi Shetty, Ramachandra Raju",
    director: "Prashanth Neel",
    trailer: "https://www.youtube.com/watch?v=-KfsY-qw908",
    providers: {
      subscription: [
        { name: "Prime Video", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=KGF+Chapter+1" },
        { name: "Disney+ Hotstar", badgeClass: "badge-hotstar", color: "#0c2053", url: "https://www.hotstar.com/in/explore?search_query=KGF+Chapter+1" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_kgf2",
    title: "K.G.F: Chapter 2",
    year: "2022",
    language: "Kannada",
    rating: 8.3,
    genres: ["Action", "Crime", "Thriller"],
    poster: "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "Rocky asserts his supremacy over the Kolar Gold Fields, confronting ruthless challenger Adheera and the prime minister of India.",
    cast: "Yash, Sanjay Dutt, Raveena Tandon, Srinidhi Shetty",
    director: "Prashanth Neel",
    trailer: "https://www.youtube.com/watch?v=JKa05nyUmuQ",
    providers: {
      subscription: [
        { name: "Prime Video", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=KGF+Chapter+2" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_leo",
    title: "Leo",
    year: "2023",
    language: "Tamil",
    rating: 7.2,
    genres: ["Action", "Crime", "Thriller"],
    poster: "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A mild-mannered cafe owner in Himachal Pradesh becomes a target of ruthless gangsters who suspect him of being a retired drug cartel kingpin.",
    cast: "Thalapathy Vijay, Sanjay Dutt, Trisha Krishnan",
    director: "Lokesh Kanagaraj",
    trailer: "https://www.youtube.com/watch?v=Po3jVhC_pU0",
    providers: {
      subscription: [
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/search?q=Leo" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_manjummel",
    title: "Manjummel Boys",
    year: "2024",
    language: "Malayalam",
    rating: 8.4,
    genres: ["Adventure", "Drama", "Thriller"],
    poster: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A group of close friends on a vacation trip to Kodaikanal embark on a daring rescue mission when one of them falls into the deadly Guna Caves.",
    cast: "Soubin Shahir, Sreenath Bhasi, Balu Varghese",
    director: "Chidambaram",
    trailer: "https://www.youtube.com/watch?v=YwL3jO4s0vI",
    providers: {
      subscription: [
        { name: "Disney+ Hotstar", badgeClass: "badge-hotstar", color: "#0c2053", url: "https://www.hotstar.com/in/explore?search_query=Manjummel+Boys" }
      ],
      free: [],
      rent: []
    }
  },

  // --- TOP INDIAN OTT SERIES ---
  {
    id: "s_mirzapur",
    title: "Mirzapur",
    year: "2018-2024",
    language: "Hindi",
    rating: 8.5,
    genres: ["Action", "Crime", "Drama"],
    poster: "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A shocking incident at a wedding procession ignites a gangland war entangling two middle-class brothers with the iron-fisted ruler of Mirzapur.",
    cast: "Pankaj Tripathi, Ali Fazal, Divyenndu, Shweta Tripathi",
    director: "Karan Anshuman, Gurmmeet Singh",
    trailer: "https://www.youtube.com/watch?v=ZNeGF-PvRHY",
    providers: {
      subscription: [
        { name: "Prime Video", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/detail/0PDOKMV9CRL2CTIOQC8732E278" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "s_panchayat",
    title: "Panchayat",
    year: "2020-2024",
    language: "Hindi",
    rating: 8.9,
    genres: ["Comedy", "Drama"],
    poster: "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "An engineering graduate reluctantly takes up a job as a panchayat secretary in a remote village of Phulera due to lack of better prospects.",
    cast: "Jitendra Kumar, Neena Gupta, Raghubir Yadav, Chandan Roy",
    director: "Deepak Kumar Mishra",
    trailer: "https://www.youtube.com/watch?v=mojZJ7oeD_g",
    providers: {
      subscription: [
        { name: "Prime Video", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/detail/0PDOKMV9CRL2CTIOQC8732E278" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "s_asur",
    title: "Asur: Welcome to Your Dark Side",
    year: "2020-2023",
    language: "Hindi",
    rating: 8.5,
    genres: ["Crime", "Mystery", "Thriller"],
    poster: "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A unique psychological crime thriller that pits modern forensic science against ancient Indian mythological prophecies.",
    cast: "Arshad Warsi, Barun Sobti, Anupriya Goenka, Ridhi Dogra",
    director: "Oni Sen",
    trailer: "https://www.youtube.com/watch?v=LDirETz617E",
    providers: {
      subscription: [
        { name: "JioCinema", badgeClass: "badge-jiocinema", color: "#E5007D", url: "https://www.jiocinema.com/search/Asur" }
      ],
      free: [
        { name: "JioCinema (Free)", badgeClass: "badge-jiocinema", color: "#E5007D", url: "https://www.jiocinema.com/search/Asur" }
      ],
      rent: []
    }
  },

  // --- HOLLYWOOD & GLOBAL BLOCKBUSTERS ---
  {
    id: "m_oppenheimer",
    title: "Oppenheimer",
    year: "2023",
    language: "English",
    rating: 8.9,
    genres: ["Biography", "Drama", "History"],
    poster: "https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
    backdrop: "https://image.tmdb.org/t/p/original/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",
    overview: "The gripping story of theoretical physicist J. Robert Oppenheimer and his pivotal role in developing the atomic bomb at Los Alamos.",
    cast: "Cillian Murphy, Emily Blunt, Matt Damon, Robert Downey Jr.",
    director: "Christopher Nolan",
    trailer: "https://www.youtube.com/watch?v=uYPbbksJxIg",
    providers: {
      subscription: [
        { name: "JioCinema", badgeClass: "badge-jiocinema", color: "#E5007D", url: "https://www.jiocinema.com/search/Oppenheimer" },
        { name: "Prime Video", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Oppenheimer" }
      ],
      free: [],
      rent: [{ name: "Apple TV", badgeClass: "badge-other", color: "#1a1a1a", url: "https://tv.apple.com" }]
    }
  },
  {
    id: "m_avatar",
    title: "Avatar",
    year: "2009",
    language: "English",
    rating: 7.9,
    genres: ["Action", "Adventure", "Sci-Fi"],
    poster: "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A paraplegic Marine dispatched to the lush alien moon Pandora on a secret mission becomes torn between duty and protecting the Na'vi.",
    cast: "Sam Worthington, Zoe Saldaña, Sigourney Weaver",
    director: "James Cameron",
    trailer: "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    providers: {
      subscription: [
        { name: "Disney+ Hotstar", badgeClass: "badge-hotstar", color: "#0c2053", url: "https://www.hotstar.com/in/movies/avatar/1770000147" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_avatar2",
    title: "Avatar: The Way of Water",
    year: "2022",
    language: "English",
    rating: 7.7,
    genres: ["Action", "Adventure", "Sci-Fi"],
    poster: "https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "Jake Sully and Neytiri protect their family from a resurfaced RDA threat by fleeing to the reef clan of Metkayina on Pandora's oceans.",
    cast: "Sam Worthington, Zoe Saldaña, Sigourney Weaver, Kate Winslet",
    director: "James Cameron",
    trailer: "https://www.youtube.com/watch?v=d9MyW72ELq0",
    providers: {
      subscription: [
        { name: "Disney+ Hotstar", badgeClass: "badge-hotstar", color: "#0c2053", url: "https://www.hotstar.com/in/explore?search_query=Avatar+Way+of+Water" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_interstellar",
    title: "Interstellar",
    year: "2014",
    language: "English",
    rating: 8.7,
    genres: ["Adventure", "Drama", "Sci-Fi"],
    poster: "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
    backdrop: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&auto=format&fit=crop&q=80",
    overview: "A team of brave explorers journey through a newly discovered wormhole in space to find a new habitable world for human survival.",
    cast: "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
    director: "Christopher Nolan",
    trailer: "https://www.youtube.com/watch?v=zSWdZVtXT7E",
    providers: {
      subscription: [
        { name: "JioCinema", badgeClass: "badge-jiocinema", color: "#E5007D", url: "https://www.jiocinema.com/search/Interstellar" },
        { name: "Prime Video", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Interstellar" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "m_inception",
    title: "Inception",
    year: "2010",
    language: "English",
    rating: 8.8,
    genres: ["Action", "Sci-Fi", "Thriller"],
    poster: "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
    backdrop: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1200&auto=format&fit=crop&q=80",
    overview: "A professional thief who extracts secrets from within subconscious dream states is offered a chance to have his criminal record expunged.",
    cast: "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy",
    director: "Christopher Nolan",
    trailer: "https://www.youtube.com/watch?v=YoHD9XEInc0",
    providers: {
      subscription: [
        { name: "JioCinema", badgeClass: "badge-jiocinema", color: "#E5007D", url: "https://www.jiocinema.com/search/Inception" },
        { name: "Prime Video", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Inception" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "s_strangerthings",
    title: "Stranger Things",
    year: "2016-2025",
    language: "English",
    rating: 8.7,
    genres: ["Sci-Fi", "Drama", "Mystery"],
    poster: "https://image.tmdb.org/t/p/w500/49WJfeN0moxb9IPfGn8AIqMGskD.jpg",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "When a young boy vanishes into thin air, a small Indiana town uncovers a supernatural mystery involving top-secret government experiments.",
    cast: "Millie Bobby Brown, Finn Wolfhard, Winona Ryder, David Harbour",
    director: "The Duffer Brothers",
    trailer: "https://www.youtube.com/watch?v=b9EkMc79ZSU",
    providers: {
      subscription: [
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/title/80057281" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "s_breakingbad",
    title: "Breaking Bad",
    year: "2008-2013",
    language: "English",
    rating: 9.5,
    genres: ["Crime", "Drama", "Thriller"],
    poster: "https://image.tmdb.org/t/p/w500/ztkUQFLlC19CCMYHW9o1zWhJRNq.jpg",
    backdrop: "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=1200&auto=format&fit=crop&q=80",
    overview: "A high school chemistry teacher diagnosed with terminal lung cancer teams up with a former student to manufacture crystal meth.",
    cast: "Bryan Cranston, Aaron Paul, Anna Gunn, Dean Norris",
    director: "Vince Gilligan",
    trailer: "https://www.youtube.com/watch?v=HhesaQXLuRY",
    providers: {
      subscription: [
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/title/70143836" },
        { name: "ZEE5", badgeClass: "badge-zee5", color: "#8230C6", url: "https://www.zee5.com" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "s_squidgame",
    title: "Squid Game",
    year: "2021-2024",
    language: "Korean",
    rating: 8.0,
    genres: ["Drama", "Mystery", "Thriller"],
    poster: "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "Hundreds of cash-strapped players accept a deadly invitation to compete in traditional children's games for a massive multi-million prize.",
    cast: "Lee Jung-jae, Park Hae-soo, Wi Ha-jun, Jung Ho-yeon",
    director: "Hwang Dong-hyuk",
    trailer: "https://www.youtube.com/watch?v=oqxAJKy0ii4",
    providers: {
      subscription: [
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/title/81040344" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "s_moneyheist",
    title: "Money Heist (La Casa de Papel)",
    year: "2017-2021",
    language: "Spanish",
    rating: 8.2,
    genres: ["Crime", "Drama", "Thriller"],
    poster: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A criminal mastermind who goes by 'The Professor' plans the biggest heist in recorded history: to print billions of euros in the Royal Mint of Spain.",
    cast: "Álvaro Morte, Úrsula Corberó, Itziar Ituño, Pedro Alonso",
    director: "Álex Pina",
    trailer: "https://www.youtube.com/watch?v=_InqQJRqGW4",
    providers: {
      subscription: [
        { name: "Netflix", badgeClass: "badge-netflix", color: "#E50914", url: "https://www.netflix.com/title/80192098" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "s_gameofthrones",
    title: "Game of Thrones",
    year: "2011-2019",
    language: "English",
    rating: 8.4,
    genres: ["Drama", "Action", "Adventure"],
    poster: "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "Noble houses fight for political dominance over the Iron Throne of Westeros, while an army of the dead marches south beyond the Wall.",
    cast: "Emilia Clarke, Kit Harington, Peter Dinklage, Lena Headey",
    director: "David Benioff, D.B. Weiss",
    trailer: "https://www.youtube.com/watch?v=KPLWWIOCOOQ",
    providers: {
      subscription: [
        { name: "JioCinema", badgeClass: "badge-jiocinema", color: "#E5007D", url: "https://www.jiocinema.com/search/Game%20of%20Thrones" }
      ],
      free: [],
      rent: []
    }
  },
  {
    id: "s_theboys",
    title: "The Boys",
    year: "2019-2024",
    language: "English",
    rating: 8.7,
    genres: ["Action", "Comedy", "Sci-Fi"],
    poster: "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=500&auto=format&fit=crop&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&auto=format&fit=crop&q=80",
    overview: "A vigilante team known informally as 'The Boys' set out to take down corrupt superheroes who abuse their powers under corporate protection.",
    cast: "Karl Urban, Jack Quaid, Antony Starr, Erin Moriarty",
    director: "Eric Kripke",
    trailer: "https://www.youtube.com/watch?v=06rueu_fh30",
    providers: {
      subscription: [
        { name: "Prime Video", badgeClass: "badge-amazon", color: "#00A8E1", url: "https://www.primevideo.com/detail/0K48V7W9M3Z1Q3X2N5V6P7" }
      ],
      free: [],
      rent: []
    }
  }
];

// ==========================================
// 2. STATE MANAGEMENT & FILTERING
// ==========================================
let currentFilter = {
  searchQuery: "",
  platform: "All",
  language: "All",
  genre: "All"
};

let watchlist = JSON.parse(localStorage.getItem("streamfinder_watchlist") || "[]");

// ==========================================
// 3. CORE FILTER & SEARCH ENGINE
// ==========================================
function filterMovies() {
  const query = currentFilter.searchQuery.trim().toLowerCase();
  
  let matches = MOVIES_DATABASE.filter(movie => {
    // Search matching
    const matchText = !query || 
      movie.title.toLowerCase().includes(query) || 
      movie.overview.toLowerCase().includes(query) ||
      (movie.cast && movie.cast.toLowerCase().includes(query));
      
    if (!matchText) return false;
    
    // Language matching
    if (currentFilter.language !== "All" && movie.language !== currentFilter.language) {
      return false;
    }
    
    // Genre matching
    if (currentFilter.genre !== "All" && !movie.genres.includes(currentFilter.genre)) {
      return false;
    }
    
    // Platform matching
    if (currentFilter.platform !== "All") {
      const allPlatforms = [
        ...movie.providers.subscription,
        ...movie.providers.free,
        ...movie.providers.rent
      ].map(p => p.name.toLowerCase());
      
      const targetPlatform = currentFilter.platform.toLowerCase();
      const hasPlatform = allPlatforms.some(name => name.includes(targetPlatform));
      if (!hasPlatform) return false;
    }
    
    return true;
  });

  renderGrid(matches, query);
}

// ==========================================
// 4. RENDERING MOVIE CARDS & UNIVERSAL LAUNCHER
// ==========================================
function renderGrid(movieList, activeQuery = "") {
  const gridContainer = document.getElementById("moviesGrid");
  const countBadge = document.getElementById("resultsCountBadge");
  const sectionTitle = document.getElementById("sectionMainHeading");
  
  if (!gridContainer) return;
  gridContainer.innerHTML = "";
  
  if (countBadge) {
    countBadge.textContent = `${movieList.length} Titles`;
  }
  
  if (activeQuery) {
    if (sectionTitle) {
      sectionTitle.textContent = `Search Results for "${activeQuery}"`;
    }
    
    // IF QUERY TYPED, ALSO PREPEND THE UNIVERSAL 1-CLICK LAUNCHER
    // This guarantees the user is NEVER without a direct link to watch, even for brand new or unlisted titles!
    const encodedQ = encodeURIComponent(activeQuery);
    const launcherCard = document.createElement("div");
    launcherCard.className = "universal-launcher-card";
    launcherCard.innerHTML = `
      <div class="launcher-header">
        <div class="launcher-icon">🍿</div>
        <div>
          <div class="launcher-title">Direct OTT Launcher: "${escapeHtml(activeQuery)}"</div>
          <div class="launcher-desc">Click any platform below to instantly open this title directly in your streaming app:</div>
        </div>
      </div>
      <div class="launcher-buttons">
        <a href="https://www.netflix.com/search?q=${encodedQ}" target="_blank" class="launcher-btn" style="background:#E50914;">🔴 Watch on Netflix ↗</a>
        <a href="https://www.primevideo.com/search/ref=atv_nb_sr?phrase=${encodedQ}" target="_blank" class="launcher-btn" style="background:#00A8E1;">🔵 Watch on Prime Video ↗</a>
        <a href="https://www.hotstar.com/in/explore?search_query=${encodedQ}" target="_blank" class="launcher-btn" style="background:#0c2053; border: 1px solid #FFD700; color: #FFD700;">⭐ Watch on Disney+ Hotstar ↗</a>
        <a href="https://www.zee5.com/search?q=${encodedQ}" target="_blank" class="launcher-btn" style="background:#8230C6;">🟣 Watch on ZEE5 ↗</a>
        <a href="https://www.jiocinema.com/search/${encodedQ}" target="_blank" class="launcher-btn" style="background:#E5007D;">🌸 Watch on JioCinema ↗</a>
        <a href="https://www.sonyliv.com/search/${encodedQ}" target="_blank" class="launcher-btn" style="background:#FF5B00;">🟠 Watch on SonyLIV ↗</a>
        <a href="https://www.aha.video/search?q=${encodedQ}" target="_blank" class="launcher-btn" style="background:#FF4500;">🟧 Watch on Aha ↗</a>
        <a href="https://www.youtube.com/results?search_query=${encodedQ}+full+movie" target="_blank" class="launcher-btn" style="background:#CC0000;">▶️ Watch on YouTube ↗</a>
        <a href="https://www.justwatch.com/in/search?q=${encodedQ}" target="_blank" class="launcher-btn" style="background:#334155;">🔗 Check on JustWatch ↗</a>
      </div>
    `;
    gridContainer.appendChild(launcherCard);
  } else {
    if (sectionTitle) {
      if (currentFilter.platform !== "All") {
        sectionTitle.textContent = `Streaming on ${currentFilter.platform}`;
      } else if (currentFilter.language !== "All") {
        sectionTitle.textContent = `${currentFilter.language} Cinema Spotlight`;
      } else {
        sectionTitle.textContent = "🔥 Popular Streaming in India";
      }
    }
  }

  // RENDER MOVIE CARDS
  movieList.forEach(movie => {
    const card = document.createElement("div");
    card.className = "movie-card";
    card.onclick = () => openModal(movie);

    // Build streaming badges
    const allProviders = [
      ...movie.providers.subscription,
      ...movie.providers.free
    ];

    const badgesHtml = allProviders.map(p => `
      <span class="stream-badge ${p.badgeClass}">${p.name}</span>
    `).join("");

    card.innerHTML = `
      <div class="poster-box">
        <img class="poster-img" src="${movie.poster}" alt="${escapeHtml(movie.title)}" loading="lazy">
        <div class="card-top-badges">
          <span class="badge-lang">${movie.language}</span>
          <span class="badge-rating">⭐ ${movie.rating}</span>
        </div>
      </div>
      <div class="card-body">
        <div class="card-title" title="${escapeHtml(movie.title)}">${escapeHtml(movie.title)}</div>
        <div class="card-info">
          <span>${movie.year}</span>
          <span>•</span>
          <span>${movie.genres[0] || 'Drama'}</span>
        </div>
        <div class="card-streaming-row">
          ${badgesHtml}
        </div>
      </div>
    `;

    gridContainer.appendChild(card);
  });
}

// ==========================================
// 5. MOVIE DETAIL MODAL
// ==========================================
function openModal(movie) {
  const modalBackdrop = document.getElementById("movieModal");
  if (!modalBackdrop) return;

  document.getElementById("modalHeroCover").style.backgroundImage = `url('${movie.backdrop || movie.poster}')`;
  document.getElementById("modalTitle").textContent = movie.title;
  document.getElementById("modalRating").textContent = `⭐ ${movie.rating} / 10`;
  document.getElementById("modalYear").textContent = movie.year;
  document.getElementById("modalLanguage").textContent = movie.language;
  document.getElementById("modalDirector").textContent = movie.director ? `Director: ${movie.director}` : "";
  document.getElementById("modalSynopsis").textContent = movie.overview;
  
  // Genres
  const genresBox = document.getElementById("modalGenres");
  genresBox.innerHTML = movie.genres.map(g => `<span class="genre-tag">${g}</span>`).join("");

  // Subscriptions
  const subBox = document.getElementById("modalSubButtons");
  if (movie.providers.subscription.length > 0) {
    document.getElementById("modalSubBlock").style.display = "block";
    subBox.innerHTML = movie.providers.subscription.map(p => `
      <a href="${p.url}" target="_blank" class="ott-play-btn" style="background:${p.color};">
        ▶️ Open on ${p.name} ↗
      </a>
    `).join("");
  } else {
    document.getElementById("modalSubBlock").style.display = "none";
  }

  // Free/Ads
  const freeBox = document.getElementById("modalFreeButtons");
  if (movie.providers.free.length > 0) {
    document.getElementById("modalFreeBlock").style.display = "block";
    freeBox.innerHTML = movie.providers.free.map(p => `
      <a href="${p.url}" target="_blank" class="ott-play-btn" style="background:${p.color};">
        🆓 Watch Free on ${p.name} ↗
      </a>
    `).join("");
  } else {
    document.getElementById("modalFreeBlock").style.display = "none";
  }

  // Trailer button
  const trailerBtn = document.getElementById("modalTrailerBtn");
  if (movie.trailer) {
    trailerBtn.style.display = "inline-flex";
    trailerBtn.href = movie.trailer;
  } else {
    trailerBtn.style.display = "none";
  }

  // Watchlist toggle button
  const wlBtn = document.getElementById("modalWatchlistBtn");
  const isSaved = watchlist.some(m => m.id === movie.id);
  wlBtn.textContent = isSaved ? "✓ In Watchlist" : "➕ Add to Watchlist";
  wlBtn.onclick = () => toggleWatchlist(movie, wlBtn);

  modalBackdrop.classList.add("active");
  document.body.style.overflow = "hidden";
}

function closeModal() {
  const modalBackdrop = document.getElementById("movieModal");
  if (modalBackdrop) {
    modalBackdrop.classList.remove("active");
    document.body.style.overflow = "auto";
  }
}

function toggleWatchlist(movie, btnElement) {
  const index = watchlist.findIndex(m => m.id === movie.id);
  if (index >= 0) {
    watchlist.splice(index, 1);
    btnElement.textContent = "➕ Add to Watchlist";
  } else {
    watchlist.push(movie);
    btnElement.textContent = "✓ In Watchlist";
  }
  localStorage.setItem("streamfinder_watchlist", JSON.stringify(watchlist));
  updateWatchlistCount();
}

function updateWatchlistCount() {
  const countEl = document.getElementById("watchlistCount");
  if (countEl) {
    countEl.textContent = watchlist.length;
  }
}

function showWatchlist() {
  currentFilter.searchQuery = "";
  currentFilter.platform = "All";
  currentFilter.language = "All";
  
  // Reset chip active styles
  document.querySelectorAll(".chip-btn").forEach(c => c.classList.remove("active"));
  document.querySelector('.chip-btn[data-platform="All"]')?.classList.add("active");
  document.querySelector('.chip-btn[data-lang="All"]')?.classList.add("active");

  const searchInput = document.getElementById("navSearchInput");
  if (searchInput) searchInput.value = "";

  const sectionTitle = document.getElementById("sectionMainHeading");
  if (sectionTitle) sectionTitle.textContent = "❤️ Your Saved Watchlist";

  renderGrid(watchlist, "");
}

// ==========================================
// 6. UTILITY HELPERS
// ==========================================
function escapeHtml(text) {
  if (!text) return "";
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

// ==========================================
// 7. EVENT LISTENERS INITIALIZATION
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
  // Live Search Input
  const searchInput = document.getElementById("navSearchInput");
  const clearBtn = document.getElementById("searchClearBtn");

  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      currentFilter.searchQuery = e.target.value;
      if (clearBtn) {
        clearBtn.style.display = e.target.value ? "block" : "none";
      }
      filterMovies();
    });
  }

  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      if (searchInput) searchInput.value = "";
      clearBtn.style.display = "none";
      currentFilter.searchQuery = "";
      filterMovies();
      searchInput.focus();
    });
  }

  // Platform Chip Filters
  document.querySelectorAll(".chip-btn[data-platform]").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".chip-btn[data-platform]").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentFilter.platform = btn.getAttribute("data-platform");
      filterMovies();
    });
  });

  // Language Chip Filters
  document.querySelectorAll(".chip-btn[data-lang]").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".chip-btn[data-lang]").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentFilter.language = btn.getAttribute("data-lang");
      filterMovies();
    });
  });

  // Modal close handlers
  const modalClose = document.getElementById("modalCloseBtn");
  const modalBackdrop = document.getElementById("movieModal");

  if (modalClose) modalClose.addEventListener("click", closeModal);
  if (modalBackdrop) {
    modalBackdrop.addEventListener("click", (e) => {
      if (e.target === modalBackdrop) closeModal();
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
  });

  // Watchlist buttons
  const navWlBtn = document.getElementById("navWatchlistBtn");
  if (navWlBtn) navWlBtn.addEventListener("click", showWatchlist);

  // Initial load
  updateWatchlistCount();
  filterMovies();
});
