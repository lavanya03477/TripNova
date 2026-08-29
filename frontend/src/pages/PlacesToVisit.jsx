import { useEffect, useState } from 'react'
import { useSearchParams, Link } from 'react-router-dom'
import Navbar from '../components/Navbar'
import AIAssistant from '../components/AIAssistant'
import InteractiveMapModal from '../components/InteractiveMapModal'
import { OptionGroup, TRAVEL_WITH } from '../components/FormOptions'
import { apiPost } from '../api'

const QUICK_DAYS = [1, 2, 3, 4, 5, 7]

export default function PlacesToVisit() {
  const [searchParams, setSearchParams] = useSearchParams()
  const [place, setPlace] = useState('')
  const [travelWith, setTravelWith] = useState('Solo')
  const [days, setDays] = useState('3')
  const [isPrefilled, setIsPrefilled] = useState(false)
  const [showChangePlace, setShowChangePlace] = useState(false)
  
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [showMapModal, setShowMapModal] = useState(false)
  const [showInlineMap, setShowInlineMap] = useState(false)

  useEffect(() => {
    const urlPlace = searchParams.get('place')
    const urlTravelWith = searchParams.get('travelWith')
    const urlDays = searchParams.get('days')

    if (urlPlace) {
      setPlace(urlPlace)
      setIsPrefilled(true)
      setShowChangePlace(false)
      if (urlTravelWith) setTravelWith(urlTravelWith)
      if (urlDays) {
        setDays(urlDays)
        fetchItinerary(urlPlace, urlTravelWith || 'Solo', urlDays)
      } else {
        // Default to 3 days and auto-load if desired, or let user pick days
        fetchItinerary(urlPlace, urlTravelWith || 'Solo', 3)
      }
    }
  }, [searchParams])

  const fetchItinerary = async (targetPlace, targetTravelWith, targetDays) => {
    if (!targetPlace || !targetPlace.trim()) return
    setError('')
    setLoading(true)
    try {
      const data = await apiPost('/api/ai/places-to-visit', {
        place: targetPlace.trim(),
        travelWith: targetTravelWith || 'Solo',
        days: parseInt(targetDays, 10) || 3,
      })
      setResult(data)
    } catch (err) {
      setError(err.message || 'Failed to generate itinerary')
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!place.trim()) {
      setError('Please enter or select a destination place.')
      return
    }
    if (!days || parseInt(days, 10) < 1) {
      setError('Please enter a valid number of days.')
      return
    }
    fetchItinerary(place, travelWith, days)
  }

  const handleSelectDays = (d) => {
    setDays(String(d))
    if (place.trim()) {
      fetchItinerary(place, travelWith, d)
    }
  }

  const handleResetDestination = () => {
    setIsPrefilled(false)
    setShowChangePlace(true)
    setResult(null)
    setPlace('')
    setSearchParams({})
  }

  return (
    <div className="page-bg">
      <Navbar />
      <main className="container py-4">
        {/* Header with Navigation and Map Actions */}
        <div className="d-flex flex-wrap justify-content-between align-items-center mb-4 gap-3">
          <div>
            <h1 className="fw-bold mb-1">
              <i className="bi bi-geo-alt-fill text-success me-2"></i>
              Places to Visit & Day-Wise Plan
            </h1>
            <p className="text-muted mb-0">
              TripNova AI recommends the most iconic attractions tailored to your trip duration.
            </p>
          </div>

          <div className="d-flex align-items-center gap-2">
            {place && (
              <button
                type="button"
                className="btn btn-outline-primary d-flex align-items-center gap-2 rounded-pill px-3 shadow-sm"
                onClick={() => setShowMapModal(true)}
                title="View Destination and Itinerary Pins on Map"
              >
                <i className="bi bi-map-fill text-danger fs-5"></i>
                <span className="fw-semibold">Interactive Map</span>
              </button>
            )}
            <Link to="/plan-my-journey" className="btn btn-outline-secondary rounded-pill px-3">
              <i className="bi bi-arrow-left me-1"></i> Plan My Journey
            </Link>
          </div>
        </div>

        {/* Selected Destination Banner from Plan My Journey */}
        {isPrefilled && !showChangePlace ? (
          <div className="card glass-card border-0 mb-4 bg-gradient-destination shadow-sm">
            <div className="card-body p-4">
              <div className="d-flex flex-wrap justify-content-between align-items-center gap-3">
                <div className="d-flex align-items-center gap-3">
                  <div className="destination-badge-icon">
                    <i className="bi bi-pin-map-fill"></i>
                  </div>
                  <div>
                    <span className="badge bg-primary-subtle text-primary border border-primary-subtle rounded-pill px-3 py-1 mb-1">
                      Selected From Plan My Journey
                    </span>
                    <h3 className="fw-bold mb-0 text-dark">{place}</h3>
                    <p className="text-muted small mb-0">
                      Travelling as: <strong className="text-dark">{travelWith}</strong>
                    </p>
                  </div>
                </div>

                <div className="d-flex align-items-center gap-2">
                  <button
                    type="button"
                    className="btn btn-sm btn-outline-secondary rounded-pill"
                    onClick={() => setShowChangePlace(true)}
                  >
                    <i className="bi bi-pencil-square me-1"></i> Change Place
                  </button>
                </div>
              </div>

              {/* Simplified Form: User only enters the Number of Days */}
              <div className="mt-4 pt-3 border-top">
                <form onSubmit={handleSubmit}>
                  <label className="form-label fw-bold d-flex align-items-center gap-2 mb-2">
                    <i className="bi bi-calendar-event text-primary"></i>
                    How many days will you stay in {place}?
                  </label>

                  {/* Quick Days Selector Chips */}
                  <div className="d-flex flex-wrap gap-2 mb-3">
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

                  <div className="row g-2 align-items-center">
                    <div className="col-sm-8 col-md-9">
                      <div className="input-group input-group-lg">
                        <span className="input-group-text bg-light border-end-0">
                          <i className="bi bi-clock-history"></i>
                        </span>
                        <input
                          type="number"
                          className="form-control border-start-0"
                          min="1"
                          max="30"
                          value={days}
                          onChange={(e) => setDays(e.target.value)}
                          placeholder="e.g. 3 (Enter number of days)"
                          required
                        />
                      </div>
                    </div>
                    <div className="col-sm-4 col-md-3">
                      <button
                        type="submit"
                        className="btn btn-warm btn-lg w-100 fw-semibold"
                        disabled={loading}
                      >
                        {loading ? (
                          <>
                            <span className="spinner-border spinner-border-sm me-2"></span>
                            Planning...
                          </>
                        ) : (
                          <>
                            <i className="bi bi-magic me-2"></i>
                            Generate Plan
                          </>
                        )}
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        ) : (
          /* Standard Full Form if user visits directly or wants to change place */
          <div className="card glass-card border-0 mb-4 shadow-sm">
            <div className="card-body p-4">
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <div className="d-flex justify-content-between align-items-center mb-1">
                    <label className="form-label fw-semibold mb-0">1) Enter Destination City / Place in India</label>
                    {isPrefilled && (
                      <button
                        type="button"
                        className="btn btn-sm btn-link text-decoration-none p-0"
                        onClick={() => setShowChangePlace(false)}
                      >
                        Cancel
                      </button>
                    )}
                  </div>
                  <input
                    type="text"
                    className="form-control form-control-lg"
                    value={place}
                    onChange={(e) => setPlace(e.target.value)}
                    placeholder="e.g. Manali, Goa, Jaipur, Madurai, Kerala, Varanasi, Ooty"
                    required
                  />
                </div>

                <OptionGroup
                  label="2) Who are you travelling with?"
                  options={TRAVEL_WITH}
                  value={travelWith}
                  onChange={setTravelWith}
                  name="ptv-travelWith"
                />

                <div className="mb-4">
                  <label className="form-label fw-semibold">3) How many days?</label>
                  <div className="d-flex flex-wrap gap-2 mb-2">
                    {QUICK_DAYS.map((d) => (
                      <button
                        key={d}
                        type="button"
                        className={`btn btn-sm rounded-pill px-3 fw-semibold ${
                          parseInt(days, 10) === d ? 'btn-primary' : 'btn-outline-secondary'
                        }`}
                        onClick={() => setDays(String(d))}
                      >
                        {d} {d === 1 ? 'Day' : 'Days'}
                      </button>
                    ))}
                  </div>
                  <input
                    type="number"
                    className="form-control form-control-lg"
                    min="1"
                    max="30"
                    value={days}
                    onChange={(e) => setDays(e.target.value)}
                    placeholder="e.g. 3"
                    required
                  />
                </div>

                {error && (
                  <div className="alert alert-danger py-2 small">
                    <i className="bi bi-exclamation-circle me-1"></i>
                    {error}
                  </div>
                )}

                <button type="submit" className="btn btn-warm btn-lg w-100 fw-semibold" disabled={loading}>
                  {loading ? (
                    <>
                      <span className="spinner-border spinner-border-sm me-2"></span>
                      Generating recommended itinerary...
                    </>
                  ) : (
                    <>
                      <i className="bi bi-calendar-check me-2"></i>
                      Recommend Places to Visit
                    </>
                  )}
                </button>
              </form>
            </div>
          </div>
        )}

        {/* Itinerary Results Section */}
        {result && (
          <div className="mb-4">
            {/* Itinerary Controls & Map Banner */}
            <div className="card glass-card border-0 mb-4 bg-light shadow-sm">
              <div className="card-body p-4 d-flex flex-wrap justify-content-between align-items-center gap-3">
                <div>
                  <div className="d-flex align-items-center gap-2 mb-1">
                    <span className="badge bg-success rounded-pill px-3 py-1">
                      <i className="bi bi-check2 me-1"></i> {result.itinerary?.length || days} Days Itinerary
                    </span>
                    {result.source === 'ai' && (
                      <span className="badge bg-info-subtle text-info border border-info-subtle rounded-pill">
                        <i className="bi bi-stars me-1"></i> TripNova AI
                      </span>
                    )}
                  </div>
                  <h3 className="fw-bold mb-1 text-dark">
                    Curated Travel Plan for {result.place || place}
                  </h3>
                  <p className="text-muted small mb-0">
                    {result.summary || `Top prioritized landmarks and attractions to visit within ${days} days.`}
                  </p>
                </div>

                <div className="d-flex align-items-center gap-2">
                  <button
                    type="button"
                    className="btn btn-primary d-flex align-items-center gap-2 rounded-pill px-4 shadow-sm"
                    onClick={() => setShowMapModal(true)}
                  >
                    <i className="bi bi-geo-alt-fill text-warning fs-5"></i>
                    <span className="fw-semibold">View On Map</span>
                  </button>
                  <button
                    type="button"
                    className="btn btn-outline-secondary rounded-pill px-3"
                    onClick={() => setShowInlineMap(!showInlineMap)}
                  >
                    <i className={`bi ${showInlineMap ? 'bi-chevron-up' : 'bi-map'} me-1`}></i>
                    {showInlineMap ? 'Hide Inline Map' : 'Toggle Inline Map'}
                  </button>
                </div>
              </div>
            </div>

            {/* Inline Interactive Map if toggled */}
            {showInlineMap && (
              <InteractiveMapModal
                place={result.place || place}
                lat={result.lat}
                lng={result.lng}
                itinerary={result.itinerary}
                isInline={true}
              />
            )}

            {/* Day-by-Day Itinerary Timeline */}
            <div className="row g-4 mb-4">
              <div className="col-lg-8">
                <div className="card glass-card border-0 shadow-sm p-4">
                  <h4 className="fw-bold mb-4 d-flex align-items-center gap-2">
                    <i className="bi bi-journal-text text-primary"></i>
                    Day-Wise Itinerary
                  </h4>

                  <div className="itinerary-timeline">
                    {result.itinerary?.map((dayItem) => (
                      <div key={dayItem.day} className="timeline-day-block mb-4 pb-3">
                        <div className="d-flex align-items-center justify-content-between mb-3">
                          <div className="d-flex align-items-center gap-2">
                            <span className="badge bg-dark rounded-pill px-3 py-2 fs-6">
                              Day {dayItem.day}
                            </span>
                            <h5 className="fw-bold mb-0 text-dark">
                              {dayItem.title || `Day ${dayItem.day} Sights`}
                            </h5>
                          </div>
                        </div>

                        <div className="row g-3">
                          {dayItem.places?.map((spot, idx) => (
                            <div className="col-12" key={idx}>
                              <div className="spot-card p-3 rounded-3 bg-white border shadow-sm">
                                <div className="d-flex flex-wrap justify-content-between align-items-start gap-2 mb-2">
                                  <div className="d-flex align-items-center gap-2">
                                    <span className="spot-number-badge">{idx + 1}</span>
                                    <h6 className="fw-bold mb-0 text-dark fs-6">{spot.name}</h6>
                                  </div>
                                  <div className="d-flex align-items-center gap-1">
                                    {spot.duration && (
                                      <span className="badge bg-light text-muted border rounded-pill">
                                        <i className="bi bi-clock me-1"></i> {spot.duration}
                                      </span>
                                    )}
                                    {spot.bestTime && (
                                      <span className="badge bg-warning-subtle text-dark border border-warning-subtle rounded-pill">
                                        <i className="bi bi-sun me-1"></i> {spot.bestTime}
                                      </span>
                                    )}
                                  </div>
                                </div>

                                <p className="text-muted small mb-2">{spot.highlight}</p>

                                <div className="d-flex align-items-center gap-2 pt-2 border-top">
                                  <button
                                    type="button"
                                    className="btn btn-sm btn-outline-primary rounded-pill px-2 py-1"
                                    onClick={() => setShowMapModal(true)}
                                  >
                                    <i className="bi bi-geo-alt me-1 text-danger"></i> Pin on Map
                                  </button>
                                  <a
                                    href={`https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(
                                      spot.name + ', ' + (result.place || place)
                                    )}`}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="btn btn-sm btn-outline-secondary rounded-pill px-2 py-1"
                                  >
                                    <i className="bi bi-arrow-up-right me-1"></i> Directions
                                  </a>
                                </div>
                              </div>
                            </div>
                          ))}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* Sidebar: Recommended Hotels & Transport Links */}
              <div className="col-lg-4">
                <div className="card glass-card border-0 shadow-sm p-4 mb-4">
                  <div className="d-flex justify-content-between align-items-center mb-3">
                    <h5 className="fw-bold mb-0">
                      <i className="bi bi-building text-info me-2"></i>
                      Top Hotels
                    </h5>
                    <Link to="/hotels" className="btn btn-sm btn-link text-decoration-none">
                      Search More ↗
                    </Link>
                  </div>

                  <div className="hotels-list">
                    {result.hotels?.map((h, i) => (
                      <div key={i} className="hotel-card p-3 mb-3 rounded-3 bg-white border shadow-sm">
                        <div className="d-flex justify-content-between align-items-start mb-1">
                          <h6 className="fw-bold mb-0 text-dark small">{h.name}</h6>
                          <span className="badge bg-warning text-dark small">{h.rating || '4.5★'}</span>
                        </div>
                        <div className="d-flex justify-content-between align-items-center mt-2">
                          <span className="badge bg-light text-muted border">{h.type}</span>
                          <span className="fw-bold text-success small">{h.price || 'Best Rates'}</span>
                        </div>
                        <Link
                          to={`/hotels?destination=${encodeURIComponent(result.place || place)}`}
                          className="btn btn-outline-primary btn-sm w-100 mt-2 rounded-pill"
                        >
                          Book Hotel In-App
                        </Link>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Quick In-App Transport Connect */}
                <div className="card glass-card border-0 shadow-sm p-4">
                  <h5 className="fw-bold mb-3">
                    <i className="bi bi-ticket-perforated text-warning me-2"></i>
                    Travel to {result.place?.split(',')[0] || place}
                  </h5>
                  <div className="d-grid gap-2">
                    <Link
                      to={`/bus-booking?to=${encodeURIComponent(result.place?.split(',')[0] || place)}`}
                      className="btn btn-outline-danger d-flex align-items-center justify-content-between p-2 rounded-3"
                    >
                      <div className="d-flex align-items-center gap-2">
                        <i className="bi bi-bus-front fs-5"></i>
                        <span>RedBus In-App Booking</span>
                      </div>
                      <i className="bi bi-arrow-right"></i>
                    </Link>
                    <Link
                      to={`/train-booking?to=${encodeURIComponent(result.place?.split(',')[0] || place)}`}
                      className="btn btn-outline-primary d-flex align-items-center justify-content-between p-2 rounded-3"
                    >
                      <div className="d-flex align-items-center gap-2">
                        <i className="bi bi-train-front fs-5"></i>
                        <span>IRCTC Train Booking</span>
                      </div>
                      <i className="bi bi-arrow-right"></i>
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Interactive Map Modal */}
        {showMapModal && (
          <InteractiveMapModal
            place={result?.place || place}
            lat={result?.lat}
            lng={result?.lng}
            itinerary={result?.itinerary}
            onClose={() => setShowMapModal(false)}
          />
        )}

        {/* AI Assistant Travel Co-Pilot */}
        <AIAssistant
          title="TripNova AI Co-Pilot"
          context={{ page: 'places-to-visit', place, travelWith, days }}
          placeholder={`Ask about ${place || 'your destination'}, local food specialties, best time to visit, or travel routes!`}
        />
      </main>
    </div>
  )
}
