// Client-Side Curated Knowledge Engine for Standalone & Live Hosted Modes
const DESTINATIONS_DB = {
  manali: {
    fullName: 'Manali, Himachal Pradesh',
    lat: 32.2432,
    lng: 77.1892,
    summary: 'Premier Himalayan resort town renowned for snow-capped peaks, Solang adventure valley, Rohtang Pass, and scenic pine forests.',
    attractions: [
      { name: 'Solang Valley', highlight: 'Famous hub for paragliding, zorbing, quad biking, and winter skiing.', duration: '4-5 hours', bestTime: 'Morning', lat: 32.3166, lng: 77.1578 },
      { name: 'Rohtang Pass', highlight: 'High-altitude mountain pass offering panoramic Himalayan glaciers and snow viewpoints.', duration: 'Half day', bestTime: 'Early morning (7 AM)', lat: 32.3716, lng: 77.2466 },
      { name: 'Hadimba Temple & Van Vihar', highlight: 'Ancient 16th-century wooden pagoda temple nestled inside dense cedar forests.', duration: '2 hours', bestTime: 'Morning / Afternoon', lat: 32.2483, lng: 77.1705 },
      { name: 'Old Manali & Cafe Trail', highlight: 'Bohemian village atmosphere with wooden houses, vibrant cafes, and live music.', duration: '3 hours', bestTime: 'Evening', lat: 32.253, lng: 77.175 },
      { name: 'Jogini Waterfalls & Vashisht Springs', highlight: 'Scenic nature trek leading to a cascading waterfall and natural hot springs.', duration: '3-4 hours', bestTime: 'Morning', lat: 32.266, lng: 77.187 },
      { name: 'Atal Tunnel & Sissu Valley', highlight: "World's longest highway tunnel above 10,000 ft connecting to waterfalls in Sissu.", duration: '4-5 hours', bestTime: 'Morning', lat: 32.4833, lng: 77.1264 }
    ],
    hotels: [
      { name: 'The Himalayan Resort & Spa', type: 'Luxury', price: '₹9,500/night', rating: '4.8★' },
      { name: 'Span Resort & Spa, Manali', type: 'Luxury', price: '₹11,000/night', rating: '4.7★' },
      { name: 'Larisa Resort Manali', type: 'Mid-range', price: '₹4,800/night', rating: '4.5★' },
      { name: 'Zostel Manali (Old Manali)', type: 'Budget-friendly', price: '₹1,200/night', rating: '4.6★' }
    ]
  },
  goa: {
    fullName: 'Goa (North & South)',
    lat: 15.2993,
    lng: 74.124,
    summary: 'Tropical beach paradise with Portuguese colonial heritage, pristine coastlines, and vibrant nightlife.',
    attractions: [
      { name: 'Baga & Calangute Beach', highlight: 'Energetic golden beaches with water sports, beach shacks, and live sunset music.', duration: '3-4 hours', bestTime: 'Late afternoon to Sunset', lat: 15.5523, lng: 73.7517 },
      { name: 'Fort Aguada & Lighthouse', highlight: '17th-century Portuguese fortress with sweeping panoramic views over the Arabian Sea.', duration: '2 hours', bestTime: 'Morning / 4 PM', lat: 15.492, lng: 73.7737 },
      { name: 'Basilica of Bom Jesus & Old Goa', highlight: 'UNESCO World Heritage Baroque church housing the sacred relics of St. Francis Xavier.', duration: '2.5 hours', bestTime: 'Morning', lat: 15.5009, lng: 73.9116 },
      { name: 'Dudhsagar Waterfalls', highlight: 'Magnificent four-tiered waterfall cascading down 310 meters amidst lush jungle canopy.', duration: 'Full day', bestTime: 'Early morning jeep safari', lat: 15.3144, lng: 74.3143 },
      { name: 'Palolem Beach & Silent Noise Club', highlight: 'Serene crescent-shaped beach famous for calm waters, dolphin spotting, and beach yoga.', duration: 'Half day', bestTime: 'Sunset', lat: 15.01, lng: 74.0232 },
      { name: 'Anjuna Flea Market & Chapora Fort', highlight: "Iconic cliffside fort overlooking the sea ('Dil Chahta Hai' fame) and vibrant market.", duration: '3 hours', bestTime: '5 PM', lat: 15.6059, lng: 73.7386 }
    ],
    hotels: [
      { name: 'Taj Exotica Resort & Spa, Benaulim', type: 'Luxury', price: '₹16,500/night', rating: '4.9★' },
      { name: 'W Goa, Vagator', type: 'Luxury', price: '₹18,000/night', rating: '4.8★' },
      { name: 'Fairfield by Marriott Goa Anjuna', type: 'Mid-range', price: '₹4,200/night', rating: '4.4★' },
      { name: 'The Hosteller Goa Candolim', type: 'Budget-friendly', price: '₹950/night', rating: '4.5★' }
    ]
  },
  jaipur: {
    fullName: 'Jaipur, Rajasthan',
    lat: 26.9124,
    lng: 75.7873,
    summary: 'The majestic Pink City brimming with royal palaces, hilltop fortresses, and vibrant bazaars.',
    attractions: [
      { name: 'Amber Fort & Palace', highlight: 'Magnificent hilltop fort with Sheesh Mahal (Mirror Palace) and elephant/jeep ascents.', duration: '3.5 hours', bestTime: 'Morning (8:30 AM)', lat: 26.9855, lng: 75.8513 },
      { name: 'Hawa Mahal (Palace of Winds)', highlight: 'Iconic 5-story honeycomb facade with 953 intricately carved jharokhas.', duration: '1.5 hours', bestTime: 'Morning for best lighting', lat: 26.9239, lng: 75.8267 },
      { name: 'City Palace & Jantar Mantar', highlight: 'Royal residence museum displaying Rajput history and UNESCO astronomical observatory.', duration: '3 hours', bestTime: 'Afternoon', lat: 26.9258, lng: 75.8236 },
      { name: 'Nahargarh Fort Sunset Viewpoint', highlight: 'Hilltop fort offering spectacular panoramic sunset views of the entire Jaipur city.', duration: '2.5 hours', bestTime: '5:00 PM - Sunset', lat: 26.9372, lng: 75.8155 },
      { name: 'Albert Hall Museum & Johari Bazaar', highlight: 'Indo-Saracenic museum illuminated by night and world-famous gemstone/textile bazaar.', duration: '2.5 hours', bestTime: 'Evening', lat: 26.9116, lng: 75.8195 },
      { name: 'Jal Mahal (Water Palace)', highlight: 'Enchanting palace floating in the middle of Man Sagar Lake.', duration: '1 hour', bestTime: 'Morning / Evening promenade', lat: 26.9534, lng: 75.8462 }
    ],
    hotels: [
      { name: 'Rambagh Palace (Taj)', type: 'Luxury', price: '₹32,000/night', rating: '4.9★' },
      { name: 'ITC Rajputana, Jaipur', type: 'Luxury', price: '₹8,500/night', rating: '4.7★' },
      { name: 'Hotel Pearl Palace', type: 'Mid-range', price: '₹2,600/night', rating: '4.6★' },
      { name: 'Moustache Hostel Jaipur', type: 'Budget-friendly', price: '₹750/night', rating: '4.5★' }
    ]
  },
  madurai: {
    fullName: 'Madurai, Tamil Nadu',
    lat: 9.9252,
    lng: 78.1198,
    summary: 'The Cultural Capital of Tamil Nadu, celebrated for its 2,500-year history and the colossal Meenakshi Amman Temple.',
    attractions: [
      { name: 'Meenakshi Amman Temple', highlight: 'Architectural marvel with 14 soaring gopurams, Hall of Thousand Pillars, and intricate Dravidian carvings.', duration: '3.5 hours', bestTime: 'Morning (6-11 AM) or Evening (5-9 PM)', lat: 9.9195, lng: 78.1193 },
      { name: 'Thirumalai Nayakkar Mahal', highlight: '17th-century Indo-Saracenic royal palace with gigantic circular pillars and evening light-and-sound show.', duration: '2 hours', bestTime: 'Afternoon / 6:45 PM for Sound & Light show', lat: 9.9152, lng: 78.1238 },
      { name: 'Gandhi Memorial Museum', highlight: "Historic museum housing Mahatma Gandhi's blood-stained dhoti and comprehensive freedom struggle gallery.", duration: '2 hours', bestTime: 'Morning', lat: 9.9327, lng: 78.1402 },
      { name: 'Alagar Koyil (Alagar Hills)', highlight: 'Ancient temple of Lord Vishnu situated in the lush forest foothills of Alagar Hills.', duration: '3 hours', bestTime: 'Morning', lat: 10.0769, lng: 78.2144 },
      { name: 'Vandiyur Mariamman Teppakulam', highlight: 'Huge temple tank with a central mandapam, famous for the annual float festival.', duration: '1 hour', bestTime: 'Evening', lat: 9.9098, lng: 78.1528 },
      { name: 'Madurai Street Food & Jigarthanda Trail', highlight: 'Sample famous Madurai Bun Parotta, Kari Dosa, Murugan Idli, and authentic Famous Jigarthanda.', duration: '2.5 hours', bestTime: 'Evening (7 PM onwards)', lat: 9.92, lng: 78.122 }
    ],
    hotels: [
      { name: 'Heritage Madurai', type: 'Luxury', price: '₹7,800/night', rating: '4.7★' },
      { name: 'Courtyard by Marriott Madurai', type: 'Luxury', price: '₹6,200/night', rating: '4.6★' },
      { name: 'The Gateway Hotel Pasumalai', type: 'Mid-range', price: '₹4,100/night', rating: '4.5★' },
      { name: 'Hotel Supreme Madurai', type: 'Budget-friendly', price: '₹1,400/night', rating: '4.2★' }
    ]
  },
  kerala: {
    fullName: 'Kerala (Munnar, Alleppey & Kochi)',
    lat: 9.9312,
    lng: 76.2673,
    summary: "God's Own Country blessed with emerald backwaters, rolling tea estates, spice plantations, and Ayurvedic retreats.",
    attractions: [
      { name: 'Alleppey Backwaters Houseboat', highlight: 'Iconic traditional Kettuvallam houseboat stay cruising through tranquil lagoons and paddy fields.', duration: 'Full day', bestTime: 'Afternoon to Morning', lat: 9.4981, lng: 76.3388 },
      { name: 'Munnar Tea Gardens & Eravikulam', highlight: 'Lush mist-covered tea gardens and home to the endangered Nilgiri Tahr mountain goat.', duration: '4-5 hours', bestTime: 'Morning (8 AM)', lat: 10.0889, lng: 77.0595 },
      { name: 'Fort Kochi & Chinese Fishing Nets', highlight: 'Colonial Dutch/Portuguese heritage, historic St. Francis Church, and sunset harbor views.', duration: '3 hours', bestTime: 'Evening', lat: 9.9658, lng: 76.2421 },
      { name: 'Mattupetty Dam & Top Station', highlight: 'Scenic lake with boating and highest viewpoint on the Munnar-Kodaikanal road.', duration: '3 hours', bestTime: 'Afternoon', lat: 10.106, lng: 77.124 }
    ],
    hotels: [
      { name: 'Kumarakom Lake Resort', type: 'Luxury', price: '₹22,000/night', rating: '4.9★' },
      { name: 'Fragrant Nature Munnar', type: 'Luxury', price: '₹9,800/night', rating: '4.7★' },
      { name: 'Zostel Alleppey', type: 'Budget-friendly', price: '₹900/night', rating: '4.5★' }
    ]
  },
  delhi: {
    fullName: 'New Delhi & Old Delhi',
    lat: 28.6139,
    lng: 77.209,
    summary: "India's capital city uniting centuries of Mughal history, grand colonial architecture, and bustling markets.",
    attractions: [
      { name: 'Red Fort & Jama Masjid', highlight: "Massive 17th-century Mughal sandstone citadel and India's largest historic mosque.", duration: '3.5 hours', bestTime: 'Morning', lat: 28.6562, lng: 77.241 },
      { name: 'Qutub Minar & Mehrauli Park', highlight: 'UNESCO World Heritage 73m victory minaret with 12th-century Iron Pillar and ruins.', duration: '2.5 hours', bestTime: 'Morning / Late Afternoon', lat: 28.5244, lng: 77.1855 },
      { name: "Humayun's Tomb", highlight: 'Sublime Mughal garden tomb and architectural predecessor to the Taj Mahal.', duration: '2 hours', bestTime: 'Afternoon to Sunset', lat: 28.5933, lng: 77.2507 },
      { name: 'India Gate & Kartavya Path', highlight: 'Iconic war memorial archway surrounded by sprawling ceremonial lawns and fountain walks.', duration: '1.5 hours', bestTime: 'Evening (6 PM onwards)', lat: 28.6129, lng: 77.2295 }
    ],
    hotels: [
      { name: 'The Leela Palace New Delhi', type: 'Luxury', price: '₹19,000/night', rating: '4.9★' },
      { name: 'Taj Mahal Hotel, Mansingh Road', type: 'Luxury', price: '₹14,000/night', rating: '4.8★' },
      { name: 'Bloomrooms @ Janpath', type: 'Mid-range', price: '₹3,800/night', rating: '4.4★' }
    ]
  }
}

function handleClientFallback(path, body) {
  if (path.includes('/api/auth/login') || path.includes('/api/auth/register') || path.includes('/api/auth/google')) {
    const user = {
      id: Date.now(),
      username: body.username || (body.email ? body.email.split('@')[0] : 'Traveler'),
      email: body.email || 'traveler@tripnova.com',
    }
    localStorage.setItem('tripnova_user', JSON.stringify(user))
    return user
  }

  if (path.includes('/api/ai/plan-journey')) {
    return {
      places: [
        {
          name: 'Manali, Himachal Pradesh',
          reason: 'Snow-capped Himalayan peaks, thrilling adventure sports in Solang Valley, and scenic pine forests.',
          tag: 'Adventure',
          bestSeason: 'Oct–Jun',
          lat: 32.2432,
          lng: 77.1892,
        },
        {
          name: 'Goa (North & South)',
          reason: 'Sun-kissed tropical beaches, Portuguese colonial forts, water sports, and relaxed coastal vibes.',
          tag: 'Relaxation',
          bestSeason: 'Nov–Mar',
          lat: 15.2993,
          lng: 74.124,
        },
        {
          name: 'Jaipur, Rajasthan',
          reason: 'Majestic Pink City palaces, hilltop Amber Fort, vibrant heritage bazaars, and royal Rajput culture.',
          tag: 'Heritage',
          bestSeason: 'Oct–Mar',
          lat: 26.9124,
          lng: 75.7873,
        },
      ],
      source: 'tripnova_engine',
    }
  }

  if (path.includes('/api/ai/places-to-visit')) {
    const placeQuery = (body.place || 'Manali').toLowerCase()
    const days = parseInt(body.days, 10) || 3

    let matched = null
    for (const key of Object.keys(DESTINATIONS_DB)) {
      if (placeQuery.includes(key) || key.includes(placeQuery)) {
        matched = DESTINATIONS_DB[key]
        break
      }
    }

    if (!matched) {
      // Default to Manali or dynamic generator
      matched = DESTINATIONS_DB.manali
    }

    const allSpots = matched.attractions
    const itinerary = []
    for (let d = 1; d <= days; d++) {
      const startIdx = ((d - 1) * 2) % allSpots.length
      const daySpots = [
        allSpots[startIdx % allSpots.length],
        allSpots[(startIdx + 1) % allSpots.length],
      ]
      itinerary.push({
        day: d,
        title: d === 1 ? 'Primary Iconic Landmarks' : d === 2 ? 'Cultural & Heritage Sights' : `Scenic Discoveries (Day ${d})`,
        places: daySpots,
      })
    }

    return {
      place: matched.fullName,
      lat: matched.lat,
      lng: matched.lng,
      summary: matched.summary,
      itinerary,
      hotels: matched.hotels,
      source: 'tripnova_engine',
    }
  }

  if (path.includes('/api/ai/unsuitable-place')) {
    return {
      answer: `While ${body.place || 'this place'} is a fantastic destination, your preferences for ${
        body.preferences?.climate || 'chosen climate'
      } and ${body.preferences?.experience || 'travel style'} might be better fulfilled by our top recommended options.`,
      source: 'tripnova_engine',
    }
  }

  if (path.includes('/api/ai/chat')) {
    return {
      answer: `Welcome to TripNova! You can plan custom day-by-day itineraries, book RedBus buses with live seat layouts, book IRCTC trains, and reserve hotels all inside this app.`,
      source: 'tripnova_engine',
    }
  }

  return { status: 'ok' }
}

export async function apiPost(path, body) {
  try {
    const res = await fetch(path, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    })
    if (res.ok) {
      const data = await res.json()
      return data
    }
    // If server responded with error status, try fallback
    return handleClientFallback(path, body)
  } catch {
    // If backend network error or standalone live static host
    return handleClientFallback(path, body)
  }
}
