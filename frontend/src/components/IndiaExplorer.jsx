import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'

const DESTINATIONS = [
  // Jammu & Kashmir and Ladakh
  { id: 'srinagar', name: 'Srinagar', region: 'Jammu & Kashmir', x: 160, y: 48, vibe: 'Houseboats, Dal Lake, Mughal gardens', season: 'Apr–Oct', tag: 'Nature' },
  { id: 'gulmarg', name: 'Gulmarg', region: 'Jammu & Kashmir', x: 154, y: 44, vibe: 'Ski slopes and alpine meadows', season: 'Dec–Mar', tag: 'Adventure' },
  { id: 'leh', name: 'Leh', region: 'Ladakh', x: 148, y: 42, vibe: 'High-altitude lakes & monasteries', season: 'Jun–Sep', tag: 'Adventure' },

  // Himachal Pradesh
  { id: 'shimla', name: 'Shimla', region: 'Himachal Pradesh', x: 140, y: 64, vibe: 'Colonial hill station & toy train', season: 'Mar–Jun & Sep–Nov', tag: 'Hill Station' },
  { id: 'manali', name: 'Manali', region: 'Himachal Pradesh', x: 142, y: 68, vibe: 'Snow peaks, pine valleys, road trips', season: 'Oct–Jun', tag: 'Nature' },
  { id: 'dharamshala', name: 'Dharamshala', region: 'Himachal Pradesh', x: 136, y: 62, vibe: 'Tibetan culture & trekking', season: 'Mar–Jun & Sep–Nov', tag: 'Culture' },

  // Punjab and Haryana
  { id: 'amritsar', name: 'Amritsar', region: 'Punjab', x: 126, y: 86, vibe: 'Golden Temple & Punjabi cuisine', season: 'Oct–Mar', tag: 'Spiritual' },
  { id: 'kurukshetra', name: 'Kurukshetra', region: 'Haryana', x: 132, y: 96, vibe: 'Mythic sites & pilgrimage', season: 'Oct–Mar', tag: 'Heritage' },

  // Uttarakhand
  { id: 'rishikesh', name: 'Rishikesh', region: 'Uttarakhand', x: 150, y: 78, vibe: 'Yoga, rafting, spiritual retreats', season: 'Feb–Jun & Sep–Nov', tag: 'Adventure' },
  { id: 'nainital', name: 'Nainital', region: 'Uttarakhand', x: 156, y: 76, vibe: 'Lake town & hill views', season: 'Mar–Jun & Sep–Nov', tag: 'Hill Station' },

  // Delhi NCR
  { id: 'delhi', name: 'Delhi', region: 'NCR', x: 138, y: 98, vibe: 'Capitals, bazaars, and Mughal monuments', season: 'Oct–Mar', tag: 'Culture' },

  // Rajasthan
  { id: 'jaipur', name: 'Jaipur', region: 'Rajasthan', x: 118, y: 118, vibe: 'Pink City palaces and desert forts', season: 'Nov–Feb', tag: 'Heritage' },
  { id: 'udaipur', name: 'Udaipur', region: 'Rajasthan', x: 108, y: 142, vibe: 'Lake palaces and romantic evenings', season: 'Oct–Mar', tag: 'Romance' },
  { id: 'jaisalmer', name: 'Jaisalmer', region: 'Rajasthan', x: 92, y: 118, vibe: 'Desert forts and camel safaris', season: 'Oct–Mar', tag: 'Adventure' },
  { id: 'jodhpur', name: 'Jodhpur', region: 'Rajasthan', x: 102, y: 128, vibe: 'Blue City & Mehrangarh Fort', season: 'Oct–Mar', tag: 'Heritage' },

  // Gujarat
  { id: 'ahmedabad', name: 'Ahmedabad', region: 'Gujarat', x: 92, y: 148, vibe: 'Sabarmati, textiles, street food', season: 'Oct–Mar', tag: 'City' },
  { id: 'gir', name: 'Gir', region: 'Gujarat', x: 86, y: 168, vibe: 'Asiatic lions & dry deciduous forests', season: 'Nov–Apr', tag: 'Wildlife' },
  { id: 'somnath', name: 'Somnath', region: 'Gujarat', x: 86, y: 178, vibe: 'Coastal temple & pilgrimage', season: 'Oct–Mar', tag: 'Spiritual' },

  // Maharashtra
  { id: 'mumbai', name: 'Mumbai', region: 'Maharashtra', x: 98, y: 188, vibe: 'Seafront energy and street food', season: 'Nov–Feb', tag: 'City' },
  { id: 'pune', name: 'Pune', region: 'Maharashtra', x: 106, y: 202, vibe: 'Cafes, history, gateway to hill stations', season: 'All year', tag: 'City' },
  { id: 'ajanta', name: 'Ajanta', region: 'Maharashtra', x: 118, y: 208, vibe: 'Ancient cave paintings & rock-cut architecture', season: 'Oct–Mar', tag: 'Heritage' },
  { id: 'ellora', name: 'Ellora', region: 'Maharashtra', x: 116, y: 210, vibe: 'Cave temples & sculptures', season: 'Oct–Mar', tag: 'Heritage' },

  // Goa
  { id: 'goa', name: 'Goa', region: 'Goa', x: 96, y: 218, vibe: 'Beaches, spice, and sunset shacks', season: 'Nov–Mar', tag: 'Beach' },

  // Karnataka
  { id: 'bangalore', name: 'Bengaluru', region: 'Karnataka', x: 132, y: 242, vibe: 'Gardens, cafes, and weekend getaways', season: 'All year', tag: 'City' },
  { id: 'mysore', name: 'Mysore', region: 'Karnataka', x: 126, y: 252, vibe: 'Palaces & Dasara festival', season: 'Oct–Mar', tag: 'Heritage' },
  { id: 'hampi', name: 'Hampi', region: 'Karnataka', x: 118, y: 228, vibe: 'UNESCO ruins & boulder landscapes', season: 'Oct–Mar', tag: 'Heritage' },
  { id: 'coorg', name: 'Coorg', region: 'Karnataka', x: 122, y: 238, vibe: 'Coffee hills & waterfalls', season: 'Oct–Mar', tag: 'Nature' },

  // Kerala
  { id: 'kochi', name: 'Kochi', region: 'Kerala', x: 118, y: 278, vibe: 'Backwaters, houseboats, and colonial ports', season: 'Sep–Mar', tag: 'Nature' },
  { id: 'munnar', name: 'Munnar', region: 'Kerala', x: 122, y: 268, vibe: 'Tea gardens & misty hills', season: 'Sep–Mar', tag: 'Hill Station' },
  { id: 'alleppey', name: 'Alleppey', region: 'Kerala', x: 116, y: 288, vibe: 'Backwaters and houseboat cruises', season: 'Sep–Mar', tag: 'Nature' },

  // Tamil Nadu
  { id: 'chennai', name: 'Chennai', region: 'Tamil Nadu', x: 158, y: 258, vibe: 'Marina, temples, and filter coffee', season: 'Nov–Feb', tag: 'Culture' },
  { id: 'madurai', name: 'Madurai', region: 'Tamil Nadu', x: 148, y: 268, vibe: 'Meenakshi Temple & Nayakar Palace', season: 'Oct–Mar', tag: 'Temple' },
  { id: 'ooty', name: 'Ooty', region: 'Tamil Nadu', x: 128, y: 252, vibe: 'Nilgiri hills, tea gardens, toy train', season: 'Apr–Jun & Sep–Nov', tag: 'Hill Station' },
  { id: 'kodaikanal', name: 'Kodaikanal', region: 'Tamil Nadu', x: 138, y: 258, vibe: 'Lakes, waterfalls & trekking trails', season: 'Apr–Jun & Sep–Nov', tag: 'Hill Station' },
  { id: 'rameshwaram', name: 'Rameshwaram', region: 'Tamil Nadu', x: 168, y: 278, vibe: 'Sacred pilgrimage & Pamban Bridge', season: 'Oct–Apr', tag: 'Spiritual' },
  { id: 'kanyakumari', name: 'Kanyakumari', region: 'Tamil Nadu', x: 158, y: 298, vibe: 'Sunrise at 3 seas & Vivekananda Rock', season: 'Oct–Mar', tag: 'Beach' },

  // Andhra Pradesh and Telangana
  { id: 'tirupati', name: 'Tirupati', region: 'Andhra Pradesh', x: 156, y: 218, vibe: 'Tirumala temple pilgrimage', season: 'All year', tag: 'Spiritual' },
  { id: 'visakhapatnam', name: 'Visakhapatnam', region: 'Andhra Pradesh', x: 188, y: 208, vibe: 'Beaches, hills, and naval history', season: 'Oct–Mar', tag: 'Beach' },
  { id: 'hyderabad', name: 'Hyderabad', region: 'Telangana', x: 148, y: 202, vibe: 'Nizami cuisine and old-city charm', season: 'Oct–Feb', tag: 'Food' },

  // Odisha
  { id: 'puri', name: 'Puri', region: 'Odisha', x: 198, y: 168, vibe: 'Jagannath Temple & golden beaches', season: 'Oct–Feb', tag: 'Spiritual' },
  { id: 'konark', name: 'Konark', region: 'Odisha', x: 202, y: 170, vibe: 'Sun Temple & stone chariot', season: 'Oct–Feb', tag: 'Heritage' },

  // West Bengal
  { id: 'kolkata', name: 'Kolkata', region: 'West Bengal', x: 218, y: 158, vibe: 'Trams, sweets, and colonial streets', season: 'Oct–Mar', tag: 'Culture' },
  { id: 'darjeeling', name: 'Darjeeling', region: 'West Bengal', x: 208, y: 128, vibe: 'Tea gardens & Himalayan views', season: 'Mar–May & Sep–Nov', tag: 'Hill Station' },
  { id: 'sundarbans', name: 'Sundarbans', region: 'West Bengal', x: 228, y: 188, vibe: 'Mangrove delta & tiger reserve', season: 'Oct–Mar', tag: 'Wildlife' },

  // Bihar and Jharkhand
  { id: 'bodhgaya', name: 'Bodh Gaya', region: 'Bihar', x: 176, y: 148, vibe: 'Buddhist pilgrimage & Mahabodhi Temple', season: 'Oct–Mar', tag: 'Spiritual' },
  { id: 'nalanda', name: 'Nalanda', region: 'Bihar', x: 172, y: 150, vibe: 'Ancient university ruins', season: 'Oct–Mar', tag: 'Heritage' },
  { id: 'ranchi', name: 'Ranchi', region: 'Jharkhand', x: 168, y: 172, vibe: 'Waterfalls & tribal culture', season: 'Oct–Mar', tag: 'Nature' },

  // Chhattisgarh and Madhya Pradesh
  { id: 'bastar', name: 'Bastar', region: 'Chhattisgarh', x: 156, y: 188, vibe: 'Tribal arts & waterfalls', season: 'Oct–Mar', tag: 'Culture' },
  { id: 'khajuraho', name: 'Khajuraho', region: 'Madhya Pradesh', x: 142, y: 168, vibe: 'Erotic temples & UNESCO heritage', season: 'Oct–Mar', tag: 'Heritage' },
  { id: 'kanha', name: 'Kanha', region: 'Madhya Pradesh', x: 132, y: 178, vibe: 'Tiger reserve & sal forests', season: 'Oct–Jun', tag: 'Wildlife' },

  // Northeast India
  { id: 'guwahati', name: 'Guwahati', region: 'Assam', x: 206, y: 118, vibe: 'Brahmaputra, temples & gateway to NE', season: 'Oct–Mar', tag: 'City' },
  { id: 'kaziranga', name: 'Kaziranga', region: 'Assam', x: 210, y: 128, vibe: 'One-horned rhino sanctuary', season: 'Nov–Apr', tag: 'Wildlife' },
  { id: 'shillong', name: 'Shillong', region: 'Meghalaya', x: 228, y: 118, vibe: 'Waterfalls & music culture', season: 'Oct–Apr', tag: 'Nature' },
  { id: 'cherrapunji', name: 'Cherrapunji', region: 'Meghalaya', x: 232, y: 122, vibe: 'Living root bridges & heavy rains', season: 'Oct–Apr', tag: 'Nature' },
  { id: 'gangtok', name: 'Gangtok', region: 'Sikkim', x: 206, y: 108, vibe: 'Himalayan views & monasteries', season: 'Mar–May & Sep–Nov', tag: 'Hill Station' },
  { id: 'tawang', name: 'Tawang', region: 'Arunachal Pradesh', x: 246, y: 78, vibe: 'Monasteries & high-altitude passes', season: 'Apr–Oct', tag: 'Adventure' },
  { id: 'kohima', name: 'Kohima', region: 'Nagaland', x: 236, y: 118, vibe: 'War memorial & tribal festivals', season: 'Oct–Mar', tag: 'Culture' },
  { id: 'imphal', name: 'Imphal', region: 'Manipur', x: 232, y: 132, vibe: 'Palaces, markets & cultural festivals', season: 'Oct–Mar', tag: 'Culture' },

  // Islands and UTs
  { id: 'portblair', name: 'Port Blair', region: 'Andaman & Nicobar', x: 258, y: 278, vibe: 'Coral reefs & tropical beaches', season: 'Nov–Apr', tag: 'Beach' },
  { id: 'kavaratti', name: 'Kavaratti', region: 'Lakshadweep', x: 86, y: 298, vibe: 'Atolls, lagoons & diving', season: 'Oct–Mar', tag: 'Beach' },
  { id: 'pondicherry', name: 'Pondicherry', region: 'Puducherry', x: 162, y: 262, vibe: 'French quarter & Auroville', season: 'Oct–Mar', tag: 'Culture' },

  // Additional notable cities
  { id: 'lucknow', name: 'Lucknow', region: 'Uttar Pradesh', x: 162, y: 118, vibe: 'Awadhi cuisine & nawabi heritage', season: 'Oct–Mar', tag: 'Culture' },
  { id: 'varanasi', name: 'Varanasi', region: 'Uttar Pradesh', x: 178, y: 132, vibe: 'Ghats, aartis, and living history', season: 'Oct–Mar', tag: 'Spiritual' },
  { id: 'agra', name: 'Agra', region: 'Uttar Pradesh', x: 152, y: 116, vibe: 'Taj Mahal and riverside sunsets', season: 'Oct–Mar', tag: 'Heritage' }
];


export default function IndiaExplorer() {
  const [activeId, setActiveId] = useState('goa')
  const [tilt, setTilt] = useState({ x: 8, y: -10 })

  const active = useMemo(
    () => DESTINATIONS.find((d) => d.id === activeId) || DESTINATIONS[0],
    [activeId],
  )

  const onMove = (e) => {
    const rect = e.currentTarget.getBoundingClientRect()
    const px = (e.clientX - rect.left) / rect.width - 0.5
    const py = (e.clientY - rect.top) / rect.height - 0.5
    setTilt({ x: 8 - py * 10, y: -10 + px * 14 })
  }

  return (
    <section className="explorer-wrap mb-4">
      <div className="explorer-copy">
        <p className="explorer-kicker">Interactive India model</p>
        <h2>Spin the map. Pick a vibe. Start planning.</h2>
        <p className="text-muted mb-3">
          Hover pins to preview destinations. Click one to open a day-wise itinerary.
        </p>
        <div className="explorer-card">
          <span className="explorer-tag">{active.tag}</span>
          <h3>{active.name}</h3>
          <p className="mb-1">{active.region}</p>
          <p className="explorer-vibe">{active.vibe}</p>
          <div className="explorer-meta">
            <span>
              <i className="bi bi-sun me-1"></i>
              Best: {active.season}
            </span>
          </div>
          <Link className="btn btn-warm mt-3" to={`/places-to-visit?place=${encodeURIComponent(active.name)}`}>
            Plan {active.name}
            <i className="bi bi-arrow-right ms-2"></i>
          </Link>
        </div>
        <div className="explorer-chips mt-3">
          {DESTINATIONS.map((d) => (
            <button
              key={d.id}
              type="button"
              className={`explorer-chip ${d.id === activeId ? 'is-active' : ''}`}
              onClick={() => setActiveId(d.id)}
            >
              {d.name}
            </button>
          ))}
        </div>
      </div>

      <div className="explorer-stage" onMouseMove={onMove} onMouseLeave={() => setTilt({ x: 8, y: -10 })}>
        <div
          className="explorer-model"
          style={{ transform: `rotateX(${tilt.x}deg) rotateY(${tilt.y}deg)` }}
        >
          <div className="explorer-glow" />
          <svg viewBox="0 0 280 360" className="india-svg" role="img" aria-label="Interactive map of India">
            <defs>
              <linearGradient id="land" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stopColor="#1d9a78" />
                <stop offset="55%" stopColor="#0f6e6a" />
                <stop offset="100%" stopColor="#155e75" />
              </linearGradient>
              <filter id="soft">
                <feGaussianBlur stdDeviation="2.2" result="b" />
                <feMerge>
                  <feMergeNode in="b" />
                  <feMergeNode in="SourceGraphic" />
                </feMerge>
              </filter>
            </defs>
            <path
              className="india-land"
              d="M138 18 L158 28 L176 42 L198 62 L214 86 L228 112 L236 138 L244 162 L252 178 L246 198 L238 214 L248 232 L254 252 L242 272 L226 288 L210 300 L198 318 L186 338 L170 348 L156 338 L148 316 L136 302 L118 292 L98 276 L80 258 L64 242 L46 228 L30 208 L22 186 L20 164 L30 142 L48 124 L42 100 L50 76 L70 54 L94 36 L116 24 Z"
            />
            <ellipse cx="168" cy="352" rx="10" ry="6" fill="#0f766e" opacity="0.85" />
            {DESTINATIONS.map((d) => (
              <g
                key={d.id}
                className={`map-pin ${d.id === activeId ? 'is-active' : ''}`}
                onMouseEnter={() => setActiveId(d.id)}
                onClick={() => setActiveId(d.id)}
                role="button"
                tabIndex={0}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' || e.key === ' ') setActiveId(d.id)
                }}
              >
                <circle className="pin-pulse" cx={d.x} cy={d.y} r="12" />
                <circle className="pin-dot" cx={d.x} cy={d.y} r="5" />
                <text x={d.x + 8} y={d.y - 8}>{d.name}</text>
              </g>
            ))}
          </svg>
          <div className="explorer-base" />
        </div>
      </div>
    </section>
  )
}
