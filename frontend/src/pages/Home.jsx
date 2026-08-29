import Navbar from '../components/Navbar'
import AIAssistant from '../components/AIAssistant'
import IndiaExplorer from '../components/IndiaExplorer'
import { useAuth } from '../context/AuthContext'
import { Link } from 'react-router-dom'

const FEATURES = [
  {
    to: '/plan-my-journey',
    icon: '🧭',
    title: 'Plan My Journey',
    desc: 'AI recommends top 3 destinations matching your vibe & budget',
    color: 'primary',
    badge: 'Smart AI',
  },
  {
    to: '/places-to-visit',
    icon: '📍',
    title: 'Places to Visit',
    desc: 'Day-wise itinerary with interactive map pins & iconic sights',
    color: 'success',
    badge: 'Interactive Map',
  },
  {
    to: '/bus-booking',
    icon: '🚌',
    title: 'Bus Booking',
    desc: 'In-app RedBus booking with live seat layout selector & e-tickets',
    color: 'danger',
    badge: 'redBus API',
  },
  {
    to: '/train-booking',
    icon: '🚂',
    title: 'Train Booking',
    desc: 'In-app IRCTC train search, live availability & PNR tracker',
    color: 'primary',
    badge: 'IRCTC In-App',
  },
  {
    to: '/hotels',
    icon: '🏨',
    title: 'Hotels & Resorts',
    desc: 'Boutique stays, heritage palaces & resorts with instant booking',
    color: 'info',
    badge: 'Best Rates',
  },
  {
    href: 'https://www.google.com/maps',
    icon: '🗺️',
    title: 'Live GPS Map',
    desc: 'Explore real-time navigation and live route directions',
    color: 'warning',
    external: true,
    badge: 'Navigation',
  },
]

export default function Home() {
  const { user, logout } = useAuth()

  return (
    <div className="page-bg">
      <Navbar />
      <main className="container py-4">
        <div className="hero-banner shadow-lg">
          <div className="d-flex align-items-center gap-2 mb-2">
            <span className="badge bg-warning text-dark px-3 py-1 fw-bold rounded-pill">
              ✨ Welcome to TripNova
            </span>
            <span className="hero-kicker mb-0">India Travel Studio</span>
          </div>
          <h1 className="display-5 mb-2 fw-bold">Hello, {user?.username || 'Explorer'}</h1>
          <p className="lead mb-0 opacity-90 fs-6" style={{ maxWidth: '640px' }}>
            Plan your complete journey in one unified app: AI-powered day-by-day itineraries, interactive map pinning, RedBus bus booking, IRCTC train booking, and handpicked hotels.
          </p>
        </div>

        {/* 3D Interactive Map Explorer */}
        <IndiaExplorer />

        {/* TripNova Studio Services */}
        <div className="d-flex justify-content-between align-items-center mb-3 mt-4">
          <div>
            <h4 className="fw-bold mb-0">TripNova Travel Studio</h4>
            <p className="text-muted small mb-0">All your travel requirements seamlessly integrated in a single app.</p>
          </div>
        </div>

        <div className="row g-3 mb-4">
          {FEATURES.map((f) => (
            <div className="col-sm-6 col-lg-4" key={f.title}>
              {f.external ? (
                <a
                  href={f.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={`card feature-card shadow-sm h-100 border-start border-4 border-${f.color}`}
                >
                  <div className="card-body p-4 d-flex flex-column justify-content-between">
                    <div>
                      <div className="d-flex justify-content-between align-items-start mb-2">
                        <div className="feature-icon mb-0">{f.icon}</div>
                        {f.badge && <span className="badge bg-light text-dark border">{f.badge}</span>}
                      </div>
                      <h5 className="card-title fw-bold mt-2">{f.title}</h5>
                      <p className="card-text text-muted small mb-0">{f.desc}</p>
                    </div>
                  </div>
                </a>
              ) : (
                <Link
                  to={f.to}
                  className={`card feature-card shadow-sm h-100 border-start border-4 border-${f.color}`}
                >
                  <div className="card-body p-4 d-flex flex-column justify-content-between">
                    <div>
                      <div className="d-flex justify-content-between align-items-start mb-2">
                        <div className="feature-icon mb-0">{f.icon}</div>
                        {f.badge && <span className="badge bg-light text-dark border">{f.badge}</span>}
                      </div>
                      <h5 className="card-title fw-bold mt-2">{f.title}</h5>
                      <p className="card-text text-muted small mb-0">{f.desc}</p>
                    </div>
                  </div>
                </Link>
              )}
            </div>
          ))}
        </div>

        {/* AI Travel Co-Pilot */}
        <AIAssistant
          title="TripNova Travel Co-Pilot"
          placeholder="Ask about destinations, best season, food, bus & train routes, or anything about India travel!"
        />

        <div className="text-center pt-2 pb-4">
          <button type="button" className="btn btn-outline-danger btn-sm rounded-pill px-4 shadow-sm" onClick={logout}>
            <i className="bi bi-box-arrow-right me-1"></i>
            Logout
          </button>
        </div>
      </main>
    </div>
  )
}
