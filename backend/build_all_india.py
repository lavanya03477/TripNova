# -*- coding: utf-8 -*-
import json
import os

ALL_INDIA_DB = {
    # TAMIL NADU
    "madurai": {
        "fullName": "Madurai, Tamil Nadu",
        "lat": 9.9252,
        "lng": 78.1198,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "history",
        "budget": "low",
        "summary": "Cultural Capital of Tamil Nadu, famous for the 2,500-year-old Meenakshi Amman Temple and royal palaces.",
        "attractions": [
            {"name": "Meenakshi Amman Temple", "highlight": "Architectural marvel with 14 soaring gopurams and Hall of 1,000 Pillars.", "duration": "3.5 hours", "bestTime": "Morning (6-11 AM) or Evening (5-9 PM)", "lat": 9.9195, "lng": 78.1193},
            {"name": "Thirumalai Nayakkar Mahal", "highlight": "17th-century Indo-Saracenic royal palace with massive pillars and light & sound show.", "duration": "2 hours", "bestTime": "Afternoon / 6:45 PM for Sound & Light show", "lat": 9.9152, "lng": 78.1238},
            {"name": "Gandhi Memorial Museum", "highlight": "Historic museum housing Mahatma Gandhi's blood-stained dhoti and freedom movement gallery.", "duration": "2 hours", "bestTime": "Morning", "lat": 9.9327, "lng": 78.1402},
            {"name": "Alagar Koyil (Alagar Hills)", "highlight": "Ancient temple of Lord Vishnu situated in the lush forest foothills of Alagar Hills.", "duration": "3 hours", "bestTime": "Morning", "lat": 10.0769, "lng": 78.2144},
            {"name": "Vandiyur Mariamman Teppakulam", "highlight": "Huge temple tank with a central mandapam, famous for the float festival.", "duration": "1 hour", "bestTime": "Evening", "lat": 9.9098, "lng": 78.1528},
            {"name": "Madurai Food & Jigarthanda Trail", "highlight": "Taste famous Bun Parotta, Kari Dosa, and Famous Jigarthanda.", "duration": "2 hours", "bestTime": "Evening (7 PM onwards)", "lat": 9.9200, "lng": 78.1220}
        ],
        "hotels": [
            {"name": "Heritage Madurai", "type": "Luxury", "price": "₹7,800/night", "rating": "4.7★"},
            {"name": "Courtyard by Marriott Madurai", "type": "Luxury", "price": "₹6,200/night", "rating": "4.6★"},
            {"name": "The Gateway Hotel Pasumalai", "type": "Mid-range", "price": "₹4,100/night", "rating": "4.5★"},
            {"name": "Hotel Supreme Madurai", "type": "Budget-friendly", "price": "₹1,400/night", "rating": "4.2★"}
        ]
    },
    "ooty": {
        "fullName": "Ooty (Udhagamandalam), Tamil Nadu",
        "lat": 11.4102,
        "lng": 76.6950,
        "region": "Tamil Nadu",
        "climate": "cold",
        "experience": "nature",
        "budget": "medium",
        "summary": "Queen of Nilgiri Hill Stations famous for tea estates, UNESCO toy train, botanical gardens, and Doddabetta Peak.",
        "attractions": [
            {"name": "Nilgiri Mountain Railway (Toy Train)", "highlight": "UNESCO World Heritage steam train journey climbing through Nilgiri tea hills.", "duration": "3 hours", "bestTime": "Morning (9 AM)", "lat": 11.4055, "lng": 76.6975},
            {"name": "Ooty Botanical Gardens & Rose Garden", "highlight": "55-acre sprawling Victorian gardens with fossilized tree trunk and rose varieties.", "duration": "2.5 hours", "bestTime": "Morning / Afternoon", "lat": 11.4172, "lng": 76.7118},
            {"name": "Doddabetta Peak", "highlight": "Highest mountain peak in the Nilgiri Hills with telescope observatory overlooking valleys.", "duration": "2.5 hours", "bestTime": "Morning (clear skies)", "lat": 11.4014, "lng": 76.7371},
            {"name": "Pykara Lake & Waterfalls", "highlight": "Scenic lake with speedboat rides and cascading pine-forest waterfalls.", "duration": "3.5 hours", "bestTime": "Afternoon", "lat": 11.4880, "lng": 76.5920},
            {"name": "Ooty Lake & Boat House", "highlight": "Serene artificial lake surrounded by eucalyptus trees with pedal and motor boating.", "duration": "2 hours", "bestTime": "Late afternoon", "lat": 11.4075, "lng": 76.6872}
        ],
        "hotels": [
            {"name": "Savoy - IHCL SeleQtions, Ooty", "type": "Luxury", "price": "₹13,500/night", "rating": "4.8★"},
            {"name": "Sterling Ooty Fern Hill", "type": "Mid-range", "price": "₹5,200/night", "rating": "4.5★"},
            {"name": "Zostel Ooty", "type": "Budget-friendly", "price": "₹950/night", "rating": "4.5★"}
        ]
    },
    "kodaikanal": {
        "fullName": "Kodaikanal, Tamil Nadu",
        "lat": 10.2381,
        "lng": 77.4892,
        "region": "Tamil Nadu",
        "climate": "cold",
        "experience": "nature",
        "budget": "medium",
        "summary": "Princess of Hill Stations in the Palani Hills, renowned for star-shaped Kodai Lake, Coaker's Walk, and Pillar Rocks.",
        "attractions": [
            {"name": "Kodaikanal Star Lake & Cycling", "highlight": "Iconic star-shaped lake offering pedal boating and cycling promenade.", "duration": "2.5 hours", "bestTime": "Morning / Evening", "lat": 10.2330, "lng": 77.4900},
            {"name": "Coaker's Walk & Bryant Park", "highlight": "1km paved pedestrian path on steep mountain ridge overlooking misty plains.", "duration": "2 hours", "bestTime": "Morning (9 AM)", "lat": 10.2312, "lng": 77.4958},
            {"name": "Pillar Rocks & Guna Caves", "highlight": "Three giant 400-ft granite pillars rising vertically out of cliff-side mist.", "duration": "2.5 hours", "bestTime": "Afternoon", "lat": 10.2078, "lng": 77.4725},
            {"name": "Dolphin's Nose & Echo Point", "highlight": "Flat rock projecting over a deep precipice offering thrilling views of the valley.", "duration": "3.5 hours", "bestTime": "Morning trek", "lat": 10.2100, "lng": 77.5180},
            {"name": "Silver Cascade & Pine Forest", "highlight": "180-ft natural waterfall and dense preserved pine forest trails.", "duration": "2 hours", "bestTime": "Morning", "lat": 10.2520, "lng": 77.5100}
        ],
        "hotels": [
            {"name": "The Tamara Kodai", "type": "Luxury", "price": "₹16,000/night", "rating": "4.9★"},
            {"name": "Carlton Hotel Kodaikanal", "type": "Luxury", "price": "₹11,000/night", "rating": "4.7★"},
            {"name": "Zostel Kodaikanal", "type": "Budget-friendly", "price": "₹900/night", "rating": "4.6★"}
        ]
    },
    "chennai": {
        "fullName": "Chennai, Tamil Nadu",
        "lat": 13.0827,
        "lng": 80.2707,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "culture",
        "budget": "medium",
        "summary": "Gateway to South India, famous for Marina Beach (world's 2nd longest), Kapaleeshwarar Temple, and Carnatic music.",
        "attractions": [
            {"name": "Marina Beach & Lighthouse", "highlight": "World's second-longest urban natural beach with street food and lighthouse view.", "duration": "2.5 hours", "bestTime": "Evening (5 PM)", "lat": 13.0500, "lng": 80.2824},
            {"name": "Kapaleeshwarar Temple (Mylapore)", "highlight": "7th-century Dravidian Shiva temple with magnificent multi-colored gopuram and tank.", "duration": "2 hours", "bestTime": "Morning / 6 PM", "lat": 13.0336, "lng": 80.2697},
            {"name": "San Thome Basilica & Fort St. George", "highlight": "Historic neo-Gothic cathedral built over St. Thomas apostle tomb and 1644 British fort museum.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 13.0337, "lng": 80.2778},
            {"name": "Guindy National Park & Snake Park", "highlight": "Protected national park inside city limits with spotted deer and blackbucks.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 13.0067, "lng": 80.2206},
            {"name": "DakshinaChitra & MGM Beach Trail", "highlight": "Living heritage museum showcasing traditional architecture of South India.", "duration": "3 hours", "bestTime": "Afternoon", "lat": 12.8256, "lng": 80.2415}
        ],
        "hotels": [
            {"name": "Taj Coromandel, Chennai", "type": "Luxury", "price": "₹12,500/night", "rating": "4.9★"},
            {"name": "The Leela Palace Chennai", "type": "Luxury", "price": "₹16,000/night", "rating": "4.9★"},
            {"name": "The Residency Towers T. Nagar", "type": "Mid-range", "price": "₹4,200/night", "rating": "4.5★"}
        ]
    },
    "rameswaram": {
        "fullName": "Rameswaram, Tamil Nadu",
        "lat": 9.2876,
        "lng": 79.3129,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "history",
        "budget": "low",
        "summary": "Sacred island pilgrimage destination in the Gulf of Mannar, celebrated for the Ramanathaswamy Temple and Dhanushkodi.",
        "attractions": [
            {"name": "Ramanathaswamy Temple & 22 Theerthams", "highlight": "One of 12 Jyotirlingas, famous for the world's longest temple corridor with 1,212 carved pillars.", "duration": "3.5 hours", "bestTime": "Early morning (5-11 AM)", "lat": 9.2881, "lng": 79.3174},
            {"name": "Pamban Sea Bridge & Railway Bridge", "highlight": "India's first sea bridge spanning over the ocean connecting Pamban Island to mainland.", "duration": "1.5 hours", "bestTime": "Sunrise / Sunset", "lat": 9.2780, "lng": 79.1960},
            {"name": "Dhanushkodi Ghost Town & Arichal Munai", "highlight": "Submerged city at the tip of India where the Bay of Bengal meets the Indian Ocean.", "duration": "3.5 hours", "bestTime": "Morning / 3 PM", "lat": 9.1764, "lng": 79.4183},
            {"name": "Dr. APJ Abdul Kalam National Memorial", "highlight": "Beautiful memorial museum celebrating the life and legacy of India's Missile Man.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 9.2930, "lng": 79.2820}
        ],
        "hotels": [
            {"name": "Hyatt Place Rameswaram", "type": "Luxury", "price": "₹6,500/night", "rating": "4.7★"},
            {"name": "Daiwik Hotels Rameswaram", "type": "Mid-range", "price": "₹3,800/night", "rating": "4.5★"}
        ]
    },
    "kanyakumari": {
        "fullName": "Kanyakumari, Tamil Nadu",
        "lat": 8.0883,
        "lng": 77.5385,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "nature",
        "budget": "low",
        "summary": "The southernmost tip of mainland India where the Indian Ocean, Arabian Sea, and Bay of Bengal converge.",
        "attractions": [
            {"name": "Vivekananda Rock Memorial & Ferry", "highlight": "Iconic rock monument built where Swami Vivekananda attained enlightenment.", "duration": "3 hours", "bestTime": "Morning ferry (8 AM)", "lat": 8.0781, "lng": 77.5553},
            {"name": "Thiruvalluvar 133-ft Statue", "highlight": "Colossal stone statue honoring Tamil philosopher poet Thiruvalluvar standing in the sea.", "duration": "1.5 hours", "bestTime": "Morning", "lat": 8.0778, "lng": 77.5540},
            {"name": "Triveni Sangam & Sunset Point", "highlight": "Spectacular vantage point to witness sunrise and sunset over three seas.", "duration": "2 hours", "bestTime": "Sunrise & Sunset", "lat": 8.0810, "lng": 77.5520},
            {"name": "Padmanabhapuram Palace", "highlight": "16th-century wooden palace displaying exquisite Kerala-Tamil teak architecture.", "duration": "3 hours", "bestTime": "Afternoon", "lat": 8.2508, "lng": 77.3275}
        ],
        "hotels": [
            {"name": "The Gopinivas Grand, Kanyakumari", "type": "Luxury", "price": "₹4,800/night", "rating": "4.6★"},
            {"name": "Hotel Sea View Kanyakumari", "type": "Mid-range", "price": "₹3,100/night", "rating": "4.4★"}
        ]
    },
    "thanjavur": {
        "fullName": "Thanjavur (Tanjore), Tamil Nadu",
        "lat": 10.7870,
        "lng": 79.1378,
        "region": "Tamil Nadu",
        "climate": "moderate",
        "experience": "history",
        "budget": "low",
        "summary": "Cradle of Chola Architecture and South Indian culture, home to the UNESCO World Heritage Brihadeeswarar Big Temple.",
        "attractions": [
            {"name": "Brihadeeswarar Temple (Big Temple - UNESCO)", "highlight": "1,000-year-old Chola architectural wonder with 216-ft vimana and single granite capstone.", "duration": "3.5 hours", "bestTime": "Morning (7-11 AM) or Sunset", "lat": 10.7828, "lng": 79.1318},
            {"name": "Thanjavur Maratha Royal Palace Complex", "highlight": "Historic palace featuring Durbar Hall, Bell Tower, and royal museum.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 10.7925, "lng": 79.1360},
            {"name": "Saraswathi Mahal Library & Art Gallery", "highlight": "One of the oldest libraries in Asia housing ancient palm leaf manuscripts and Chola bronzes.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 10.7930, "lng": 79.1368}
        ],
        "hotels": [
            {"name": "Svatma, Thanjavur", "type": "Luxury", "price": "₹14,000/night", "rating": "4.9★"},
            {"name": "Great Trails River View Thanjavur", "type": "Luxury", "price": "₹6,800/night", "rating": "4.7★"}
        ]
    },
    "coimbatore": {
        "fullName": "Coimbatore & Isha Yoga, Tamil Nadu",
        "lat": 11.0168,
        "lng": 76.9558,
        "region": "Tamil Nadu",
        "climate": "moderate",
        "experience": "culture",
        "budget": "medium",
        "summary": "Manchester of South India, gateway to the Western Ghats and home of the 112ft Adiyogi Shiva Statue at Isha Yoga.",
        "attractions": [
            {"name": "Isha Yoga Center & 112-ft Adiyogi Statue", "highlight": "Guinness Record largest bust sculpture of Adiyogi Shiva, Dhyanalinga, and evening 3D light show.", "duration": "4-5 hours", "bestTime": "Afternoon till 7:30 PM", "lat": 10.9760, "lng": 76.7410},
            {"name": "Marudhamalai Murugan Hill Temple", "highlight": "1,200-year-old scenic hilltop temple dedicated to Lord Murugan.", "duration": "2.5 hours", "bestTime": "Morning (7 AM)", "lat": 11.0450, "lng": 76.8520},
            {"name": "Siruvani Waterfalls & Dam", "highlight": "Renowned for having one of the sweetest natural mineral waters in the world.", "duration": "3.5 hours", "bestTime": "Morning", "lat": 10.9400, "lng": 76.6800},
            {"name": "GD Naidu Science & Vintage Car Museum", "highlight": "Automotive museum exhibiting rare antique cars and scientific inventions.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 11.0110, "lng": 76.9740}
        ],
        "hotels": [
            {"name": "The Residency Towers Coimbatore", "type": "Luxury", "price": "₹6,800/night", "rating": "4.8★"},
            {"name": "Radisson Blu Hotel Coimbatore", "type": "Luxury", "price": "₹6,200/night", "rating": "4.7★"}
        ]
    },

    # KERALA
    "munnar": {
        "fullName": "Munnar, Kerala",
        "lat": 10.0889,
        "lng": 77.0595,
        "region": "Kerala",
        "climate": "cold",
        "experience": "nature",
        "budget": "medium",
        "summary": "Emerald tea hills, mist-shrouded valleys, Eravikulam National Park, and Top Station.",
        "attractions": [
            {"name": "Eravikulam National Park & Rajamalai", "highlight": "Home to the endangered Nilgiri Tahr and Anamudi Peak (highest peak in South India).", "duration": "4 hours", "bestTime": "Morning (8 AM)", "lat": 10.1500, "lng": 77.0600},
            {"name": "Mattupetty Dam & Echo Point", "highlight": "Scenic lake with speedboating and natural echo phenomenon.", "duration": "2.5 hours", "bestTime": "Morning / Afternoon", "lat": 10.1060, "lng": 77.1240},
            {"name": "Tea Museum & Tata Tea Estate", "highlight": "Historic tea processing machinery and tea tasting demonstrations.", "duration": "2 hours", "bestTime": "Morning", "lat": 10.0900, "lng": 77.0550},
            {"name": "Top Station Viewpoint", "highlight": "Highest viewpoint on the Munnar-Kodaikanal border overlooking Western Ghats clouds.", "duration": "3 hours", "bestTime": "Early morning", "lat": 10.1250, "lng": 77.2450}
        ],
        "hotels": [
            {"name": "Fragrant Nature Munnar", "type": "Luxury", "price": "₹9,800/night", "rating": "4.7★"},
            {"name": "Blanket Hotel & Spa Munnar", "type": "Luxury", "price": "₹8,500/night", "rating": "4.8★"},
            {"name": "Zostel Munnar", "type": "Budget-friendly", "price": "₹950/night", "rating": "4.5★"}
        ]
    },
    "alleppey": {
        "fullName": "Alleppey (Alappuzha), Kerala",
        "lat": 9.4981,
        "lng": 76.3388,
        "region": "Kerala",
        "climate": "rainy",
        "experience": "relaxation",
        "budget": "medium",
        "summary": "Venice of the East, famous for emerald backwaters, luxury houseboat cruises, and palm-fringed canals.",
        "attractions": [
            {"name": "Alleppey Backwaters Houseboat Cruise", "highlight": "Cruise through tranquil lagoons, paddy fields, and traditional village life.", "duration": "Full day / Overnight", "bestTime": "Afternoon to Morning", "lat": 9.4981, "lng": 76.3388},
            {"name": "Marari Beach", "highlight": "Pristine white sand beach with coconut groves and serene sunset.", "duration": "2.5 hours", "bestTime": "Sunset (5:30 PM)", "lat": 9.5980, "lng": 76.2970},
            {"name": "Alappuzha Beach & Lighthouse", "highlight": "Historic 150-year-old lighthouse and scenic beach pier.", "duration": "2 hours", "bestTime": "Late afternoon", "lat": 9.4920, "lng": 76.3190}
        ],
        "hotels": [
            {"name": "Kumarakom Lake Resort", "type": "Luxury", "price": "₹22,000/night", "rating": "4.9★"},
            {"name": "Zostel Alleppey", "type": "Budget-friendly", "price": "₹900/night", "rating": "4.5★"}
        ]
    },

    # KARNATAKA
    "coorg": {
        "fullName": "Coorg (Madikeri), Karnataka",
        "lat": 12.4244,
        "lng": 75.7382,
        "region": "Karnataka",
        "climate": "cold",
        "experience": "nature",
        "budget": "medium",
        "summary": "Scotland of India, famous for aromatic coffee plantations, Abbey Falls, and Tibetan Golden Temple.",
        "attractions": [
            {"name": "Abbey Falls", "highlight": "70-ft cascading waterfall tucked inside dense coffee and spice estates.", "duration": "2 hours", "bestTime": "Morning", "lat": 12.4530, "lng": 75.7190},
            {"name": "Namdroling Tibetan Golden Temple (Bylakuppe)", "highlight": "Grand Tibetan monastery with 40-ft gilded Buddha statues and colorful prayer halls.", "duration": "2.5 hours", "bestTime": "Morning / 3 PM", "lat": 12.4300, "lng": 75.9670},
            {"name": "Raja's Seat Sunset Viewpoint", "highlight": "Royal seasonal garden where Kodagu kings watched panoramic mountain sunsets.", "duration": "2 hours", "bestTime": "5:30 PM (Sunset)", "lat": 12.4170, "lng": 75.7360},
            {"name": "Dubare Elephant Camp & River Rafting", "highlight": "Interact with elephants, bathing sessions, and Kaveri river rafting.", "duration": "3 hours", "bestTime": "Morning (9 AM)", "lat": 12.3680, "lng": 75.9050}
        ],
        "hotels": [
            {"name": "Taj Madikeri Resort & Spa, Coorg", "type": "Luxury", "price": "₹24,000/night", "rating": "4.9★"},
            {"name": "Evolve Back, Kabini & Coorg", "type": "Luxury", "price": "₹28,000/night", "rating": "4.9★"},
            {"name": "Zostel Coorg", "type": "Budget-friendly", "price": "₹950/night", "rating": "4.5★"}
        ]
    },
    "hampi": {
        "fullName": "Hampi, Karnataka",
        "lat": 15.3350,
        "lng": 76.4600,
        "region": "Karnataka",
        "climate": "moderate",
        "experience": "history",
        "budget": "low",
        "summary": "UNESCO World Heritage ruin city of the Vijayanagara Empire with stone chariots, boulder-strewn hills, and Virupaksha Temple.",
        "attractions": [
            {"name": "Virupaksha Temple & Hampi Bazaar", "highlight": "7th-century active temple dedicated to Lord Shiva with 50-meter gopuram.", "duration": "2.5 hours", "bestTime": "Morning (7 AM)", "lat": 15.3350, "lng": 76.4600},
            {"name": "Vittala Temple & Iconic Stone Chariot", "highlight": "Architectural masterpiece with musical pillars and world-famous monolithic stone chariot.", "duration": "3 hours", "bestTime": "Morning / 4 PM", "lat": 15.3430, "lng": 76.4780},
            {"name": "Matanga Hill Sunrise Viewpoint", "highlight": "Highest point in Hampi offering 360-degree sunrise panoramas across ruins and boulders.", "duration": "2 hours", "bestTime": "5:30 AM Sunrise", "lat": 15.3310, "lng": 76.4670},
            {"name": "Lotus Mahal & Elephant Stables", "highlight": "Indo-Islamic royal enclosure featuring domed royal elephant chambers.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 15.3200, "lng": 76.4700}
        ],
        "hotels": [
            {"name": "Evolve Back Kamalapura Palace Hampi", "type": "Luxury", "price": "₹26,000/night", "rating": "4.9★"},
            {"name": "Heritage Resort Hampi", "type": "Mid-range", "price": "₹5,800/night", "rating": "4.6★"},
            {"name": "Zostel Hampi", "type": "Budget-friendly", "price": "₹900/night", "rating": "4.5★"}
        ]
    },

    # NORTH & HIMALAYAS
    "manali": {
        "fullName": "Manali, Himachal Pradesh",
        "lat": 32.2432,
        "lng": 77.1892,
        "region": "Himachal Pradesh",
        "climate": "cold",
        "experience": "adventure",
        "budget": "medium",
        "summary": "Premier Himalayan resort town renowned for snow-capped peaks, Solang adventure valley, Rohtang Pass, and pine forests.",
        "attractions": [
            {"name": "Solang Valley", "highlight": "Famous hub for paragliding, zorbing, quad biking, and winter skiing.", "duration": "4-5 hours", "bestTime": "Morning", "lat": 32.3166, "lng": 77.1578},
            {"name": "Rohtang Pass", "highlight": "High-altitude mountain pass offering panoramic Himalayan glaciers and snow viewpoints.", "duration": "Half day", "bestTime": "Early morning (7 AM)", "lat": 32.3716, "lng": 77.2466},
            {"name": "Hadimba Temple & Van Vihar", "highlight": "Ancient 16th-century wooden pagoda temple nestled inside dense cedar forests.", "duration": "2 hours", "bestTime": "Morning / Afternoon", "lat": 32.2483, "lng": 77.1705},
            {"name": "Old Manali & Cafe Trail", "highlight": "Bohemian village atmosphere with wooden houses, vibrant cafes, and live acoustic music.", "duration": "3 hours", "bestTime": "Evening", "lat": 32.2530, "lng": 77.1750},
            {"name": "Atal Tunnel & Sissu Valley", "highlight": "World's longest highway tunnel above 10,000 ft connecting to waterfalls in Sissu.", "duration": "4-5 hours", "bestTime": "Morning", "lat": 32.4833, "lng": 77.1264}
        ],
        "hotels": [
            {"name": "The Himalayan Resort & Spa", "type": "Luxury", "price": "₹9,500/night", "rating": "4.8★"},
            {"name": "Span Resort & Spa, Manali", "type": "Luxury", "price": "₹11,000/night", "rating": "4.7★"},
            {"name": "Zostel Manali", "type": "Budget-friendly", "price": "₹1,200/night", "rating": "4.6★"}
        ]
    },
    "shimla": {
        "fullName": "Shimla, Himachal Pradesh",
        "lat": 31.1048,
        "lng": 77.1734,
        "region": "Himachal Pradesh",
        "climate": "cold",
        "experience": "relaxation",
        "budget": "medium",
        "summary": "Queen of the Hills, former British summer capital, celebrated for colonial charm, Mall Road, and Kalka Toy Train.",
        "attractions": [
            {"name": "The Ridge & Mall Road", "highlight": "Pedestrian promenade featuring Christ Church, Scandal Point, and mountain viewpoints.", "duration": "3 hours", "bestTime": "Afternoon & Evening", "lat": 31.1044, "lng": 77.1746},
            {"name": "Jakhoo Hill & 108ft Hanuman Statue", "highlight": "Highest peak in Shimla with a 108-ft giant Hanuman statue and cable car ride.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 31.1010, "lng": 77.1852},
            {"name": "Kalka-Shimla Toy Train (UNESCO)", "highlight": "Historic narrow-gauge railway journey curving through 102 tunnels.", "duration": "3-4 hours", "bestTime": "Morning", "lat": 31.1030, "lng": 77.1640}
        ],
        "hotels": [
            {"name": "Wildflower Hall, An Oberoi Resort", "type": "Luxury", "price": "₹28,000/night", "rating": "4.9★"},
            {"name": "Radisson Hotel Shimla", "type": "Mid-range", "price": "₹5,800/night", "rating": "4.4★"}
        ]
    },
    "rishikesh": {
        "fullName": "Rishikesh, Uttarakhand",
        "lat": 30.0869,
        "lng": 78.2676,
        "region": "Uttarakhand",
        "climate": "moderate",
        "experience": "adventure",
        "budget": "low",
        "summary": "Yoga Capital of the World and adventure hub along the holy Ganga in the Himalayan foothills.",
        "attractions": [
            {"name": "White Water River Rafting & Cliff Jumping", "highlight": "Thrilling 16km/24km rapids on the holy Ganges River.", "duration": "4 hours", "bestTime": "Morning (8:30 AM)", "lat": 30.1265, "lng": 78.3312},
            {"name": "Triveni Ghat Evening Maha Aarti", "highlight": "Spiritual evening river prayer with chanting, fire torches, and floating diyas.", "duration": "2 hours", "bestTime": "5:30 PM", "lat": 30.1030, "lng": 78.2930},
            {"name": "Ram Jhula & Beatles Ashram", "highlight": "Iconic suspension bridge and Maharishi Mahesh Yogi Ashram with vibrant murals.", "duration": "3 hours", "bestTime": "Morning / 3 PM", "lat": 30.1190, "lng": 78.3140}
        ],
        "hotels": [
            {"name": "Ananda in the Himalayas", "type": "Luxury", "price": "₹36,000/night", "rating": "4.9★"},
            {"name": "Aloha On The Ganges", "type": "Mid-range", "price": "₹6,500/night", "rating": "4.6★"}
        ]
    },
    "jaipur": {
        "fullName": "Jaipur (Pink City), Rajasthan",
        "lat": 26.9124,
        "lng": 75.7873,
        "region": "Rajasthan",
        "climate": "moderate",
        "experience": "history",
        "budget": "medium",
        "summary": "The majestic Pink City brimming with royal palaces, hilltop fortresses, and vibrant bazaars.",
        "attractions": [
            {"name": "Amber Fort & Palace", "highlight": "Magnificent hilltop fort with Sheesh Mahal (Mirror Palace) and elephant/jeep ascents.", "duration": "3.5 hours", "bestTime": "Morning (8:30 AM)", "lat": 26.9855, "lng": 75.8513},
            {"name": "Hawa Mahal (Palace of Winds)", "highlight": "Iconic 5-story honeycomb facade with 953 intricately carved jharokhas.", "duration": "1.5 hours", "bestTime": "Morning for best lighting", "lat": 26.9239, "lng": 75.8267},
            {"name": "City Palace & Jantar Mantar", "highlight": "Royal residence museum displaying Rajput history and UNESCO astronomical observatory.", "duration": "3 hours", "bestTime": "Afternoon", "lat": 26.9258, "lng": 75.8236},
            {"name": "Nahargarh Fort Sunset Viewpoint", "highlight": "Hilltop fort offering spectacular panoramic sunset views of the entire Jaipur city.", "duration": "2.5 hours", "bestTime": "5:00 PM - Sunset", "lat": 26.9372, "lng": 75.8155}
        ],
        "hotels": [
            {"name": "Rambagh Palace (Taj)", "type": "Luxury", "price": "₹32,000/night", "rating": "4.9★"},
            {"name": "ITC Rajputana, Jaipur", "type": "Luxury", "price": "₹8,500/night", "rating": "4.7★"},
            {"name": "Moustache Hostel Jaipur", "type": "Budget-friendly", "price": "₹750/night", "rating": "4.5★"}
        ]
    },
    "goa": {
        "fullName": "Goa (North & South)",
        "lat": 15.2993,
        "lng": 74.1240,
        "region": "West Coast",
        "climate": "hot",
        "experience": "relaxation",
        "budget": "medium",
        "summary": "Tropical beach paradise with Portuguese colonial heritage, pristine coastlines, and vibrant nightlife.",
        "attractions": [
            {"name": "Baga & Calangute Beach", "highlight": "Energetic golden beaches with water sports, beach shacks, and live sunset music.", "duration": "3-4 hours", "bestTime": "Late afternoon to Sunset", "lat": 15.5523, "lng": 73.7517},
            {"name": "Fort Aguada & Lighthouse", "highlight": "17th-century Portuguese fortress with sweeping panoramic views over the Arabian Sea.", "duration": "2 hours", "bestTime": "Morning / 4 PM", "lat": 15.4920, "lng": 73.7737},
            {"name": "Basilica of Bom Jesus & Old Goa", "highlight": "UNESCO World Heritage Baroque church housing the sacred relics of St. Francis Xavier.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 15.5009, "lng": 73.9116},
            {"name": "Dudhsagar Waterfalls", "highlight": "Magnificent four-tiered waterfall cascading down 310 meters amidst lush jungle canopy.", "duration": "Full day", "bestTime": "Early morning jeep safari", "lat": 15.3144, "lng": 74.3143}
        ],
        "hotels": [
            {"name": "Taj Exotica Resort & Spa, Benaulim", "type": "Luxury", "price": "₹16,500/night", "rating": "4.9★"},
            {"name": "W Goa, Vagator", "type": "Luxury", "price": "₹18,000/night", "rating": "4.8★"},
            {"name": "The Hosteller Goa", "type": "Budget-friendly", "price": "₹950/night", "rating": "4.5★"}
        ]
    },
    "varanasi": {
        "fullName": "Varanasi (Kashi), Uttar Pradesh",
        "lat": 25.3176,
        "lng": 82.9739,
        "region": "Uttar Pradesh",
        "climate": "moderate",
        "experience": "history",
        "budget": "low",
        "summary": "One of the world's oldest continuously inhabited cities, spiritual heart of Hinduism along the sacred River Ganga.",
        "attractions": [
            {"name": "Dashashwamedh Ghat & Evening Ganga Aarti", "highlight": "Mesmerizing multi-priest synchronized fire ritual with chanting, bells, and floating lamps on the river.", "duration": "2.5 hours", "bestTime": "6:00 PM (arrive by 5:30 PM)", "lat": 25.3073, "lng": 83.0104},
            {"name": "Sunrise Boat Ride on the Ganga", "highlight": "Morning boat ride capturing spiritual life across 84 historic ghats from Assi to Manikarnika.", "duration": "2 hours", "bestTime": "5:30 AM Sunrise", "lat": 25.2899, "lng": 83.0069},
            {"name": "Kashi Vishwanath Golden Temple", "highlight": "One of the 12 sacred Jyotirlingas of Lord Shiva with magnificent newly renovated Corridor.", "duration": "2.5 hours", "bestTime": "Early morning (7 AM)", "lat": 25.3109, "lng": 83.0107}
        ],
        "hotels": [
            {"name": "BrijRama Palace, Varanasi", "type": "Luxury", "price": "₹24,000/night", "rating": "4.9★"},
            {"name": "Taj Ganges, Varanasi", "type": "Luxury", "price": "₹12,500/night", "rating": "4.7★"}
        ]
    },
    "srinagar": {
        "fullName": "Srinagar & Kashmir Valley, Jammu & Kashmir",
        "lat": 34.0837,
        "lng": 74.7973,
        "region": "Jammu & Kashmir",
        "climate": "cold",
        "experience": "nature",
        "budget": "medium",
        "summary": "Paradise on Earth, celebrated for Dal Lake Shikara rides, Mughal Gardens, and snow peaks in Gulmarg & Pahalgam.",
        "attractions": [
            {"name": "Dal Lake & Shikara Boat Ride", "highlight": "Traditional wooden Shikara boat cruise past floating vegetable gardens and houseboats.", "duration": "2.5 hours", "bestTime": "Sunrise / Sunset", "lat": 34.0837, "lng": 74.8370},
            {"name": "Mughal Gardens (Shalimar & Nishat Bagh)", "highlight": "Terraced Persian Mughal pleasure gardens with cascading fountains overlooking the lake.", "duration": "3 hours", "bestTime": "Morning / Afternoon", "lat": 34.1480, "lng": 74.8720},
            {"name": "Gulmarg Snow Gondola Cable Car", "highlight": "World's second-highest operating cable car taking you to 13,780 ft snow peaks.", "duration": "Full day", "bestTime": "Morning (9 AM)", "lat": 34.0484, "lng": 74.3805}
        ],
        "hotels": [
            {"name": "The Lalit Grand Palace Srinagar", "type": "Luxury", "price": "₹22,000/night", "rating": "4.9★"},
            {"name": "Welcomhotel by ITC Hotels Pine N Peak Pahalgam", "type": "Luxury", "price": "₹18,000/night", "rating": "4.8★"}
        ]
    },
    "leh": {
        "fullName": "Leh & Ladakh",
        "lat": 34.1526,
        "lng": 77.5771,
        "region": "Ladakh",
        "climate": "cold",
        "experience": "adventure",
        "budget": "high",
        "summary": "Land of High Passes, azure Pangong Tso Lake, ancient monasteries, and dramatic moonscape Himalayan valleys.",
        "attractions": [
            {"name": "Pangong Tso High Altitude Lake", "highlight": "134-km long crystal-blue lake changing colors from turquoise to emerald.", "duration": "Full day / Overnight", "bestTime": "Morning (clear skies)", "lat": 33.7595, "lng": 78.6674},
            {"name": "Nubra Valley & Hunder Sand Dunes", "highlight": "Double-humped Bactrian camel safaris in cold desert dunes surrounded by snow peaks.", "duration": "Full day", "bestTime": "Morning / Sunset", "lat": 34.5800, "lng": 77.5500},
            {"name": "Thiksey & Hemis Monasteries", "highlight": "Miniature Potala Palace of Ladakh perched on a hill with colossal Maitreya Buddha statue.", "duration": "3 hours", "bestTime": "Morning prayer (7 AM)", "lat": 34.0570, "lng": 77.6670}
        ],
        "hotels": [
            {"name": "The Grand Dragon Ladakh", "type": "Luxury", "price": "₹16,000/night", "rating": "4.9★"},
            {"name": "Zostel Leh", "type": "Budget-friendly", "price": "₹1,400/night", "rating": "4.6★"}
        ]
    }
}

print(f"Total Database entries: {len(ALL_INDIA_DB)}")
