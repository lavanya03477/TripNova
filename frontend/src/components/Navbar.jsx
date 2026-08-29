import { Link, useLocation } from 'react-router-dom'

const NAV_ITEMS = [
  { label: 'Home', path: '/', icon: 'bi-house-door-fill' },
  { label: 'Plan My Journey', path: '/plan-my-journey', icon: 'bi-compass-fill' },
  { label: 'Places to Visit', path: '/places-to-visit', icon: 'bi-geo-alt-fill' },
  { label: 'Bus Booking', path: '/bus-booking', icon: 'bi-bus-front-fill' },
  { label: 'Train Booking', path: '/train-booking', icon: 'bi-train-front-fill' },
  { label: 'Hotels', path: '/hotels', icon: 'bi-building-fill' },
  { label: 'Map', path: 'https://www.google.com/maps', external: true, icon: 'bi-map-fill' },
]

export default function Navbar() {
  const location = useLocation()

  return (
    <nav className="navbar navbar-expand-lg navbar-light navbar-tripnova sticky-top">
      <div className="container">
        <Link to="/" className="brand-mark" title="TripNova - AI Travel Planner" aria-label="TripNova Home">
          <span className="brand-orb" aria-hidden="true" />
          <span className="brand-title fw-bold">TRIPNOVA</span>
        </Link>

        <button
          className="navbar-toggler border-0"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#mainNav"
          aria-controls="mainNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="mainNav">
          <ul className="navbar-nav ms-auto gap-lg-1">
            {NAV_ITEMS.map((item) => (
              <li className="nav-item" key={item.label}>
                {item.external ? (
                  <a
                    href={item.path}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="nav-link nav-link-text d-flex align-items-center gap-1"
                  >
                    <i className={`bi ${item.icon}`}></i>
                    {item.label}
                  </a>
                ) : (
                  <Link
                    to={item.path}
                    className={`nav-link nav-link-text d-flex align-items-center gap-1 ${
                      location.pathname === item.path ? 'active' : ''
                    }`}
                  >
                    <i className={`bi ${item.icon}`}></i>
                    {item.label}
                  </Link>
                )}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </nav>
  )
}
