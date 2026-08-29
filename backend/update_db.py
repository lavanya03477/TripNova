# -*- coding: utf-8 -*-
import json
import os

TAMIL_NADU_PLACES = {
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
            {"name": "Marina Beach & Lighthouse", "highlight": "World's second-longest urban natural beach with street food and lighthouse view.", "duration": "2.5 hours", "bestTime": "Evening (5 PM)", "lat": 13.0500, "lng": 80.2824},
            {"name": "Kapaleeshwarar Temple (Mylapore)", "highlight": "7th-century Dravidian Shiva temple with magnificent multi-colored gopuram and tank.", "duration": "2 hours", "bestTime": "Morning / 6 PM", "lat": 13.0336, "lng": 80.2697},
            {"name": "San Thome Basilica & Fort St. George", "highlight": "Historic neo-Gothic cathedral built over St. Thomas apostle tomb and 1644 British fort museum.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 13.0337, "lng": 80.2778},
            {"name": "Guindy National Park & Snake Park", "highlight": "Unique protected national park situated right within city limits with spotted deer and blackbucks.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 13.0067, "lng": 80.2206},
            {"name": "DakshinaChitra & MGM Beach Trail", "highlight": "Living heritage museum showcasing traditional architecture and crafts of South India.", "duration": "3 hours", "bestTime": "Afternoon", "lat": 12.8256, "lng": 80.2415},
            {"name": "Valluvar Kottam & T. Nagar Shopping", "highlight": "Monument dedicated to classical Tamil poet Thiruvalluvar and famous silk/gold bazaar.", "duration": "2 hours", "bestTime": "Evening", "lat": 13.0543, "lng": 80.2417}
        ],
        "hotels": [
            {"name": "Taj Coromandel, Chennai", "type": "Luxury", "price": "₹12,500/night", "rating": "4.9★"},
            {"name": "The Leela Palace Chennai", "type": "Luxury", "price": "₹16,000/night", "rating": "4.9★"},
            {"name": "The Residency Towers T. Nagar", "type": "Mid-range", "price": "₹4,200/night", "rating": "4.5★"},
            {"name": "Zostel Chennai", "type": "Budget-friendly", "price": "₹850/night", "rating": "4.4★"}
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
            {"name": "Meenakshi Amman Temple", "highlight": "Architectural marvel with 14 soaring gopurams, Hall of Thousand Pillars, and intricate Dravidian carvings.", "duration": "3.5 hours", "bestTime": "Morning (6-11 AM) or Evening (5-9 PM)", "lat": 9.9195, "lng": 78.1193},
            {"name": "Thirumalai Nayakkar Mahal", "highlight": "17th-century Indo-Saracenic royal palace with gigantic circular pillars and evening light-and-sound show.", "duration": "2 hours", "bestTime": "Afternoon / 6:45 PM for Sound & Light show", "lat": 9.9152, "lng": 78.1238},
            {"name": "Gandhi Memorial Museum & Tamukkam Palace", "highlight": "Historic museum housing Mahatma Gandhi's blood-stained dhoti and freedom struggle gallery.", "duration": "2 hours", "bestTime": "Morning", "lat": 9.9327, "lng": 78.1402},
            {"name": "Alagar Koyil (Alagar Hills)", "highlight": "Ancient temple of Lord Vishnu situated in the lush forest foothills of Alagar Hills.", "duration": "3 hours", "bestTime": "Morning", "lat": 10.0769, "lng": 78.2144},
            {"name": "Vandiyur Mariamman Teppakulam", "highlight": "Huge temple tank with a central mandapam, famous for the annual float festival.", "duration": "1 hour", "bestTime": "Evening", "lat": 9.9098, "lng": 78.1528},
            {"name": "Madurai Street Food & Jigarthanda Trail", "highlight": "Sample famous Madurai Bun Parotta, Kari Dosa, Murugan Idli, and authentic Famous Jigarthanda.", "duration": "2.5 hours", "bestTime": "Evening (7 PM onwards)", "lat": 9.9200, "lng": 78.1220}
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
        "summary": "Queen of the Nilgiris known for rolling tea estates, UNESCO toy train rides, botanical gardens, and mist-clad peaks.",
        "attractions": [
            {"name": "Nilgiri Mountain Railway (Toy Train)", "highlight": "UNESCO World Heritage steam train journey climbing through Nilgiri tea hills.", "duration": "3 hours", "bestTime": "Morning (9 AM)", "lat": 11.4055, "lng": 76.6975},
            {"name": "Ooty Botanical Gardens & Rose Garden", "highlight": "55-acre sprawling Victorian gardens with fossilized tree trunk and thousands of rose varieties.", "duration": "2.5 hours", "bestTime": "Morning / Afternoon", "lat": 11.4172, "lng": 76.7118},
            {"name": "Doddabetta Peak", "highlight": "Highest mountain peak in the Nilgiri Hills with telescope observatory overlooking valleys.", "duration": "2.5 hours", "bestTime": "Morning (clear skies)", "lat": 11.4014, "lng": 76.7371},
            {"name": "Pykara Lake & Waterfalls", "highlight": "Scenic lake with speedboat rides, Toda tribal settlements, and cascading pine-forest falls.", "duration": "3.5 hours", "bestTime": "Afternoon", "lat": 11.4880, "lng": 76.5920},
            {"name": "Ooty Lake & Boat House", "highlight": "Serene artificial lake surrounded by eucalyptus trees with pedal and motor boating.", "duration": "2 hours", "bestTime": "Late afternoon", "lat": 11.4075, "lng": 76.6872},
            {"name": "Avalanche Lake & Emerald Dam", "highlight": "Pristine untouched valley lake surrounded by trout streams and shola forests.", "duration": "4 hours", "bestTime": "Morning jeep safari", "lat": 11.2989, "lng": 76.5866}
        ],
        "hotels": [
            {"name": "Savoy - IHCL SeleQtions, Ooty", "type": "Luxury", "price": "₹13,500/night", "rating": "4.8★"},
            {"name": "Sterling Ooty Fern Hill", "type": "Mid-range", "price": "₹5,200/night", "rating": "4.5★"},
            {"name": "Sinclairs Retreat Ooty", "type": "Mid-range", "price": "₹4,200/night", "rating": "4.3★"},
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
        "summary": "Princess of Hill Stations in the Palani Hills, renowned for its star-shaped Kodai Lake, Coaker's Walk, and Pillar Rocks.",
        "attractions": [
            {"name": "Kodaikanal Star Lake & Cycling", "highlight": "Iconic star-shaped lake offering pedal boating, horse riding, and cycling promenade.", "duration": "2.5 hours", "bestTime": "Morning / Evening", "lat": 10.2330, "lng": 77.4900},
            {"name": "Coaker's Walk & Bryant Park", "highlight": "1km paved pedestrian path on steep mountain ridge overlooking misty plains below.", "duration": "2 hours", "bestTime": "Morning (9 AM)", "lat": 10.2312, "lng": 77.4958},
            {"name": "Pillar Rocks & Guna Caves (Devil's Kitchen)", "highlight": "Three giant 400-ft granite pillars rising vertically out of cliff-side mist.", "duration": "2.5 hours", "bestTime": "Afternoon", "lat": 10.2078, "lng": 77.4725},
            {"name": "Dolphin's Nose & Echo Point", "highlight": "Flat rock projecting over a 6,600-ft deep precipice offering thrilling views of the valley.", "duration": "3.5 hours", "bestTime": "Morning trek", "lat": 10.2100, "lng": 77.5180},
            {"name": "Silver Cascade Falls & Bear Shola Falls", "highlight": "180-ft natural waterfall created from Kodai Lake overflow amidst pine woods.", "duration": "1.5 hours", "bestTime": "Morning", "lat": 10.2520, "lng": 77.5100},
            {"name": "Pine Forest & Mannavanur Eco Lake", "highlight": "Dense preserved pine plantations (movie shooting spot) and peaceful sheep farm lake.", "duration": "4 hours", "bestTime": "Morning", "lat": 10.2150, "lng": 77.4520}
        ],
        "hotels": [
            {"name": "The Tamara Kodai", "type": "Luxury", "price": "₹16,000/night", "rating": "4.9★"},
            {"name": "Carlton Hotel Kodaikanal", "type": "Luxury", "price": "₹11,000/night", "rating": "4.7★"},
            {"name": "Sterling Kodai Lake", "type": "Mid-range", "price": "₹4,800/night", "rating": "4.4★"},
            {"name": "Zostel Kodaikanal", "type": "Budget-friendly", "price": "₹900/night", "rating": "4.6★"}
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
            {"name": "Ramanathaswamy Temple & 22 Theerthams", "highlight": "One of 12 Jyotirlingas, famous for the world's longest temple corridor with 1212 carved pillars.", "duration": "3.5 hours", "bestTime": "Early morning (5-11 AM)", "lat": 9.2881, "lng": 79.3174},
            {"name": "Pamban Sea Bridge & Railway Bridge", "highlight": "India's first sea bridge spanning over the ocean connecting Pamban Island to mainland India.", "duration": "1.5 hours", "bestTime": "Sunrise / Sunset", "lat": 9.2780, "lng": 79.1960},
            {"name": "Dhanushkodi Ghost Town & Arichal Munai", "highlight": "Submerged city at the tip of India where the Bay of Bengal meets the Indian Ocean.", "duration": "3.5 hours", "bestTime": "Morning / 3 PM", "lat": 9.1764, "lng": 79.4183},
            {"name": "Agni Theertham & Sangumal Beach", "highlight": "Sacred ocean bathing shore facing the temple where devotees take holy dips in calm waves.", "duration": "1.5 hours", "bestTime": "Sunrise", "lat": 9.2890, "lng": 79.3210},
            {"name": "Dr. APJ Abdul Kalam National Memorial", "highlight": "Beautiful memorial museum celebrating the life, rockets, and legacy of India's Missile Man.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 9.2930, "lng": 79.2820}
        ],
        "hotels": [
            {"name": "Daiwik Hotels Rameswaram", "type": "Mid-range", "price": "₹3,800/night", "rating": "4.5★"},
            {"name": "Hyatt Place Rameswaram", "type": "Luxury", "price": "₹6,500/night", "rating": "4.7★"},
            {"name": "Hotel MCM Towers", "type": "Budget-friendly", "price": "₹1,500/night", "rating": "4.2★"}
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
            {"name": "Vivekananda Rock Memorial & Ferry", "highlight": "Iconic rock monument built in 1970 where Swami Vivekananda attained enlightenment.", "duration": "3 hours", "bestTime": "Morning ferry (8 AM)", "lat": 8.0781, "lng": 77.5553},
            {"name": "Thiruvalluvar 133-ft Statue", "highlight": "Colossal stone statue honoring Tamil philosopher poet Thiruvalluvar standing in the ocean.", "duration": "1.5 hours", "bestTime": "Morning", "lat": 8.0778, "lng": 77.5540},
            {"name": "Triveni Sangam & Sunset / Sunrise Point", "highlight": "Spectacular geographical vantage point to witness simultaneous sunrise and sunset over three seas.", "duration": "2 hours", "bestTime": "Sunrise (6 AM) & Sunset (6 PM)", "lat": 8.0810, "lng": 77.5520},
            {"name": "Padmanabhapuram Palace (Thuckalay)", "highlight": "Magnificent 16th-century wooden palace displaying Kerala-Tamil teak architecture.", "duration": "3 hours", "bestTime": "Afternoon", "lat": 8.2508, "lng": 77.3275},
            {"name": "Bhagavathy Amman Temple & Gandhi Mandapam", "highlight": "3000-year-old temple of Goddess Kanya Kumari and memorial built in Odishan style.", "duration": "2 hours", "bestTime": "Morning / Evening", "lat": 8.0815, "lng": 77.5535}
        ],
        "hotels": [
            {"name": "The Gopinivas Grand, Kanyakumari", "type": "Luxury", "price": "₹4,800/night", "rating": "4.6★"},
            {"name": "Annai Resorts & Spa", "type": "Luxury", "price": "₹6,200/night", "rating": "4.7★"},
            {"name": "Hotel Sea View Kanyakumari", "type": "Mid-range", "price": "₹3,100/night", "rating": "4.4★"},
            {"name": "Hotel Sun World", "type": "Budget-friendly", "price": "₹1,200/night", "rating": "4.1★"}
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
        "summary": "The Cradle of Chola Architecture and South Indian culture, home to the UNESCO World Heritage Brihadeeswarar Big Temple.",
        "attractions": [
            {"name": "Brihadeeswarar Temple (Peruvudaiyar Kovil / Big Temple)", "highlight": "1000-year-old Chola architectural wonder with 216-ft vimana and 80-tonne single granite capstone.", "duration": "3.5 hours", "bestTime": "Morning (7-11 AM) or Evening sunset", "lat": 10.7828, "lng": 79.1318},
            {"name": "Thanjavur Maratha Royal Palace Complex", "highlight": "Historic palace featuring Durbar Hall, Bell Tower, and royal residence courtyards.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 10.7925, "lng": 79.1360},
            {"name": "Saraswathi Mahal Library & Art Gallery", "highlight": "One of the oldest medieval libraries in Asia housing ancient palm leaf manuscripts and Chola bronze statues.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 10.7930, "lng": 79.1368},
            {"name": "Punnainallur Mariamman Temple", "highlight": "Famous 17th-century temple built by Venkoji Maharaja known for natural anthill deity.", "duration": "1.5 hours", "bestTime": "Morning / 5 PM", "lat": 10.7760, "lng": 79.1910},
            {"name": "Thanjavur Art Plate & Dancing Doll Workshop Trail", "highlight": "Witness master craftsmen crafting traditional Thanjavur paintings, bronze plates, and roly-poly dolls.", "duration": "2 hours", "bestTime": "Evening", "lat": 10.7880, "lng": 79.1400}
        ],
        "hotels": [
            {"name": "Svatma, Thanjavur - Relais & Châteaux", "type": "Luxury", "price": "₹14,000/night", "rating": "4.9★"},
            {"name": "Great Trails River View Thanjavur by GRT", "type": "Luxury", "price": "₹6,800/night", "rating": "4.7★"},
            {"name": "Hotel Gnanam", "type": "Mid-range", "price": "₹2,400/night", "rating": "4.3★"},
            {"name": "Hotel Parisutham", "type": "Mid-range", "price": "₹2,800/night", "rating": "4.4★"}
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
            {"name": "Isha Yoga Center & 112-ft Adiyogi Statue", "highlight": "Guinness World Record largest bust sculpture of Adiyogi Shiva, Dhyanalinga, and evening laser 3D show.", "duration": "4-5 hours", "bestTime": "Afternoon till 7:30 PM light show", "lat": 10.9760, "lng": 76.7410},
            {"name": "Marudhamalai Murugan Hill Temple", "highlight": "1200-year-old scenic hilltop temple dedicated to Lord Murugan surrounded by medicinal herbal groves.", "duration": "2.5 hours", "bestTime": "Morning (7 AM)", "lat": 11.0450, "lng": 76.8520},
            {"name": "Siruvani Waterfalls & Dam", "highlight": "Crystal-clear waterfalls renowned for having one of the sweetest natural mineral waters in the world.", "duration": "3.5 hours", "bestTime": "Morning (permit required)", "lat": 10.9400, "lng": 76.6800},
            {"name": "GD Naidu Science & Vintage Car Museum", "highlight": "Fascinating automotive museum exhibiting rare antique cars from Britain, Germany, and America.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 11.0110, "lng": 76.9740},
            {"name": "Perur Pateeswarar Temple", "highlight": "Ancient Chola temple with exquisite Kanaka Sabha hall displaying intricately carved stone statues.", "duration": "2 hours", "bestTime": "Morning / Evening", "lat": 10.9710, "lng": 76.9180}
        ],
        "hotels": [
            {"name": "The Residency Towers Coimbatore", "type": "Luxury", "price": "₹6,800/night", "rating": "4.8★"},
            {"name": "Radisson Blu Hotel Coimbatore", "type": "Luxury", "price": "₹6,200/night", "rating": "4.7★"},
            {"name": "Zone by The Park Coimbatore", "type": "Mid-range", "price": "₹3,400/night", "rating": "4.4★"},
            {"name": "Ibis Coimbatore City Centre", "type": "Mid-range", "price": "₹2,900/night", "rating": "4.3★"}
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
            {"name": "UNESCO Shore Temple", "highlight": "8th-century structural granite temple built directly on the shores of the Bay of Bengal.", "duration": "2 hours", "bestTime": "Sunrise or 4 PM", "lat": 12.6163, "lng": 80.1983},
            {"name": "Pancha Rathas (Five Rathas)", "highlight": "Monolithic rock-cut shrines carved out of single granite stones in the shape of chariots.", "duration": "2 hours", "bestTime": "Morning", "lat": 12.6092, "lng": 80.1914},
            {"name": "Arjuna's Penance & Krishna's Butterball", "highlight": "World's largest open-air rock bas-relief and a 250-tonne gigantic boulder balanced on a 45-degree rock slope.", "duration": "2 hours", "bestTime": "Morning / 3 PM", "lat": 12.6186, "lng": 80.1936},
            {"name": "Mahabalipuram Lighthouse & Cave Temples", "highlight": "Historic circular stone lighthouse offering 360-degree ocean views and Varaha Cave mandapam.", "duration": "2 hours", "bestTime": "Late afternoon", "lat": 12.6160, "lng": 80.1920},
            {"name": "Covelong Beach & Surfing School", "highlight": "Premier surfing village on the East Coast Road with windsurfing and fresh seafood.", "duration": "3 hours", "bestTime": "Morning", "lat": 12.7880, "lng": 80.2520}
        ],
        "hotels": [
            {"name": "Radisson Blu Resort Temple Bay", "type": "Luxury", "price": "₹11,500/night", "rating": "4.8★"},
            {"name": "InterContinental Chennai Mahabalipuram", "type": "Luxury", "price": "₹15,000/night", "rating": "4.9★"},
            {"name": "Grande Bay Resort & Spa", "type": "Mid-range", "price": "₹5,800/night", "rating": "4.6★"},
            {"name": "Myna Villa Mahabalipuram", "type": "Budget-friendly", "price": "₹1,200/night", "rating": "4.3★"}
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
            {"name": "Kanchi Kamakshi Amman Temple", "highlight": "One of 51 Shakti Peethas with golden gopuram and sanctum in the heart of Kanchi.", "duration": "2.5 hours", "bestTime": "Morning (6-11 AM)", "lat": 12.8406, "lng": 79.7030},
            {"name": "Ekambareswarar Temple (Earth Element)", "highlight": "Massive 23-acre temple featuring 59-meter tall raja gopuram and 3,500-year-old sacred mango tree.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 12.8475, "lng": 79.6997},
            {"name": "Kailasanathar Temple", "highlight": "Oldest sandstone temple in Kanchipuram built by Pallava king Rajasimha in 685 AD.", "duration": "2 hours", "bestTime": "Morning / 4 PM", "lat": 12.8420, "lng": 79.6890},
            {"name": "Varadharaja Perumal Temple", "highlight": "Celebrated Vishnu temple with 100-pillar hall carved with chains from single granite rocks.", "duration": "2 hours", "bestTime": "Evening (5 PM)", "lat": 12.8190, "lng": 79.7240},
            {"name": "Kanchipuram Silk Weavers Society Trail", "highlight": "Witness live handloom silk weaving with genuine gold zari borders and buy direct from master weavers.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 12.8350, "lng": 79.7050}
        ],
        "hotels": [
            {"name": "MM Legacy Kanchipuram", "type": "Luxury", "price": "₹4,200/night", "rating": "4.6★"},
            {"name": "Regency Kanchipuram by GRT Hotels", "type": "Mid-range", "price": "₹3,400/night", "rating": "4.4★"},
            {"name": "Hotel Baboo Soorya", "type": "Budget-friendly", "price": "₹1,500/night", "rating": "4.1★"}
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
            {"name": "Sri Ranganathaswamy Temple (Srirangam)", "highlight": "World's largest functioning Hindu temple complex spanning 156 acres with 21 magnificent gopurams.", "duration": "4 hours", "bestTime": "Early morning (6-11 AM)", "lat": 10.8623, "lng": 78.6902},
            {"name": "Ucchi Pillayar Rockfort Temple", "highlight": "Ancient fort built on an 83-meter high monolithic rock; climb 437 steps for 360-degree city views.", "duration": "2.5 hours", "bestTime": "Sunset (5 PM)", "lat": 10.8286, "lng": 78.6974},
            {"name": "Jambukeswarar Temple (Thiruvanaikaval)", "highlight": "Pancha Bhoota Stalam representing Water Element with an underground natural spring in the sanctum.", "duration": "2 hours", "bestTime": "Morning / 6 PM", "lat": 10.8530, "lng": 78.7050},
            {"name": "Kallanai Dam (Grand Anicut)", "highlight": "World's 4th oldest water-diversion dam, built in 2nd century AD by King Karikala Cholan.", "duration": "2.5 hours", "bestTime": "Late afternoon", "lat": 10.8350, "lng": 78.8180},
            {"name": "Mukkombu Dam & Butterfly Park", "highlight": "Scenic picnic barrage on River Cauvery with tropical butterfly conservatory.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 10.8750, "lng": 78.6050}
        ],
        "hotels": [
            {"name": "SRM Hotel Trichy", "type": "Luxury", "price": "₹4,800/night", "rating": "4.6★"},
            {"name": "Courtyard by Marriott Tiruchirappalli", "type": "Luxury", "price": "₹6,500/night", "rating": "4.7★"},
            {"name": "Grand Gardenia Trichy", "type": "Mid-range", "price": "₹2,600/night", "rating": "4.3★"},
            {"name": "Hotel Ramyas", "type": "Budget-friendly", "price": "₹1,800/night", "rating": "4.2★"}
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
            {"name": "Yercaud Emerald Lake & Boating", "highlight": "Scenic lake surrounded by gardens and deer park with pedal and motor boating.", "duration": "2 hours", "bestTime": "Morning / Evening", "lat": 11.7750, "lng": 78.2090},
            {"name": "Lady's Seat, Gent's Seat & Pagoda Point", "highlight": "Panoramic cliff viewpoints offering telescope views of Salem city and Mettur Dam.", "duration": "2.5 hours", "bestTime": "Sunset (5:30 PM)", "lat": 11.7680, "lng": 78.2030},
            {"name": "Killiyur Waterfalls", "highlight": "300-ft natural waterfall tumbling into a serene forest gorge (accessible via forest trek).", "duration": "3 hours", "bestTime": "Morning", "lat": 11.7920, "lng": 78.2010},
            {"name": "Shevaroy Temple & Bear's Cave", "highlight": "Highest peak in Yercaud (5,326 ft) with ancient cave shrine dedicated to Lord Shevaroyan.", "duration": "2 hours", "bestTime": "Morning", "lat": 11.8310, "lng": 78.2320},
            {"name": "Botanical Garden & Orchidarium", "highlight": "Houses over 250 species of rare orchids and the National Pitcher Plant reserve.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 11.7820, "lng": 78.2140}
        ],
        "hotels": [
            {"name": "Great Trails Yercaud by GRT Hotels", "type": "Luxury", "price": "₹6,800/night", "rating": "4.7★"},
            {"name": "Sterling Yercaud", "type": "Luxury", "price": "₹5,400/night", "rating": "4.5★"},
            {"name": "Grand Palace Hotel & Spa", "type": "Mid-range", "price": "₹3,500/night", "rating": "4.3★"},
            {"name": "Hotel Shevaroys", "type": "Budget-friendly", "price": "₹1,600/night", "rating": "4.1★"}
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
            {"name": "Arunachaleswarar Temple (Fire Element)", "highlight": "Massive 25-acre temple representing the Fire Element with four soaring gateway towers.", "duration": "3.5 hours", "bestTime": "Early morning (6 AM) or 6 PM", "lat": 12.2317, "lng": 79.0674},
            {"name": "Giri Valam 14-km Circumambulation", "highlight": "Sacred walking trail around Mount Arunachala with 8 directional Shiva Lingam shrines.", "duration": "4-5 hours", "bestTime": "Full Moon night / Early morning", "lat": 12.2280, "lng": 79.0550},
            {"name": "Sri Ramana Maharshi Ashram", "highlight": "Tranquil meditation hall, samadhi shrine, and library of the celebrated Advaita sage.", "duration": "2 hours", "bestTime": "Morning / 4 PM", "lat": 12.2200, "lng": 79.0556},
            {"name": "Virupaksha Cave & Skandasramam", "highlight": "Ancient caves on the hill slopes where Ramana Maharshi meditated for 16 years.", "duration": "2.5 hours", "bestTime": "Morning trek", "lat": 12.2270, "lng": 79.0600},
            {"name": "Sathanur Dam & Crocodile Park", "highlight": "Picturesque dam across Thenpennai River with landscaped gardens and children's park.", "duration": "3 hours", "bestTime": "Afternoon", "lat": 12.1850, "lng": 78.8500}
        ],
        "hotels": [
            {"name": "Sparsa Resort Thiruvannamalai", "type": "Luxury", "price": "₹5,200/night", "rating": "4.8★"},
            {"name": "Arunai Anantha Resort", "type": "Mid-range", "price": "₹3,100/night", "rating": "4.4★"},
            {"name": "Hotel Himalayaa", "type": "Mid-range", "price": "₹2,200/night", "rating": "4.3★"},
            {"name": "Aakash Inn Tiruvannamalai", "type": "Budget-friendly", "price": "₹1,200/night", "rating": "4.1★"}
        ]
    },
    "courtallam": {
        "fullName": "Courtallam (Kutralam), Tenkasi, Tamil Nadu",
        "lat": 8.9298,
        "lng": 77.2690,
        "region": "Tamil Nadu",
        "climate": "rainy",
        "experience": "nature",
        "budget": "low",
        "summary": "The Spa of South India, famous for mineral-rich medicinal waterfalls flowing through the Western Ghats during the monsoon season.",
        "attractions": [
            {"name": "Main Falls (Peraruvi)", "highlight": "Iconic 60-meter cascade where the waters of Chittar River fall over medicinal herbal rocks.", "duration": "2.5 hours", "bestTime": "Morning bath (7-10 AM)", "lat": 8.9310, "lng": 77.2720},
            {"name": "Five Falls (Aintharuvi)", "highlight": "Spectacular waterfall where the stream splits into five distinct cascades like the five heads of a serpent.", "duration": "2.5 hours", "bestTime": "Morning / 3 PM", "lat": 8.9410, "lng": 77.2580},
            {"name": "Old Courtallam Falls (Pazhaya Kutralam)", "highlight": "Picturesque waterfall set in a tranquil valley with spacious natural bathing pools.", "duration": "2 hours", "bestTime": "Morning", "lat": 8.9550, "lng": 77.2920},
            {"name": "Kasi Viswanathar Temple (Tenkasi)", "highlight": "13th-century Pandyan temple in Tenkasi with massive 180-ft tower (Gopuram) with musical pillars.", "duration": "2 hours", "bestTime": "Evening (5:30 PM)", "lat": 8.9580, "lng": 77.3150},
            {"name": "Gundar Dam & Eco Park", "highlight": "Scenic reservoir amidst Western Ghats jungle with mountain views and clean air.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 8.9750, "lng": 77.2450}
        ],
        "hotels": [
            {"name": "Saaral Resorts Courtallam", "type": "Luxury", "price": "₹4,500/night", "rating": "4.6★"},
            {"name": "Green Garden Resort", "type": "Mid-range", "price": "₹2,800/night", "rating": "4.3★"},
            {"name": "Hotel Sree Annamalaiyar", "type": "Budget-friendly", "price": "₹1,200/night", "rating": "4.1★"}
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
            {"name": "Thillai Nataraja Temple (Akasha / Space Element)", "highlight": "Famous for the Chidambara Rahasyam (secret of space), golden roof sanctum, and gemstone lingam.", "duration": "3 hours", "bestTime": "Morning (6-11 AM) or 6 PM", "lat": 11.3995, "lng": 79.6930},
            {"name": "Pichavaram Mangrove Forest Boating", "highlight": "Row-boating through 1,100 hectares of natural mangrove water canals and bird watching.", "duration": "3 hours", "bestTime": "Morning (8-11 AM)", "lat": 11.4280, "lng": 79.7820},
            {"name": "Vaitheeswaran Koil", "highlight": "Famous temple dedicated to Lord Shiva as the Divine Healer and world hub for Nadi Astrology.", "duration": "2 hours", "bestTime": "Morning / 5 PM", "lat": 11.2000, "lng": 79.7120},
            {"name": "Tarangambadi (Tranquebar Danish Fort)", "highlight": "17th-century Danish fort (Dansborg) and colonial seaside settlement on the Coromandel Coast.", "duration": "2.5 hours", "bestTime": "Late afternoon", "lat": 11.0320, "lng": 79.8540}
        ],
        "hotels": [
            {"name": "The Gateway Hotel Chidambaram", "type": "Mid-range", "price": "₹3,400/night", "rating": "4.4★"},
            {"name": "Pichavaram Adventure Resort", "type": "Mid-range", "price": "₹2,600/night", "rating": "4.2★"},
            {"name": "Hotel Saradharam Chidambaram", "type": "Budget-friendly", "price": "₹1,400/night", "rating": "4.1★"}
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
            {"name": "Sholayar Dam & Reservoir", "highlight": "Second deepest dam in Asia offering majestic views of the emerald reservoir and rainforests.", "duration": "2.5 hours", "bestTime": "Morning / Afternoon", "lat": 10.2980, "lng": 76.7550},
            {"name": "40 Hairpin Bends & Loam's Viewpoint", "highlight": "Thrilling mountain road journey from Pollachi with stunning views of Aliyar Dam below.", "duration": "2 hours", "bestTime": "Morning / Sunset", "lat": 10.4200, "lng": 76.9700},
            {"name": "Aliyar Dam, Park & Monkey Falls", "highlight": "Picturesque dam at the foothills with landscaped gardens and natural spring waterfall.", "duration": "3 hours", "bestTime": "Morning", "lat": 10.4850, "lng": 76.9740},
            {"name": "Anamalai Tiger Reserve (Topslip Safari)", "highlight": "Jungle safari, elephant camp, and birding in dense evergreen Western Ghats canopy.", "duration": "4 hours", "bestTime": "Early morning safari (6:30 AM)", "lat": 10.4700, "lng": 76.8500},
            {"name": "Chinnakallar & Nirar Dam Waterfalls", "highlight": "Third highest rainfall region in India (Cheerapunji of South India) with suspension bridge.", "duration": "3 hours", "bestTime": "Morning", "lat": 10.3020, "lng": 77.0150}
        ],
        "hotels": [
            {"name": "Briar Tea Bungalows Valparai", "type": "Luxury", "price": "₹8,500/night", "rating": "4.8★"},
            {"name": "Stanmore Garden Bungalow", "type": "Luxury", "price": "₹7,200/night", "rating": "4.7★"},
            {"name": "Hotel Green Hill Valparai", "type": "Budget-friendly", "price": "₹1,600/night", "rating": "4.2★"}
        ]
    },
    "coonoor": {
        "fullName": "Coonoor, Nilgiris, Tamil Nadu",
        "lat": 11.3530,
        "lng": 76.7959,
        "region": "Tamil Nadu",
        "climate": "cold",
        "experience": "nature",
        "budget": "medium",
        "summary": "Picturesque Nilgiri tea hill station famous for Sim's Park, Dolphin's Nose viewpoint, and organic tea tastings.",
        "attractions": [
            {"name": "Sim's Park Botanical Gardens", "highlight": "12-hectare Victorian botanical park housing rare magnolia, camellia, and century-old pines.", "duration": "2.5 hours", "bestTime": "Morning (9 AM)", "lat": 11.3550, "lng": 76.8010},
            {"name": "Dolphin's Nose & Catherine Falls View", "highlight": "Breathtaking cliff viewpoint overlooking the Catherine double-cascading waterfall.", "duration": "2.5 hours", "bestTime": "Morning (clear skies)", "lat": 11.3320, "lng": 76.8790},
            {"name": "Lamb's Rock & Droog Fort", "highlight": "Precipitous cliff over Coimbatore plains and historic 16th-century Tipu Sultan outpost.", "duration": "3 hours", "bestTime": "Morning trek", "lat": 11.3480, "lng": 76.8450},
            {"name": "Highfield Tea Factory & Museum Trail", "highlight": "50-year-old operational tea factory demonstrating orthodox tea making and essential oils.", "duration": "2 hours", "bestTime": "Afternoon", "lat": 11.3620, "lng": 76.8120}
        ],
        "hotels": [
            {"name": "Gateway Coonoor - IHCL SeleQtions", "type": "Luxury", "price": "₹11,000/night", "rating": "4.8★"},
            {"name": "Sunvalley Homestay Coonoor", "type": "Mid-range", "price": "₹4,200/night", "rating": "4.6★"},
            {"name": "Orchid Square Boutique Hotel", "type": "Mid-range", "price": "₹3,200/night", "rating": "4.4★"}
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
            {"name": "Hogenakkal Main Waterfalls", "highlight": "Spectacular cascade where River Cauvery drops through carbonatite rocks creating smoking mist.", "duration": "3 hours", "bestTime": "Morning (8 AM)", "lat": 12.1180, "lng": 77.7760},
            {"name": "Coracle (Parisal) Round Boat Ride", "highlight": "Traditional circular bamboo basket boat ride beneath roaring waterfalls into the river canyon.", "duration": "2 hours", "bestTime": "Morning / 3 PM", "lat": 12.1150, "lng": 77.7720},
            {"name": "Hanging Suspension Bridge", "highlight": "Walkway suspended high above the gorge offering panoramic photography of all cascades.", "duration": "1 hour", "bestTime": "Morning", "lat": 12.1190, "lng": 77.7790},
            {"name": "Melagiri Hills & River Forest Bath", "highlight": "Natural mineral-rich water bath combined with traditional massage and freshly fried river fish.", "duration": "2.5 hours", "bestTime": "Afternoon", "lat": 12.1250, "lng": 77.7650}
        ],
        "hotels": [
            {"name": "Tamil Nadu Tourism Hotel (TTDC Hogenakkal)", "type": "Mid-range", "price": "₹2,200/night", "rating": "4.3★"},
            {"name": "CM Hotel Hogenakkal", "type": "Budget-friendly", "price": "₹1,400/night", "rating": "4.0★"}
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
            {"name": "Nellaiappar & Kanthimathi Temple", "highlight": "7th-century architectural gem featuring musical stone pillars and magnificent Mani Mandapam.", "duration": "3 hours", "bestTime": "Morning (6-11 AM) or 6 PM", "lat": 8.7280, "lng": 77.6890},
            {"name": "Manimuthar Waterfalls & Dam", "highlight": "Cascading mountain waterfall with natural swimming pond and teak forest views.", "duration": "3 hours", "bestTime": "Morning", "lat": 8.5900, "lng": 77.4100},
            {"name": "Papanasam Agasthiyar Falls & River", "highlight": "Sacred falls where sage Agastya received Shiva's darshan; pure Thamirabarani river bath.", "duration": "3 hours", "bestTime": "Morning", "lat": 8.7050, "lng": 77.3680},
            {"name": "Manjolai Tea Estates & Cloud Forest", "highlight": "Hill station in the Western Ghats (Kalakkad Mundanthurai Tiger Reserve) with tea plantations.", "duration": "Full day", "bestTime": "Morning jeep ride (permit required)", "lat": 8.5500, "lng": 77.3800},
            {"name": "Famous Iruttu Kadai Halwa Trail", "highlight": "Taste authentic hot wheat halwa made with pure ghee and Thamirabarani water.", "duration": "1.5 hours", "bestTime": "5:30 PM", "lat": 8.7290, "lng": 77.6910}
        ],
        "hotels": [
            {"name": "Hotel Aryas Tirunelveli", "type": "Mid-range", "price": "₹2,600/night", "rating": "4.4★"},
            {"name": "Regency Tirunelveli by GRT Hotels", "type": "Luxury", "price": "₹4,500/night", "rating": "4.7★"},
            {"name": "Hotel Sree Bharani", "type": "Budget-friendly", "price": "₹1,500/night", "rating": "4.2★"}
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
            {"name": "Chettinad Palace & Thousand Windows House (Kanadukathan)", "highlight": "Opulent palatial mansion with Italian marble, teak pillars, Belgian mirrors, and stained glass.", "duration": "3 hours", "bestTime": "Morning (9 AM)", "lat": 10.1520, "lng": 78.7910},
            {"name": "Athangudi Handmade Tile Workshops", "highlight": "Witness master artisans handcrafting vibrant floral glass-finish mosaic tiles.", "duration": "2 hours", "bestTime": "Morning", "lat": 10.1700, "lng": 78.8400},
            {"name": "Pillayarpatti Karpaga Vinayagar Temple", "highlight": "1600-year-old rock-cut cave temple dedicated to Lord Ganesha carved on mountain face.", "duration": "2 hours", "bestTime": "Morning / 5 PM", "lat": 10.1210, "lng": 78.6810},
            {"name": "Thirumayam Fort & Rock Cut Temple", "highlight": "17th-century ring fort with rock-cut Shiva and Vishnu cave shrines and panoramic views.", "duration": "2.5 hours", "bestTime": "Late afternoon", "lat": 10.2450, "lng": 78.7520},
            {"name": "Chettinad Banana Leaf Culinary Trail", "highlight": "Authentic Chettinad spicy chicken/mutton pepper fry, vazhaipoo vadai, and seeyam.", "duration": "2 hours", "bestTime": "Lunch (12:30 PM)", "lat": 10.0680, "lng": 78.7800}
        ],
        "hotels": [
            {"name": "Chidambara Vilas - Luxury Heritage Resort", "type": "Luxury", "price": "₹8,500/night", "rating": "4.9★"},
            {"name": "The Bangala, Karaikudi", "type": "Luxury", "price": "₹9,200/night", "rating": "4.8★"},
            {"name": "Chettinadu Mansion Kanadukathan", "type": "Mid-range", "price": "₹4,500/night", "rating": "4.6★"},
            {"name": "Hotel Subhalakshmi Palace", "type": "Budget-friendly", "price": "₹1,800/night", "rating": "4.2★"}
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
            {"name": "Vellore Fort & Jalakandeswarar Temple", "highlight": "Massive 16th-century granite fort surrounded by a deep moat with exquisite Vijayanagara temple.", "duration": "3 hours", "bestTime": "Morning (8 AM)", "lat": 12.9230, "lng": 79.1300},
            {"name": "Sripuram Golden Temple (Maha Lakshmi)", "highlight": "Dazzling spiritual park temple covered in 1,500 kg of pure gold leaf foil inside a star-shaped path.", "duration": "3.5 hours", "bestTime": "Afternoon till illuminated evening", "lat": 12.8710, "lng": 79.0880},
            {"name": "Amirthi Zoological Forest Park", "highlight": "Eco-park with natural waterfalls, wildlife zoo, and trekking paths in Javadi Hills.", "duration": "3 hours", "bestTime": "Morning", "lat": 12.7500, "lng": 79.0500},
            {"name": "Ratnagiri Murugan Temple & Science Park", "highlight": "Hilltop temple with panoramic vistas of the surrounding Eastern Ghats plains.", "duration": "2 hours", "bestTime": "Evening", "lat": 12.9700, "lng": 79.2500}
        ],
        "hotels": [
            {"name": "Fortune Park Vellore - Member ITC Hotel Group", "type": "Luxury", "price": "₹5,200/night", "rating": "4.7★"},
            {"name": "Rangalaya Royal Vellore", "type": "Mid-range", "price": "₹2,800/night", "rating": "4.3★"},
            {"name": "Darling Residency Vellore", "type": "Budget-friendly", "price": "₹1,800/night", "rating": "4.2★"}
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
            {"name": "70 Hairpin Bends Mountain Drive", "highlight": "One of India's most thrilling winding hill climbs with breathtaking panoramic viewpoints.", "duration": "2 hours", "bestTime": "Morning (8 AM)", "lat": 11.2900, "lng": 78.3100},
            {"name": "Agaya Gangai Waterfalls (300 ft)", "highlight": "Spectacular 300-ft cascade reached by descending 1,000 stone steps into the river canyon.", "duration": "3.5 hours", "bestTime": "Morning", "lat": 11.2750, "lng": 78.3450},
            {"name": "Arapaleeswarar Temple", "highlight": "Ancient Shiva temple on the mountain mentioned in classical Sangam literature.", "duration": "1.5 hours", "bestTime": "Morning / 4 PM", "lat": 11.2760, "lng": 78.3440},
            {"name": "Seekuparai & Selur Viewpoint", "highlight": "Watchtowers offering bird's eye views over the emerald valleys and pineapple estates.", "duration": "2 hours", "bestTime": "Sunset (5 PM)", "lat": 11.2550, "lng": 78.3600},
            {"name": "Namakkal Anjaneyar Temple & Rock Fort", "highlight": "Single-stone 18-ft open-sky Hanuman statue and historic hilltop rock fortress.", "duration": "2.5 hours", "bestTime": "Morning", "lat": 11.2189, "lng": 78.1674}
        ],
        "hotels": [
            {"name": "Silverline Retreat Hotel Kolli Hills", "type": "Mid-range", "price": "₹2,800/night", "rating": "4.3★"},
            {"name": "Nallathambi Resort Kolli Hills", "type": "Budget-friendly", "price": "₹1,600/night", "rating": "4.1★"}
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
            {"name": "Adi Kumbeswarar Temple & Mahamaham Tank", "highlight": "Largest Shiva temple in Kumbakonam with 6.2-acre sacred tank (Kumbh Mela of South India).", "duration": "2.5 hours", "bestTime": "Morning (6-11 AM)", "lat": 10.9580, "lng": 79.3780},
            {"name": "Airavatesvara Temple (Darasuram - UNESCO)", "highlight": "Chola architectural masterpiece featuring chariot-shaped stone mandapam and singing musical steps.", "duration": "2.5 hours", "bestTime": "Morning / 4 PM", "lat": 10.9480, "lng": 79.3560},
            {"name": "Sarangapani Temple & Ramaswamy Temple", "highlight": "Grand 12-tier Vishnu temple with chariot-shaped sanctum and Ramayana fresco paintings.", "duration": "2 hours", "bestTime": "Morning / 6 PM", "lat": 10.9610, "lng": 79.3750},
            {"name": "Swamimalai Murugan Temple", "highlight": "One of the Six Abodes (Arupadai Veedu) of Lord Murugan where he taught the Pranava Mantra to Shiva.", "duration": "2 hours", "bestTime": "Morning", "lat": 10.9540, "lng": 79.3280},
            {"name": "Kumbakonam Degree Filter Coffee Trail", "highlight": "Sample authentic rich South Indian chicory filter coffee served in brass davarah-tumblers.", "duration": "1 hour", "bestTime": "Morning / Evening", "lat": 10.9600, "lng": 79.3800}
        ],
        "hotels": [
            {"name": "Mantra Koodam - CGH Earth, Kumbakonam", "type": "Luxury", "price": "₹9,500/night", "rating": "4.9★"},
            {"name": "Paradise Resort Kumbakonam", "type": "Mid-range", "price": "₹3,800/night", "rating": "4.5★"},
            {"name": "Hotel Raya's Kumbakonam", "type": "Budget-friendly", "price": "₹1,400/night", "rating": "4.1★"}
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
            {"name": "Punganoor Lake & Nature Park", "highlight": "Artificial lake with boating, musical fountain, flower gardens, and walking trails.", "duration": "2.5 hours", "bestTime": "Morning / Evening", "lat": 12.5810, "lng": 78.6420},
            {"name": "Swamimalai Hill Trekking Peak", "highlight": "Highest peak in Yelagiri (4,338 ft) offering trekking trails and views of the valley.", "duration": "3.5 hours", "bestTime": "Early morning trek", "lat": 12.5650, "lng": 78.6320},
            {"name": "Jalagamparai Waterfalls", "highlight": "Natural mountain waterfall created by the Attaru River cascading over rocky terrain.", "duration": "3 hours", "bestTime": "Morning", "lat": 12.6020, "lng": 78.6700},
            {"name": "Yelagiri Adventure Camp & Telescope House", "highlight": "Zip lining, rock climbing, paragliding, and observatory views.", "duration": "2.5 hours", "bestTime": "Afternoon", "lat": 12.5850, "lng": 78.6480}
        ],
        "hotels": [
            {"name": "Sterling Yelagiri", "type": "Luxury", "price": "₹4,800/night", "rating": "4.6★"},
            {"name": "Marigold Ridge Resort", "type": "Mid-range", "price": "₹3,200/night", "rating": "4.3★"},
            {"name": "Hotel Landmark Yelagiri", "type": "Budget-friendly", "price": "₹1,500/night", "rating": "4.1★"}
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
            {"name": "Meenakshi Amman Temple (Madurai)", "highlight": "World-famous architectural wonder with 14 gopurams and Hall of 1000 Pillars.", "duration": "3.5 hours", "bestTime": "Morning / Evening", "lat": 9.9195, "lng": 78.1193},
            {"name": "Brihadeeswarar Big Temple (Thanjavur - UNESCO)", "highlight": "1000-year-old Chola architectural wonder with 216-ft vimana.", "duration": "3 hours", "bestTime": "Morning / Evening", "lat": 10.7828, "lng": 79.1318},
            {"name": "Nilgiri Mountain Railway & Doddabetta (Ooty)", "highlight": "UNESCO World Heritage steam train journey climbing through Nilgiri tea hills.", "duration": "4 hours", "bestTime": "Morning", "lat": 11.4055, "lng": 76.6975},
            {"name": "Dhanushkodi & Pamban Bridge (Rameswaram)", "highlight": "Tip of India where two oceans meet and historic sea bridge.", "duration": "4 hours", "bestTime": "Morning", "lat": 9.1764, "lng": 79.4183},
            {"name": "Vivekananda Rock Memorial (Kanyakumari)", "highlight": "Sacred rock monument where three seas meet at India's southern tip.", "duration": "3 hours", "bestTime": "Sunrise / Morning", "lat": 8.0781, "lng": 77.5553},
            {"name": "Shore Temple & Pancha Rathas (Mahabalipuram)", "highlight": "UNESCO 7th-century coastal rock-cut temples on the Bay of Bengal.", "duration": "3 hours", "bestTime": "Morning / Afternoon", "lat": 12.6163, "lng": 80.1983}
        ],
        "hotels": [
            {"name": "Taj Coromandel, Chennai", "type": "Luxury", "price": "₹12,500/night", "rating": "4.9★"},
            {"name": "Heritage Madurai", "type": "Luxury", "price": "₹7,800/night", "rating": "4.7★"},
            {"name": "The Tamara Kodai", "type": "Luxury", "price": "₹16,000/night", "rating": "4.9★"}
        ]
    }
}

print("Tamil Nadu Places Database compiled with", len(TAMIL_NADU_PLACES), "major destinations!")
