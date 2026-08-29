# -*- coding: utf-8 -*-
import json
import os
import update_db

# India Destinations
INDIA_PLACES = {
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
            {"name": "Solang Valley", "highlight": "Famous hub for paragliding, zorbing, quad biking, and winter skiing.", "duration": "4-5 hours", "bestTime": "Morning", "lat": 32.3166, "lng": 77.1578},
            {"name": "Rohtang Pass", "highlight": "High-altitude mountain pass offering panoramic Himalayan glaciers and snow viewpoints (permit required).", "duration": "Half day", "bestTime": "Early morning (7 AM)", "lat": 32.3716, "lng": 77.2466},
            {"name": "Hadimba Temple & Van Vihar", "highlight": "Ancient 16th-century wooden pagoda temple nestled inside dense cedar forests.", "duration": "2 hours", "bestTime": "Morning / Afternoon", "lat": 32.2483, "lng": 77.1705},
            {"name": "Old Manali & Cafe Trail", "highlight": "Bohemian village atmosphere with wooden houses, vibrant cafes, and live acoustic music.", "duration": "3 hours", "bestTime": "Evening", "lat": 32.2530, "lng": 77.1750},
            {"name": "Jogini Waterfalls & Vashisht Hot Springs", "highlight": "Scenic nature trek leading to a cascading waterfall and natural sulphur hot baths.", "duration": "3-4 hours", "bestTime": "Morning", "lat": 32.2660, "lng": 77.1870},
            {"name": "Atal Tunnel & Sissu (Lahaul Valley)", "highlight": "World's longest highway tunnel above 10,000 ft connecting to majestic waterfalls in Sissu.", "duration": "4-5 hours", "bestTime": "Morning", "lat": 32.4833, "lng": 77.1264}
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
            {"name": "Baga & Calangute Beach", "highlight": "Energetic golden beaches with water sports, beach shacks, and live sunset music.", "duration": "3-4 hours", "bestTime": "Late afternoon to Sunset", "lat": 15.5523, "lng": 73.7517},
            {"name": "Fort Aguada & Lighthouse", "highlight": "17th-century Portuguese fortress with sweeping panoramic views over the Arabian Sea.", "duration": "2 hours", "bestTime": "Morning / 4 PM", "lat": 15.4920, "lng": 73.7737},
            {"name": "Basilica of Bom Jesus & Old Goa", "highlight": "UNESCO World Heritage Baroque church housing the sacred relics of St. Francis Xavier.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 15.5009, "lng": 73.9116},
            {"name": "Dudhsagar Waterfalls", "highlight": "Magnificent four-tiered waterfall cascading down 310 meters amidst lush jungle canopy.", "duration": "Full day", "bestTime": "Early morning jeep safari", "lat": 15.3144, "lng": 74.3143},
            {"name": "Palolem Beach (South Goa)", "highlight": "Serene crescent-shaped beach famous for calm waters, dolphin spotting, and beach yoga.", "duration": "Half day", "bestTime": "Sunset", "lat": 15.0100, "lng": 74.0232},
            {"name": "Anjuna Flea Market & Chapora Fort", "highlight": "Iconic cliffside fort overlooking the sea ('Dil Chahta Hai' fame) and vibrant market.", "duration": "3 hours", "bestTime": "5 PM", "lat": 15.6059, "lng": 73.7386}
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
            {"name": "Amber Fort & Palace", "highlight": "Magnificent hilltop fort with Sheesh Mahal (Mirror Palace) and elephant/jeep ascents.", "duration": "3.5 hours", "bestTime": "Morning (8:30 AM)", "lat": 26.9855, "lng": 75.8513},
            {"name": "Hawa Mahal (Palace of Winds)", "highlight": "Iconic 5-story honeycomb facade with 953 intricately carved jharokhas.", "duration": "1.5 hours", "bestTime": "Morning for best lighting", "lat": 26.9239, "lng": 75.8267},
            {"name": "City Palace & Jantar Mantar", "highlight": "Royal residence museum displaying Rajput history and UNESCO astronomical observatory.", "duration": "3 hours", "bestTime": "Afternoon", "lat": 26.9258, "lng": 75.8236},
            {"name": "Nahargarh Fort Sunset Viewpoint", "highlight": "Hilltop fort offering spectacular panoramic sunset views of the entire Jaipur city.", "duration": "2.5 hours", "bestTime": "5:00 PM - Sunset", "lat": 26.9372, "lng": 75.8155},
            {"name": "Albert Hall Museum & Johari Bazaar", "highlight": "Indo-Saracenic museum illuminated by night and world-famous gemstone/textile bazaar.", "duration": "2.5 hours", "bestTime": "Evening", "lat": 26.9116, "lng": 75.8195},
            {"name": "Jal Mahal (Water Palace)", "highlight": "Enchanting palace floating in the middle of Man Sagar Lake.", "duration": "1 hour", "bestTime": "Morning / Evening promenade", "lat": 26.9534, "lng": 75.8462}
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
            {"name": "Red Fort & Jama Masjid", "highlight": "Massive 17th-century Mughal sandstone citadel and India's largest historic mosque.", "duration": "3.5 hours", "bestTime": "Morning", "lat": 28.6562, "lng": 77.2410},
            {"name": "Qutub Minar & Mehrauli Archaeological Park", "highlight": "UNESCO World Heritage 73m victory minaret with 12th-century Iron Pillar and ruins.", "duration": "2.5 hours", "bestTime": "Morning / Late Afternoon", "lat": 28.5244, "lng": 77.1855},
            {"name": "Humayun's Tomb", "highlight": "Sublime Mughal garden tomb and architectural predecessor to the Taj Mahal.", "duration": "2 hours", "bestTime": "Afternoon to Sunset", "lat": 28.5933, "lng": 77.2507},
            {"name": "India Gate & Kartavya Path", "highlight": "Iconic war memorial archway surrounded by sprawling ceremonial lawns and fountain walks.", "duration": "1.5 hours", "bestTime": "Evening (6 PM onwards)", "lat": 28.6129, "lng": 77.2295},
            {"name": "Swaminarayan Akshardham Temple", "highlight": "Grand modern spiritual monument with musical water show and boat ride through Vedic history.", "duration": "4 hours", "bestTime": "Afternoon till night show", "lat": 28.6127, "lng": 77.2773},
            {"name": "Lotus Temple & Hauz Khas Village", "highlight": "Bahá'í House of Worship shaped like a lotus, followed by medieval reservoir lake & hip cafes.", "duration": "3 hours", "bestTime": "Afternoon / Sunset", "lat": 28.5535, "lng": 77.2588}
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
            {"name": "The Taj Mahal", "highlight": "One of the Seven Wonders of the World; marble mausoleum built by Shah Jahan for Mumtaz Mahal.", "duration": "3 hours", "bestTime": "Sunrise (6:00 AM) or Full Moon night", "lat": 27.1751, "lng": 78.0421},
            {"name": "Agra Fort", "highlight": "Expansive red sandstone fortress containing Jahangiri Mahal, Khas Mahal, and Taj viewpoints.", "duration": "2.5 hours", "bestTime": "Morning / 3 PM", "lat": 27.1795, "lng": 78.0211},
            {"name": "Fatehpur Sikri", "highlight": "Preserved Mughal imperial city with Buland Darwaza (world's tallest gateway) and Salim Chishti Dargah.", "duration": "3.5 hours", "bestTime": "Morning", "lat": 27.0945, "lng": 77.6679},
            {"name": "Mehtab Bagh (Moonlight Garden)", "highlight": "Botanical garden across the Yamuna River offering picturesque sunset silhouettes of the Taj.", "duration": "1.5 hours", "bestTime": "Sunset (5:30 PM)", "lat": 27.1800, "lng": 78.0416}
        ],
        "hotels": [
            {"name": "The Oberoi Amarvilas, Agra", "type": "Luxury", "price": "₹38,000/night", "rating": "4.9★"},
            {"name": "Taj Hotel & Convention Centre", "type": "Luxury", "price": "₹7,200/night", "rating": "4.6★"},
            {"name": "Howard Plaza - The Fern", "type": "Mid-range", "price": "₹3,100/night", "rating": "4.3★"}
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
            {"name": "Alleppey Backwaters & Houseboat Cruise", "highlight": "Iconic traditional Kettuvallam houseboat stay cruising through tranquil lagoons and paddy fields.", "duration": "Full day / Overnight", "bestTime": "Afternoon to Morning", "lat": 9.4981, "lng": 76.3388},
            {"name": "Munnar Tea Plantations & Eravikulam National Park", "highlight": "Lush mist-covered tea gardens and home to the endangered Nilgiri Tahr mountain goat.", "duration": "4-5 hours", "bestTime": "Morning (8 AM)", "lat": 10.0889, "lng": 77.0595},
            {"name": "Fort Kochi & Chinese Fishing Nets", "highlight": "Colonial Dutch/Portuguese heritage, historic St. Francis Church, and sunset harbor views.", "duration": "3 hours", "bestTime": "Evening", "lat": 9.9658, "lng": 76.2421},
            {"name": "Mattupetty Dam & Top Station (Munnar)", "highlight": "Scenic lake with boating and highest viewpoint on the Munnar-Kodaikanal road.", "duration": "3 hours", "bestTime": "Afternoon", "lat": 10.1060, "lng": 77.1240}
        ],
        "hotels": [
            {"name": "Kumarakom Lake Resort", "type": "Luxury", "price": "₹22,000/night", "rating": "4.9★"},
            {"name": "Fragrant Nature Munnar", "type": "Luxury", "price": "₹9,800/night", "rating": "4.7★"},
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
            {"name": "Dashashwamedh Ghat & Evening Ganga Aarti", "highlight": "Mesmerizing multi-priest synchronized fire ritual with chanting, bells, and floating lamps on the river.", "duration": "2.5 hours", "bestTime": "6:00 PM (arrive by 5:30 PM)", "lat": 25.3073, "lng": 83.0104},
            {"name": "Sunrise Boat Ride on the Ganga", "highlight": "Morning boat ride capturing spiritual life across 84 historic ghats from Assi to Manikarnika.", "duration": "2 hours", "bestTime": "5:30 AM Sunrise", "lat": 25.2899, "lng": 83.0069},
            {"name": "Kashi Vishwanath Golden Temple", "highlight": "One of the 12 sacred Jyotirlingas of Lord Shiva with magnificent newly renovated Corridor.", "duration": "2.5 hours", "bestTime": "Early morning (7 AM)", "lat": 25.3109, "lng": 83.0107},
            {"name": "Sarnath (Dhamek Stupa & Deer Park)", "highlight": "Sacred Buddhist site where Lord Buddha delivered his first sermon; Museum with Ashoka Lion Capital.", "duration": "3 hours", "bestTime": "Morning / 2 PM", "lat": 25.3811, "lng": 83.0227}
        ],
        "hotels": [
            {"name": "BrijRama Palace, Varanasi", "type": "Luxury", "price": "₹24,000/night", "rating": "4.9★"},
            {"name": "Taj Ganges, Varanasi", "type": "Luxury", "price": "₹12,500/night", "rating": "4.7★"},
            {"name": "Hotel Surya, Kaiser Palace", "type": "Mid-range", "price": "₹3,400/night", "rating": "4.4★"}
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
            {"name": "City Palace of Udaipur", "highlight": "Sprawling hilltop palace complex overlooking Lake Pichola with crystal galleries and courtyards.", "duration": "3 hours", "bestTime": "Morning (9:30 AM)", "lat": 24.5764, "lng": 73.6835},
            {"name": "Lake Pichola Boat Cruise & Jag Mandir", "highlight": "Magical boat ride past Lake Palace and Jag Mandir island palace.", "duration": "2 hours", "bestTime": "5:00 PM (Sunset cruise)", "lat": 24.5724, "lng": 73.6788},
            {"name": "Saheliyon-ki-Bari (Courtyard of Maidens)", "highlight": "Royal ornamental garden with marble fountains, lotus pools, and elephant statues.", "duration": "1.5 hours", "bestTime": "Morning", "lat": 24.6038, "lng": 73.6853},
            {"name": "Monsoon Palace (Sajjangarh)", "highlight": "Hilltop fort palace offering breathtaking sunset vistas over the lakes and Aravalli mountain range.", "duration": "2.5 hours", "bestTime": "4:30 PM - Sunset", "lat": 24.5937, "lng": 73.6372}
        ],
        "hotels": [
            {"name": "Taj Lake Palace, Udaipur", "type": "Luxury", "price": "₹45,000/night", "rating": "4.9★"},
            {"name": "The Oberoi Udaivilas", "type": "Luxury", "price": "₹42,000/night", "rating": "4.9★"},
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
            {"name": "The Ridge & Mall Road", "highlight": "Pedestrian promenade featuring Christ Church, Scandal Point, and mountain viewpoints.", "duration": "3 hours", "bestTime": "Afternoon & Evening", "lat": 31.1044, "lng": 77.1746},
            {"name": "Jakhoo Hill & Temple", "highlight": "Highest peak in Shimla with a 108-ft giant Hanuman statue and cable car ride.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 31.1010, "lng": 77.1852},
            {"name": "Kalka-Shimla Toy Train (UNESCO)", "highlight": "Historic narrow-gauge railway journey curving through 102 tunnels and lush pine forests.", "duration": "3-4 hours", "bestTime": "Morning", "lat": 31.1030, "lng": 77.1640},
            {"name": "Kufri Adventure Park & Mahasu Peak", "highlight": "Snow activities, horse riding, and nature trails with Himalayan wildlife zoo.", "duration": "4 hours", "bestTime": "Morning", "lat": 31.0980, "lng": 77.2680}
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
        "summary": "Yoga Capital of the World and adventure hub nestled in Himalayan foothills along the holy Ganga.",
        "attractions": [
            {"name": "White Water River Rafting & Cliff Jumping", "highlight": "Thrilling 16km/24km rapids (Marine Drive to Shivpuri / Lakshman Jhula) on the Ganges.", "duration": "4 hours", "bestTime": "Morning (8:30 AM)", "lat": 30.1265, "lng": 78.3312},
            {"name": "Triveni Ghat Evening Maha Aarti", "highlight": "Spiritual evening river prayer with drums, conch blowing, fire torches, and floating leaf diyas.", "duration": "2 hours", "bestTime": "5:30 PM", "lat": 30.1030, "lng": 78.2930},
            {"name": "Ram Jhula, Lakshman Jhula & Beatles Ashram", "highlight": "Iconic suspension bridges and Maharishi Mahesh Yogi Ashram covered in vibrant murals.", "duration": "3 hours", "bestTime": "Morning / 3 PM", "lat": 30.1190, "lng": 78.3140}
        ],
        "hotels": [
            {"name": "Ananda in the Himalayas", "type": "Luxury", "price": "₹36,000/night", "rating": "4.9★"},
            {"name": "Aloha On The Ganges", "type": "Mid-range", "price": "₹6,500/night", "rating": "4.6★"}
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
            {"name": "Gateway of India & Taj Mahal Palace", "highlight": "Iconic 1924 colonial basalt archway overlooking Mumbai Harbour alongside legendary landmark hotel.", "duration": "2 hours", "bestTime": "Early morning or Sunset", "lat": 18.9220, "lng": 72.8347},
            {"name": "Elephanta Caves", "highlight": "UNESCO rock-cut cave temples dedicated to Lord Shiva, reached by scenic 1-hr ferry from Gateway.", "duration": "4 hours", "bestTime": "Morning ferry (9 AM)", "lat": 18.9633, "lng": 72.9315},
            {"name": "Marine Drive & Girgaon Chowpatty", "highlight": "The Queen's Necklace promenade, Arabian sea breeze, and famous Mumbai street food (Pav Bhaji, Bhelpuri).", "duration": "2.5 hours", "bestTime": "Evening sunset", "lat": 18.9438, "lng": 72.8232}
        ],
        "hotels": [
            {"name": "The Taj Mahal Palace, Mumbai", "type": "Luxury", "price": "₹26,000/night", "rating": "4.9★"},
            {"name": "The St. Regis Mumbai", "type": "Luxury", "price": "₹16,000/night", "rating": "4.8★"}
        ]
    }
}

# Merge Tamil Nadu + India destinations
COMBINED_DB = {}
# Put Tamil Nadu places first for high priority matching
for k, v in update_db.TAMIL_NADU_PLACES.items():
    COMBINED_DB[k] = v
for k, v in INDIA_PLACES.items():
    if k not in COMBINED_DB:
        COMBINED_DB[k] = v

print(f"Total merged destinations: {len(COMBINED_DB)}")

# Generate backend/ai_service.py
ai_service_code = f'''import json
import os
import re
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")


# -------------------------------------------------------------------------
# Comprehensive Curated Knowledge Base for Tamil Nadu & Indian Destinations
# Contains verified coordinates, top iconic attractions prioritized by importance,
# detailed descriptions, best visiting hours, and top-rated hotels.
# -------------------------------------------------------------------------
DESTINATIONS_DB = {json.dumps(COMBINED_DB, indent=4, ensure_ascii=False)}


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
    """Fuzzy match place query against our curated knowledge base with Tamil Nadu aliases."""
    if not place_query:
        return None
    q = place_query.lower().strip()

    # Direct / Alias mappings
    aliases = {{
        "tanjore": "thanjavur",
        "trichy": "trichy",
        "tiruchirappalli": "trichy",
        "tiruchirapalli": "trichy",
        "kutralam": "courtallam",
        "courtallam": "courtallam",
        "tenkasi": "courtallam",
        "mamallapuram": "mahabalipuram",
        "mahabalipuram": "mahabalipuram",
        "rameshwaram": "rameswaram",
        "rameswaram": "rameswaram",
        "kodai": "kodaikanal",
        "kodaikanal": "kodaikanal",
        "udhagamandalam": "ooty",
        "ooty": "ooty",
        "pollachi": "valparai",
        "valparai": "valparai",
        "karaikudi": "chettinad",
        "chettinad": "chettinad",
        "kolli": "kolli hills",
        "kolli malai": "kolli hills",
        "namakkal": "kolli hills",
        "dharmapuri": "hogenakkal",
        "pichavaram": "chidambaram",
        "tamilnadu": "tamil nadu",
        "tamil nadu": "tamil nadu",
    }}

    for alias_key, target_key in aliases.items():
        if alias_key in q or q in alias_key:
            if target_key in DESTINATIONS_DB:
                return target_key

    # Standard loop matching
    for key, data in DESTINATIONS_DB.items():
        if key in q or q in key or data["fullName"].lower() in q or q in data["fullName"].lower():
            return key
        if data.get("region") and data["region"].lower() in q:
            return key
    return None


def _call_llm(system_prompt, user_prompt):
    """Call Gemini API or OpenAI API based on configured keys."""
    # 1. Try Gemini API first if configured
    if GEMINI_API_KEY:
        try:
            import httpx
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={{GEMINI_API_KEY}}"
            payload = {{
                "contents": [
                    {{
                        "role": "user",
                        "parts": [{{"text": f"{{system_prompt}}\\n\\nTask:\\n{{user_prompt}}"}}]
                    }}
                ],
                "generationConfig": {{
                    "temperature": 0.4,
                    "responseMimeType": "application/json"
                }}
            }}
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
                    {{"role": "system", "content": system_prompt}},
                    {{"role": "user", "content": user_prompt}},
                ],
                temperature=0.4,
                response_format={{"type": "json_object"}}
            )
            return response.choices[0].message.content
        except Exception as e:
            print("OpenAI API call failed:", e)

    return None


def _parse_json(text):
    if not text:
        return None
    match = re.search(r"\\{{[\\s\\S]*\\}}", text)
    if not match:
        return None
    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return None


def recommend_places(preferences):
    """Recommend top 3 destinations tailored to user preferences."""
    system = (
        "You are TripNova's premier India and Tamil Nadu travel planner. Given user preferences, "
        "recommend exactly 3 top famous destinations. "
        "Respond ONLY with valid JSON format: "
        '{{"places":['
        '{{"name":"Destination, State","reason":"Detailed explanation why it fits",'
        '"tag":"Adventure|Nature|Heritage|Relaxation|Spiritual|Culture","bestSeason":"e.g. Oct-Mar","lat":13.08,"lng":80.27}}'
        ']}}'
    )
    user = json.dumps(preferences)
    raw = _call_llm(system, user)
    parsed = _parse_json(raw)
    if parsed and "places" in parsed and len(parsed["places"]) >= 3:
        parsed["source"] = "ai"
        return parsed

    # High-quality knowledge engine matching
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

    scored_places.sort(key=lambda x: x[0], reverse=True)
    top_3 = scored_places[:3]

    places = []
    for _, data in top_3:
        places.append({{
            "name": data["fullName"],
            "reason": data["summary"],
            "tag": data.get("experience", "Explore").title(),
            "bestSeason": "Oct–Mar",
            "lat": data["lat"],
            "lng": data["lng"]
        }})

    return {{"places": places, "source": "knowledge_engine"}}


def generate_itinerary(place, travel_with, days):
    """
    Generate an intelligent, prioritized Day-by-Day itinerary.
    Prioritizes top iconic landmarks per day with accurate coordinates,
    highlights, visiting durations, and recommended hotels.
    """
    days = max(1, min(30, int(days)))

    system = (
        "You are TripNova's expert travel itinerary generator. "
        f"Generate a realistic, comprehensive, prioritized {{days}}-day itinerary for {{place}}, India "
        f"for {{travel_with}} travellers. "
        "CRITICAL RULES: "
        "1. Prioritize TOP ICONIC, FAMOUS tourist landmarks (e.g. major forts, UNESCO heritage, temples, beaches, viewpoints). "
        "2. Structure Day 1 with the most iconic must-visit landmarks. Day 2 with major heritage & cultural hubs. Day 3+ with scenic nature, viewpoints, and local experiences. "
        "3. Provide exact or realistic latitude and longitude coordinates for the destination city and for each attraction spot so they can be pinned on an interactive map. "
        "4. Include 3-4 top hotels (Luxury, Mid-range, Budget-friendly) with price range and rating. "
        "Respond ONLY with valid JSON schema: "
        '{{"place":"City, State","lat":13.0827,"lng":80.2707,'
        '"summary":"Overview of the destination",'
        '"itinerary":['
        '{{"day":1,"title":"Iconic Heritage & Landmarks",'
        '"places":['
        '{{"name":"Spot Name","highlight":"Why it is a must-visit","duration":"2-3 hours","bestTime":"Morning","lat":13.05,"lng":80.28}}'
        ']}}'
        '],'
        '"hotels":['
        '{{"name":"Hotel Name","type":"Luxury|Mid-range|Budget-friendly","price":"₹X/night","rating":"4.8★"}}'
        ']}}'
    )

    user = json.dumps({{"place": place, "travelWith": travel_with, "days": days}})
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

            for offset in range(attractions_per_day):
                spot_idx = (start_idx + offset) % len(all_attractions)
                spot = all_attractions[spot_idx]
                day_spots.append({{
                    "name": spot["name"],
                    "highlight": spot["highlight"],
                    "duration": spot.get("duration", "2-3 hours"),
                    "bestTime": spot.get("bestTime", "Morning/Evening"),
                    "lat": spot.get("lat", dest_lat + (offset * 0.015)),
                    "lng": spot.get("lng", dest_lng + (offset * 0.015))
                }})

            day_title = "Must-Visit Highlights" if d == 1 else ("Cultural & Heritage Exploration" if d == 2 else f"Scenic Discoveries & Local Vibe (Day {{d}})")
            itinerary.append({{
                "day": d,
                "title": day_title,
                "places": day_spots
            }})

        return {{
            "place": full_name,
            "lat": dest_lat,
            "lng": dest_lng,
            "summary": summary,
            "itinerary": itinerary,
            "hotels": hotels,
            "source": "knowledge_engine"
        }}

    # Dynamic algorithmic generation for any custom Indian or Tamil Nadu place
    dest_name = place.title()
    approx_lat = 11.1271 if "tamil" in place.lower() else 20.5937
    approx_lng = 78.6569 if "tamil" in place.lower() else 78.9629

    dynamic_itinerary = []
    for d in range(1, days + 1):
        if d == 1:
            spots = [
                {{"name": f"Iconic Landmark & Center of {{dest_name}}", "highlight": f"Top historic monument and central tourist highlight of {{dest_name}}.", "duration": "2.5 hours", "bestTime": "Morning", "lat": approx_lat + 0.01, "lng": approx_lng + 0.01}},
                {{"name": f"{{dest_name}} Heritage Fort / Temple", "highlight": "Major historical architectural attraction with panoramic views.", "duration": "3 hours", "bestTime": "Afternoon", "lat": approx_lat - 0.01, "lng": approx_lng + 0.01}}
            ]
            title = "Historic Highlights & Main Sights"
        elif d == 2:
            spots = [
                {{"name": f"{{dest_name}} Nature Reserve & Viewpoint", "highlight": "Serene natural reserve, viewpoints, and walking trails.", "duration": "3 hours", "bestTime": "Morning", "lat": approx_lat + 0.02, "lng": approx_lng - 0.01}},
                {{"name": f"Traditional Bazaar & Food Trail of {{dest_name}}", "highlight": "Famous local markets, authentic cuisine, and artisan handicrafts.", "duration": "2.5 hours", "bestTime": "Evening", "lat": approx_lat, "lng": approx_lng}}
            ]
            title = "Nature Trails & Cultural Bazaars"
        else:
            spots = [
                {{"name": f"Scenic Sunset Viewpoint in {{dest_name}}", "highlight": "Breathtaking panoramic viewpoints and photography spot.", "duration": "2 hours", "bestTime": "Late Afternoon", "lat": approx_lat - 0.02, "lng": approx_lng - 0.02}},
                {{"name": f"Ancient Spiritual Center of {{dest_name}}", "highlight": "Sacred cultural temple known for rich Dravidian architecture.", "duration": "2 hours", "bestTime": "Morning", "lat": approx_lat + 0.015, "lng": approx_lng - 0.015}}
            ]
            title = f"Scenic Viewpoints & Hidden Gems (Day {{d}})"

        dynamic_itinerary.append({{
            "day": d,
            "title": title,
            "places": spots
        }})

    dynamic_hotels = [
        {{"name": f"Grand Heritage Stay {{dest_name}}", "type": "Luxury", "price": "₹6,500/night", "rating": "4.8★"}},
        {{"name": f"The Residency {{dest_name}}", "type": "Mid-range", "price": "₹3,200/night", "rating": "4.5★"}},
        {{"name": f"TripNova Comfort Stay {{dest_name}}", "type": "Budget-friendly", "price": "₹1,200/night", "rating": "4.3★"}}
    ]

    return {{
        "place": dest_name,
        "lat": approx_lat,
        "lng": approx_lng,
        "summary": f"A vibrant destination in Tamil Nadu / India with cultural heritage, scenic landmarks, and local flavors.",
        "itinerary": dynamic_itinerary,
        "hotels": dynamic_hotels,
        "source": "dynamic_engine"
    }}


def explain_unsuitable_place(preferences, place_name):
    """Explain why a particular place might not match user preferences."""
    system = (
        "You are TripNova's expert travel advisor. Explain constructively in 2-3 friendly sentences "
        "why a given destination might not perfectly match the user's selected preferences (climate, budget, companions, vibe)."
    )
    user = f"Preferences: {{json.dumps(preferences)}}\\nPlace asked: {{place_name}}"
    raw = _call_llm(system, user)
    if raw:
        parsed = _parse_json(raw)
        if parsed and "answer" in parsed:
            return {{"answer": parsed["answer"], "source": "ai"}}
        return {{"answer": raw.strip().strip('"'), "source": "ai"}}

    return {{
        "answer": (
            f"While {{place_name}} is a wonderful place, it may not best match your preference for "
            f"{{preferences.get('climate', 'your chosen climate')}} climate and {{preferences.get('experience', 'chosen vibe')}} "
            f"style travelling as {{preferences.get('travelWith', 'a group')}} on a {{preferences.get('budget', 'budget')}} plan."
        ),
        "source": "fallback",
    }}


def general_chat(message, context=None):
    """AI Co-Pilot chat assistant for India & Tamil Nadu travel inquiries."""
    system = (
        "You are TripNova's AI Travel Co-Pilot. Answer questions about travelling in India and Tamil Nadu "
        "(itineraries, transport, buses, trains, IRCTC, RedBus, hotels, local cuisine, safety, seasons, temples, hill stations). "
        "Keep answers concise, engaging, helpful, and formatted with bullet points if helpful."
    )
    user = message
    if context:
        user = f"Context: {{json.dumps(context)}}\\n\\nQuestion: {{message}}"

    raw = _call_llm(system, user)
    if raw:
        parsed = _parse_json(raw)
        if parsed and "answer" in parsed:
            return {{"answer": parsed["answer"], "source": "ai"}}
        return {{"answer": raw.strip().strip('"'), "source": "ai"}}

    msg_lower = message.lower()
    if any(w in msg_lower for w in ["tamil nadu", "tamilnadu", "madurai", "ooty", "kodai", "chennai", "rameswaram", "kanyakumari", "thanjavur", "coimbatore"]):
        return {{
            "answer": "Tamil Nadu has incredible destinations: Ooty and Kodaikanal for mist-clad hill retreats, Madurai and Thanjavur for historic Chola/Pandya temples, Rameswaram and Kanyakumari for sacred coastal wonders, and Chennai for vibrant coastal culture! Check 'Places to Visit' for a day-wise itinerary.",
            "source": "fallback"
        }}
    elif any(w in msg_lower for w in ["bus", "redbus", "seat", "route"]):
        return {{
            "answer": "You can book buses directly in TripNova under 'Bus Booking'! We support RedBus and top operators like SETC, KSRTC, IntrCity, and Zingbus with live seat selection and boarding points.",
            "source": "fallback"
        }}
    elif any(w in msg_lower for w in ["train", "irctc", "pnr", "rail"]):
        return {{
            "answer": "TripNova includes a built-in IRCTC train booking engine under 'Train Booking'! You can search train schedules across Southern Railways (Vande Bharat, Pandian, Cheran, Rockfort Express), check seat availability, and track live PNR status.",
            "source": "fallback"
        }}
    elif any(w in msg_lower for w in ["hotel", "stay", "room", "oyo", "taj"]):
        return {{
            "answer": "Use our 'Hotels' tab to search luxury heritage stays in Chettinad, hill resort villas in Ooty/Kodai, and budget stays with instant in-app booking.",
            "source": "fallback"
        }}
    else:
        return {{
            "answer": "Welcome to TripNova! Ask me anything about Tamil Nadu and Indian destinations, best travel seasons, bus & train routes, budget tips, or customized day-wise itineraries.",
            "source": "fallback"
        }}
'''

with open('ai_service.py', 'w', encoding='utf-8') as f:
    f.write(ai_service_code)

print("Saved backend/ai_service.py successfully!")

# Also generate frontend/src/api.js with the combined database
api_js_code = f'''// Client-Side Curated Knowledge Engine for Tamil Nadu & India (Standalone & Live Hosted Modes)
const DESTINATIONS_DB = {json.dumps(COMBINED_DB, indent=2, ensure_ascii=False)};

const ALIASES = {{
  tanjore: 'thanjavur',
  trichy: 'trichy',
  tiruchirappalli: 'trichy',
  kutralam: 'courtallam',
  courtallam: 'courtallam',
  tenkasi: 'courtallam',
  mamallapuram: 'mahabalipuram',
  mahabalipuram: 'mahabalipuram',
  rameshwaram: 'rameswaram',
  rameswaram: 'rameswaram',
  kodai: 'kodaikanal',
  kodaikanal: 'kodaikanal',
  udhagamandalam: 'ooty',
  ooty: 'ooty',
  pollachi: 'valparai',
  valparai: 'valparai',
  karaikudi: 'chettinad',
  chettinad: 'chettinad',
  kolli: 'kolli hills',
  namakkal: 'kolli hills',
  dharmapuri: 'hogenakkal',
  pichavaram: 'chidambaram',
  tamilnadu: 'tamil nadu',
  'tamil nadu': 'tamil nadu',
}};

function handleClientFallback(path, body) {{
  if (path.includes('/api/auth/login') || path.includes('/api/auth/register') || path.includes('/api/auth/google')) {{
    const user = {{
      id: Date.now(),
      username: body.username || (body.email ? body.email.split('@')[0] : 'Traveler'),
      email: body.email || 'traveler@tripnova.com',
    }};
    localStorage.setItem('tripnova_user', JSON.stringify(user));
    return user;
  }}

  if (path.includes('/api/ai/plan-journey')) {{
    return {{
      places: [
        {{
          name: 'Ooty (Udhagamandalam), Tamil Nadu',
          reason: 'Rolling Nilgiri tea estates, UNESCO toy train rides, botanical gardens, and mist-clad mountain peaks.',
          tag: 'Nature',
          bestSeason: 'Oct–Jun',
          lat: 11.4102,
          lng: 76.6950,
        }},
        {{
          name: 'Madurai, Tamil Nadu',
          reason: 'Cultural capital of Tamil Nadu featuring the 2,500-year-old Meenakshi Amman Temple and royal palaces.',
          tag: 'Heritage',
          bestSeason: 'Oct–Mar',
          lat: 9.9252,
          lng: 78.1198,
        }},
        {{
          name: 'Kanyakumari, Tamil Nadu',
          reason: 'Southernmost tip of India where three seas converge, Vivekananda Rock Memorial, and sunset views.',
          tag: 'Spiritual',
          bestSeason: 'Oct–Mar',
          lat: 8.0883,
          lng: 77.5385,
        }},
      ],
      source: 'tripnova_engine',
    }};
  }}

  if (path.includes('/api/ai/places-to-visit')) {{
    const placeQuery = (body.place || 'Madurai').toLowerCase().trim();
    const days = parseInt(body.days, 10) || 3;

    let targetKey = null;
    for (const [alias, canonical] of Object.entries(ALIASES)) {{
      if (placeQuery.includes(alias) || alias.includes(placeQuery)) {{
        targetKey = canonical;
        break;
      }}
    }}

    if (!targetKey) {{
      for (const key of Object.keys(DESTINATIONS_DB)) {{
        if (placeQuery.includes(key) || key.includes(placeQuery)) {{
          targetKey = key;
          break;
        }}
      }}
    }}

    let matched = targetKey ? DESTINATIONS_DB[targetKey] : DESTINATIONS_DB['madurai'];

    const allSpots = matched.attractions || [];
    const itinerary = [];
    for (let d = 1; d <= days; d++) {{
      const startIdx = ((d - 1) * 2) % allSpots.length;
      const daySpots = [
        allSpots[startIdx % allSpots.length],
        allSpots[(startIdx + 1) % allSpots.length],
      ];
      itinerary.push({{
        day: d,
        title: d === 1 ? 'Primary Iconic Landmarks' : d === 2 ? 'Cultural & Heritage Sights' : `Scenic Discoveries (Day ${{d}})`,
        places: daySpots,
      }});
    }}

    return {{
      place: matched.fullName,
      lat: matched.lat,
      lng: matched.lng,
      summary: matched.summary,
      itinerary,
      hotels: matched.hotels,
      source: 'tripnova_engine',
    }};
  }}

  if (path.includes('/api/ai/unsuitable-place')) {{
    return {{
      answer: `While ${{body.place || 'this destination'}} is wonderful, your preference for ${{
        body.preferences?.climate || 'your selected climate'
      }} and ${{body.preferences?.experience || 'travel style'}} might be better suited by our top recommendations.`,
      source: 'tripnova_engine',
    }};
  }}

  if (path.includes('/api/ai/chat')) {{
    return {{
      answer: `Welcome to TripNova! You can explore all destinations across Tamil Nadu and India, plan day-by-day itineraries, book RedBus buses with seat layout, and book IRCTC trains directly in this app.`,
      source: 'tripnova_engine',
    }};
  }}

  return {{ status: 'ok' }};
}}

export async function apiPost(path, body) {{
  try {{
    const res = await fetch(path, {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify(body),
    }});
    if (res.ok) {{
      const data = await res.json();
      return data;
    }}
    return handleClientFallback(path, body);
  }} catch {{
    return handleClientFallback(path, body);
  }}
}}
'''

frontend_api_path = os.path.abspath(os.path.join('..', 'frontend', 'src', 'api.js'))
with open(frontend_api_path, 'w', encoding='utf-8') as f:
    f.write(api_js_code)

print("Saved frontend/src/api.js successfully!")
