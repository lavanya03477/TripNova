import json
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
DESTINATIONS_DB = {
    "chennai": {
        "fullName": "Chennai, Tamil Nadu",
        "lat": 13.0827,
        "lng": 80.2707,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "culture",
        "budget": "medium",
        "summary": "The Gateway to South India, famous for Marina Beach (world's 2nd longest), ancient Kapaleeshwarar Temple, and Carnatic music heritage.",
        "attractions": [
            {
                "name": "Marina Beach & Lighthouse",
                "highlight": "World's second-longest urban natural beach with street food and lighthouse view.",
                "duration": "2.5 hours",
                "bestTime": "Evening (5 PM)",
                "lat": 13.05,
                "lng": 80.2824
            },
            {
                "name": "Kapaleeshwarar Temple (Mylapore)",
                "highlight": "7th-century Dravidian Shiva temple with magnificent multi-colored gopuram and tank.",
                "duration": "2 hours",
                "bestTime": "Morning / 6 PM",
                "lat": 13.0336,
                "lng": 80.2697
            },
            {
                "name": "San Thome Basilica & Fort St. George",
                "highlight": "Historic neo-Gothic cathedral built over St. Thomas apostle tomb and 1644 British fort museum.",
                "duration": "2.5 hours",
                "bestTime": "Morning",
                "lat": 13.0337,
                "lng": 80.2778
            },
            {
                "name": "Guindy National Park & Snake Park",
                "highlight": "Unique protected national park situated right within city limits with spotted deer and blackbucks.",
                "duration": "2.5 hours",
                "bestTime": "Morning",
                "lat": 13.0067,
                "lng": 80.2206
            },
            {
                "name": "DakshinaChitra & MGM Beach Trail",
                "highlight": "Living heritage museum showcasing traditional architecture and crafts of South India.",
                "duration": "3 hours",
                "bestTime": "Afternoon",
                "lat": 12.8256,
                "lng": 80.2415
            },
            {
                "name": "Valluvar Kottam & T. Nagar Shopping",
                "highlight": "Monument dedicated to classical Tamil poet Thiruvalluvar and famous silk/gold bazaar.",
                "duration": "2 hours",
                "bestTime": "Evening",
                "lat": 13.0543,
                "lng": 80.2417
            }
        ],
        "hotels": [
            {
                "name": "Taj Coromandel, Chennai",
                "type": "Luxury",
                "price": "₹12,500/night",
                "rating": "4.9★"
            },
            {
                "name": "The Leela Palace Chennai",
                "type": "Luxury",
                "price": "₹16,000/night",
                "rating": "4.9★"
            },
            {
                "name": "The Residency Towers T. Nagar",
                "type": "Mid-range",
                "price": "₹4,200/night",
                "rating": "4.5★"
            },
            {
                "name": "Zostel Chennai",
                "type": "Budget-friendly",
                "price": "₹850/night",
                "rating": "4.4★"
            }
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
                "highlight": "Historic museum housing Mahatma Gandhi's blood-stained dhoti and freedom struggle gallery.",
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
                "lat": 9.92,
                "lng": 78.122
            }
        ],
        "hotels": [
            {
                "name": "Heritage Madurai",
                "type": "Luxury",
                "price": "₹7,800/night",
                "rating": "4.7★"
            },
            {
                "name": "Courtyard by Marriott Madurai",
                "type": "Luxury",
                "price": "₹6,200/night",
                "rating": "4.6★"
            },
            {
                "name": "The Gateway Hotel Pasumalai",
                "type": "Mid-range",
                "price": "₹4,100/night",
                "rating": "4.5★"
            },
            {
                "name": "Hotel Supreme Madurai",
                "type": "Budget-friendly",
                "price": "₹1,400/night",
                "rating": "4.2★"
            }
        ]
    },
    "ooty": {
        "fullName": "Ooty (Udhagamandalam), Tamil Nadu",
        "lat": 11.4102,
        "lng": 76.695,
        "region": "Tamil Nadu",
        "climate": "cold",
        "experience": "nature",
        "budget": "medium",
        "summary": "Queen of the Nilgiris known for rolling tea estates, UNESCO toy train rides, botanical gardens, and mist-clad peaks.",
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
                "lat": 11.488,
                "lng": 76.592
            },
            {
                "name": "Ooty Lake & Boat House",
                "highlight": "Serene artificial lake surrounded by eucalyptus trees with pedal and motor boating.",
                "duration": "2 hours",
                "bestTime": "Late afternoon",
                "lat": 11.4075,
                "lng": 76.6872
            },
            {
                "name": "Avalanche Lake & Emerald Dam",
                "highlight": "Pristine untouched valley lake surrounded by trout streams and shola forests.",
                "duration": "4 hours",
                "bestTime": "Morning jeep safari",
                "lat": 11.2989,
                "lng": 76.5866
            }
        ],
        "hotels": [
            {
                "name": "Savoy - IHCL SeleQtions, Ooty",
                "type": "Luxury",
                "price": "₹13,500/night",
                "rating": "4.8★"
            },
            {
                "name": "Sterling Ooty Fern Hill",
                "type": "Mid-range",
                "price": "₹5,200/night",
                "rating": "4.5★"
            },
            {
                "name": "Sinclairs Retreat Ooty",
                "type": "Mid-range",
                "price": "₹4,200/night",
                "rating": "4.3★"
            },
            {
                "name": "Zostel Ooty",
                "type": "Budget-friendly",
                "price": "₹950/night",
                "rating": "4.5★"
            }
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
        "summary": "Princess of Hill Stations in the Palani Hills, renowned for its star-shaped Kodai Lake, Coaker's Walk, and Pillar Rocks.",
        "attractions": [
            {
                "name": "Kodaikanal Star Lake & Cycling",
                "highlight": "Iconic star-shaped lake offering pedal boating, horse riding, and cycling promenade.",
                "duration": "2.5 hours",
                "bestTime": "Morning / Evening",
                "lat": 10.233,
                "lng": 77.49
            },
            {
                "name": "Coaker's Walk & Bryant Park",
                "highlight": "1km paved pedestrian path on steep mountain ridge overlooking misty plains below.",
                "duration": "2 hours",
                "bestTime": "Morning (9 AM)",
                "lat": 10.2312,
                "lng": 77.4958
            },
            {
                "name": "Pillar Rocks & Guna Caves (Devil's Kitchen)",
                "highlight": "Three giant 400-ft granite pillars rising vertically out of cliff-side mist.",
                "duration": "2.5 hours",
                "bestTime": "Afternoon",
                "lat": 10.2078,
                "lng": 77.4725
            },
            {
                "name": "Dolphin's Nose & Echo Point",
                "highlight": "Flat rock projecting over a 6,600-ft deep precipice offering thrilling views of the valley.",
                "duration": "3.5 hours",
                "bestTime": "Morning trek",
                "lat": 10.21,
                "lng": 77.518
            },
            {
                "name": "Silver Cascade Falls & Bear Shola Falls",
                "highlight": "180-ft natural waterfall created from Kodai Lake overflow amidst pine woods.",
                "duration": "1.5 hours",
                "bestTime": "Morning",
                "lat": 10.252,
                "lng": 77.51
            },
            {
                "name": "Pine Forest & Mannavanur Eco Lake",
                "highlight": "Dense preserved pine plantations (movie shooting spot) and peaceful sheep farm lake.",
                "duration": "4 hours",
                "bestTime": "Morning",
                "lat": 10.215,
                "lng": 77.452
            }
        ],
        "hotels": [
            {
                "name": "The Tamara Kodai",
                "type": "Luxury",
                "price": "₹16,000/night",
                "rating": "4.9★"
            },
            {
                "name": "Carlton Hotel Kodaikanal",
                "type": "Luxury",
                "price": "₹11,000/night",
                "rating": "4.7★"
            },
            {
                "name": "Sterling Kodai Lake",
                "type": "Mid-range",
                "price": "₹4,800/night",
                "rating": "4.4★"
            },
            {
                "name": "Zostel Kodaikanal",
                "type": "Budget-friendly",
                "price": "₹900/night",
                "rating": "4.6★"
            }
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
        "summary": "Sacred island pilgrimage destination in the Gulf of Mannar, celebrated for the Ramanathaswamy Temple, Pamban Bridge, and Dhanushkodi.",
        "attractions": [
            {
                "name": "Ramanathaswamy Temple & 22 Theerthams",
                "highlight": "One of 12 Jyotirlingas, famous for the world's longest temple corridor with 1212 carved pillars.",
                "duration": "3.5 hours",
                "bestTime": "Early morning (5-11 AM)",
                "lat": 9.2881,
                "lng": 79.3174
            },
            {
                "name": "Pamban Sea Bridge & Railway Bridge",
                "highlight": "India's first sea bridge spanning over the ocean connecting Pamban Island to mainland India.",
                "duration": "1.5 hours",
                "bestTime": "Sunrise / Sunset",
                "lat": 9.278,
                "lng": 79.196
            },
            {
                "name": "Dhanushkodi Ghost Town & Arichal Munai",
                "highlight": "Submerged city at the tip of India where the Bay of Bengal meets the Indian Ocean.",
                "duration": "3.5 hours",
                "bestTime": "Morning / 3 PM",
                "lat": 9.1764,
                "lng": 79.4183
            },
            {
                "name": "Agni Theertham & Sangumal Beach",
                "highlight": "Sacred ocean bathing shore facing the temple where devotees take holy dips in calm waves.",
                "duration": "1.5 hours",
                "bestTime": "Sunrise",
                "lat": 9.289,
                "lng": 79.321
            },
            {
                "name": "Dr. APJ Abdul Kalam National Memorial",
                "highlight": "Beautiful memorial museum celebrating the life, rockets, and legacy of India's Missile Man.",
                "duration": "2 hours",
                "bestTime": "Afternoon",
                "lat": 9.293,
                "lng": 79.282
            }
        ],
        "hotels": [
            {
                "name": "Daiwik Hotels Rameswaram",
                "type": "Mid-range",
                "price": "₹3,800/night",
                "rating": "4.5★"
            },
            {
                "name": "Hyatt Place Rameswaram",
                "type": "Luxury",
                "price": "₹6,500/night",
                "rating": "4.7★"
            },
            {
                "name": "Hotel MCM Towers",
                "type": "Budget-friendly",
                "price": "₹1,500/night",
                "rating": "4.2★"
            }
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
        "summary": "The southernmost tip of mainland India where the Indian Ocean, Arabian Sea, and Bay of Bengal converge (Triveni Sangam).",
        "attractions": [
            {
                "name": "Vivekananda Rock Memorial & Ferry",
                "highlight": "Iconic rock monument built in 1970 where Swami Vivekananda attained enlightenment.",
                "duration": "3 hours",
                "bestTime": "Morning ferry (8 AM)",
                "lat": 8.0781,
                "lng": 77.5553
            },
            {
                "name": "Thiruvalluvar 133-ft Statue",
                "highlight": "Colossal stone statue honoring Tamil philosopher poet Thiruvalluvar standing in the ocean.",
                "duration": "1.5 hours",
                "bestTime": "Morning",
                "lat": 8.0778,
                "lng": 77.554
            },
            {
                "name": "Triveni Sangam & Sunset / Sunrise Point",
                "highlight": "Spectacular geographical vantage point to witness simultaneous sunrise and sunset over three seas.",
                "duration": "2 hours",
                "bestTime": "Sunrise (6 AM) & Sunset (6 PM)",
                "lat": 8.081,
                "lng": 77.552
            },
            {
                "name": "Padmanabhapuram Palace (Thuckalay)",
                "highlight": "Magnificent 16th-century wooden palace displaying Kerala-Tamil teak architecture.",
                "duration": "3 hours",
                "bestTime": "Afternoon",
                "lat": 8.2508,
                "lng": 77.3275
            },
            {
                "name": "Bhagavathy Amman Temple & Gandhi Mandapam",
                "highlight": "3000-year-old temple of Goddess Kanya Kumari and memorial built in Odishan style.",
                "duration": "2 hours",
                "bestTime": "Morning / Evening",
                "lat": 8.0815,
                "lng": 77.5535
            }
        ],
        "hotels": [
            {
                "name": "The Gopinivas Grand, Kanyakumari",
                "type": "Luxury",
                "price": "₹4,800/night",
                "rating": "4.6★"
            },
            {
                "name": "Annai Resorts & Spa",
                "type": "Luxury",
                "price": "₹6,200/night",
                "rating": "4.7★"
            },
            {
                "name": "Hotel Sea View Kanyakumari",
                "type": "Mid-range",
                "price": "₹3,100/night",
                "rating": "4.4★"
            },
            {
                "name": "Hotel Sun World",
                "type": "Budget-friendly",
                "price": "₹1,200/night",
                "rating": "4.1★"
            }
        ]
    },
    "thanjavur": {
        "fullName": "Thanjavur (Tanjore), Tamil Nadu",
        "lat": 10.787,
        "lng": 79.1378,
        "region": "Tamil Nadu",
        "climate": "moderate",
        "experience": "history",
        "budget": "low",
        "summary": "The Cradle of Chola Architecture and South Indian culture, home to the UNESCO World Heritage Brihadeeswarar Big Temple.",
        "attractions": [
            {
                "name": "Brihadeeswarar Temple (Peruvudaiyar Kovil / Big Temple)",
                "highlight": "1000-year-old Chola architectural wonder with 216-ft vimana and 80-tonne single granite capstone.",
                "duration": "3.5 hours",
                "bestTime": "Morning (7-11 AM) or Evening sunset",
                "lat": 10.7828,
                "lng": 79.1318
            },
            {
                "name": "Thanjavur Maratha Royal Palace Complex",
                "highlight": "Historic palace featuring Durbar Hall, Bell Tower, and royal residence courtyards.",
                "duration": "2.5 hours",
                "bestTime": "Morning",
                "lat": 10.7925,
                "lng": 79.136
            },
            {
                "name": "Saraswathi Mahal Library & Art Gallery",
                "highlight": "One of the oldest medieval libraries in Asia housing ancient palm leaf manuscripts and Chola bronze statues.",
                "duration": "2 hours",
                "bestTime": "Afternoon",
                "lat": 10.793,
                "lng": 79.1368
            },
            {
                "name": "Punnainallur Mariamman Temple",
                "highlight": "Famous 17th-century temple built by Venkoji Maharaja known for natural anthill deity.",
                "duration": "1.5 hours",
                "bestTime": "Morning / 5 PM",
                "lat": 10.776,
                "lng": 79.191
            },
            {
                "name": "Thanjavur Art Plate & Dancing Doll Workshop Trail",
                "highlight": "Witness master craftsmen crafting traditional Thanjavur paintings, bronze plates, and roly-poly dolls.",
                "duration": "2 hours",
                "bestTime": "Evening",
                "lat": 10.788,
                "lng": 79.14
            }
        ],
        "hotels": [
            {
                "name": "Svatma, Thanjavur - Relais & Châteaux",
                "type": "Luxury",
                "price": "₹14,000/night",
                "rating": "4.9★"
            },
            {
                "name": "Great Trails River View Thanjavur by GRT",
                "type": "Luxury",
                "price": "₹6,800/night",
                "rating": "4.7★"
            },
            {
                "name": "Hotel Gnanam",
                "type": "Mid-range",
                "price": "₹2,400/night",
                "rating": "4.3★"
            },
            {
                "name": "Hotel Parisutham",
                "type": "Mid-range",
                "price": "₹2,800/night",
                "rating": "4.4★"
            }
        ]
    },
    "coimbatore": {
        "fullName": "Coimbatore, Tamil Nadu",
        "lat": 11.0168,
        "lng": 76.9558,
        "region": "Tamil Nadu",
        "climate": "moderate",
        "experience": "culture",
        "budget": "medium",
        "summary": "Manchester of South India, gateway to the Western Ghats and home of the world-famous 112ft Adiyogi Shiva Statue at Isha Yoga.",
        "attractions": [
            {
                "name": "Isha Yoga Center & 112-ft Adiyogi Statue",
                "highlight": "Guinness World Record largest bust sculpture of Adiyogi Shiva, Dhyanalinga, and evening laser 3D show.",
                "duration": "4-5 hours",
                "bestTime": "Afternoon till 7:30 PM light show",
                "lat": 10.976,
                "lng": 76.741
            },
            {
                "name": "Marudhamalai Murugan Hill Temple",
                "highlight": "1200-year-old scenic hilltop temple dedicated to Lord Murugan surrounded by medicinal herbal groves.",
                "duration": "2.5 hours",
                "bestTime": "Morning (7 AM)",
                "lat": 11.045,
                "lng": 76.852
            },
            {
                "name": "Siruvani Waterfalls & Dam",
                "highlight": "Crystal-clear waterfalls renowned for having one of the sweetest natural mineral waters in the world.",
                "duration": "3.5 hours",
                "bestTime": "Morning (permit required)",
                "lat": 10.94,
                "lng": 76.68
            },
            {
                "name": "GD Naidu Science & Vintage Car Museum",
                "highlight": "Fascinating automotive museum exhibiting rare antique cars from Britain, Germany, and America.",
                "duration": "2 hours",
                "bestTime": "Afternoon",
                "lat": 11.011,
                "lng": 76.974
            },
            {
                "name": "Perur Pateeswarar Temple",
                "highlight": "Ancient Chola temple with exquisite Kanaka Sabha hall displaying intricately carved stone statues.",
                "duration": "2 hours",
                "bestTime": "Morning / Evening",
                "lat": 10.971,
                "lng": 76.918
            }
        ],
        "hotels": [
            {
                "name": "The Residency Towers Coimbatore",
                "type": "Luxury",
                "price": "₹6,800/night",
                "rating": "4.8★"
            },
            {
                "name": "Radisson Blu Hotel Coimbatore",
                "type": "Luxury",
                "price": "₹6,200/night",
                "rating": "4.7★"
            },
            {
                "name": "Zone by The Park Coimbatore",
                "type": "Mid-range",
                "price": "₹3,400/night",
                "rating": "4.4★"
            },
            {
                "name": "Ibis Coimbatore City Centre",
                "type": "Mid-range",
                "price": "₹2,900/night",
                "rating": "4.3★"
            }
        ]
    },
    "mahabalipuram": {
        "fullName": "Mahabalipuram (Mamallapuram), Tamil Nadu",
        "lat": 12.6269,
        "lng": 80.1927,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "history",
        "budget": "medium",
        "summary": "UNESCO World Heritage coastal town celebrated for 7th-century Pallava rock-cut cave temples, Shore Temple, and surf beaches.",
        "attractions": [
            {
                "name": "UNESCO Shore Temple",
                "highlight": "8th-century structural granite temple built directly on the shores of the Bay of Bengal.",
                "duration": "2 hours",
                "bestTime": "Sunrise or 4 PM",
                "lat": 12.6163,
                "lng": 80.1983
            },
            {
                "name": "Pancha Rathas (Five Rathas)",
                "highlight": "Monolithic rock-cut shrines carved out of single granite stones in the shape of chariots.",
                "duration": "2 hours",
                "bestTime": "Morning",
                "lat": 12.6092,
                "lng": 80.1914
            },
            {
                "name": "Arjuna's Penance & Krishna's Butterball",
                "highlight": "World's largest open-air rock bas-relief and a 250-tonne gigantic boulder balanced on a 45-degree rock slope.",
                "duration": "2 hours",
                "bestTime": "Morning / 3 PM",
                "lat": 12.6186,
                "lng": 80.1936
            },
            {
                "name": "Mahabalipuram Lighthouse & Cave Temples",
                "highlight": "Historic circular stone lighthouse offering 360-degree ocean views and Varaha Cave mandapam.",
                "duration": "2 hours",
                "bestTime": "Late afternoon",
                "lat": 12.616,
                "lng": 80.192
            },
            {
                "name": "Covelong Beach & Surfing School",
                "highlight": "Premier surfing village on the East Coast Road with windsurfing and fresh seafood.",
                "duration": "3 hours",
                "bestTime": "Morning",
                "lat": 12.788,
                "lng": 80.252
            }
        ],
        "hotels": [
            {
                "name": "Radisson Blu Resort Temple Bay",
                "type": "Luxury",
                "price": "₹11,500/night",
                "rating": "4.8★"
            },
            {
                "name": "InterContinental Chennai Mahabalipuram",
                "type": "Luxury",
                "price": "₹15,000/night",
                "rating": "4.9★"
            },
            {
                "name": "Grande Bay Resort & Spa",
                "type": "Mid-range",
                "price": "₹5,800/night",
                "rating": "4.6★"
            },
            {
                "name": "Myna Villa Mahabalipuram",
                "type": "Budget-friendly",
                "price": "₹1,200/night",
                "rating": "4.3★"
            }
        ]
    },
    "kanchipuram": {
        "fullName": "Kanchipuram, Tamil Nadu",
        "lat": 12.8342,
        "lng": 79.7036,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "history",
        "budget": "low",
        "summary": "City of Thousand Temples and world capital of authentic handwoven pure mulberry silk sarees.",
        "attractions": [
            {
                "name": "Kanchi Kamakshi Amman Temple",
                "highlight": "One of 51 Shakti Peethas with golden gopuram and sanctum in the heart of Kanchi.",
                "duration": "2.5 hours",
                "bestTime": "Morning (6-11 AM)",
                "lat": 12.8406,
                "lng": 79.703
            },
            {
                "name": "Ekambareswarar Temple (Earth Element)",
                "highlight": "Massive 23-acre temple featuring 59-meter tall raja gopuram and 3,500-year-old sacred mango tree.",
                "duration": "2.5 hours",
                "bestTime": "Morning",
                "lat": 12.8475,
                "lng": 79.6997
            },
            {
                "name": "Kailasanathar Temple",
                "highlight": "Oldest sandstone temple in Kanchipuram built by Pallava king Rajasimha in 685 AD.",
                "duration": "2 hours",
                "bestTime": "Morning / 4 PM",
                "lat": 12.842,
                "lng": 79.689
            },
            {
                "name": "Varadharaja Perumal Temple",
                "highlight": "Celebrated Vishnu temple with 100-pillar hall carved with chains from single granite rocks.",
                "duration": "2 hours",
                "bestTime": "Evening (5 PM)",
                "lat": 12.819,
                "lng": 79.724
            },
            {
                "name": "Kanchipuram Silk Weavers Society Trail",
                "highlight": "Witness live handloom silk weaving with genuine gold zari borders and buy direct from master weavers.",
                "duration": "2 hours",
                "bestTime": "Afternoon",
                "lat": 12.835,
                "lng": 79.705
            }
        ],
        "hotels": [
            {
                "name": "MM Legacy Kanchipuram",
                "type": "Luxury",
                "price": "₹4,200/night",
                "rating": "4.6★"
            },
            {
                "name": "Regency Kanchipuram by GRT Hotels",
                "type": "Mid-range",
                "price": "₹3,400/night",
                "rating": "4.4★"
            },
            {
                "name": "Hotel Baboo Soorya",
                "type": "Budget-friendly",
                "price": "₹1,500/night",
                "rating": "4.1★"
            }
        ]
    },
    "trichy": {
        "fullName": "Tiruchirappalli (Trichy), Tamil Nadu",
        "lat": 10.7905,
        "lng": 78.7047,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "history",
        "budget": "low",
        "summary": "Historic Chola/Nayaka heartland on the banks of River Cauvery, home to Srirangam and the iconic Rockfort.",
        "attractions": [
            {
                "name": "Sri Ranganathaswamy Temple (Srirangam)",
                "highlight": "World's largest functioning Hindu temple complex spanning 156 acres with 21 magnificent gopurams.",
                "duration": "4 hours",
                "bestTime": "Early morning (6-11 AM)",
                "lat": 10.8623,
                "lng": 78.6902
            },
            {
                "name": "Ucchi Pillayar Rockfort Temple",
                "highlight": "Ancient fort built on an 83-meter high monolithic rock; climb 437 steps for 360-degree city views.",
                "duration": "2.5 hours",
                "bestTime": "Sunset (5 PM)",
                "lat": 10.8286,
                "lng": 78.6974
            },
            {
                "name": "Jambukeswarar Temple (Thiruvanaikaval)",
                "highlight": "Pancha Bhoota Stalam representing Water Element with an underground natural spring in the sanctum.",
                "duration": "2 hours",
                "bestTime": "Morning / 6 PM",
                "lat": 10.853,
                "lng": 78.705
            },
            {
                "name": "Kallanai Dam (Grand Anicut)",
                "highlight": "World's 4th oldest water-diversion dam, built in 2nd century AD by King Karikala Cholan.",
                "duration": "2.5 hours",
                "bestTime": "Late afternoon",
                "lat": 10.835,
                "lng": 78.818
            },
            {
                "name": "Mukkombu Dam & Butterfly Park",
                "highlight": "Scenic picnic barrage on River Cauvery with tropical butterfly conservatory.",
                "duration": "2.5 hours",
                "bestTime": "Morning",
                "lat": 10.875,
                "lng": 78.605
            }
        ],
        "hotels": [
            {
                "name": "SRM Hotel Trichy",
                "type": "Luxury",
                "price": "₹4,800/night",
                "rating": "4.6★"
            },
            {
                "name": "Courtyard by Marriott Tiruchirappalli",
                "type": "Luxury",
                "price": "₹6,500/night",
                "rating": "4.7★"
            },
            {
                "name": "Grand Gardenia Trichy",
                "type": "Mid-range",
                "price": "₹2,600/night",
                "rating": "4.3★"
            },
            {
                "name": "Hotel Ramyas",
                "type": "Budget-friendly",
                "price": "₹1,800/night",
                "rating": "4.2★"
            }
        ]
    },
    "yercaud": {
        "fullName": "Yercaud (Shevaroy Hills), Tamil Nadu",
        "lat": 11.7753,
        "lng": 78.2093,
        "region": "Tamil Nadu",
        "climate": "cold",
        "experience": "nature",
        "budget": "low",
        "summary": "Jewel of the South nestled in the Shevaroy Hills near Salem, known for cool mountain lakes, orange groves, and coffee estates.",
        "attractions": [
            {
                "name": "Yercaud Emerald Lake & Boating",
                "highlight": "Scenic lake surrounded by gardens and deer park with pedal and motor boating.",
                "duration": "2 hours",
                "bestTime": "Morning / Evening",
                "lat": 11.775,
                "lng": 78.209
            },
            {
                "name": "Lady's Seat, Gent's Seat & Pagoda Point",
                "highlight": "Panoramic cliff viewpoints offering telescope views of Salem city and Mettur Dam.",
                "duration": "2.5 hours",
                "bestTime": "Sunset (5:30 PM)",
                "lat": 11.768,
                "lng": 78.203
            },
            {
                "name": "Killiyur Waterfalls",
                "highlight": "300-ft natural waterfall tumbling into a serene forest gorge (accessible via forest trek).",
                "duration": "3 hours",
                "bestTime": "Morning",
                "lat": 11.792,
                "lng": 78.201
            },
            {
                "name": "Shevaroy Temple & Bear's Cave",
                "highlight": "Highest peak in Yercaud (5,326 ft) with ancient cave shrine dedicated to Lord Shevaroyan.",
                "duration": "2 hours",
                "bestTime": "Morning",
                "lat": 11.831,
                "lng": 78.232
            },
            {
                "name": "Botanical Garden & Orchidarium",
                "highlight": "Houses over 250 species of rare orchids and the National Pitcher Plant reserve.",
                "duration": "2 hours",
                "bestTime": "Afternoon",
                "lat": 11.782,
                "lng": 78.214
            }
        ],
        "hotels": [
            {
                "name": "Great Trails Yercaud by GRT Hotels",
                "type": "Luxury",
                "price": "₹6,800/night",
                "rating": "4.7★"
            },
            {
                "name": "Sterling Yercaud",
                "type": "Luxury",
                "price": "₹5,400/night",
                "rating": "4.5★"
            },
            {
                "name": "Grand Palace Hotel & Spa",
                "type": "Mid-range",
                "price": "₹3,500/night",
                "rating": "4.3★"
            },
            {
                "name": "Hotel Shevaroys",
                "type": "Budget-friendly",
                "price": "₹1,600/night",
                "rating": "4.1★"
            }
        ]
    },
    "tiruvannamalai": {
        "fullName": "Tiruvannamalai, Tamil Nadu",
        "lat": 12.2253,
        "lng": 79.0747,
        "region": "Tamil Nadu",
        "climate": "moderate",
        "experience": "history",
        "budget": "low",
        "summary": "World-famous spiritual energy center at the base of sacred Mount Arunachala, celebrated for the Annamalaiyar Temple and Ramana Maharshi Ashram.",
        "attractions": [
            {
                "name": "Arunachaleswarar Temple (Fire Element)",
                "highlight": "Massive 25-acre temple representing the Fire Element with four soaring gateway towers.",
                "duration": "3.5 hours",
                "bestTime": "Early morning (6 AM) or 6 PM",
                "lat": 12.2317,
                "lng": 79.0674
            },
            {
                "name": "Giri Valam 14-km Circumambulation",
                "highlight": "Sacred walking trail around Mount Arunachala with 8 directional Shiva Lingam shrines.",
                "duration": "4-5 hours",
                "bestTime": "Full Moon night / Early morning",
                "lat": 12.228,
                "lng": 79.055
            },
            {
                "name": "Sri Ramana Maharshi Ashram",
                "highlight": "Tranquil meditation hall, samadhi shrine, and library of the celebrated Advaita sage.",
                "duration": "2 hours",
                "bestTime": "Morning / 4 PM",
                "lat": 12.22,
                "lng": 79.0556
            },
            {
                "name": "Virupaksha Cave & Skandasramam",
                "highlight": "Ancient caves on the hill slopes where Ramana Maharshi meditated for 16 years.",
                "duration": "2.5 hours",
                "bestTime": "Morning trek",
                "lat": 12.227,
                "lng": 79.06
            },
            {
                "name": "Sathanur Dam & Crocodile Park",
                "highlight": "Picturesque dam across Thenpennai River with landscaped gardens and children's park.",
                "duration": "3 hours",
                "bestTime": "Afternoon",
                "lat": 12.185,
                "lng": 78.85
            }
        ],
        "hotels": [
            {
                "name": "Sparsa Resort Thiruvannamalai",
                "type": "Luxury",
                "price": "₹5,200/night",
                "rating": "4.8★"
            },
            {
                "name": "Arunai Anantha Resort",
                "type": "Mid-range",
                "price": "₹3,100/night",
                "rating": "4.4★"
            },
            {
                "name": "Hotel Himalayaa",
                "type": "Mid-range",
                "price": "₹2,200/night",
                "rating": "4.3★"
            },
            {
                "name": "Aakash Inn Tiruvannamalai",
                "type": "Budget-friendly",
                "price": "₹1,200/night",
                "rating": "4.1★"
            }
        ]
    },
    "courtallam": {
        "fullName": "Courtallam (Kutralam), Tenkasi, Tamil Nadu",
        "lat": 8.9298,
        "lng": 77.269,
        "region": "Tamil Nadu",
        "climate": "rainy",
        "experience": "nature",
        "budget": "low",
        "summary": "The Spa of South India, famous for mineral-rich medicinal waterfalls flowing through the Western Ghats during the monsoon season.",
        "attractions": [
            {
                "name": "Main Falls (Peraruvi)",
                "highlight": "Iconic 60-meter cascade where the waters of Chittar River fall over medicinal herbal rocks.",
                "duration": "2.5 hours",
                "bestTime": "Morning bath (7-10 AM)",
                "lat": 8.931,
                "lng": 77.272
            },
            {
                "name": "Five Falls (Aintharuvi)",
                "highlight": "Spectacular waterfall where the stream splits into five distinct cascades like the five heads of a serpent.",
                "duration": "2.5 hours",
                "bestTime": "Morning / 3 PM",
                "lat": 8.941,
                "lng": 77.258
            },
            {
                "name": "Old Courtallam Falls (Pazhaya Kutralam)",
                "highlight": "Picturesque waterfall set in a tranquil valley with spacious natural bathing pools.",
                "duration": "2 hours",
                "bestTime": "Morning",
                "lat": 8.955,
                "lng": 77.292
            },
            {
                "name": "Kasi Viswanathar Temple (Tenkasi)",
                "highlight": "13th-century Pandyan temple in Tenkasi with massive 180-ft tower (Gopuram) with musical pillars.",
                "duration": "2 hours",
                "bestTime": "Evening (5:30 PM)",
                "lat": 8.958,
                "lng": 77.315
            },
            {
                "name": "Gundar Dam & Eco Park",
                "highlight": "Scenic reservoir amidst Western Ghats jungle with mountain views and clean air.",
                "duration": "2 hours",
                "bestTime": "Afternoon",
                "lat": 8.975,
                "lng": 77.245
            }
        ],
        "hotels": [
            {
                "name": "Saaral Resorts Courtallam",
                "type": "Luxury",
                "price": "₹4,500/night",
                "rating": "4.6★"
            },
            {
                "name": "Green Garden Resort",
                "type": "Mid-range",
                "price": "₹2,800/night",
                "rating": "4.3★"
            },
            {
                "name": "Hotel Sree Annamalaiyar",
                "type": "Budget-friendly",
                "price": "₹1,200/night",
                "rating": "4.1★"
            }
        ]
    },
    "chidambaram": {
        "fullName": "Chidambaram & Pichavaram, Tamil Nadu",
        "lat": 11.3992,
        "lng": 79.6935,
        "region": "Tamil Nadu",
        "climate": "moderate",
        "experience": "history",
        "budget": "low",
        "summary": "Sacred center of the Cosmic Dance (Ananda Tandavam) of Nataraja, along with the world's second-largest mangrove forest at Pichavaram.",
        "attractions": [
            {
                "name": "Thillai Nataraja Temple (Akasha / Space Element)",
                "highlight": "Famous for the Chidambara Rahasyam (secret of space), golden roof sanctum, and gemstone lingam.",
                "duration": "3 hours",
                "bestTime": "Morning (6-11 AM) or 6 PM",
                "lat": 11.3995,
                "lng": 79.693
            },
            {
                "name": "Pichavaram Mangrove Forest Boating",
                "highlight": "Row-boating through 1,100 hectares of natural mangrove water canals and bird watching.",
                "duration": "3 hours",
                "bestTime": "Morning (8-11 AM)",
                "lat": 11.428,
                "lng": 79.782
            },
            {
                "name": "Vaitheeswaran Koil",
                "highlight": "Famous temple dedicated to Lord Shiva as the Divine Healer and world hub for Nadi Astrology.",
                "duration": "2 hours",
                "bestTime": "Morning / 5 PM",
                "lat": 11.2,
                "lng": 79.712
            },
            {
                "name": "Tarangambadi (Tranquebar Danish Fort)",
                "highlight": "17th-century Danish fort (Dansborg) and colonial seaside settlement on the Coromandel Coast.",
                "duration": "2.5 hours",
                "bestTime": "Late afternoon",
                "lat": 11.032,
                "lng": 79.854
            }
        ],
        "hotels": [
            {
                "name": "The Gateway Hotel Chidambaram",
                "type": "Mid-range",
                "price": "₹3,400/night",
                "rating": "4.4★"
            },
            {
                "name": "Pichavaram Adventure Resort",
                "type": "Mid-range",
                "price": "₹2,600/night",
                "rating": "4.2★"
            },
            {
                "name": "Hotel Saradharam Chidambaram",
                "type": "Budget-friendly",
                "price": "₹1,400/night",
                "rating": "4.1★"
            }
        ]
    },
    "valparai": {
        "fullName": "Valparai & Pollachi, Tamil Nadu",
        "lat": 10.3262,
        "lng": 76.9554,
        "region": "Tamil Nadu",
        "climate": "cold",
        "experience": "nature",
        "budget": "medium",
        "summary": "Pristine hill station with 40 hairpin bends, rolling tea gardens, Sholayar Dam, and wildlife sightings (Nilgiri Tahr, Elephants).",
        "attractions": [
            {
                "name": "Sholayar Dam & Reservoir",
                "highlight": "Second deepest dam in Asia offering majestic views of the emerald reservoir and rainforests.",
                "duration": "2.5 hours",
                "bestTime": "Morning / Afternoon",
                "lat": 10.298,
                "lng": 76.755
            },
            {
                "name": "40 Hairpin Bends & Loam's Viewpoint",
                "highlight": "Thrilling mountain road journey from Pollachi with stunning views of Aliyar Dam below.",
                "duration": "2 hours",
                "bestTime": "Morning / Sunset",
                "lat": 10.42,
                "lng": 76.97
            },
            {
                "name": "Aliyar Dam, Park & Monkey Falls",
                "highlight": "Picturesque dam at the foothills with landscaped gardens and natural spring waterfall.",
                "duration": "3 hours",
                "bestTime": "Morning",
                "lat": 10.485,
                "lng": 76.974
            },
            {
                "name": "Anamalai Tiger Reserve (Topslip Safari)",
                "highlight": "Jungle safari, elephant camp, and birding in dense evergreen Western Ghats canopy.",
                "duration": "4 hours",
                "bestTime": "Early morning safari (6:30 AM)",
                "lat": 10.47,
                "lng": 76.85
            },
            {
                "name": "Chinnakallar & Nirar Dam Waterfalls",
                "highlight": "Third highest rainfall region in India (Cheerapunji of South India) with suspension bridge.",
                "duration": "3 hours",
                "bestTime": "Morning",
                "lat": 10.302,
                "lng": 77.015
            }
        ],
        "hotels": [
            {
                "name": "Briar Tea Bungalows Valparai",
                "type": "Luxury",
                "price": "₹8,500/night",
                "rating": "4.8★"
            },
            {
                "name": "Stanmore Garden Bungalow",
                "type": "Luxury",
                "price": "₹7,200/night",
                "rating": "4.7★"
            },
            {
                "name": "Hotel Green Hill Valparai",
                "type": "Budget-friendly",
                "price": "₹1,600/night",
                "rating": "4.2★"
            }
        ]
    },
    "coonoor": {
        "fullName": "Coonoor, Nilgiris, Tamil Nadu",
        "lat": 11.353,
        "lng": 76.7959,
        "region": "Tamil Nadu",
        "climate": "cold",
        "experience": "nature",
        "budget": "medium",
        "summary": "Picturesque Nilgiri tea hill station famous for Sim's Park, Dolphin's Nose viewpoint, and organic tea tastings.",
        "attractions": [
            {
                "name": "Sim's Park Botanical Gardens",
                "highlight": "12-hectare Victorian botanical park housing rare magnolia, camellia, and century-old pines.",
                "duration": "2.5 hours",
                "bestTime": "Morning (9 AM)",
                "lat": 11.355,
                "lng": 76.801
            },
            {
                "name": "Dolphin's Nose & Catherine Falls View",
                "highlight": "Breathtaking cliff viewpoint overlooking the Catherine double-cascading waterfall.",
                "duration": "2.5 hours",
                "bestTime": "Morning (clear skies)",
                "lat": 11.332,
                "lng": 76.879
            },
            {
                "name": "Lamb's Rock & Droog Fort",
                "highlight": "Precipitous cliff over Coimbatore plains and historic 16th-century Tipu Sultan outpost.",
                "duration": "3 hours",
                "bestTime": "Morning trek",
                "lat": 11.348,
                "lng": 76.845
            },
            {
                "name": "Highfield Tea Factory & Museum Trail",
                "highlight": "50-year-old operational tea factory demonstrating orthodox tea making and essential oils.",
                "duration": "2 hours",
                "bestTime": "Afternoon",
                "lat": 11.362,
                "lng": 76.812
            }
        ],
        "hotels": [
            {
                "name": "Gateway Coonoor - IHCL SeleQtions",
                "type": "Luxury",
                "price": "₹11,000/night",
                "rating": "4.8★"
            },
            {
                "name": "Sunvalley Homestay Coonoor",
                "type": "Mid-range",
                "price": "₹4,200/night",
                "rating": "4.6★"
            },
            {
                "name": "Orchid Square Boutique Hotel",
                "type": "Mid-range",
                "price": "₹3,200/night",
                "rating": "4.4★"
            }
        ]
    },
    "hogenakkal": {
        "fullName": "Hogenakkal Falls, Dharmapuri, Tamil Nadu",
        "lat": 12.1182,
        "lng": 77.7766,
        "region": "Tamil Nadu",
        "climate": "moderate",
        "experience": "nature",
        "budget": "low",
        "summary": "The Niagara of India on the River Cauvery, renowned for exhilarating coracle (parisal) boat rides, herbal oil massages, and fish fry.",
        "attractions": [
            {
                "name": "Hogenakkal Main Waterfalls",
                "highlight": "Spectacular cascade where River Cauvery drops through carbonatite rocks creating smoking mist.",
                "duration": "3 hours",
                "bestTime": "Morning (8 AM)",
                "lat": 12.118,
                "lng": 77.776
            },
            {
                "name": "Coracle (Parisal) Round Boat Ride",
                "highlight": "Traditional circular bamboo basket boat ride beneath roaring waterfalls into the river canyon.",
                "duration": "2 hours",
                "bestTime": "Morning / 3 PM",
                "lat": 12.115,
                "lng": 77.772
            },
            {
                "name": "Hanging Suspension Bridge",
                "highlight": "Walkway suspended high above the gorge offering panoramic photography of all cascades.",
                "duration": "1 hour",
                "bestTime": "Morning",
                "lat": 12.119,
                "lng": 77.779
            },
            {
                "name": "Melagiri Hills & River Forest Bath",
                "highlight": "Natural mineral-rich water bath combined with traditional massage and freshly fried river fish.",
                "duration": "2.5 hours",
                "bestTime": "Afternoon",
                "lat": 12.125,
                "lng": 77.765
            }
        ],
        "hotels": [
            {
                "name": "Tamil Nadu Tourism Hotel (TTDC Hogenakkal)",
                "type": "Mid-range",
                "price": "₹2,200/night",
                "rating": "4.3★"
            },
            {
                "name": "CM Hotel Hogenakkal",
                "type": "Budget-friendly",
                "price": "₹1,400/night",
                "rating": "4.0★"
            }
        ]
    },
    "tirunelveli": {
        "fullName": "Tirunelveli, Tamil Nadu",
        "lat": 8.7139,
        "lng": 77.7567,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "history",
        "budget": "low",
        "summary": "Historic temple city on the sacred Thamirabarani River, world-famous for Nellaiappar Temple, Manimuthar waterfalls, and Halwa.",
        "attractions": [
            {
                "name": "Nellaiappar & Kanthimathi Temple",
                "highlight": "7th-century architectural gem featuring musical stone pillars and magnificent Mani Mandapam.",
                "duration": "3 hours",
                "bestTime": "Morning (6-11 AM) or 6 PM",
                "lat": 8.728,
                "lng": 77.689
            },
            {
                "name": "Manimuthar Waterfalls & Dam",
                "highlight": "Cascading mountain waterfall with natural swimming pond and teak forest views.",
                "duration": "3 hours",
                "bestTime": "Morning",
                "lat": 8.59,
                "lng": 77.41
            },
            {
                "name": "Papanasam Agasthiyar Falls & River",
                "highlight": "Sacred falls where sage Agastya received Shiva's darshan; pure Thamirabarani river bath.",
                "duration": "3 hours",
                "bestTime": "Morning",
                "lat": 8.705,
                "lng": 77.368
            },
            {
                "name": "Manjolai Tea Estates & Cloud Forest",
                "highlight": "Hill station in the Western Ghats (Kalakkad Mundanthurai Tiger Reserve) with tea plantations.",
                "duration": "Full day",
                "bestTime": "Morning jeep ride (permit required)",
                "lat": 8.55,
                "lng": 77.38
            },
            {
                "name": "Famous Iruttu Kadai Halwa Trail",
                "highlight": "Taste authentic hot wheat halwa made with pure ghee and Thamirabarani water.",
                "duration": "1.5 hours",
                "bestTime": "5:30 PM",
                "lat": 8.729,
                "lng": 77.691
            }
        ],
        "hotels": [
            {
                "name": "Hotel Aryas Tirunelveli",
                "type": "Mid-range",
                "price": "₹2,600/night",
                "rating": "4.4★"
            },
            {
                "name": "Regency Tirunelveli by GRT Hotels",
                "type": "Luxury",
                "price": "₹4,500/night",
                "rating": "4.7★"
            },
            {
                "name": "Hotel Sree Bharani",
                "type": "Budget-friendly",
                "price": "₹1,500/night",
                "rating": "4.2★"
            }
        ]
    },
    "chettinad": {
        "fullName": "Chettinad (Karaikudi), Tamil Nadu",
        "lat": 10.0682,
        "lng": 78.7804,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "history",
        "budget": "medium",
        "summary": "Land of magnificent palatial heritage mansions, Athangudi handmade tiles, antique markets, and world-famous Chettinad cuisine.",
        "attractions": [
            {
                "name": "Chettinad Palace & Thousand Windows House (Kanadukathan)",
                "highlight": "Opulent palatial mansion with Italian marble, teak pillars, Belgian mirrors, and stained glass.",
                "duration": "3 hours",
                "bestTime": "Morning (9 AM)",
                "lat": 10.152,
                "lng": 78.791
            },
            {
                "name": "Athangudi Handmade Tile Workshops",
                "highlight": "Witness master artisans handcrafting vibrant floral glass-finish mosaic tiles.",
                "duration": "2 hours",
                "bestTime": "Morning",
                "lat": 10.17,
                "lng": 78.84
            },
            {
                "name": "Pillayarpatti Karpaga Vinayagar Temple",
                "highlight": "1600-year-old rock-cut cave temple dedicated to Lord Ganesha carved on mountain face.",
                "duration": "2 hours",
                "bestTime": "Morning / 5 PM",
                "lat": 10.121,
                "lng": 78.681
            },
            {
                "name": "Thirumayam Fort & Rock Cut Temple",
                "highlight": "17th-century ring fort with rock-cut Shiva and Vishnu cave shrines and panoramic views.",
                "duration": "2.5 hours",
                "bestTime": "Late afternoon",
                "lat": 10.245,
                "lng": 78.752
            },
            {
                "name": "Chettinad Banana Leaf Culinary Trail",
                "highlight": "Authentic Chettinad spicy chicken/mutton pepper fry, vazhaipoo vadai, and seeyam.",
                "duration": "2 hours",
                "bestTime": "Lunch (12:30 PM)",
                "lat": 10.068,
                "lng": 78.78
            }
        ],
        "hotels": [
            {
                "name": "Chidambara Vilas - Luxury Heritage Resort",
                "type": "Luxury",
                "price": "₹8,500/night",
                "rating": "4.9★"
            },
            {
                "name": "The Bangala, Karaikudi",
                "type": "Luxury",
                "price": "₹9,200/night",
                "rating": "4.8★"
            },
            {
                "name": "Chettinadu Mansion Kanadukathan",
                "type": "Mid-range",
                "price": "₹4,500/night",
                "rating": "4.6★"
            },
            {
                "name": "Hotel Subhalakshmi Palace",
                "type": "Budget-friendly",
                "price": "₹1,800/night",
                "rating": "4.2★"
            }
        ]
    },
    "vellore": {
        "fullName": "Vellore, Tamil Nadu",
        "lat": 12.9165,
        "lng": 79.1325,
        "region": "Tamil Nadu",
        "climate": "hot",
        "experience": "history",
        "budget": "low",
        "summary": "Historic fort city renowned for the 16th-century Vellore Granite Fort and the dazzling Sripuram Golden Temple.",
        "attractions": [
            {
                "name": "Vellore Fort & Jalakandeswarar Temple",
                "highlight": "Massive 16th-century granite fort surrounded by a deep moat with exquisite Vijayanagara temple.",
                "duration": "3 hours",
                "bestTime": "Morning (8 AM)",
                "lat": 12.923,
                "lng": 79.13
            },
            {
                "name": "Sripuram Golden Temple (Maha Lakshmi)",
                "highlight": "Dazzling spiritual park temple covered in 1,500 kg of pure gold leaf foil inside a star-shaped path.",
                "duration": "3.5 hours",
                "bestTime": "Afternoon till illuminated evening",
                "lat": 12.871,
                "lng": 79.088
            },
            {
                "name": "Amirthi Zoological Forest Park",
                "highlight": "Eco-park with natural waterfalls, wildlife zoo, and trekking paths in Javadi Hills.",
                "duration": "3 hours",
                "bestTime": "Morning",
                "lat": 12.75,
                "lng": 79.05
            },
            {
                "name": "Ratnagiri Murugan Temple & Science Park",
                "highlight": "Hilltop temple with panoramic vistas of the surrounding Eastern Ghats plains.",
                "duration": "2 hours",
                "bestTime": "Evening",
                "lat": 12.97,
                "lng": 79.25
            }
        ],
        "hotels": [
            {
                "name": "Fortune Park Vellore - Member ITC Hotel Group",
                "type": "Luxury",
                "price": "₹5,200/night",
                "rating": "4.7★"
            },
            {
                "name": "Rangalaya Royal Vellore",
                "type": "Mid-range",
                "price": "₹2,800/night",
                "rating": "4.3★"
            },
            {
                "name": "Darling Residency Vellore",
                "type": "Budget-friendly",
                "price": "₹1,800/night",
                "rating": "4.2★"
            }
        ]
    },
    "kolli hills": {
        "fullName": "Kolli Hills (Kolli Malai), Namakkal, Tamil Nadu",
        "lat": 11.2485,
        "lng": 78.3387,
        "region": "Tamil Nadu",
        "climate": "cold",
        "experience": "adventure",
        "budget": "low",
        "summary": "Mountain of Death (now mountain of life) famous for 70 exhilarating hairpin bends, the roaring Agaya Gangai waterfall, and herbal honey.",
        "attractions": [
            {
                "name": "70 Hairpin Bends Mountain Drive",
                "highlight": "One of India's most thrilling winding hill climbs with breathtaking panoramic viewpoints.",
                "duration": "2 hours",
                "bestTime": "Morning (8 AM)",
                "lat": 11.29,
                "lng": 78.31
            },
            {
                "name": "Agaya Gangai Waterfalls (300 ft)",
                "highlight": "Spectacular 300-ft cascade reached by descending 1,000 stone steps into the river canyon.",
                "duration": "3.5 hours",
                "bestTime": "Morning",
                "lat": 11.275,
                "lng": 78.345
            },
            {
                "name": "Arapaleeswarar Temple",
                "highlight": "Ancient Shiva temple on the mountain mentioned in classical Sangam literature.",
                "duration": "1.5 hours",
                "bestTime": "Morning / 4 PM",
                "lat": 11.276,
                "lng": 78.344
            },
            {
                "name": "Seekuparai & Selur Viewpoint",
                "highlight": "Watchtowers offering bird's eye views over the emerald valleys and pineapple estates.",
                "duration": "2 hours",
                "bestTime": "Sunset (5 PM)",
                "lat": 11.255,
                "lng": 78.36
            },
            {
                "name": "Namakkal Anjaneyar Temple & Rock Fort",
                "highlight": "Single-stone 18-ft open-sky Hanuman statue and historic hilltop rock fortress.",
                "duration": "2.5 hours",
                "bestTime": "Morning",
                "lat": 11.2189,
                "lng": 78.1674
            }
        ],
        "hotels": [
            {
                "name": "Silverline Retreat Hotel Kolli Hills",
                "type": "Mid-range",
                "price": "₹2,800/night",
                "rating": "4.3★"
            },
            {
                "name": "Nallathambi Resort Kolli Hills",
                "type": "Budget-friendly",
                "price": "₹1,600/night",
                "rating": "4.1★"
            }
        ]
    },
    "kumbakonam": {
        "fullName": "Kumbakonam, Tamil Nadu",
        "lat": 10.9602,
        "lng": 79.3845,
        "region": "Tamil Nadu",
        "climate": "moderate",
        "experience": "history",
        "budget": "low",
        "summary": "The Temple Town of South India, famous for Navagraha temple circuits, UNESCO Airavatesvara Temple, and the Mahamaham festival.",
        "attractions": [
            {
                "name": "Adi Kumbeswarar Temple & Mahamaham Tank",
                "highlight": "Largest Shiva temple in Kumbakonam with 6.2-acre sacred tank (Kumbh Mela of South India).",
                "duration": "2.5 hours",
                "bestTime": "Morning (6-11 AM)",
                "lat": 10.958,
                "lng": 79.378
            },
            {
                "name": "Airavatesvara Temple (Darasuram - UNESCO)",
                "highlight": "Chola architectural masterpiece featuring chariot-shaped stone mandapam and singing musical steps.",
                "duration": "2.5 hours",
                "bestTime": "Morning / 4 PM",
                "lat": 10.948,
                "lng": 79.356
            },
            {
                "name": "Sarangapani Temple & Ramaswamy Temple",
                "highlight": "Grand 12-tier Vishnu temple with chariot-shaped sanctum and Ramayana fresco paintings.",
                "duration": "2 hours",
                "bestTime": "Morning / 6 PM",
                "lat": 10.961,
                "lng": 79.375
            },
            {
                "name": "Swamimalai Murugan Temple",
                "highlight": "One of the Six Abodes (Arupadai Veedu) of Lord Murugan where he taught the Pranava Mantra to Shiva.",
                "duration": "2 hours",
                "bestTime": "Morning",
                "lat": 10.954,
                "lng": 79.328
            },
            {
                "name": "Kumbakonam Degree Filter Coffee Trail",
                "highlight": "Sample authentic rich South Indian chicory filter coffee served in brass davarah-tumblers.",
                "duration": "1 hour",
                "bestTime": "Morning / Evening",
                "lat": 10.96,
                "lng": 79.38
            }
        ],
        "hotels": [
            {
                "name": "Mantra Koodam - CGH Earth, Kumbakonam",
                "type": "Luxury",
                "price": "₹9,500/night",
                "rating": "4.9★"
            },
            {
                "name": "Paradise Resort Kumbakonam",
                "type": "Mid-range",
                "price": "₹3,800/night",
                "rating": "4.5★"
            },
            {
                "name": "Hotel Raya's Kumbakonam",
                "type": "Budget-friendly",
                "price": "₹1,400/night",
                "rating": "4.1★"
            }
        ]
    },
    "yelagiri": {
        "fullName": "Yelagiri Hills, Tirupattur, Tamil Nadu",
        "lat": 12.5786,
        "lng": 78.6397,
        "region": "Tamil Nadu",
        "climate": "cold",
        "experience": "nature",
        "budget": "low",
        "summary": "Quiet hill station surrounded by orchards, rose gardens, and green valleys, perfect for peaceful weekend retreats.",
        "attractions": [
            {
                "name": "Punganoor Lake & Nature Park",
                "highlight": "Artificial lake with boating, musical fountain, flower gardens, and walking trails.",
                "duration": "2.5 hours",
                "bestTime": "Morning / Evening",
                "lat": 12.581,
                "lng": 78.642
            },
            {
                "name": "Swamimalai Hill Trekking Peak",
                "highlight": "Highest peak in Yelagiri (4,338 ft) offering trekking trails and views of the valley.",
                "duration": "3.5 hours",
                "bestTime": "Early morning trek",
                "lat": 12.565,
                "lng": 78.632
            },
            {
                "name": "Jalagamparai Waterfalls",
                "highlight": "Natural mountain waterfall created by the Attaru River cascading over rocky terrain.",
                "duration": "3 hours",
                "bestTime": "Morning",
                "lat": 12.602,
                "lng": 78.67
            },
            {
                "name": "Yelagiri Adventure Camp & Telescope House",
                "highlight": "Zip lining, rock climbing, paragliding, and observatory views.",
                "duration": "2.5 hours",
                "bestTime": "Afternoon",
                "lat": 12.585,
                "lng": 78.648
            }
        ],
        "hotels": [
            {
                "name": "Sterling Yelagiri",
                "type": "Luxury",
                "price": "₹4,800/night",
                "rating": "4.6★"
            },
            {
                "name": "Marigold Ridge Resort",
                "type": "Mid-range",
                "price": "₹3,200/night",
                "rating": "4.3★"
            },
            {
                "name": "Hotel Landmark Yelagiri",
                "type": "Budget-friendly",
                "price": "₹1,500/night",
                "rating": "4.1★"
            }
        ]
    },
    "tamil nadu": {
        "fullName": "Tamil Nadu (Grand Heritage & Hill Circuit)",
        "lat": 11.1271,
        "lng": 78.6569,
        "region": "Tamil Nadu",
        "climate": "moderate",
        "experience": "history",
        "budget": "medium",
        "summary": "Enchanting state of grand Dravidian temples, misty Nilgiri and Palani hill stations, and tropical coastal heritage.",
        "attractions": [
            {
                "name": "Meenakshi Amman Temple (Madurai)",
                "highlight": "World-famous architectural wonder with 14 gopurams and Hall of 1000 Pillars.",
                "duration": "3.5 hours",
                "bestTime": "Morning / Evening",
                "lat": 9.9195,
                "lng": 78.1193
            },
            {
                "name": "Brihadeeswarar Big Temple (Thanjavur - UNESCO)",
                "highlight": "1000-year-old Chola architectural wonder with 216-ft vimana.",
                "duration": "3 hours",
                "bestTime": "Morning / Evening",
                "lat": 10.7828,
                "lng": 79.1318
            },
            {
                "name": "Nilgiri Mountain Railway & Doddabetta (Ooty)",
                "highlight": "UNESCO World Heritage steam train journey climbing through Nilgiri tea hills.",
                "duration": "4 hours",
                "bestTime": "Morning",
                "lat": 11.4055,
                "lng": 76.6975
            },
            {
                "name": "Dhanushkodi & Pamban Bridge (Rameswaram)",
                "highlight": "Tip of India where two oceans meet and historic sea bridge.",
                "duration": "4 hours",
                "bestTime": "Morning",
                "lat": 9.1764,
                "lng": 79.4183
            },
            {
                "name": "Vivekananda Rock Memorial (Kanyakumari)",
                "highlight": "Sacred rock monument where three seas meet at India's southern tip.",
                "duration": "3 hours",
                "bestTime": "Sunrise / Morning",
                "lat": 8.0781,
                "lng": 77.5553
            },
            {
                "name": "Shore Temple & Pancha Rathas (Mahabalipuram)",
                "highlight": "UNESCO 7th-century coastal rock-cut temples on the Bay of Bengal.",
                "duration": "3 hours",
                "bestTime": "Morning / Afternoon",
                "lat": 12.6163,
                "lng": 80.1983
            }
        ],
        "hotels": [
            {
                "name": "Taj Coromandel, Chennai",
                "type": "Luxury",
                "price": "₹12,500/night",
                "rating": "4.9★"
            },
            {
                "name": "Heritage Madurai",
                "type": "Luxury",
                "price": "₹7,800/night",
                "rating": "4.7★"
            },
            {
                "name": "The Tamara Kodai",
                "type": "Luxury",
                "price": "₹16,000/night",
                "rating": "4.9★"
            }
        ]
    },
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
                "lat": 32.253,
                "lng": 77.175
            },
            {
                "name": "Jogini Waterfalls & Vashisht Hot Springs",
                "highlight": "Scenic nature trek leading to a cascading waterfall and natural sulphur hot baths.",
                "duration": "3-4 hours",
                "bestTime": "Morning",
                "lat": 32.266,
                "lng": 77.187
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
            {
                "name": "The Himalayan Resort & Spa",
                "type": "Luxury",
                "price": "₹9,500/night",
                "rating": "4.8★"
            },
            {
                "name": "Span Resort & Spa, Manali",
                "type": "Luxury",
                "price": "₹11,000/night",
                "rating": "4.7★"
            },
            {
                "name": "Larisa Resort Manali",
                "type": "Mid-range",
                "price": "₹4,800/night",
                "rating": "4.5★"
            },
            {
                "name": "Zostel Manali (Old Manali)",
                "type": "Budget-friendly",
                "price": "₹1,200/night",
                "rating": "4.6★"
            }
        ]
    },
    "goa": {
        "fullName": "Goa (North & South)",
        "lat": 15.2993,
        "lng": 74.124,
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
                "lat": 15.492,
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
                "lat": 15.01,
                "lng": 74.0232
            },
            {
                "name": "Anjuna Flea Market & Chapora Fort",
                "highlight": "Iconic cliffside fort overlooking the sea ('Dil Chahta Hai' fame) and vibrant market.",
                "duration": "3 hours",
                "bestTime": "5 PM",
                "lat": 15.6059,
                "lng": 73.7386
            }
        ],
        "hotels": [
            {
                "name": "Taj Exotica Resort & Spa, Benaulim",
                "type": "Luxury",
                "price": "₹16,500/night",
                "rating": "4.9★"
            },
            {
                "name": "W Goa, Vagator",
                "type": "Luxury",
                "price": "₹18,000/night",
                "rating": "4.8★"
            },
            {
                "name": "Fairfield by Marriott Goa Anjuna",
                "type": "Mid-range",
                "price": "₹4,200/night",
                "rating": "4.4★"
            },
            {
                "name": "The Hosteller Goa Candolim",
                "type": "Budget-friendly",
                "price": "₹950/night",
                "rating": "4.5★"
            }
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
            {
                "name": "Rambagh Palace (Taj)",
                "type": "Luxury",
                "price": "₹32,000/night",
                "rating": "4.9★"
            },
            {
                "name": "ITC Rajputana, Jaipur",
                "type": "Luxury",
                "price": "₹8,500/night",
                "rating": "4.7★"
            },
            {
                "name": "Hotel Pearl Palace",
                "type": "Mid-range",
                "price": "₹2,600/night",
                "rating": "4.6★"
            },
            {
                "name": "Moustache Hostel Jaipur",
                "type": "Budget-friendly",
                "price": "₹750/night",
                "rating": "4.5★"
            }
        ]
    },
    "delhi": {
        "fullName": "New Delhi & Old Delhi",
        "lat": 28.6139,
        "lng": 77.209,
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
                "lng": 77.241
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
            }
        ],
        "hotels": [
            {
                "name": "The Leela Palace New Delhi",
                "type": "Luxury",
                "price": "₹19,000/night",
                "rating": "4.9★"
            },
            {
                "name": "Taj Mahal Hotel, Mansingh Road",
                "type": "Luxury",
                "price": "₹14,000/night",
                "rating": "4.8★"
            },
            {
                "name": "Bloomrooms @ Janpath",
                "type": "Mid-range",
                "price": "₹3,800/night",
                "rating": "4.4★"
            },
            {
                "name": "goStops Delhi",
                "type": "Budget-friendly",
                "price": "₹850/night",
                "rating": "4.5★"
            }
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
                "lat": 27.18,
                "lng": 78.0416
            }
        ],
        "hotels": [
            {
                "name": "The Oberoi Amarvilas, Agra",
                "type": "Luxury",
                "price": "₹38,000/night",
                "rating": "4.9★"
            },
            {
                "name": "Taj Hotel & Convention Centre",
                "type": "Luxury",
                "price": "₹7,200/night",
                "rating": "4.6★"
            },
            {
                "name": "Howard Plaza - The Fern",
                "type": "Mid-range",
                "price": "₹3,100/night",
                "rating": "4.3★"
            }
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
                "lat": 10.106,
                "lng": 77.124
            }
        ],
        "hotels": [
            {
                "name": "Kumarakom Lake Resort",
                "type": "Luxury",
                "price": "₹22,000/night",
                "rating": "4.9★"
            },
            {
                "name": "Fragrant Nature Munnar",
                "type": "Luxury",
                "price": "₹9,800/night",
                "rating": "4.7★"
            },
            {
                "name": "Zostel Alleppey",
                "type": "Budget-friendly",
                "price": "₹900/night",
                "rating": "4.5★"
            }
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
            }
        ],
        "hotels": [
            {
                "name": "BrijRama Palace, Varanasi",
                "type": "Luxury",
                "price": "₹24,000/night",
                "rating": "4.9★"
            },
            {
                "name": "Taj Ganges, Varanasi",
                "type": "Luxury",
                "price": "₹12,500/night",
                "rating": "4.7★"
            },
            {
                "name": "Hotel Surya, Kaiser Palace",
                "type": "Mid-range",
                "price": "₹3,400/night",
                "rating": "4.4★"
            }
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
            }
        ],
        "hotels": [
            {
                "name": "Taj Lake Palace, Udaipur",
                "type": "Luxury",
                "price": "₹45,000/night",
                "rating": "4.9★"
            },
            {
                "name": "The Oberoi Udaivilas",
                "type": "Luxury",
                "price": "₹42,000/night",
                "rating": "4.9★"
            },
            {
                "name": "Zostel Udaipur",
                "type": "Budget-friendly",
                "price": "₹950/night",
                "rating": "4.6★"
            }
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
                "lat": 31.101,
                "lng": 77.1852
            },
            {
                "name": "Kalka-Shimla Toy Train (UNESCO)",
                "highlight": "Historic narrow-gauge railway journey curving through 102 tunnels and lush pine forests.",
                "duration": "3-4 hours",
                "bestTime": "Morning",
                "lat": 31.103,
                "lng": 77.164
            },
            {
                "name": "Kufri Adventure Park & Mahasu Peak",
                "highlight": "Snow activities, horse riding, and nature trails with Himalayan wildlife zoo.",
                "duration": "4 hours",
                "bestTime": "Morning",
                "lat": 31.098,
                "lng": 77.268
            }
        ],
        "hotels": [
            {
                "name": "Wildflower Hall, An Oberoi Resort",
                "type": "Luxury",
                "price": "₹28,000/night",
                "rating": "4.9★"
            },
            {
                "name": "Radisson Hotel Shimla",
                "type": "Mid-range",
                "price": "₹5,800/night",
                "rating": "4.4★"
            }
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
                "lat": 30.103,
                "lng": 78.293
            },
            {
                "name": "Ram Jhula, Lakshman Jhula & Beatles Ashram",
                "highlight": "Iconic suspension bridges and Maharishi Mahesh Yogi Ashram covered in vibrant murals.",
                "duration": "3 hours",
                "bestTime": "Morning / 3 PM",
                "lat": 30.119,
                "lng": 78.314
            }
        ],
        "hotels": [
            {
                "name": "Ananda in the Himalayas",
                "type": "Luxury",
                "price": "₹36,000/night",
                "rating": "4.9★"
            },
            {
                "name": "Aloha On The Ganges",
                "type": "Mid-range",
                "price": "₹6,500/night",
                "rating": "4.6★"
            }
        ]
    },
    "mumbai": {
        "fullName": "Mumbai, Maharashtra",
        "lat": 18.922,
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
                "lat": 18.922,
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
            }
        ],
        "hotels": [
            {
                "name": "The Taj Mahal Palace, Mumbai",
                "type": "Luxury",
                "price": "₹26,000/night",
                "rating": "4.9★"
            },
            {
                "name": "The St. Regis Mumbai",
                "type": "Luxury",
                "price": "₹16,000/night",
                "rating": "4.8★"
            }
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
    """Fuzzy match place query against our curated knowledge base with Tamil Nadu aliases."""
    if not place_query:
        return None
    q = place_query.lower().strip()

    # Direct / Alias mappings
    aliases = {
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
    }

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
        "You are TripNova's premier India and Tamil Nadu travel planner. Given user preferences, "
        "recommend exactly 3 top famous destinations. "
        "Respond ONLY with valid JSON format: "
        '{"places":['
        '{"name":"Destination, State","reason":"Detailed explanation why it fits",'
        '"tag":"Adventure|Nature|Heritage|Relaxation|Spiritual|Culture","bestSeason":"e.g. Oct-Mar","lat":13.08,"lng":80.27}'
        ']}'
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
        "You are TripNova's expert travel itinerary generator. "
        f"Generate a realistic, comprehensive, prioritized {days}-day itinerary for {place}, India "
        f"for {travel_with} travellers. "
        "CRITICAL RULES: "
        "1. Prioritize TOP ICONIC, FAMOUS tourist landmarks (e.g. major forts, UNESCO heritage, temples, beaches, viewpoints). "
        "2. Structure Day 1 with the most iconic must-visit landmarks. Day 2 with major heritage & cultural hubs. Day 3+ with scenic nature, viewpoints, and local experiences. "
        "3. Provide exact or realistic latitude and longitude coordinates for the destination city and for each attraction spot so they can be pinned on an interactive map. "
        "4. Include 3-4 top hotels (Luxury, Mid-range, Budget-friendly) with price range and rating. "
        "Respond ONLY with valid JSON schema: "
        '{"place":"City, State","lat":13.0827,"lng":80.2707,'
        '"summary":"Overview of the destination",'
        '"itinerary":['
        '{"day":1,"title":"Iconic Heritage & Landmarks",'
        '"places":['
        '{"name":"Spot Name","highlight":"Why it is a must-visit","duration":"2-3 hours","bestTime":"Morning","lat":13.05,"lng":80.28}'
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

    # Dynamic algorithmic generation for any custom Indian or Tamil Nadu place
    dest_name = place.title()
    approx_lat = 11.1271 if "tamil" in place.lower() else 20.5937
    approx_lng = 78.6569 if "tamil" in place.lower() else 78.9629

    dynamic_itinerary = []
    for d in range(1, days + 1):
        if d == 1:
            spots = [
                {"name": f"Iconic Landmark & Center of {dest_name}", "highlight": f"Top historic monument and central tourist highlight of {dest_name}.", "duration": "2.5 hours", "bestTime": "Morning", "lat": approx_lat + 0.01, "lng": approx_lng + 0.01},
                {"name": f"{dest_name} Heritage Fort / Temple", "highlight": "Major historical architectural attraction with panoramic views.", "duration": "3 hours", "bestTime": "Afternoon", "lat": approx_lat - 0.01, "lng": approx_lng + 0.01}
            ]
            title = "Historic Highlights & Main Sights"
        elif d == 2:
            spots = [
                {"name": f"{dest_name} Nature Reserve & Viewpoint", "highlight": "Serene natural reserve, viewpoints, and walking trails.", "duration": "3 hours", "bestTime": "Morning", "lat": approx_lat + 0.02, "lng": approx_lng - 0.01},
                {"name": f"Traditional Bazaar & Food Trail of {dest_name}", "highlight": "Famous local markets, authentic cuisine, and artisan handicrafts.", "duration": "2.5 hours", "bestTime": "Evening", "lat": approx_lat, "lng": approx_lng}
            ]
            title = "Nature Trails & Cultural Bazaars"
        else:
            spots = [
                {"name": f"Scenic Sunset Viewpoint in {dest_name}", "highlight": "Breathtaking panoramic viewpoints and photography spot.", "duration": "2 hours", "bestTime": "Late Afternoon", "lat": approx_lat - 0.02, "lng": approx_lng - 0.02},
                {"name": f"Ancient Spiritual Center of {dest_name}", "highlight": "Sacred cultural temple known for rich Dravidian architecture.", "duration": "2 hours", "bestTime": "Morning", "lat": approx_lat + 0.015, "lng": approx_lng - 0.015}
            ]
            title = f"Scenic Viewpoints & Hidden Gems (Day {d})"

        dynamic_itinerary.append({
            "day": d,
            "title": title,
            "places": spots
        })

    dynamic_hotels = [
        {"name": f"Grand Heritage Stay {dest_name}", "type": "Luxury", "price": "₹6,500/night", "rating": "4.8★"},
        {"name": f"The Residency {dest_name}", "type": "Mid-range", "price": "₹3,200/night", "rating": "4.5★"},
        {"name": f"TripNova Comfort Stay {dest_name}", "type": "Budget-friendly", "price": "₹1,200/night", "rating": "4.3★"}
    ]

    return {
        "place": dest_name,
        "lat": approx_lat,
        "lng": approx_lng,
        "summary": f"A vibrant destination in Tamil Nadu / India with cultural heritage, scenic landmarks, and local flavors.",
        "itinerary": dynamic_itinerary,
        "hotels": dynamic_hotels,
        "source": "dynamic_engine"
    }


def explain_unsuitable_place(preferences, place_name):
    """Explain why a particular place might not match user preferences."""
    system = (
        "You are TripNova's expert travel advisor. Explain constructively in 2-3 friendly sentences "
        "why a given destination might not perfectly match the user's selected preferences (climate, budget, companions, vibe)."
    )
    user = f"Preferences: {json.dumps(preferences)}\nPlace asked: {place_name}"
    raw = _call_llm(system, user)
    if raw:
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
    """AI Co-Pilot chat assistant for India & Tamil Nadu travel inquiries."""
    system = (
        "You are TripNova's AI Travel Co-Pilot. Answer questions about travelling in India and Tamil Nadu "
        "(itineraries, transport, buses, trains, IRCTC, RedBus, hotels, local cuisine, safety, seasons, temples, hill stations). "
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

    msg_lower = message.lower().strip()
    if any(w in msg_lower for w in ["kerala", "munnar", "alleppey", "best time to visit kerala"]):
        return {
            "answer": "🌴 Best Time & Tips for Kerala:\n\n• Peak Season (Oct–March): Pleasant winter weather (22°C–30°C), ideal for Alleppey backwater houseboats, Munnar tea hills, and beach sunsets at Varkala & Kovalam.\n• Monsoon Season (June–Sept): Best for authentic Ayurvedic rejuvenation treatments and roaring waterfalls (Athirappilly).\n• Top Highlights: Alleppey Shikara/Houseboat, Eravikulam Tahr sanctuary, Fort Kochi colonial streets, and traditional Kerala Sadhya feast!",
            "source": "knowledge_engine"
        }
    elif any(w in msg_lower for w in ["rajasthan", "family trip in rajasthan", "jaipur", "udaipur"]):
        return {
            "answer": "🏰 Perfect Family Trip in Rajasthan:\n\n• Ideal Circuit (5–7 Days): Jaipur (Amber Fort & Hawa Mahal) ➔ Jodhpur (Mehrangarh Blue Fort) ➔ Udaipur (Lake Pichola Boat Cruise & City Palace).\n• Desert Adventure: Take an overnight Swiss-tent camel safari in Jaisalmer Sam Sand Dunes.\n• Culinary Treats: Authentic Dal Baati Churma, Pyaaz Kachori, and Ghevar sweets.\n• Best Season: October to March.",
            "source": "knowledge_engine"
        }
    elif any(w in msg_lower for w in ["hidden", "offbeat", "hill station"]):
        return {
            "answer": "🏔️ Top Hidden & Offbeat Hill Stations in India:\n\n1. Yercaud & Valparai (Tamil Nadu): 40 scenic hairpin bends, tea valleys, and Sholayar dam without commercial crowds.\n2. Kolli Hills (Tamil Nadu): 70 thrilling mountain curves and the 300-ft Agaya Gangai waterfall.\n3. Jibhi & Tirthan Valley (Himachal): Wooden pine cottages, trout streams, and Serolsar lake.\n4. Chopta (Uttarakhand): The 'Mini Switzerland of India' and base for Tungnath.\n5. Vagamon (Kerala): Rolling pine forests and mist-covered tea knolls.",
            "source": "knowledge_engine"
        }
    elif any(w in msg_lower for w in ["vegetarian", "food", "cuisine", "dish"]):
        return {
            "answer": "🍲 Top Vegetarian Food Trails Across India:\n\n• Tamil Nadu: Madurai Bun Parotta & Kari Dosa alternatives, Kumbakonam Degree Filter Coffee & Ghee Roast Dosa, Murugan Idli, and authentic Jigarthanda.\n• Rajasthan: Authentic Rajasthani Thali with Dal Baati Churma, Gatte ki Sabzi, and Ker Sangri.\n• Varanasi & UP: Banarasi Tamatar Chaat, Kachori Jalebi, Malaiyo froth, and Banarasi Meetha Paan.\n• Gujarat: Kathiyawadi Thali with Dhokla, Handvo, Undhiyu, and Shrikhand.\n• Punjab & Delhi: Amritsari Kulcha with Chole, Dal Makhani, and thick Lassi.",
            "source": "knowledge_engine"
        }
    elif any(w in msg_lower for w in ["bus", "redbus", "seat", "route"]):
        return {
            "answer": "🚌 Bus Booking in TripNova:\n\nYou can book buses directly inside this app under the 'Bus Booking' tab! It includes live route searches for RedBus, IntrCity, Zingbus, and KSRTC, an interactive lower & upper deck seat layout picker, and instant e-ticket generation with PNR.",
            "source": "knowledge_engine"
        }
    elif any(w in msg_lower for w in ["train", "irctc", "pnr", "rail"]):
        return {
            "answer": "🚂 Train Booking in TripNova:\n\nUse our built-in 'Train Booking' tab to search Indian Railways train routes (Vande Bharat, Rajdhani, Express), check real-time class availability (1A, 2A, 3A, SL, CC), and track 10-digit Live PNR Status instantly!",
            "source": "knowledge_engine"
        }
    elif any(w in msg_lower for w in ["hotel", "stay", "room", "oyo", "taj"]):
        return {
            "answer": "🏨 Hotel Reservations in TripNova:\n\nCheck out the 'Hotels' tab to find handpicked luxury heritage palaces, mountain tea-bungalows, beach resorts, and verified budget-friendly rooms with instant reservation vouchers.",
            "source": "knowledge_engine"
        }
    elif any(w in msg_lower for w in ["tamil nadu", "tamilnadu", "madurai", "ooty", "kodai", "kodaikanal", "rameswaram", "thanjavur"]):
        return {
            "answer": "🛕 Tamil Nadu Travel Highlights:\n\n• Hill Stations: Ooty (Toy Train & Botanical Gardens), Kodaikanal (Star Lake & Pillar Rocks), Yercaud & Valparai.\n• UNESCO Heritage & Temples: Madurai Meenakshi Amman, Thanjavur Brihadeeswarar Big Temple, Rameswaram Pamban Bridge & 22 Theerthams, and Kanchipuram silk shrines.\n• Coastal Wonders: Kanyakumari Triveni Sangam and Mahabalipuram Shore Temples.",
            "source": "knowledge_engine"
        }
    elif any(w in msg_lower for w in ["manali", "snow", "himachal"]):
        return {
            "answer": "❄️ Manali & Himachal Travel Guide:\n\n• Snow Season: December to February for fresh snowfall in Solang Valley, Rohtang Pass, and Sissu.\n• Adventure: Paragliding, river rafting in Kullu Beas, and trekking to Jogini Waterfall.\n• Cafe Trail: Old Manali Bohemian cafes with trout fish and wood-fired pizzas.",
            "source": "knowledge_engine"
        }
    else:
        return {
            "answer": "✨ Welcome to TripNova! I can help you plan your journey across all states and places in India. Ask me about specific destinations, best travel months, local food trails, bus & train routes, or customized day-wise itineraries.",
            "source": "knowledge_engine"
        }

