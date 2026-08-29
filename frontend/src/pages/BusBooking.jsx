import { useState, useEffect } from 'react'
import { useSearchParams } from 'react-router-dom'
import Navbar from '../components/Navbar'

const POPULAR_CITIES = [
  'Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Hyderabad',
  'Jaipur', 'Manali', 'Goa', 'Madurai', 'Kochi', 'Varanasi', 'Ooty', 'Pune', 'Agra'
]

const SAMPLE_BUSES = [
  {
    id: 'RB-101',
    operator: 'RedBus Select - IntrCity SmartBus',
    type: 'AC Sleeper (2+1)',
    deptTime: '20:30',
    arrTime: '06:00',
    duration: '9h 30m',
    rating: 4.8,
    reviews: 1420,
    fare: 899,
    seatsAvailable: 14,
    boardingPoint: 'Main Terminal / Kashmiri Gate / Majestic',
    droppingPoint: 'City Center / Mall Road / Beach Junction',
    amenities: ['Live Tracking', 'Water Bottle', 'Charging Point', 'Blanket', 'Emergency SOS'],
  },
  {
    id: 'RB-102',
    operator: 'Zingbus Electric Multi-Axle',
    type: 'Volvo 9600 AC Semi-Sleeper (2+2)',
    deptTime: '21:15',
    arrTime: '06:45',
    duration: '9h 30m',
    rating: 4.7,
    reviews: 980,
    fare: 749,
    seatsAvailable: 22,
    boardingPoint: 'ISBT / Central Hub',
    droppingPoint: 'Main Bus Stand',
    amenities: ['Live Tracking', 'Reading Light', 'Charging Point', 'Free WiFi'],
  },
  {
    id: 'RB-103',
    operator: 'KSRTC / State Express Airavat Club Class',
    type: 'Multi-Axle Volvo AC Sleeper',
    deptTime: '22:00',
    arrTime: '07:30',
    duration: '9h 30m',
    rating: 4.9,
    reviews: 3200,
    fare: 1050,
    seatsAvailable: 8,
    boardingPoint: 'Central Govt Bus Stand',
    droppingPoint: 'City Bus Terminal',
    amenities: ['Government Certified', 'Punctual Guarantee', 'Blanket', 'Water Bottle'],
  },
  {
    id: 'RB-104',
    operator: 'VRL Travels Executive',
    type: 'Scania AC Diamond Class (2+1)',
    deptTime: '19:45',
    arrTime: '05:15',
    duration: '9h 30m',
    rating: 4.6,
    reviews: 840,
    fare: 820,
    seatsAvailable: 19,
    boardingPoint: 'VRL Hub Station',
    droppingPoint: 'Highway Bypass Junction',
    amenities: ['Charging Point', 'Movies / TV', 'Snacks'],
  },
  {
    id: 'RB-105',
    operator: 'Orange Tours & Travels',
    type: 'BharatBenz AC Sleeper (2+1)',
    deptTime: '22:30',
    arrTime: '08:00',
    duration: '9h 30m',
    rating: 4.7,
    reviews: 610,
    fare: 940,
    seatsAvailable: 11,
    boardingPoint: 'Express Way Toll Gate',
    droppingPoint: 'Central Station',
    amenities: ['Live Tracking', 'Pillow', 'Water Bottle', 'USB Port'],
  },
]

export default function BusBooking() {
  const [searchParams] = useSearchParams()
  const [fromCity, setFromCity] = useState('Delhi')
  const [toCity, setToCity] = useState('Manali')
  const [date, setDate] = useState(new Date().toISOString().split('T')[0])
  const [busType, setBusType] = useState('ALL')
  const [searched, setSearched] = useState(true)
  
  // Seat selection modal / state
  const [activeBus, setActiveBus] = useState(null)
  const [selectedSeats, setSelectedSeats] = useState([])
  const [bookingConfirmed, setBookingConfirmed] = useState(null)
  const [passengerName, setPassengerName] = useState('')
  const [passengerPhone, setPassengerPhone] = useState('')
  const [passengerAge, setPassengerAge] = useState('')

  useEffect(() => {
    const toParam = searchParams.get('to')
    const fromParam = searchParams.get('from')
    if (toParam) setToCity(toParam)
    if (fromParam) setFromCity(fromParam)
  }, [searchParams])

  const handleSearch = (e) => {
    e.preventDefault()
    setSearched(true)
    setActiveBus(null)
  }

  const handleSwapCities = () => {
    const temp = fromCity
    setFromCity(toCity)
    setToCity(temp)
  }

  const openSeatPicker = (bus) => {
    setActiveBus(bus)
    setSelectedSeats(['L3']) // default one seat
    setBookingConfirmed(null)
  }

  const toggleSeat = (seatId) => {
    if (selectedSeats.includes(seatId)) {
      setSelectedSeats(selectedSeats.filter((s) => s !== seatId))
    } else {
      if (selectedSeats.length >= 4) {
        alert('You can select a maximum of 4 seats per booking.')
        return
      }
      setSelectedSeats([...selectedSeats, seatId])
    }
  }

  const handleConfirmBooking = (e) => {
    e.preventDefault()
    if (!passengerName || !passengerPhone) {
      alert('Please fill passenger name and phone number.')
      return
    }
    const pnr = 'RB' + Math.floor(10000000 + Math.random() * 90000000)
    setBookingConfirmed({
      pnr,
      bus: activeBus,
      from: fromCity,
      to: toCity,
      date,
      seats: selectedSeats,
      totalFare: selectedSeats.length * activeBus.fare,
      passenger: { name: passengerName, phone: passengerPhone, age: passengerAge || '28' },
    })
  }

  // Filter buses based on busType
  const filteredBuses = SAMPLE_BUSES.filter((b) => {
    if (busType === 'ALL') return true
    if (busType === 'AC_SLEEPER') return b.type.includes('Sleeper')
    if (busType === 'VOLVO') return b.type.includes('Volvo') || b.type.includes('Scania')
    return true
  })

  return (
    <div className="page-bg">
      <Navbar />
      <main className="container py-4">
        {/* Header with RedBus Integration Banner */}
        <div className="card glass-card border-0 mb-4 bg-gradient-redbus text-white overflow-hidden shadow-lg">
          <div className="card-body p-4 position-relative">
            <div className="d-flex flex-wrap justify-content-between align-items-center gap-3">
              <div>
                <div className="d-flex align-items-center gap-2 mb-2">
                  <span className="badge bg-white text-danger px-3 py-1 fw-bold rounded-pill">
                    <i className="bi bi-bus-front-fill me-1"></i> redBus API In-App Engine
                  </span>
                  <span className="badge bg-black bg-opacity-25 rounded-pill px-3 py-1">
                    TripNova Transport Hub
                  </span>
                </div>
                <h1 className="fw-bold mb-1 display-6">Bus Ticket Booking</h1>
                <p className="lead mb-0 opacity-90 fs-6">
                  Book 3500+ bus operators across India inside TripNova without external redirection.
                </p>
              </div>

              <div className="d-flex align-items-center gap-2">
                <div className="text-end d-none d-md-block">
                  <div className="badge bg-warning text-dark px-3 py-2 rounded-3 fw-bold">
                    <i className="bi bi-shield-check me-1"></i> Instant Live Seat Confirmation
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Bus Search Form */}
        <div className="card glass-card border-0 mb-4 shadow-sm">
          <div className="card-body p-4">
            <form onSubmit={handleSearch}>
              <div className="row g-3 align-items-end">
                <div className="col-md-3 col-sm-6">
                  <label className="form-label fw-bold small text-uppercase text-muted">
                    <i className="bi bi-geo-alt text-danger me-1"></i> From City
                  </label>
                  <input
                    type="text"
                    className="form-control form-control-lg fw-semibold"
                    list="fromCitiesList"
                    value={fromCity}
                    onChange={(e) => setFromCity(e.target.value)}
                    placeholder="e.g. Delhi"
                    required
                  />
                  <datalist id="fromCitiesList">
                    {POPULAR_CITIES.map((c) => (
                      <option key={c} value={c} />
                    ))}
                  </datalist>
                </div>

                <div className="col-auto d-none d-md-flex align-items-center justify-content-center pb-2">
                  <button
                    type="button"
                    className="btn btn-light rounded-circle shadow-sm p-2 border"
                    onClick={handleSwapCities}
                    title="Swap Cities"
                  >
                    <i className="bi bi-arrow-left-right text-primary"></i>
                  </button>
                </div>

                <div className="col-md-3 col-sm-6">
                  <label className="form-label fw-bold small text-uppercase text-muted">
                    <i className="bi bi-pin-map-fill text-success me-1"></i> Destination
                  </label>
                  <input
                    type="text"
                    className="form-control form-control-lg fw-semibold"
                    list="toCitiesList"
                    value={toCity}
                    onChange={(e) => setToCity(e.target.value)}
                    placeholder="e.g. Manali, Goa, Jaipur"
                    required
                  />
                  <datalist id="toCitiesList">
                    {POPULAR_CITIES.map((c) => (
                      <option key={c} value={c} />
                    ))}
                  </datalist>
                </div>

                <div className="col-md-3 col-sm-6">
                  <label className="form-label fw-bold small text-uppercase text-muted">
                    <i className="bi bi-calendar3 text-primary me-1"></i> Date of Journey
                  </label>
                  <input
                    type="date"
                    className="form-control form-control-lg"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    required
                  />
                </div>

                <div className="col-md-2 col-sm-6">
                  <button type="submit" className="btn btn-danger btn-lg w-100 fw-bold shadow-sm">
                    <i className="bi bi-search me-1"></i> Search
                  </button>
                </div>
              </div>

              {/* Filters */}
              <div className="d-flex flex-wrap align-items-center gap-2 mt-3 pt-3 border-top">
                <span className="small fw-bold text-muted me-2">Bus Type:</span>
                {[
                  { id: 'ALL', label: 'All Buses' },
                  { id: 'AC_SLEEPER', label: 'AC Sleeper' },
                  { id: 'VOLVO', label: 'Volvo / Scania Luxury' },
                ].map((t) => (
                  <button
                    key={t.id}
                    type="button"
                    className={`btn btn-sm rounded-pill px-3 fw-semibold ${
                      busType === t.id ? 'btn-dark' : 'btn-outline-secondary'
                    }`}
                    onClick={() => setBusType(t.id)}
                  >
                    {t.label}
                  </button>
                ))}
              </div>
            </form>
          </div>
        </div>

        {/* Bus Search Results */}
        {searched && (
          <div className="mb-4">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <h5 className="fw-bold mb-0">
                <i className="bi bi-bus-front text-danger me-2"></i>
                Buses from {fromCity} to {toCity} on {date}
                <span className="badge bg-light text-dark ms-2 border">
                  {filteredBuses.length} buses found
                </span>
              </h5>
            </div>

            <div className="row g-3">
              {filteredBuses.map((bus) => (
                <div className="col-12" key={bus.id}>
                  <div className="card glass-card border-0 shadow-sm p-4 hover-lift">
                    <div className="row align-items-center g-3">
                      {/* Operator Info */}
                      <div className="col-lg-4 col-md-5">
                        <div className="d-flex align-items-center gap-2 mb-1">
                          <h5 className="fw-bold text-dark mb-0">{bus.operator}</h5>
                          <span className="badge bg-success rounded-pill px-2 py-1 small">
                            ★ {bus.rating}
                          </span>
                        </div>
                        <p className="text-muted small mb-2">{bus.type}</p>
                        <div className="d-flex flex-wrap gap-1">
                          {bus.amenities.slice(0, 3).map((a, i) => (
                            <span key={i} className="badge bg-light text-muted border" style={{ fontSize: '10px' }}>
                              ✓ {a}
                            </span>
                          ))}
                        </div>
                      </div>

                      {/* Schedule */}
                      <div className="col-lg-4 col-md-4">
                        <div className="d-flex align-items-center justify-content-between text-center">
                          <div>
                            <div className="fs-5 fw-bold text-dark">{bus.deptTime}</div>
                            <div className="text-muted small">{fromCity}</div>
                          </div>
                          <div className="px-2">
                            <span className="badge bg-light text-muted border mb-1">{bus.duration}</span>
                            <div style={{ height: '2px', background: '#cbd5e1', width: '60px' }}></div>
                          </div>
                          <div>
                            <div className="fs-5 fw-bold text-dark">{bus.arrTime}</div>
                            <div className="text-muted small">{toCity}</div>
                          </div>
                        </div>
                      </div>

                      {/* Pricing & Booking Action */}
                      <div className="col-lg-4 col-md-3 text-lg-end text-md-end">
                        <div className="mb-2">
                          <span className="text-muted small">Starts from </span>
                          <span className="fs-4 fw-bold text-danger">₹{bus.fare}</span>
                        </div>
                        <div className="small text-success mb-2 fw-semibold">
                          <i className="bi bi-people-fill me-1"></i>
                          {bus.seatsAvailable} seats left
                        </div>
                        <button
                          type="button"
                          className="btn btn-danger rounded-pill px-4 fw-bold shadow-sm"
                          onClick={() => openSeatPicker(bus)}
                        >
                          Select Seats & Book
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Seat Picker & In-App Booking Modal */}
        {activeBus && (
          <div
            className="modal d-block"
            tabIndex="-1"
            style={{ backgroundColor: 'rgba(0,0,0,0.65)', zIndex: 1055, backdropFilter: 'blur(3px)' }}
          >
            <div className="modal-dialog modal-lg modal-dialog-centered">
              <div className="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
                <div className="modal-header bg-danger text-white">
                  <div>
                    <h5 className="modal-title fw-bold">
                      <i className="bi bi-bus-front-fill me-2"></i>
                      {activeBus.operator} — In-App Seat Selection
                    </h5>
                    <p className="small mb-0 opacity-90">
                      {fromCity} ➔ {toCity} | {date} | {activeBus.type}
                    </p>
                  </div>
                  <button
                    type="button"
                    className="btn-close btn-close-white"
                    onClick={() => setActiveBus(null)}
                    aria-label="Close"
                  ></button>
                </div>

                {!bookingConfirmed ? (
                  <div className="modal-body p-4">
                    <div className="row g-4">
                      {/* Left: Interactive Bus Layout */}
                      <div className="col-md-6 border-end">
                        <h6 className="fw-bold mb-3 text-center">
                          <i className="bi bi-grid-3x3-gap-fill text-danger me-1"></i>
                          Lower & Upper Deck Layout
                        </h6>

                        <div className="bus-chassis p-3 bg-light rounded-4 border mx-auto" style={{ maxWidth: '280px' }}>
                          <div className="d-flex justify-content-between align-items-center mb-3 pb-2 border-bottom">
                            <span className="small fw-bold text-muted">Driver Front</span>
                            <span className="badge bg-secondary">🚪 Door</span>
                          </div>

                          <div className="row g-2 mb-2">
                            {['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'U1', 'U2', 'U3', 'U4', 'U5', 'U6'].map((seat) => {
                              const isSelected = selectedSeats.includes(seat)
                              const isBooked = ['L2', 'U4'].includes(seat)

                              return (
                                <div className="col-4" key={seat}>
                                  <button
                                    type="button"
                                    disabled={isBooked}
                                    onClick={() => toggleSeat(seat)}
                                    className={`btn btn-sm w-100 p-2 text-center rounded-3 fw-bold transition-all ${
                                      isBooked
                                        ? 'btn-secondary opacity-50'
                                        : isSelected
                                        ? 'btn-danger shadow-sm'
                                        : 'btn-outline-dark bg-white'
                                    }`}
                                  >
                                    <div style={{ fontSize: '11px' }}>{seat}</div>
                                    <div style={{ fontSize: '9px' }}>{isBooked ? 'Sold' : `₹${activeBus.fare}`}</div>
                                  </button>
                                </div>
                              )
                            })}
                          </div>

                          <div className="d-flex justify-content-around mt-3 pt-2 border-top small text-muted">
                            <div><span className="badge bg-white text-dark border me-1">□</span> Available</div>
                            <div><span className="badge bg-danger me-1">✓</span> Selected</div>
                            <div><span className="badge bg-secondary me-1">✕</span> Booked</div>
                          </div>
                        </div>
                      </div>

                      {/* Right: Passenger Form & Fare Summary */}
                      <div className="col-md-6">
                        <h6 className="fw-bold mb-3">
                          <i className="bi bi-person-lines-fill text-primary me-1"></i>
                          Passenger & Contact Details
                        </h6>

                        <form onSubmit={handleConfirmBooking}>
                          <div className="mb-3">
                            <label className="form-label small fw-bold">Primary Passenger Name</label>
                            <input
                              type="text"
                              className="form-control"
                              value={passengerName}
                              onChange={(e) => setPassengerName(e.target.value)}
                              placeholder="e.g. Rahul Sharma"
                              required
                            />
                          </div>

                          <div className="row g-2 mb-3">
                            <div className="col-8">
                              <label className="form-label small fw-bold">Mobile Number</label>
                              <input
                                type="tel"
                                className="form-control"
                                value={passengerPhone}
                                onChange={(e) => setPassengerPhone(e.target.value)}
                                placeholder="10-digit mobile"
                                required
                              />
                            </div>
                            <div className="col-4">
                              <label className="form-label small fw-bold">Age</label>
                              <input
                                type="number"
                                className="form-control"
                                value={passengerAge}
                                onChange={(e) => setPassengerAge(e.target.value)}
                                placeholder="Age"
                                min="5"
                                max="100"
                              />
                            </div>
                          </div>

                          {/* Price Summary Card */}
                          <div className="card bg-light border-0 p-3 rounded-3 mb-3">
                            <div className="d-flex justify-content-between small mb-1">
                              <span>Selected Seats ({selectedSeats.length}):</span>
                              <strong className="text-danger">{selectedSeats.join(', ') || 'None'}</strong>
                            </div>
                            <div className="d-flex justify-content-between small mb-1">
                              <span>Fare per seat:</span>
                              <span>₹{activeBus.fare}</span>
                            </div>
                            <div className="d-flex justify-content-between fw-bold fs-6 border-top pt-2 mt-1">
                              <span>Total Amount:</span>
                              <span className="text-danger">₹{selectedSeats.length * activeBus.fare}</span>
                            </div>
                          </div>

                          <button
                            type="submit"
                            className="btn btn-danger btn-lg w-100 fw-bold shadow-sm"
                            disabled={selectedSeats.length === 0}
                          >
                            <i className="bi bi-check-circle me-1"></i>
                            Confirm & Issue Ticket (In-App)
                          </button>
                        </form>
                      </div>
                    </div>
                  </div>
                ) : (
                  /* Booking Confirmation E-Ticket */
                  <div className="modal-body p-4 text-center">
                    <div className="alert alert-success d-inline-block rounded-circle p-3 mb-3 shadow-sm">
                      <i className="bi bi-check-lg display-5 text-success"></i>
                    </div>
                    <h4 className="fw-bold text-success mb-1">Booking Confirmed!</h4>
                    <p className="text-muted small mb-3">Your e-ticket has been generated via RedBus In-App Engine.</p>

                    <div className="card border-2 border-success bg-light text-start p-3 rounded-4 mx-auto mb-3" style={{ maxWidth: '420px' }}>
                      <div className="d-flex justify-content-between border-bottom pb-2 mb-2">
                        <div>
                          <span className="badge bg-danger">redBus e-Ticket</span>
                          <h6 className="fw-bold mb-0 mt-1">{bookingConfirmed.bus.operator}</h6>
                        </div>
                        <div className="text-end">
                          <span className="small text-muted">PNR:</span>
                          <strong className="d-block text-dark">{bookingConfirmed.pnr}</strong>
                        </div>
                      </div>

                      <div className="row g-2 small mb-2">
                        <div className="col-6">
                          <span className="text-muted">From: </span>
                          <strong>{bookingConfirmed.from}</strong>
                        </div>
                        <div className="col-6">
                          <span className="text-muted">To: </span>
                          <strong>{bookingConfirmed.to}</strong>
                        </div>
                        <div className="col-6">
                          <span className="text-muted">Date: </span>
                          <strong>{bookingConfirmed.date}</strong>
                        </div>
                        <div className="col-6">
                          <span className="text-muted">Seats: </span>
                          <strong className="text-danger">{bookingConfirmed.seats.join(', ')}</strong>
                        </div>
                      </div>

                      <div className="border-top pt-2 d-flex justify-content-between align-items-center">
                        <span className="small text-muted">Passenger: {bookingConfirmed.passenger.name}</span>
                        <span className="fw-bold text-success fs-6">Paid: ₹{bookingConfirmed.totalFare}</span>
                      </div>
                    </div>

                    <button
                      type="button"
                      className="btn btn-outline-dark rounded-pill px-4"
                      onClick={() => setActiveBus(null)}
                    >
                      Done & Close
                    </button>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  )
}
