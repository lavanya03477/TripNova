import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'

const DESTINATIONS = [
  { id: 'leh', name: 'Leh', region: 'Ladakh', x: 148, y: 42, vibe: 'High-altitude lakes & monasteries', season: 'Jun–Sep', tag: 'Adventure' },
  { id: 'manali', name: 'Manali', region: 'Himachal', x: 142, y: 68, vibe: 'Snow peaks, pine valleys, road trips', season: 'Oct–Jun', tag: 'Nature' },
  { id: 'delhi', name: 'Delhi', region: 'NCR', x: 138, y: 98, vibe: 'Capitals, bazaars, and Mughal monuments', season: 'Oct–Mar', tag: 'Culture' },
  { id: 'jaipur', name: 'Jaipur', region: 'Rajasthan', x: 118, y: 118, vibe: 'Pink City palaces and desert forts', season: 'Nov–Feb', tag: 'Heritage' },
  { id: 'agra', name: 'Agra', region: 'Uttar Pradesh', x: 152, y: 116, vibe: 'Taj Mahal and riverside sunsets', season: 'Oct–Mar', tag: 'Heritage' },
  { id: 'varanasi', name: 'Varanasi', region: 'Uttar Pradesh', x: 178, y: 132, vibe: 'Ghats, aartis, and living history', season: 'Oct–Mar', tag: 'Spiritual' },
  { id: 'kolkata', name: 'Kolkata', region: 'West Bengal', x: 218, y: 158, vibe: 'Trams, sweets, and colonial streets', season: 'Oct–Mar', tag: 'Culture' },
  { id: 'udaipur', name: 'Udaipur', region: 'Rajasthan', x: 108, y: 142, vibe: 'Lake palaces and romantic evenings', season: 'Oct–Mar', tag: 'Romance' },
  { id: 'mumbai', name: 'Mumbai', region: 'Maharashtra', x: 98, y: 188, vibe: 'Seafront energy and street food', season: 'Nov–Feb', tag: 'City' },
  { id: 'goa', name: 'Goa', region: 'West Coast', x: 96, y: 218, vibe: 'Beaches, spice, and sunset shacks', season: 'Nov–Mar', tag: 'Beach' },
  { id: 'hyderabad', name: 'Hyderabad', region: 'Telangana', x: 148, y: 202, vibe: 'Nizami cuisine and old-city charm', season: 'Oct–Feb', tag: 'Food' },
  { id: 'bangalore', name: 'Bengaluru', region: 'Karnataka', x: 132, y: 242, vibe: 'Gardens, cafes, and weekend getaways', season: 'All year', tag: 'City' },
  { id: 'chennai', name: 'Chennai', region: 'Tamil Nadu', x: 158, y: 258, vibe: 'Marina, temples, and filter coffee', season: 'Nov–Feb', tag: 'Culture' },
  { id: 'kerala', name: 'Kochi', region: 'Kerala', x: 118, y: 278, vibe: 'Backwaters, houseboats, and monsoon green', season: 'Sep–Mar', tag: 'Nature' },
]

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
