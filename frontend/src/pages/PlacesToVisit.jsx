import { useEffect, useState } from 'react'
import { useSearchParams, Link } from 'react-router-dom'
import Navbar from '../components/Navbar'
import AIAssistant from '../components/AIAssistant'
import InteractiveMapModal from '../components/InteractiveMapModal'
import InPageTransportBooking from '../components/InPageTransportBooking'
import { OptionGroup, TRAVEL_WITH, INDIAN_STATES_DATA, POPULAR_DESTINATIONS } from '../components/FormOptions'
import { apiPost } from '../api'

const QUICK_DAYS = [1, 2, 3, 4, 5, 7]

export default function PlacesToVisit() {
  const [searchParams, setSearchParams] = useSearchParams()
  const [place, setPlace] = useState('')
  const [travelWith, setTravelWith] = useState('Solo')
  const [days, setDays] = useState('3')
  const [selectedStateFilter, setSelectedStateFilter] = useState('Tamil Nadu')
  const [searchFilter, setSearchFilter] = useState('')
  
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [showMapModal, setShowMapModal] = useState(false)
  const [showInlineMap, setShowInlineMap] = useState(false)
  const [showStateDirectory, setShowStateDirectory] = useState(false)

  // Initialize from URL search parameters if available
  useEffect(() => {
    const urlPlace = searchParams.get('place')
    const urlTravelWith = searchParams.get('travelWith')
    const urlDays = searchParams.get('days')

    if (urlPlace) {
      setPlace(urlPlace)
      if (urlTravelWith) setTravelWith(urlTravelWith)
      const targetDays = urlDays || days || '3'
      setDays(targetDays)
      fetchItinerary(urlPlace, urlTravelWith || travelWith || 'Solo', targetDays)
    } else if (!place) {
      // Default to Kanyakumari on fresh visit
      setPlace('Kanyakumari, Tamil Nadu')
      fetchItinerary('Kanyakumari, Tamil Nadu', 'Solo', 3)
    }
  }, [searchParams])

  const fetchItinerary = async (targetPlace, targetTravelWith, targetDays) => {
    if (!targetPlace || !targetPlace.trim()) return
    setError('')
    setLoading(true)
    try {
      const parsedDays = parseInt(targetDays, 10) || 3
      const data = await apiPost('/api/ai/places-to-visit', {
        place: targetPlace.trim(),
        travelWith: targetTravelWith || 'Solo',
        days: parsedDays,
      })
      setResult(data)
    } catch (err) {
      setError(err.message || 'Failed to generate itinerary')
    } finally {
      setLoading(false)
    }
  }

  // Handle switching destination immediately
  const handleSelectPlace = (newPlace) => {
    if (!newPlace) return
    setPlace(newPlace)
    setSearchParams({ place: newPlace, travelWith, days })
    fetchItinerary(newPlace, travelWith, days)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!place.trim()) {
      setError('Please enter or select a destination place in India.')
      return
    }
    const targetDays = parseInt(days, 10) || 3
    setSearchParams({ place: place.trim(), travelWith, days: String(targetDays) })
    fetchItinerary(place.trim(), travelWith, targetDays)
  }

  const handleSelectDays = (d) => {
    const dStr = String(d)
    setDays(dStr)
    if (place.trim()) {
      setSearchParams({ place: place.trim(), travelWith, days: dStr })
      fetchItinerary(place.trim(), travelWith, d)
    }
  }

  // Filtered places across Indian states based on search box
  const activeStateData = INDIAN_STATES_DATA.find((s) => s.state === selectedStateFilter) || INDIAN_STATES_DATA[0]
  const allFilteredPlaces = searchFilter.trim()
    ? INDIAN_STATES_DATA.flatMap((s) =>
        s.places
          .filter((p) => p.toLowerCase().includes(searchFilter.toLowerCase()))
          .map((p) => ({ place: p, state: s.state, icon: s.icon }))
      )
    : []

  return (
    <div className="page-bg">
      <Navbar />
      <main className="container py-4">
        {/* Header with Navigation and Quick Jump Actions */}
        <div className="d-flex flex-wrap justify-content-between align-items-center mb-4 gap-3">
          <div>
            <h1 className="fw-bold mb-1">
              <i className="bi bi-geo-alt-fill text-success me-2"></i>
              Places to Visit & Travel Planner
            </h1>
            <p className="text-muted mb-0">
              TripNova AI recommends iconic attractions, day-wise itineraries, map pins, and in-page transport booking.
            </p>
          </div>

          <div className="d-flex flex-wrap align-items-center gap-2">
            {place && (
              <>
                <button
                  type="button"
                  className="btn btn-outline-primary d-flex align-items-center gap-2 rounded-pill px-3 shadow-sm"
                  onClick={() => setShowMapModal(true)}
                  title="View Destination and Itinerary Pins on Map"
                >
                  <i className="bi bi-map-fill text-danger fs-5"></i>
                  <span className="fw-semibold">Interactive Map</span>
                </button>
                <a
                  href="#inpage-transport-section"
                  className="btn btn-outline-danger d-flex align-items-center gap-2 rounded-pill px-3 shadow-sm"
                >
                  <i className="bi bi-bus-front-fill"></i>
                  <span className="fw-semibold">Book Transport</span>
                </a>
              </>
            )}
            <Link to="/plan-my-journey" className="btn btn-outline-secondary rounded-pill px-3">
              <i className="bi bi-compass me-1"></i> Plan My Journey
            </Link>
          </div>
        </div>

        {/* Active Destination Selection & Search Card */}
        <div className="card glass-card border-0 mb-4 shadow-sm">
          <div className="card-body p-4">
            <form onSubmit={handleSubmit}>
              <div className="row g-3">
                {/* Destination Input & Place Selector */}
                <div className="col-lg-6">
                  <label className="form-label fw-bold d-flex justify-content-between align-items-center">
                    <span>
                      <i className="bi bi-pin-map-fill text-danger me-1"></i> Destination in India
                    </span>
                    <button
                      type="button"
                      className="btn btn-sm btn-link text-decoration-none p-0 fw-semibold"
                      onClick={() => setShowStateDirectory(!showStateDirectory)}
                    >
                      {showStateDirectory ? '▲ Hide State Directory' : '🗺️ Select by State & All Places'}
                    </button>
                  </label>
                  <div className="input-group input-group-lg">
                    <span className="input-group-text bg-light">
                      <i className="bi bi-search"></i>
                    </span>
                    <input
                      type="text"
                      className="form-control"
                      value={place}
                      onChange={(e) => setPlace(e.target.value)}
                      placeholder="Type any place (e.g. Kanyakumari, Ooty, Manali, Madurai, Goa, Munnar)"
                      required
                    />
                  </div>
                </div>

                {/* Duration / Days Input */}
                <div className="col-sm-6 col-lg-3">
                  <label className="form-label fw-bold">
                    <i className="bi bi-calendar-event text-primary me-1"></i> Duration (Days)
                  </label>
                  <div className="input-group input-group-lg">
                    <input
                      type="number"
                      className="form-control"
                      min="1"
                      max="30"
                      value={days}
                      onChange={(e) => setDays(e.target.value)}
                      placeholder="Days (e.g. 3)"
                      required
                    />
                    <span className="input-group-text bg-light">Days</span>
                  </div>
                </div>

                {/* Travelling With Companion */}
                <div className="col-sm-6 col-lg-3">
                  <label className="form-label fw-bold">
                    <i className="bi bi-people-fill text-info me-1"></i> Travelling With
                  </label>
                  <select
                    className="form-select form-select-lg"
                    value={travelWith}
                    onChange={(e) => {
                      setTravelWith(e.target.value)
                      if (place.trim()) {
                        fetchItinerary(place.trim(), e.target.value, days)
                      }
                    }}
                  >
                    {TRAVEL_WITH.map((t) => (
                      <option key={t} value={t}>
                        {t}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Quick Days Chips & Submit Action */}
              <div className="d-flex flex-wrap justify-content-between align-items-center gap-3 mt-3 pt-3 border-top">
                <div className="d-flex flex-wrap align-items-center gap-2">
                  <span className="text-muted small fw-semibold">Quick Days:</span>
                  {QUICK_DAYS.map((d) => (
                    <button
                      key={d}
                      type="button"
                      className={`btn btn-sm rounded-pill px-3 fw-semibold ${
                        parseInt(days, 10) === d ? 'btn-primary' : 'btn-outline-secondary'
                      }`}
                      onClick={() => handleSelectDays(d)}
                    >
                      {d} {d === 1 ? 'Day' : 'Days'}
                    </button>
                  ))}
                </div>

                <button
                  type="submit"
                  className="btn btn-warm btn-lg rounded-pill px-4 fw-semibold shadow-sm"
                  disabled={loading || !place.trim()}
                >
                  {loading ? (
                    <>
                      <span className="spinner-border spinner-border-sm me-2"></span>
                      Generating Plan...
                    </>
                  ) : (
                    <>
                      <i className="bi bi-magic me-2"></i>
                      Generate Plan
                    </>
                  )}
                </button>
              </div>
            </form>

            {/* Quick Popular India Destinations Chips */}
            <div className="mt-3 pt-2">
              <span className="text-muted small fw-semibold me-2">🔥 Popular Destinations:</span>
              <div className="d-inline-flex flex-wrap gap-1 mt-1">
                {POPULAR_DESTINATIONS.map((p) => (
                  <button
                    key={p}
                    type="button"
                    className={`btn btn-sm rounded-pill py-0 px-2 small ${
                      place.toLowerCase().includes(p.toLowerCase()) ? 'btn-success fw-bold' : 'btn-light border'
                    }`}
                    onClick={() => handleSelectPlace(p)}
                  >
                    {p}
                  </button>
                ))}
              </div>
            </div>

            {/* Expandable States & All Places in India Directory */}
            {showStateDirectory && (
              <div className="mt-4 pt-3 border-top bg-light rounded-3 p-3">
                <div className="d-flex flex-wrap justify-content-between align-items-center mb-3 gap-2">
                  <h6 className="fw-bold mb-0">
                    <i className="bi bi-map text-primary me-2"></i>
                    Select from All States & Places in India
                  </h6>
                  <div style={{ maxWidth: '260px' }} className="w-100">
                    <input
                      type="text"
                      className="form-control form-control-sm"
                      placeholder="Filter all places (e.g. Ooty, Munnar)..."
                      value={searchFilter}
                      onChange={(e) => setSearchFilter(e.target.value)}
                    />
                  </div>
                </div>

                {searchFilter.trim() ? (
                  /* Search Results Across All States */
                  <div>
                    <p className="text-muted small mb-2">Matching places ({allFilteredPlaces.length}):</p>
                    <div className="d-flex flex-wrap gap-2">
                      {allFilteredPlaces.map(({ place: p, state: s, icon }) => (
                        <button
                          key={`${s}-${p}`}
                          type="button"
                          className="btn btn-outline-success btn-sm rounded-pill"
                          onClick={() => {
                            handleSelectPlace(p)
                            setShowStateDirectory(false)
                          }}
                        >
                          <span className="me-1">{icon}</span>
                          <strong>{p}</strong> <span className="text-muted small">({s})</span>
                        </button>
                      ))}
                      {allFilteredPlaces.length === 0 && (
                        <span className="text-muted small">No direct match found. You can type any city in the search box above!</span>
                      )}
                    </div>
                  </div>
                ) : (
                  /* State Tabs & Specific Places */
                  <div>
                    {/* State Selector Buttons */}
                    <div className="d-flex flex-wrap gap-1 mb-3">
                      {INDIAN_STATES_DATA.map((s) => (
                        <button
                          key={s.state}
                          type="button"
                          className={`btn btn-sm rounded-pill ${
                            selectedStateFilter === s.state ? 'btn-primary' : 'btn-outline-secondary'
                          }`}
                          onClick={() => setSelectedStateFilter(s.state)}
                        >
                          <span className="me-1">{s.icon}</span>
                          {s.state}
                        </button>
                      ))}
                    </div>

                    {/* Places for the Selected State */}
                    <div className="p-3 bg-white rounded-3 border">
                      <h6 className="fw-bold text-dark mb-2">
                        {activeStateData.icon} {activeStateData.state} Destinations:
                      </h6>
                      <div className="d-flex flex-wrap gap-2">
                        {activeStateData.places.map((p) => (
                          <button
                            key={p}
                            type="button"
                            className={`btn btn-sm rounded-pill ${
                              place.toLowerCase().includes(p.toLowerCase())
                                ? 'btn-success fw-bold'
                                : 'btn-outline-dark'
                            }`}
                            onClick={() => {
                              handleSelectPlace(p)
                              setShowStateDirectory(false)
                            }}
                          >
                            📍 {p}
                          </button>
                        ))}
                      </div>
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>

        {/* Error Alert */}
        {error && (
          <div className="alert alert-danger shadow-sm py-3 mb-4 d-flex align-items-center gap-2">
            <i className="bi bi-exclamation-triangle-fill fs-4"></i>
            <div>
              <strong>Error:</strong> {error}
            </div>
          </div>
        )}

        {/* Loading Skeleton */}
        {loading && (
          <div className="card glass-card border-0 p-5 text-center shadow-sm mb-4">
            <div className="spinner-grow text-success mx-auto mb-3" style={{ width: '3rem', height: '3rem' }} role="status"></div>
            <h4 className="fw-bold">TripNova AI is building your itinerary...</h4>
            <p className="text-muted mb-0">Prioritizing iconic landmarks, timings, GPS coordinates, and hotels for {place}...</p>
          </div>
        )}

        {/* Result: Destination Overview, Map Button & Itinerary */}
        {result && !loading && (
          <div>
            {/* Destination Highlight Banner */}
            <div className="card glass-card border-0 mb-4 bg-gradient-destination shadow-sm">
              <div className="card-body p-4">
                <div className="d-flex flex-wrap justify-content-between align-items-start gap-3">
                  <div>
                    <div className="d-flex align-items-center gap-2 mb-1">
                      <span className="badge bg-success rounded-pill px-3 py-1 fw-bold">
                        🌟 Verified Destination
                      </span>
                      <span className="text-muted small">
                        {result.itinerary?.length || days} Days Itinerary · {travelWith}
                      </span>
                    </div>
                    <h2 className="fw-bold mb-1 text-dark">{result.place || place}</h2>
                    <p className="text-muted mb-0" style={{ maxWidth: '780px' }}>
                      {result.summary}
                    </p>
                  </div>

                  <div className="d-flex flex-wrap gap-2">
                    <button
                      type="button"
                      className="btn btn-primary d-flex align-items-center gap-2 rounded-pill px-3 shadow-sm"
                      onClick={() => setShowMapModal(true)}
                    >
                      <i className="bi bi-map-fill"></i>
                      <span>Open Interactive Map</span>
                    </button>
                    <button
                      type="button"
                      className={`btn rounded-pill px-3 ${showInlineMap ? 'btn-secondary' : 'btn-outline-primary'}`}
                      onClick={() => setShowInlineMap(!showInlineMap)}
                    >
                      <i className={`bi ${showInlineMap ? 'bi-eye-slash' : 'bi-geo-alt'} me-1`}></i>
                      {showInlineMap ? 'Hide Inline Map' : 'Show Inline Map'}
                    </button>
                  </div>
                </div>
              </div>
            </div>

            {/* Inline Map View (if toggled) */}
            {showInlineMap && (
              <div className="card glass-card border-0 mb-4 shadow-sm overflow-hidden">
                <div className="card-header bg-white py-3 border-0 d-flex justify-content-between align-items-center">
                  <h5 className="fw-bold mb-0">
                    <i className="bi bi-map text-danger me-2"></i>
                    Live Route & Landmark Pins for {result.place || place}
                  </h5>
                  <button
                    type="button"
                    className="btn btn-sm btn-outline-secondary rounded-pill"
                    onClick={() => setShowInlineMap(false)}
                  >
                    Close Map
                  </button>
                </div>
                <div className="card-body p-0">
                  <InteractiveMapModal
                    place={result.place || place}
                    lat={result.lat}
                    lng={result.lng}
                    itinerary={result.itinerary}
                    inline={true}
                  />
                </div>
              </div>
            )}

            {/* Day by Day Curated Itinerary */}
            <div className="mb-4">
              <div className="d-flex justify-content-between align-items-center mb-3">
                <h4 className="fw-bold mb-0">
                  <i className="bi bi-calendar-check text-primary me-2"></i>
                  Day-by-Day Prioritized Sights ({result.itinerary?.length} Days)
                </h4>
              </div>

              <div className="d-flex flex-column gap-3">
                {result.itinerary?.map((dayPlan) => (
                  <div key={dayPlan.day} className="card glass-card border-0 shadow-sm">
                    <div className="card-header bg-transparent border-0 pt-3 pb-2">
                      <div className="d-flex align-items-center gap-2">
                        <span className="badge bg-primary rounded-pill px-3 py-2 fw-bold">
                          Day {dayPlan.day}
                        </span>
                        <h5 className="fw-bold mb-0 text-dark">{dayPlan.title}</h5>
                      </div>
                    </div>
                    <div className="card-body pt-1 pb-3">
                      <div className="row g-3">
                        {dayPlan.places?.map((spot, idx) => (
                          <div className="col-md-6" key={spot.name || idx}>
                            <div className="card h-100 border rounded-3 p-3 bg-white shadow-none hover-lift">
                              <div className="d-flex justify-content-between align-items-start mb-2">
                                <div className="d-flex align-items-center gap-2">
                                  <span className="spot-number-badge">
                                    {idx + 1}
                                  </span>
                                  <h6 className="fw-bold mb-0 text-dark">{spot.name}</h6>
                                </div>
                                {spot.bestTime && (
                                  <span className="badge bg-warning text-dark border">
                                    <i className="bi bi-clock me-1"></i>
                                    {spot.bestTime}
                                  </span>
                                )}
                              </div>
                              <p className="card-text text-muted small mb-2 flex-grow-1">
                                {spot.highlight}
                              </p>
                              <div className="d-flex justify-content-between align-items-center pt-2 border-top">
                                <span className="badge bg-light text-muted border">
                                  <i className="bi bi-hourglass-split me-1"></i>
                                  {spot.duration || '2-3 hours'}
                                </span>
                                <a
                                  href={`https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(
                                    spot.name + ' ' + (result.place || place)
                                  )}`}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="btn btn-sm btn-outline-primary rounded-pill d-flex align-items-center gap-1"
                                >
                                  <i className="bi bi-signpost-2"></i>
                                  Directions
                                </a>
                              </div>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* ================= IN-PAGE TRANSPORT BOOKING WIDGET ================= */}
            <InPageTransportBooking destination={result.place || place} />

            {/* Recommended Stays & Hotels */}
            {result.hotels && result.hotels.length > 0 && (
              <div className="mb-4">
                <div className="d-flex justify-content-between align-items-center mb-3">
                  <h4 className="fw-bold mb-0">
                    <i className="bi bi-building text-info me-2"></i>
                    Recommended Stays & Resorts in {result.place || place}
                  </h4>
                  <Link to={`/hotels?city=${encodeURIComponent(result.place || place)}`} className="btn btn-sm btn-outline-primary rounded-pill">
                    View All Hotels & Book <i className="bi bi-arrow-right ms-1"></i>
                  </Link>
                </div>

                <div className="row g-3">
                  {result.hotels.map((h, i) => (
                    <div className="col-sm-6 col-lg-3" key={h.name || i}>
                      <div className="card h-100 border-0 shadow-sm rounded-3 p-3 bg-white">
                        <div className="d-flex justify-content-between align-items-start mb-2">
                          <span className="badge bg-info-subtle text-info border border-info-subtle rounded-pill">
                            {h.type}
                          </span>
                          <span className="badge bg-warning text-dark fw-bold">
                            {h.rating}
                          </span>
                        </div>
                        <h6 className="fw-bold mb-1 text-dark">{h.name}</h6>
                        <p className="text-success fw-bold small mb-3">{h.price}</p>
                        <Link
                          to={`/hotels?city=${encodeURIComponent(result.place || place)}`}
                          className="btn btn-sm btn-outline-info rounded-pill w-100 mt-auto"
                        >
                          Book Stay <i className="bi bi-check-circle ms-1"></i>
                        </Link>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {/* Modal Interactive Map */}
        {showMapModal && result && (
          <InteractiveMapModal
            place={result.place || place}
            lat={result.lat}
            lng={result.lng}
            itinerary={result.itinerary}
            onClose={() => setShowMapModal(false)}
          />
        )}

        {/* AI Travel Co-Pilot Assistant */}
        <div className="mt-4">
          <AIAssistant
            title={`TripNova AI Guide for ${place || 'India Travel'}`}
            placeholder={`Ask about ${place || 'any Indian city'}, best time, local food, bus & train routes...`}
            context={{ place: result?.place || place, days, travelWith }}
          />
        </div>
      </main>
    </div>
  )
}
