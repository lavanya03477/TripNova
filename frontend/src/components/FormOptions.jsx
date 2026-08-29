const CLIMATE = ['❄️ Cold / Chill', '☀️ Hot / Sunny', '🌧️ Rainy', '🌤️ Moderate']
const TRAVEL_WITH = ['Solo', 'Friends', 'Family', 'Couple']
const EXPERIENCE = ['🏔️ Adventure', '🌿 Nature', '🏖️ Relaxation', '🏛️ History & Culture', '🎉 Entertainment']
const BUDGET = ['Low', 'Medium', 'High']

// Comprehensive Directory of All Indian States, UTs, and Top Tourist Destinations
const INDIAN_STATES_DATA = [
  {
    state: 'Tamil Nadu',
    icon: '🛕',
    places: [
      'Madurai', 'Ooty (Udhagamandalam)', 'Kodaikanal', 'Chennai', 'Rameswaram',
      'Kanyakumari', 'Thanjavur', 'Coimbatore & Isha Yoga', 'Mahabalipuram',
      'Kanchipuram', 'Tiruchirappalli (Trichy)', 'Yercaud', 'Tiruvannamalai',
      'Courtallam', 'Chidambaram & Pichavaram', 'Valparai & Pollachi', 'Coonoor',
      'Hogenakkal Falls', 'Tirunelveli & Papanasam', 'Chettinad (Karaikudi)',
      'Vellore', 'Kolli Hills', 'Kumbakonam', 'Yelagiri Hills', 'Theni & Megamalai',
    ],
  },
  {
    state: 'Kerala',
    icon: '🌴',
    places: [
      'Munnar', 'Alleppey (Alappuzha)', 'Kochi (Cochin)', 'Wayanad', 'Varkala Beach',
      'Kovalam', 'Thekkady (Periyar)', 'Athirappilly Falls', 'Kumarakom', 'Bekal Fort',
      'Poovar Island', 'Vagamon',
    ],
  },
  {
    state: 'Karnataka',
    icon: '🏰',
    places: [
      'Bangalore (Bengaluru)', 'Mysore (Mysuru)', 'Coorg (Madikeri)', 'Hampi (UNESCO)',
      'Gokarna', 'Chikmagalur', 'Dandeli', 'Badami & Pattadakal', 'Kabini Wildlife',
      'Udupi & Murudeshwar', 'Bandipur',
    ],
  },
  {
    state: 'Goa',
    icon: '🏖️',
    places: [
      'North Goa (Baga & Calangute)', 'South Goa (Palolem & Colva)', 'Panaji & Old Goa',
      'Dudhsagar Waterfalls', 'Vagator & Anjuna',
    ],
  },
  {
    state: 'Maharashtra',
    icon: '🌊',
    places: [
      'Mumbai', 'Pune', 'Lonavala & Khandala', 'Mahabaleshwar & Panchgani',
      'Alibaug Beach', 'Shirdi', 'Ajanta & Ellora Caves', 'Matheran', 'Tadoba National Park',
    ],
  },
  {
    state: 'Rajasthan',
    icon: '🐪',
    places: [
      'Jaipur (Pink City)', 'Udaipur (City of Lakes)', 'Jodhpur (Blue City)',
      'Jaisalmer (Golden City)', 'Pushkar', 'Mount Abu', 'Ranthambore National Park',
      'Bikaner', 'Chittorgarh Fort',
    ],
  },
  {
    state: 'Himachal Pradesh',
    icon: '❄️',
    places: [
      'Manali & Solang Valley', 'Shimla & Kufri', 'Dharamshala & McLeodGanj',
      'Kasol & Parvati Valley', 'Spiti Valley', 'Dalhousie & Khajjiar', 'Bir Billing (Paragliding)',
      'Jibhi & Tirthan Valley',
    ],
  },
  {
    state: 'Uttarakhand',
    icon: '🏔️',
    places: [
      'Rishikesh (Yoga & Rafting)', 'Nainital & Bhimtal', 'Mussoorie', 'Haridwar',
      'Auli (Skiing)', 'Jim Corbett National Park', 'Kedarnath', 'Badrinath',
      'Valley of Flowers & Chopta',
    ],
  },
  {
    state: 'Jammu & Kashmir & Ladakh',
    icon: '⛷️',
    places: [
      'Srinagar & Dal Lake', 'Gulmarg (Snow Gondola)', 'Pahalgam & Betaab Valley',
      'Sonmarg', 'Leh & Pangong Lake', 'Nubra Valley & Khardung La', 'Zanskar Valley',
    ],
  },
  {
    state: 'Delhi & NCR',
    icon: '🏛️',
    places: ['New Delhi & India Gate', 'Old Delhi & Red Fort', 'Qutub Minar & Akshardham'],
  },
  {
    state: 'Uttar Pradesh',
    icon: '🪔',
    places: [
      'Varanasi (Kashi & Ganga Ghats)', 'Agra (Taj Mahal)', 'Ayodhya (Ram Mandir)',
      'Lucknow (Nawabi Heritage)', 'Mathura & Vrindavan', 'Prayagraj (Triveni Sangam)',
    ],
  },
  {
    state: 'West Bengal & Sikkim',
    icon: '🍃',
    places: [
      'Kolkata (City of Joy)', 'Darjeeling (Toy Train & Tea)', 'Gangtok (Sikkim)',
      'Pelling & Kanchenjunga', 'Kalimpong', 'Sundarbans Mangrove', 'Digha Beach',
    ],
  },
  {
    state: 'Northeast India',
    icon: '🌁',
    places: [
      'Shillong & Cherrapunji (Meghalaya)', 'Kaziranga (Assam)', 'Tawang (Arunachal Pradesh)',
      'Majuli Island', 'Dawki Crystal River', 'Ziro Valley', 'Kohima & Dzukou Valley',
    ],
  },
  {
    state: 'Andhra Pradesh & Telangana',
    icon: '💎',
    places: [
      'Hyderabad (Charminar & Golconda)', 'Visakhapatnam (Vizag & Araku Valley)',
      'Tirupati (Lord Venkateswara)', 'Vijayawada', 'Gandikota (Grand Canyon of India)',
    ],
  },
  {
    state: 'Gujarat',
    icon: '🦁',
    places: [
      'Rann of Kutch (White Desert)', 'Statue of Unity (Kevadia)', 'Gir National Park (Asiatic Lions)',
      'Somnath & Dwarka', 'Ahmedabad Heritage',
    ],
  },
  {
    state: 'Madhya Pradesh',
    icon: '🐅',
    places: [
      'Khajuraho Temples', 'Pachmarhi Hill Station', 'Kanha & Bandhavgarh Tiger Reserves',
      'Ujjain Mahakaleshwar', 'Gwalior Fort', 'Orchha',
    ],
  },
  {
    state: 'Odisha',
    icon: '☀️',
    places: ['Puri (Jagannath Temple)', 'Konark Sun Temple', 'Bhubaneswar', 'Chilika Lake'],
  },
  {
    state: 'Islands & Union Territories',
    icon: '🏝️',
    places: [
      'Pondicherry (Puducherry & Auroville)', 'Andaman (Havelock & Neil Island)',
      'Port Blair', 'Lakshadweep (Agatti & Bangaram)',
    ],
  },
]

const POPULAR_DESTINATIONS = [
  'Manali', 'Goa', 'Ooty', 'Kodaikanal', 'Madurai', 'Jaipur', 'Rishikesh',
  'Kerala (Munnar)', 'Kanyakumari', 'Rameswaram', 'Udaipur', 'Varanasi',
  'Coorg', 'Shimla', 'Darjeeling', 'Pondicherry', 'Leh Ladakh', 'Agra',
]

function OptionGroup({ label, options, value, onChange, name }) {
  return (
    <div className="mb-4">
      <label className="form-label fw-semibold">{label}</label>
      <div className="d-flex flex-wrap gap-2 option-chip-group">
        {options.map((opt, idx) => {
          const id = `${name}-${idx}`
          return (
            <span key={opt}>
              <input
                type="radio"
                className="btn-check"
                name={name}
                id={id}
                checked={value === opt}
                onChange={() => onChange(opt)}
              />
              <label className="btn btn-outline-primary rounded-pill px-3" htmlFor={id}>
                {opt}
              </label>
            </span>
          )
        })}
      </div>
    </div>
  )
}

export {
  CLIMATE,
  TRAVEL_WITH,
  EXPERIENCE,
  BUDGET,
  INDIAN_STATES_DATA,
  POPULAR_DESTINATIONS,
  OptionGroup,
}
