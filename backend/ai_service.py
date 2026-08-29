import json
import os
import re
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")


# -------------------------------------------------------------------------
# Comprehensive Curated Knowledge Base for Indian Destinations
# Contains verified coordinates, top iconic attractions prioritized by importance,
# detailed descriptions, best visiting hours, and top-rated hotels.
# -------------------------------------------------------------------------
DESTINATIONS_DB = {
    "manali": {
        "fullName": "Manali, Himachal Pradesh",
        "lat": 32.2432,
        "lng": 77.1892,
        "region": "Himachal Pradesh",
        "climate": "cold",
        "experience": "adventure",
        "budget": "medium",
        "summary": "Premier Himalayan resort town renowned for snow-capped peaks, Solang adventure valley, Rohtang Pass, and scenic pine forests.",
        "attractions": [
            {
                "name": "Solang Valley",
                "highlight": "Famous hub for paragliding, zorbing, quad biking, and winter skiing.",
                "duration": "4-5 hours",
                "bestTime": "Morning",
                "lat": 32.3166,
                "lng": 77.1578
            },
            {
                "name": "Rohtang Pass",
                "highlight": "High-altitude mountain pass offering panoramic Himalayan glaciers and snow viewpoints (permit required).",
                "duration": "Half day",
                "bestTime": "Early morning (7 AM)",
                "lat": 32.3716,
                "lng": 77.2466
            },
            {
                "name": "Hadimba Temple & Van Vihar",
                "highlight": "Ancient 16th-century wooden pagoda temple nestled inside dense cedar forests.",
                "duration": "2 hours",
                "bestTime": "Morning / Afternoon",
                "lat": 32.2483,
                "lng": 77.1705
            },
            {
                "name": "Old Manali & Cafe Trail",
                "highlight": "Bohemian village atmosphere with wooden houses, vibrant cafes, and live acoustic music.",
                "duration": "3 hours",
                "bestTime": "Evening",
                "lat": 32.2530,
                "lng": 77.1750
            },
            {
                "name": "Jogini Waterfalls & Vashisht Hot Springs",
                "highlight": "Scenic nature trek leading to a cascading waterfall and natural sulphur hot baths.",
                "duration": "3-4 hours",
                "bestTime": "Morning",
                "lat": 32.2660,
                "lng": 77.1870
            },
            {
                "name": "Naggar Castle & Art Gallery",
                "highlight": "Historic medieval wood and stone castle overlooking the Beas River valley.",
                "duration": "2.5 hours",
                "bestTime": "Afternoon",
                "lat": 32.1378,
                "lng": 77.1689
            },
            {
                "name": "Atal Tunnel & Sissu (Lahaul Valley)",
                "highlight": "World's longest highway tunnel above 10,000 ft connecting to majestic waterfalls in Sissu.",
                "duration": "4-5 hours",
                "bestTime": "Morning",
                "lat": 32.4833,
                "lng": 77.1264
            }
        ],
        "hotels": [
            {"name": "The Himalayan Resort & Spa", "type": "Luxury", "price": "₹9,500/night", "rating": "4.8★"},
            {"name": "Span Resort & Spa, Manali", "type": "Luxury", "price": "₹11,000/night", "rating": "4.7★"},
            {"name": "Larisa Resort Manali", "type": "Mid-range", "price": "₹4,800/night", "rating": "4.5★"},
            {"name": "Zostel Manali (Old Manali)", "type": "Budget-friendly", "price": "₹1,200/night", "rating": "4.6★"}
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
            {
                "name": "Baga & Calangute Beach",
                "highlight": "Energetic golden beaches with water sports, beach shacks, and live sunset music.",
                "duration": "3-4 hours",
                "bestTime": "Late afternoon to Sunset",
                "lat": 15.5523,
                "lng": 73.7517
            },
            {
                "name": "Fort Aguada & Lighthouse",
                "highlight": "17th-century Portuguese fortress with sweeping panoramic views over the Arabian Sea.",
                "duration": "2 hours",
                "bestTime": "Morning / 4 PM",
                "lat": 15.4920,
                "lng": 73.7737
            },
            {
                "name": "Basilica of Bom Jesus & Old Goa",
                "highlight": "UNESCO World Heritage Baroque church housing the sacred relics of St. Francis Xavier.",
                "duration": "2.5 hours",
                "bestTime": "Morning",
                "lat": 15.5009,
                "lng": 73.9116
            },
            {
                "name": "Dudhsagar Waterfalls",
                "highlight": "Magnificent four-tiered waterfall cascading down 310 meters amidst lush jungle canopy.",
                "duration": "Full day",
                "bestTime": "Early morning jeep safari",
                "lat": 15.3144,
                "lng": 74.3143
            },
            {
                "name": "Palolem Beach (South Goa)",
                "highlight": "Serene crescent-shaped beach famous for calm waters, dolphin spotting, and beach yoga.",
                "duration": "Half day",
                "bestTime": "Sunset",
                "lat": 15.0100,
                "lng": 74.0232
            },
            {
                "name": "Anjuna Flea Market & Chapora Fort",
                "highlight": "Iconic cliffside fort overlooking the sea ('Dil Chahta Hai' fame) and vibrant market.",
                "duration": "3 hours",
                "bestTime": "5 PM",
                "lat": 15.6059,
                "lng": 73.7386
            },
            {
                "name": "Fontainhas Latin Quarter (Panaji)",
                "highlight": "Colourful historic Portuguese quarter with charming lanes, art galleries, and bakeries.",
                "duration": "2 hours",
                "bestTime": "Morning / Evening",
                "lat": 15.4989,
                "lng": 73.8278
            }
        ],
        "hotels": [
            {"name": "Taj Exotica Resort & Spa, Benaulim", "type": "Luxury", "price": "₹16,500/night", "rating": "4.9★"},
            {"name": "W Goa, Vagator", "type": "Luxury", "price": "₹18,000/night", "rating": "4.8★"},
            {"name": "Fairfield by Marriott Goa Anjuna", "type": "Mid-range", "price": "₹4,200/night", "rating": "4.4★"},
            {"name": "The Hosteller Goa Candolim", "type": "Budget-friendly", "price": "₹950/night", "rating": "4.5★"}
        ]
    },
    "jaipur": {
        "fullName": "Jaipur, Rajasthan",
        "lat": 26.9124,
        "lng": 75.7873,
        "region": "Rajasthan",
        "climate": "moderate",
        "experience": "history",
        "budget": "medium",
        "summary": "The majestic Pink City brimming with royal palaces, hilltop fortresses, and vibrant bazaars.",
        "attractions": [
            {
                "name": "Amber Fort & Palace",
                "highlight": "Magnificent hilltop fort with Sheesh Mahal (Mirror Palace) and elephant/jeep ascents.",
                "duration": "3.5 hours",
                "bestTime": "Morning (8:30 AM)",
                "lat": 26.9855,
                "lng": 75.8513
            },
            {
                "name": "Hawa Mahal (Palace of Winds)",
                "highlight": "Iconic 5-story honeycomb facade with 953 intricately carved jharokhas.",
                "duration": "1.5 hours",
                "bestTime": "Morning for best lighting",
                "lat": 26.9239,
                "lng": 75.8267
            },
            {
                "name": "City Palace & Jantar Mantar",
                "highlight": "Royal residence museum displaying Rajput history and UNESCO astronomical observatory.",
                "duration": "3 hours",
                "bestTime": "Afternoon",
                "lat": 26.9258,
                "lng": 75.8236
            },
            {
                "name": "Nahargarh Fort Sunset Viewpoint",
                "highlight": "Hilltop fort offering spectacular panoramic sunset views of the entire Jaipur city.",
                "duration": "2.5 hours",
                "bestTime": "5:00 PM - Sunset",
                "lat": 26.9372,
                "lng": 75.8155
            },
            {
                "name": "Albert Hall Museum & Johari Bazaar",
                "highlight": "Indo-Saracenic museum illuminated by night and world-famous gemstone/textile bazaar.",
                "duration": "2.5 hours",
                "bestTime": "Evening",
                "lat": 26.9116,
                "lng": 75.8195
            },
            {
                "name": "Jal Mahal (Water Palace)",
                "highlight": "Enchanting palace floating in the middle of Man Sagar Lake.",
                "duration": "1 hour",
                "bestTime": "Morning / Evening promenade",
                "lat": 26.9534,
                "lng": 75.8462
            }
        ],
        "hotels": [
            {"name": "Rambagh Palace (Taj)", "type": "Luxury", "price": "₹32,000/night", "rating": "4.9★"},
            {"name": "ITC Rajputana, Jaipur", "type": "Luxury", "price": "₹8,500/night", "rating": "4.7★"},
            {"name": "Hotel Pearl Palace", "type": "Mid-range", "price": "₹2,600/night", "rating": "4.6★"},
            {"name": "Moustache Hostel Jaipur", "type": "Budget-friendly", "price": "₹750/night", "rating": "4.5★"}
        ]
    },
    "delhi": {
        "fullName": "New Delhi & Old Delhi",
        "lat": 28.6139,
        "lng": 77.2090,
        "region": "NCR",
        "climate": "moderate",
        "experience": "history",
        "budget": "medium",
        "summary": "India's capital city uniting centuries of Mughal history, grand colonial architecture, and bustling markets.",
        "attractions": [
            {
                "name": "Red Fort & Jama Masjid",
                "highlight": "Massive 17th-century Mughal sandstone citadel and India's largest historic mosque.",
                "duration": "3.5 hours",
                "bestTime": "Morning",
                "lat": 28.6562,
                "lng": 77.2410
            },
            {
                "name": "Qutub Minar & Mehrauli Archaeological Park",
                "highlight": "UNESCO World Heritage 73m victory minaret with 12th-century Iron Pillar and ruins.",
                "duration": "2.5 hours",
                "bestTime": "Morning / Late Afternoon",
                "lat": 28.5244,
                "lng": 77.1855
            },
            {
                "name": "Humayun's Tomb",
                "highlight": "Sublime Mughal garden tomb and architectural predecessor to the Taj Mahal.",
                "duration": "2 hours",
                "bestTime": "Afternoon to Sunset",
                "lat": 28.5933,
                "lng": 77.2507
            },
            {
                "name": "India Gate & Kartavya Path",
                "highlight": "Iconic war memorial archway surrounded by sprawling ceremonial lawns and fountain walks.",
                "duration": "1.5 hours",
                "bestTime": "Evening (6 PM onwards)",
                "lat": 28.6129,
                "lng": 77.2295
            },
            {
                "name": "Swaminarayan Akshardham Temple",
                "highlight": "Grand modern spiritual monument with musical water show and boat ride through Vedic history.",
                "duration": "4 hours",
                "bestTime": "Afternoon till night show",
                "lat": 28.6127,
                "lng": 77.2773
            },
            {
                "name": "Lotus Temple & Hauz Khas Village",
                "highlight": "Bahá'í House of Worship shaped like a lotus, followed by medieval reservoir lake & hip cafes.",
                "duration": "3 hours",
                "bestTime": "Afternoon / Sunset",
                "lat": 28.5535,
                "lng": 77.2588
            },
            {
                "name": "Chandni Chowk Food & Heritage Trail",
                "highlight": "Legendary street food (Paranthe Wali Gali, Jalebis, Natraj Dahi Bhalla) & spice market.",
                "duration": "3 hours",
                "bestTime": "Evening",
                "lat": 28.6506,
                "lng": 77.2303
            }
        ],
        "hotels": [
            {"name": "The Leela Palace New Delhi", "type": "Luxury", "price": "₹19,000/night", "rating": "4.9★"},
            {"name": "Taj Mahal Hotel, Mansingh Road", "type": "Luxury", "price": "₹14,000/night", "rating": "4.8★"},
            {"name": "Bloomrooms @ Janpath", "type": "Mid-range", "price": "₹3,800/night", "rating": "4.4★"},
            {"name": "goStops Delhi", "type": "Budget-friendly", "price": "₹850/night", "rating": "4.5★"}
        ]
    },
    "agra": {
        "fullName": "Agra, Uttar Pradesh",
        "lat": 27.1767,
        "lng": 78.0081,
        "region": "Uttar Pradesh",
        "climate": "hot",
        "experience": "history",
        "budget": "medium",
        "summary": "Home of the iconic Taj Mahal, grand Mughal fortresses, and UNESCO World Heritage wonders.",
        "attractions": [
            {
                "name": "The Taj Mahal",
                "highlight": "One of the Seven Wonders of the World; marble mausoleum built by Shah Jahan for Mumtaz Mahal.",
                "duration": "3 hours",
                "bestTime": "Sunrise (6:00 AM) or Full Moon night",
                "lat": 27.1751,
                "lng": 78.0421
            },
            {
                "name": "Agra Fort",
                "highlight": "Expansive red sandstone fortress containing Jahangiri Mahal, Khas Mahal, and Taj viewpoints.",
                "duration": "2.5 hours",
                "bestTime": "Morning / 3 PM",
                "lat": 27.1795,
                "lng": 78.0211
            },
            {
                "name": "Fatehpur Sikri",
                "highlight": "Preserved Mughal imperial city with Buland Darwaza (world's tallest gateway) and Salim Chishti Dargah.",
                "duration": "3.5 hours",
                "bestTime": "Morning",
                "lat": 27.0945,
                "lng": 77.6679
            },
            {
                "name": "Mehtab Bagh (Moonlight Garden)",
                "highlight": "Botanical garden across the Yamuna River offering picturesque sunset silhouettes of the Taj.",
                "duration": "1.5 hours",
                "bestTime": "Sunset (5:30 PM)",
                "lat": 27.1800,
                "lng": 78.0416
            },
            {
                "name": "Itmad-ud-Daulah (Baby Taj)",
                "highlight": "Delicate precursor to the Taj Mahal with fine pietra dura inlay marble work.",
                "duration": "1.5 hours",
                "bestTime": "Late afternoon",
                "lat": 27.1929,
                "lng": 78.0310
            }
        ],
        "hotels": [
            {"name": "The Oberoi Amarvilas, Agra", "type": "Luxury", "price": "₹38,000/night", "rating": "4.9★"},
            {"name": "Taj Hotel & Convention Centre", "type": "Luxury", "price": "₹7,200/night", "rating": "4.6★"},
            {"name": "Howard Plaza - The Fern", "type": "Mid-range", "price": "₹3,100/night", "rating": "4.3★"},
            {"name": "Joey's Hostel Agra (Taj View)", "type": "Budget-friendly", "price": "₹700/night", "rating": "4.6★"}
        ]
    },
    "kerala": {
        "fullName": "Kerala (Munnar, Alleppey & Kochi)",
        "lat": 9.9312,
        "lng": 76.2673,
        "region": "Kerala",
        "climate": "rainy",
        "experience": "nature",
        "budget": "medium",
        "summary": "God's Own Country blessed with emerald backwaters, rolling tea estates, spice plantations, and Ayurvedic retreats.",
        "attractions": [
            {
                "name": "Alleppey Backwaters & Houseboat Cruise",
                "highlight": "Iconic traditional Kettuvallam houseboat stay cruising through tranquil lagoons and paddy fields.",
                "duration": "Full day / Overnight",
                "bestTime": "Afternoon to Morning",
                "lat": 9.4981,
                "lng": 76.3388
            },
            {
                "name": "Munnar Tea Plantations & Eravikulam National Park",
                "highlight": "Lush mist-covered tea gardens and home to the endangered Nilgiri Tahr mountain goat.",
                "duration": "4-5 hours",
                "bestTime": "Morning (8 AM)",
                "lat": 10.0889,
                "lng": 77.0595
            },
            {
                "name": "Fort Kochi & Chinese Fishing Nets",
                "highlight": "Colonial Dutch/Portuguese heritage, historic St. Francis Church, and sunset harbor views.",
                "duration": "3 hours",
                "bestTime": "Evening",
                "lat": 9.9658,
                "lng": 76.2421
            },
            {
                "name": "Mattupetty Dam & Top Station (Munnar)",
                "highlight": "Scenic lake with boating and highest viewpoint on the Munnar-Kodaikanal road.",
                "duration": "3 hours",
                "bestTime": "Afternoon",
                "lat": 10.1060,
                "lng": 77.1240
            },
            {
                "name": "Periyar Wildlife Sanctuary (Thekkady)",
                "highlight": "Boat safari in elephant reserve, spice garden walks, and bamboo rafting.",
                "duration": "4 hours",
                "bestTime": "Early morning boat safari",
                "lat": 9.4679,
                "lng": 77.1435
            },
            {
                "name": "Varkala Cliff Beach",
                "highlight": "Dramatic red laterite cliffs bordering the Arabian Sea with seaside cafes and sunset spots.",
                "duration": "Half day",
                "bestTime": "Sunset",
                "lat": 8.7379,
                "lng": 76.7163
            }
        ],
        "hotels": [
            {"name": "Kumarakom Lake Resort", "type": "Luxury", "price": "₹22,000/night", "rating": "4.9★"},
            {"name": "Fragrant Nature Munnar", "type": "Luxury", "price": "₹9,800/night", "rating": "4.7★"},
            {"name": "Brunton Boatyard - CGH Earth (Kochi)", "type": "Mid-range", "price": "₹6,500/night", "rating": "4.6★"},
            {"name": "Zostel Alleppey", "type": "Budget-friendly", "price": "₹900/night", "rating": "4.5★"}
        ]
    },
    "varanasi": {
        "fullName": "Varanasi, Uttar Pradesh",
        "lat": 25.3176,
        "lng": 82.9739,
        "region": "Uttar Pradesh",
        "climate": "moderate",
        "experience": "history",
        "budget": "low",
        "summary": "One of the world's oldest continuously inhabited cities, spiritual heart of Hinduism along the sacred River Ganga.",
        "attractions": [
            {
                "name": "Dashashwamedh Ghat & Evening Ganga Aarti",
                "highlight": "Mesmerizing multi-priest synchronized fire ritual with chanting, bells, and floating lamps on the river.",
                "duration": "2.5 hours",
                "bestTime": "6:00 PM (arrive by 5:30 PM)",
                "lat": 25.3073,
                "lng": 83.0104
            },
            {
                "name": "Sunrise Boat Ride on the Ganga",
                "highlight": "Morning boat ride capturing spiritual life across 84 historic ghats from Assi to Manikarnika.",
                "duration": "2 hours",
                "bestTime": "5:30 AM Sunrise",
                "lat": 25.2899,
                "lng": 83.0069
            },
            {
                "name": "Kashi Vishwanath Golden Temple",
                "highlight": "One of the 12 sacred Jyotirlingas of Lord Shiva with magnificent newly renovated Corridor.",
                "duration": "2.5 hours",
                "bestTime": "Early morning (7 AM)",
                "lat": 25.3109,
                "lng": 83.0107
            },
            {
                "name": "Sarnath (Dhamek Stupa & Deer Park)",
                "highlight": "Sacred Buddhist site where Lord Buddha delivered his first sermon; Museum with Ashoka Lion Capital.",
                "duration": "3 hours",
                "bestTime": "Morning / 2 PM",
                "lat": 25.3811,
                "lng": 83.0227
            },
            {
                "name": "Banarasi Silk Weaving & Food Trail",
                "highlight": "Explore traditional loom workshops, authentic Banarasi Paan, Malaiyo (winter), and blue lassi.",
                "duration": "2.5 hours",
                "bestTime": "Afternoon / Evening",
                "lat": 25.3180,
                "lng": 83.0050
            },
            {
                "name": "Ramnagar Fort & Museum",
                "highlight": "18th-century royal palace across the river featuring antique cars, armory, and astronomical clocks.",
                "duration": "2 hours",
                "bestTime": "Late afternoon",
                "lat": 25.2678,
                "lng": 83.0248
            }
        ],
        "hotels": [
            {"name": "BrijRama Palace, Varanasi", "type": "Luxury", "price": "₹24,000/night", "rating": "4.9★"},
            {"name": "Taj Ganges, Varanasi", "type": "Luxury", "price": "₹12,500/night", "rating": "4.7★"},
            {"name": "Hotel Surya, Kaiser Palace", "type": "Mid-range", "price": "₹3,400/night", "rating": "4.4★"},
            {"name": "Moustache Varanasi (Assi Ghat)", "type": "Budget-friendly", "price": "₹800/night", "rating": "4.5★"}
        ]
    },
    "madurai": {
        "fullName": "Madurai, Tamil Nadu",
        "lat": 9.9252,
        "lng": 78.1198,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "history",
        "budget": "low",
        "summary": "The Cultural Capital of Tamil Nadu, celebrated for its 2,500-year history and the colossal Meenakshi Amman Temple.",
        "attractions": [
            {
                "name": "Meenakshi Amman Temple",
                "highlight": "Architectural marvel with 14 soaring gopurams, Hall of Thousand Pillars, and intricate Dravidian carvings.",
                "duration": "3.5 hours",
                "bestTime": "Morning (6-11 AM) or Evening (5-9 PM)",
                "lat": 9.9195,
                "lng": 78.1193
            },
            {
                "name": "Thirumalai Nayakkar Mahal",
                "highlight": "17th-century Indo-Saracenic royal palace with gigantic circular pillars and evening light-and-sound show.",
                "duration": "2 hours",
                "bestTime": "Afternoon / 6:45 PM for Sound & Light show",
                "lat": 9.9152,
                "lng": 78.1238
            },
            {
                "name": "Gandhi Memorial Museum & Tamukkam Palace",
                "highlight": "Historic museum housing Mahatma Gandhi's blood-stained dhoti and comprehensive freedom struggle gallery.",
                "duration": "2 hours",
                "bestTime": "Morning",
                "lat": 9.9327,
                "lng": 78.1402
            },
            {
                "name": "Alagar Koyil (Alagar Hills)",
                "highlight": "Ancient temple of Lord Vishnu situated in the lush forest foothills of Alagar Hills.",
                "duration": "3 hours",
                "bestTime": "Morning",
                "lat": 10.0769,
                "lng": 78.2144
            },
            {
                "name": "Vandiyur Mariamman Teppakulam",
                "highlight": "Huge temple tank with a central mandapam, famous for the annual float festival.",
                "duration": "1 hour",
                "bestTime": "Evening",
                "lat": 9.9098,
                "lng": 78.1528
            },
            {
                "name": "Madurai Street Food & Jigarthanda Trail",
                "highlight": "Sample famous Madurai Bun Parotta, Kari Dosa, Murugan Idli, and authentic Famous Jigarthanda.",
                "duration": "2.5 hours",
                "bestTime": "Evening (7 PM onwards)",
                "lat": 9.9200,
                "lng": 78.1220
            }
        ],
        "hotels": [
            {"name": "Heritage Madurai", "type": "Luxury", "price": "₹7,800/night", "rating": "4.7★"},
            {"name": "Courtyard by Marriott Madurai", "type": "Luxury", "price": "₹6,200/night", "rating": "4.6★"},
            {"name": "The Gateway Hotel Pasumalai", "type": "Mid-range", "price": "₹4,100/night", "rating": "4.5★"},
            {"name": "Hotel Supreme Madurai", "type": "Budget-friendly", "price": "₹1,400/night", "rating": "4.2★"}
        ]
    },
    "udaipur": {
        "fullName": "Udaipur, Rajasthan",
        "lat": 24.5854,
        "lng": 73.7125,
        "region": "Rajasthan",
        "climate": "moderate",
        "experience": "relaxation",
        "budget": "high",
        "summary": "The City of Lakes and Venice of the East, surrounded by the Aravalli Hills, palaces, and boat cruises.",
        "attractions": [
            {
                "name": "City Palace of Udaipur",
                "highlight": "Sprawling hilltop palace complex overlooking Lake Pichola with crystal galleries and courtyards.",
                "duration": "3 hours",
                "bestTime": "Morning (9:30 AM)",
                "lat": 24.5764,
                "lng": 73.6835
            },
            {
                "name": "Lake Pichola Boat Cruise & Jag Mandir",
                "highlight": "Magical boat ride past Lake Palace and Jag Mandir island palace.",
                "duration": "2 hours",
                "bestTime": "5:00 PM (Sunset cruise)",
                "lat": 24.5724,
                "lng": 73.6788
            },
            {
                "name": "Saheliyon-ki-Bari (Courtyard of Maidens)",
                "highlight": "Royal ornamental garden with marble fountains, lotus pools, and elephant statues.",
                "duration": "1.5 hours",
                "bestTime": "Morning",
                "lat": 24.6038,
                "lng": 73.6853
            },
            {
                "name": "Monsoon Palace (Sajjangarh)",
                "highlight": "Hilltop fort palace offering breathtaking sunset vistas over the lakes and Aravalli mountain range.",
                "duration": "2.5 hours",
                "bestTime": "4:30 PM - Sunset",
                "lat": 24.5937,
                "lng": 73.6372
            },
            {
                "name": "Bagore Ki Haveli (Dharohar Folk Dance)",
                "highlight": "18th-century waterfront haveli with evening Rajasthani folk dance and puppet show.",
                "duration": "2 hours",
                "bestTime": "6:30 PM",
                "lat": 24.5802,
                "lng": 73.6806
            },
            {
                "name": "Fateh Sagar Lake & Neemach Mata",
                "highlight": "Picturesque artificial lake with Nehru Park island and cable car to hilltop temple.",
                "duration": "2 hours",
                "bestTime": "Evening",
                "lat": 24.6033,
                "lng": 73.6744
            }
        ],
        "hotels": [
            {"name": "Taj Lake Palace, Udaipur", "type": "Luxury", "price": "₹45,000/night", "rating": "4.9★"},
            {"name": "The Oberoi Udaivilas", "type": "Luxury", "price": "₹42,000/night", "rating": "4.9★"},
            {"name": "Fateh Garh Heritage Resort", "type": "Mid-range", "price": "₹6,800/night", "rating": "4.6★"},
            {"name": "Zostel Udaipur", "type": "Budget-friendly", "price": "₹950/night", "rating": "4.6★"}
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
        "summary": "Queen of the Hills and former British summer capital, celebrated for colonial charm, Mall Road, and pine valleys.",
        "attractions": [
            {
                "name": "The Ridge & Mall Road",
                "highlight": "Pedestrian promenade featuring Christ Church, Scandal Point, and mountain viewpoints.",
                "duration": "3 hours",
                "bestTime": "Afternoon & Evening",
                "lat": 31.1044,
                "lng": 77.1746
            },
            {
                "name": "Jakhoo Hill & Temple",
                "highlight": "Highest peak in Shimla with a 108-ft giant Hanuman statue and cable car ride.",
                "duration": "2.5 hours",
                "bestTime": "Morning",
                "lat": 31.1010,
                "lng": 77.1852
            },
            {
                "name": "Kalka-Shimla Toy Train (UNESCO)",
                "highlight": "Historic narrow-gauge railway journey curving through 102 tunnels and lush pine forests.",
                "duration": "3-4 hours",
                "bestTime": "Morning",
                "lat": 31.1030,
                "lng": 77.1640
            },
            {
                "name": "Kufri Adventure Park & Mahasu Peak",
                "highlight": "Snow activities, horse riding, and nature trails with Himalayan wildlife zoo.",
                "duration": "4 hours",
                "bestTime": "Morning",
                "lat": 31.0980,
                "lng": 77.2680
            },
            {
                "name": "Viceregal Lodge (IIAS)",
                "highlight": "Grand Scottish baronial mansion surrounded by manicured botanical gardens.",
                "duration": "2 hours",
                "bestTime": "Morning / 2 PM",
                "lat": 31.1037,
                "lng": 77.1408
            }
        ],
        "hotels": [
            {"name": "Wildflower Hall, An Oberoi Resort", "type": "Luxury", "price": "₹28,000/night", "rating": "4.9★"},
            {"name": "The Cecil - Oberoi Shimla", "type": "Luxury", "price": "₹16,500/night", "rating": "4.8★"},
            {"name": "Radisson Hotel Shimla", "type": "Mid-range", "price": "₹5,800/night", "rating": "4.4★"},
            {"name": "goStops Shimla", "type": "Budget-friendly", "price": "₹850/night", "rating": "4.4★"}
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
        "summary": "Queen of the Nilgiris known for rolling tea estates, toy train rides, botanical gardens, and mist-clad peaks.",
        "attractions": [
            {
                "name": "Nilgiri Mountain Railway (Toy Train)",
                "highlight": "UNESCO World Heritage steam train journey climbing through Nilgiri tea hills.",
                "duration": "3 hours",
                "bestTime": "Morning (9 AM)",
                "lat": 11.4055,
                "lng": 76.6975
            },
            {
                "name": "Ooty Botanical Gardens & Rose Garden",
                "highlight": "55-acre sprawling Victorian gardens with fossilized tree trunk and thousands of rose varieties.",
                "duration": "2.5 hours",
                "bestTime": "Morning / Afternoon",
                "lat": 11.4172,
                "lng": 76.7118
            },
            {
                "name": "Doddabetta Peak",
                "highlight": "Highest mountain peak in the Nilgiri Hills with telescope observatory overlooking valleys.",
                "duration": "2.5 hours",
                "bestTime": "Morning (clear skies)",
                "lat": 11.4014,
                "lng": 76.7371
            },
            {
                "name": "Pykara Lake & Waterfalls",
                "highlight": "Scenic lake with speedboat rides, Toda tribal settlements, and cascading pine-forest falls.",
                "duration": "3.5 hours",
                "bestTime": "Afternoon",
                "lat": 11.4880,
                "lng": 76.5920
            },
            {
                "name": "Ooty Lake & Boat House",
                "highlight": "Serene artificial lake surrounded by eucalyptus trees with pedal and motor boating.",
                "duration": "2 hours",
                "bestTime": "Late afternoon",
                "lat": 11.4075,
                "lng": 76.6872
            }
        ],
        "hotels": [
            {"name": "Savoy - IHCL SeleQtions, Ooty", "type": "Luxury", "price": "₹13,500/night", "rating": "4.8★"},
            {"name": "Sterling Ooty Fern Hill", "type": "Mid-range", "price": "₹5,200/night", "rating": "4.5★"},
            {"name": "Sinclairs Retreat Ooty", "type": "Mid-range", "price": "₹4,200/night", "rating": "4.3★"},
            {"name": "Zostel Ooty", "type": "Budget-friendly", "price": "₹950/night", "rating": "4.5★"}
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
        "summary": "Yoga Capital of the World and adventure hub nestled in Himalayan foothills along the holy Ganga.",
        "attractions": [
            {
                "name": "White Water River Rafting & Cliff Jumping",
                "highlight": "Thrilling 16km/24km rapids (Marine Drive to Shivpuri / Lakshman Jhula) on the Ganges.",
                "duration": "4 hours",
                "bestTime": "Morning (8:30 AM)",
                "lat": 30.1265,
                "lng": 78.3312
            },
            {
                "name": "Triveni Ghat Evening Maha Aarti",
                "highlight": "Spiritual evening river prayer with drums, conch blowing, fire torches, and floating leaf diyas.",
                "duration": "2 hours",
                "bestTime": "5:30 PM",
                "lat": 30.1030,
                "lng": 78.2930
            },
            {
                "name": "Ram Jhula, Lakshman Jhula & Beatles Ashram",
                "highlight": "Iconic suspension bridges and Maharishi Mahesh Yogi Ashram covered in vibrant murals.",
                "duration": "3 hours",
                "bestTime": "Morning / 3 PM",
                "lat": 30.1190,
                "lng": 78.3140
            },
            {
                "name": "Neer Garh Waterfall Trek",
                "highlight": "Cascading jungle waterfall with natural limestone pools for swimming.",
                "duration": "2.5 hours",
                "bestTime": "Morning",
                "lat": 30.1440,
                "lng": 78.3380
            },
            {
                "name": "Bungee Jumping at Jumpin Heights",
                "highlight": "India's highest fixed-platform bungee jump (83 meters) and giant swing in Mohan Chatti.",
                "duration": "3 hours",
                "bestTime": "Morning slot",
                "lat": 30.0540,
                "lng": 78.3970
            }
        ],
        "hotels": [
            {"name": "Ananda in the Himalayas", "type": "Luxury", "price": "₹36,000/night", "rating": "4.9★"},
            {"name": "Taj Rishikesh Resort & Spa", "type": "Luxury", "price": "₹22,000/night", "rating": "4.8★"},
            {"name": "Aloha On The Ganges", "type": "Mid-range", "price": "₹6,500/night", "rating": "4.6★"},
            {"name": "Zostel Rishikesh (Tapovan)", "type": "Budget-friendly", "price": "₹800/night", "rating": "4.6★"}
        ]
    },
    "mumbai": {
        "fullName": "Mumbai, Maharashtra",
        "lat": 18.9220,
        "lng": 72.8347,
        "region": "Maharashtra",
        "climate": "moderate",
        "experience": "entertainment",
        "budget": "high",
        "summary": "The City of Dreams, financial powerhouse, Bollywood capital, and vibrant coastal metropolis.",
        "attractions": [
            {
                "name": "Gateway of India & Taj Mahal Palace",
                "highlight": "Iconic 1924 colonial basalt archway overlooking Mumbai Harbour alongside legendary landmark hotel.",
                "duration": "2 hours",
                "bestTime": "Early morning or Sunset",
                "lat": 18.9220,
                "lng": 72.8347
            },
            {
                "name": "Elephanta Caves",
                "highlight": "UNESCO rock-cut cave temples dedicated to Lord Shiva, reached by scenic 1-hr ferry from Gateway.",
                "duration": "4 hours",
                "bestTime": "Morning ferry (9 AM)",
                "lat": 18.9633,
                "lng": 72.9315
            },
            {
                "name": "Marine Drive & Girgaon Chowpatty",
                "highlight": "The Queen's Necklace promenade, Arabian sea breeze, and famous Mumbai street food (Pav Bhaji, Bhelpuri).",
                "duration": "2.5 hours",
                "bestTime": "Evening sunset",
                "lat": 18.9438,
                "lng": 72.8232
            },
            {
                "name": "Chhatrapati Shivaji Maharaj Terminus (CSMT)",
                "highlight": "UNESCO Victorian Gothic revival architectural masterpiece, stunningly lit up at night.",
                "duration": "1.5 hours",
                "bestTime": "Evening illumination",
                "lat": 18.9400,
                "lng": 72.8354
            },
            {
                "name": "Bandra Bandstand & Bandra-Worli Sea Link",
                "highlight": "Seafront promenade with Bollywood celebrity residences (Mannat, Galaxy) and drive over sea cable bridge.",
                "duration": "2 hours",
                "bestTime": "Late afternoon",
                "lat": 19.0435,
                "lng": 72.8190
            }
        ],
        "hotels": [
            {"name": "The Taj Mahal Palace, Mumbai", "type": "Luxury", "price": "₹26,000/night", "rating": "4.9★"},
            {"name": "The St. Regis Mumbai", "type": "Luxury", "price": "₹16,000/night", "rating": "4.8★"},
            {"name": "Residency Hotel Fort", "type": "Mid-range", "price": "₹4,500/night", "rating": "4.4★"},
            {"name": "Zostel Mumbai (Andheri)", "type": "Budget-friendly", "price": "₹950/night", "rating": "4.5★"}
        ]
    }
}


def _clean_preference_value(val):
    """Normalize preference strings by removing emojis and keywords."""
    if not val:
        return ""
    val = ''.join(char for char in val if ord(char) < 128)
    if '/' in val:
        val = val.split('/')[0]
    val = val.lower().strip()
    if 'hot' in val or 'sunny' in val:
        return 'hot'
    elif 'cold' in val or 'chill' in val or 'cool' in val:
        return 'cold'
    elif 'rainy' in val or 'monsoon' in val or 'rain' in val:
        return 'rainy'
    elif 'moderate' in val or 'pleasant' in val or 'mild' in val:
        return 'moderate'
    elif 'adventure' in val:
        return 'adventure'
    elif 'nature' in val:
        return 'nature'
    elif 'relaxation' in val or 'relax' in val or 'beach' in val:
        return 'relaxation'
    elif 'history' in val or 'culture' in val or 'heritage' in val:
        return 'history'
    elif 'entertainment' in val or 'city' in val:
        return 'entertainment'
    return val


def _find_matched_destination_key(place_query):
    """Fuzzy match place query against our curated knowledge base."""
    if not place_query:
        return None
    q = place_query.lower().strip()
    for key, data in DESTINATIONS_DB.items():
        if key in q or q in key or data["fullName"].lower() in q or q in data["fullName"].lower():
            return key
        if data.get("region") and data["region"].lower() in q:
            return key
    return None


def _call_llm(system_prompt, user_prompt):
    """
    Call Gemini API or OpenAI API based on configured keys.
    Falls back gracefully if neither is available.
    """
    # 1. Try Gemini API first if configured
    if GEMINI_API_KEY:
        try:
            import httpx
            # Using Gemini v1beta REST endpoint
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
            payload = {
                "contents": [
                    {
                        "role": "user",
                        "parts": [{"text": f"{system_prompt}\n\nTask:\n{user_prompt}"}]
                    }
                ],
                "generationConfig": {
                    "temperature": 0.4,
                    "responseMimeType": "application/json"
                }
            }
            res = httpx.post(url, json=payload, timeout=20.0)
            if res.status_code == 200:
                data = res.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                return text
        except Exception as e:
            print("Gemini API call failed:", e)

    # 2. Try OpenAI API if configured
    if OPENAI_API_KEY:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=OPENAI_API_KEY)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.4,
                response_format={"type": "json_object"}
            )
            return response.choices[0].message.content
        except Exception as e:
            print("OpenAI API call failed:", e)

    return None


def _parse_json(text):
    if not text:
        return None
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        return None
    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return None


def recommend_places(preferences):
    """Recommend top 3 destinations tailored to user preferences."""
    system = (
        "You are TripNova's premier India travel planner. Given user preferences, "
        "recommend exactly 3 top famous destinations in India. "
        "Respond ONLY with valid JSON format: "
        '{"places":['
        '{"name":"Destination, State","reason":"Detailed 1-2 sentence explanation why this iconic destination fits",'
        '"tag":"Adventure|Nature|Heritage|Relaxation|Spiritual|Culture","bestSeason":"e.g. Oct-Mar","lat":28.61,"lng":77.20}'
        ']}'
    )
    user = json.dumps(preferences)
    raw = _call_llm(system, user)
    parsed = _parse_json(raw)
    if parsed and "places" in parsed and len(parsed["places"]) >= 3:
        parsed["source"] = "ai"
        return parsed

    # High-quality fallback matching
    climate = _clean_preference_value(preferences.get("climate", ""))
    experience = _clean_preference_value(preferences.get("experience", ""))
    budget = preferences.get("budget", "").lower()
    travel_with = preferences.get("travelWith", "Travellers")

    scored_places = []
    for key, data in DESTINATIONS_DB.items():
        score = 0
        if data.get("climate") == climate:
            score += 3
        if data.get("experience") == experience:
            score += 4
        if data.get("budget") and data["budget"] in budget:
            score += 2
        scored_places.append((score, data))

    # Sort descending by score
    scored_places.sort(key=lambda x: x[0], reverse=True)
    top_3 = scored_places[:3]

    places = []
    for _, data in top_3:
        places.append({
            "name": data["fullName"],
            "reason": data["summary"],
            "tag": data.get("experience", "Explore").title(),
            "bestSeason": "Oct–Mar",
            "lat": data["lat"],
            "lng": data["lng"]
        })

    return {"places": places, "source": "knowledge_engine"}


def generate_itinerary(place, travel_with, days):
    """
    Generate an intelligent, prioritized Day-by-Day itinerary.
    Prioritizes top iconic landmarks per day with accurate coordinates,
    highlights, visiting durations, and recommended hotels.
    """
    days = max(1, min(30, int(days)))

    system = (
        "You are TripNova's expert India travel itinerary generator. "
        f"Generate a realistic, comprehensive, prioritized {days}-day itinerary for {place}, India "
        f"for {travel_with} travellers. "
        "CRITICAL RULES: "
        "1. Prioritize TOP ICONIC, FAMOUS tourist landmarks (e.g. major forts, UNESCO heritage, top beaches, famous temples, major viewpoints). "
        "2. Structure Day 1 with the most iconic must-visit landmarks. Day 2 with major heritage & cultural hubs. Day 3+ with scenic nature, viewpoints, and famous local experiences. "
        "3. Provide exact or realistic latitude and longitude coordinates for the destination city and for each attraction spot so they can be pinned on an interactive map. "
        "4. Include 3-4 top hotels (Luxury, Mid-range, Budget-friendly) with price range and rating. "
        "Respond ONLY with valid JSON schema: "
        '{"place":"City, State","lat":28.6139,"lng":77.2090,'
        '"summary":"Overview of the destination",'
        '"itinerary":['
        '{"day":1,"title":"Iconic Heritage & Landmarks",'
        '"places":['
        '{"name":"Spot Name","highlight":"Why it is a must-visit","duration":"2-3 hours","bestTime":"Morning","lat":28.65,"lng":77.24}'
        ']}'
        '],'
        '"hotels":['
        '{"name":"Hotel Name","type":"Luxury|Mid-range|Budget-friendly","price":"₹X/night","rating":"4.8★"}'
        ']}'
    )

    user = json.dumps({"place": place, "travelWith": travel_with, "days": days})
    raw = _call_llm(system, user)
    parsed = _parse_json(raw)

    if parsed and "itinerary" in parsed and len(parsed["itinerary"]) > 0:
        parsed["source"] = "ai"
        if not parsed.get("place"):
            parsed["place"] = place
        return parsed

    # Curated Knowledge Engine Fallback
    key = _find_matched_destination_key(place)
    if key:
        dest = DESTINATIONS_DB[key]
        all_attractions = dest["attractions"]
        hotels = dest["hotels"]
        dest_lat = dest["lat"]
        dest_lng = dest["lng"]
        full_name = dest["fullName"]
        summary = dest["summary"]

        itinerary = []
        attractions_per_day = 2

        for d in range(1, days + 1):
            start_idx = ((d - 1) * attractions_per_day) % len(all_attractions)
            day_spots = []

            # Pick 2-3 distinct spots for this day
            for offset in range(attractions_per_day):
                spot_idx = (start_idx + offset) % len(all_attractions)
                spot = all_attractions[spot_idx]
                day_spots.append({
                    "name": spot["name"],
                    "highlight": spot["highlight"],
                    "duration": spot.get("duration", "2-3 hours"),
                    "bestTime": spot.get("bestTime", "Morning/Evening"),
                    "lat": spot.get("lat", dest_lat + (offset * 0.015)),
                    "lng": spot.get("lng", dest_lng + (offset * 0.015))
                })

            day_title = "Must-Visit Highlights" if d == 1 else ("Cultural & Heritage Exploration" if d == 2 else f"Scenic Discoveries & Local Vibe (Day {d})")
            itinerary.append({
                "day": d,
                "title": day_title,
                "places": day_spots
            })

        return {
            "place": full_name,
            "lat": dest_lat,
            "lng": dest_lng,
            "summary": summary,
            "itinerary": itinerary,
            "hotels": hotels,
            "source": "knowledge_engine"
        }

    # Dynamic algorithmic generation for any custom Indian place
    dest_name = place.title()
    approx_lat = 20.5937
    approx_lng = 78.9629

    dynamic_itinerary = []
    for d in range(1, days + 1):
        if d == 1:
            spots = [
                {"name": f"Iconic Landmark & Center of {dest_name}", "highlight": f"Top historic monument and central tourist highlight of {dest_name}.", "duration": "2.5 hours", "bestTime": "Morning", "lat": approx_lat + 0.01, "lng": approx_lng + 0.01},
                {"name": f"{dest_name} Heritage Fort / Palace", "highlight": "Major historical architectural attraction with panoramic views.", "duration": "3 hours", "bestTime": "Afternoon", "lat": approx_lat - 0.01, "lng": approx_lng + 0.01}
            ]
            title = "Historic Highlights & Main Sights"
        elif d == 2:
            spots = [
                {"name": f"{dest_name} Botanical Nature Sanctuary", "highlight": "Serene natural reserve, viewpoints, and walking trails.", "duration": "3 hours", "bestTime": "Morning", "lat": approx_lat + 0.02, "lng": approx_lng - 0.01},
                {"name": f"Traditional Bazaar & Food Trail of {dest_name}", "highlight": "Famous local markets, authentic cuisine, and artisan handicrafts.", "duration": "2.5 hours", "bestTime": "Evening", "lat": approx_lat, "lng": approx_lng}
            ]
            title = "Nature Trails & Cultural Bazaars"
        else:
            spots = [
                {"name": f"Scenic Sunset Viewpoint in {dest_name}", "highlight": "Breathtaking panoramic viewpoints and photography spot.", "duration": "2 hours", "bestTime": "Late Afternoon", "lat": approx_lat - 0.02, "lng": approx_lng - 0.02},
                {"name": f"Ancient Temple & Spiritual Center of {dest_name}", "highlight": "Sacred cultural temple known for rich Dravidian/Nagara architecture.", "duration": "2 hours", "bestTime": "Morning", "lat": approx_lat + 0.015, "lng": approx_lng - 0.015}
            ]
            title = f"Scenic Viewpoints & Hidden Gems (Day {d})"

        dynamic_itinerary.append({
            "day": d,
            "title": title,
            "places": spots
        })

    dynamic_hotels = [
        {"name": f"Grand Heritage Palace {dest_name}", "type": "Luxury", "price": "₹8,500/night", "rating": "4.8★"},
        {"name": f"The Royal Residency {dest_name}", "type": "Mid-range", "price": "₹3,400/night", "rating": "4.5★"},
        {"name": f"TripNova Comfort Stay {dest_name}", "type": "Budget-friendly", "price": "₹1,200/night", "rating": "4.3★"}
    ]

    return {
        "place": dest_name,
        "lat": approx_lat,
        "lng": approx_lng,
        "summary": f"A vibrant destination in India with cultural heritage, scenic landmarks, and local flavors.",
        "itinerary": dynamic_itinerary,
        "hotels": dynamic_hotels,
        "source": "dynamic_engine"
    }


def explain_unsuitable_place(preferences, place_name):
    """Explain why a particular place might not match user preferences."""
    system = (
        "You are TripNova's expert India travel advisor. Explain constructively in 2-3 friendly sentences "
        "why a given destination might not perfectly match the user's selected preferences (climate, budget, companions, vibe)."
    )
    user = f"Preferences: {json.dumps(preferences)}\nPlace asked: {place_name}"
    raw = _call_llm(system, user)
    if raw:
        # Check if json or plain text
        parsed = _parse_json(raw)
        if parsed and "answer" in parsed:
            return {"answer": parsed["answer"], "source": "ai"}
        return {"answer": raw.strip().strip('"'), "source": "ai"}

    return {
        "answer": (
            f"While {place_name} is a wonderful place, it may not best match your preference for "
            f"{preferences.get('climate', 'your chosen climate')} climate and {preferences.get('experience', 'chosen vibe')} "
            f"style travelling as {preferences.get('travelWith', 'a group')} on a {preferences.get('budget', 'budget')} plan."
        ),
        "source": "fallback",
    }


def general_chat(message, context=None):
    """AI Co-Pilot chat assistant for India travel inquiries."""
    system = (
        "You are TripNova's AI Travel Co-Pilot. Answer questions about travelling in India "
        "(itineraries, transport, buses, trains, IRCTC, RedBus, hotels, local cuisine, safety, seasons). "
        "Keep answers concise, engaging, helpful, and formatted with bullet points if helpful."
    )
    user = message
    if context:
        user = f"Context: {json.dumps(context)}\n\nQuestion: {message}"

    raw = _call_llm(system, user)
    if raw:
        parsed = _parse_json(raw)
        if parsed and "answer" in parsed:
            return {"answer": parsed["answer"], "source": "ai"}
        return {"answer": raw.strip().strip('"'), "source": "ai"}

    msg_lower = message.lower()
    if any(w in msg_lower for w in ["bus", "redbus", "seat", "route"]):
        return {
            "answer": "You can book buses directly in TripNova under 'Bus Booking'! We support RedBus and top operators like IntrCity, Zingbus, KSRTC, and VRL with live seat selection and boarding points.",
            "source": "fallback"
        }
    elif any(w in msg_lower for w in ["train", "irctc", "pnr", "rail"]):
        return {
            "answer": "TripNova includes a built-in IRCTC train booking engine under 'Train Booking'! You can search train schedules, check real-time seat availability across 1A/2A/3A/SL classes, and track live PNR status.",
            "source": "fallback"
        }
    elif any(w in msg_lower for w in ["hotel", "stay", "room", "oyo", "taj"]):
        return {
            "answer": "Use our 'Hotels' tab to search luxury resorts, boutique heritage stays, and budget-friendly hotels with instant in-app booking and transparent pricing.",
            "source": "fallback"
        }
    elif any(w in msg_lower for w in ["manali", "goa", "kerala", "jaipur", "delhi", "varanasi", "madurai", "ooty", "rishikesh", "udaipur"]):
        return {
            "answer": f"Great choice! Visit the 'Places to Visit' tab to generate a complete day-by-day itinerary with interactive map pinning and top hotel recommendations.",
            "source": "fallback"
        }
    else:
        return {
            "answer": "Welcome to TripNova! Ask me anything about Indian destinations, best travel seasons, bus & train routes, budget tips, or customized day-wise itineraries.",
            "source": "fallback"
        }

