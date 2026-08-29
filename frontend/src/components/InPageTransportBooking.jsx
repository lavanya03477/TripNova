import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

const DEPARTURE_CITIES = ['Chennai', 'Bangalore', 'Madurai', 'Coimbatore', 'Delhi', 'Mumbai', 'Hyderabad', 'Kochi']

const SAMPLE_BUSES = [
  {
    id: 'RB-201',
    operator: 'RedBus Select - IntrCity SmartBus',
    type: 'AC Sleeper (2+1)',
    deptTime: '21:00',
    arrTime: '06:30',
    duration: '9h 30m',
    rating: 4.8,
    fare: 849,
    seatsAvailable: 12,
    amenities: ['Live Tracking', 'Water Bottle', 'Charging Point', 'Blanket'],
  },
  {
    id: 'RB-202',
    operator: 'Zingbus Electric Multi-Axle',
    type: 'Volvo AC Semi-Sleeper (2+2)',
    deptTime: '22:15',
    arrTime: '07:45',
    duration: '9h 30m',
    rating: 4.7,
    fare: 699,
    seatsAvailable: 18,
    amenities: ['Live Tracking', 'Reading Light', 'Charging Point', 'Free WiFi'],
  },
  {
    id: 'RB-203',
    operator: 'KSRTC / SETC Airavat Club Class',
    type: 'Multi-Axle Volvo AC Sleeper',
    deptTime: '20:30',
    arrTime: '05:45',
    duration: '9h 15m',
    rating: 4.9,
    fare: 990,
    seatsAvailable: 8,
    amenities: ['Government Certified', 'Punctual Guarantee', 'Blanket'],
  },
]

const SAMPLE_TRAINS = [
  {
    trainNumber: '20641',
    name: 'Vande Bharat Express',
    type: 'Superfast Express',
    deptTime: '06:00',
    arrTime: '13:50',
    duration: '7h 50m',
    runsOn: 'Mon, Tue, Wed, Thu, Fri, Sat',
    classes: [
      { code: 'CC', name: 'AC Chair Car', fare: 1240, status: 'AVAILABLE - 42' },
      { code: 'EC', name: 'Exec Chair Car', fare: 2360, status: 'AVAILABLE - 16' },
    ],
  },
  {
    trainNumber: '12633',
    name: 'Superfast Mail Express',
    type: 'Superfast',
    deptTime: '19:45',
    arrTime: '06:20',
    duration: '10h 35m',
    runsOn: 'Daily',
    classes: [
      { code: '3A', name: '3rd AC Economy', fare: 890, status: 'AVAILABLE - 28' },
      { code: '2A', name: '2nd AC Sleeper', fare: 1280, status: 'AVAILABLE - 12' },
      { code: '1A', name: '1st AC Coupe', fare: 2150, status: 'AVAILABLE - 4' },
      { code: 'SL', name: 'Sleeper Class', fare: 340, status: 'RAC 08' },
    ],
  },
]

export default function InPageTransportBooking({ destination }) {
  const cleanDest = (destination || 'Destination').split(',')[0].trim()
  const [activeMode, setActiveMode] = useState('bus') // 'bus' or 'train'
  const [fromCity, setFromCity] = useState('Chennai')
  const [journeyDate, setJourneyDate] = useState(
    new Date(Date.now() + 86400000).toISOString().split('T')[0]
  )
  
  // Bus Seat Booking State
  const [selectedBus, setSelectedBus] = useState(null)
  const [selectedSeats, setSelectedSeats] = useState([])
  const [busBookedTicket, setBusBookedTicket] = useState(null)

  // Train Booking State
  const [selectedTrain, setSelectedTrain] = useState(null)
  const [selectedClass, setSelectedClass] = useState(null)
  const [trainBookedTicket, setTrainBookedTicket] = useState(null)

  // Passenger state
  const [passengerName, setPassengerName] = useState('Lavanya')
  const [passengerAge, setPassengerAge] = useState('24')
  const [passengerGender, setPassengerGender] = useState('Female')

  useEffect(() => {
    // Reset selections when destination changes
    setSelectedBus(null)
    setSelectedSeats([])
    setBusBookedTicket(null)
    setSelectedTrain(null)
    setSelectedClass(null)
    setTrainBookedTicket(null)
  }, [destination])

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

  const handleConfirmBusBooking = (e) => {
    e.preventDefault()
    if (selectedSeats.length === 0) {
      alert('Please select at least 1 seat on the bus layout.')
      return
    }
    const ticket = {
      pnr: `RB${Math.floor(100000000 + Math.random() * 900000000)}`,
      bus: selectedBus,
      from: fromCity,
      to: cleanDest,
      date: journeyDate,
      seats: selectedSeats,
      passenger: { name: passengerName, age: passengerAge, gender: passengerGender },
      totalFare: selectedSeats.length * selectedBus.fare,
      bookedAt: new Date().toLocaleString(),
    }
    setBusBookedTicket(ticket)
  }

  const handleConfirmTrainBooking = (e) => {
    e.preventDefault()
    if (!selectedTrain || !selectedClass) {
      alert('Please select a train and class.')
      return
    }
    const ticket = {
      pnr: `${Math.floor(1000000000 + Math.random() * 9000000000)}`,
      train: selectedTrain,
      selectedClass,
      from: fromCity,
      to: cleanDest,
      date: journeyDate,
      coach: `${selectedClass.code}1`,
      berth: `${Math.floor(12 + Math.random() * 40)} (Lower)`,
      passenger: { name: passengerName, age: passengerAge, gender: passengerGender },
      totalFare: selectedClass.fare,
      bookedAt: new Date().toLocaleString(),
    }
    setTrainBookedTicket(ticket)
  }

  return (
    <div className="card glass-card border-0 mb-4 shadow-sm overflow-hidden" id="inpage-transport-section">
      {/* Header Banner */}
      <div className="card-header bg-gradient-destination py-3 border-0">
        <div className="d-flex flex-wrap justify-content-between align-items-center gap-3">
          <div>
            <span className="badge bg-danger rounded-pill px-3 py-1 fw-bold mb-1">
              🚀 In-Page Booking
            </span>
            <h4 className="fw-bold mb-0 text-dark">
              Book Transport to {cleanDest}
            </h4>
            <p className="text-muted small mb-0">
              Instant RedBus bus seats & IRCTC train tickets directly for this destination.
            </p>
          </div>

          {/* Mode Switcher Tabs */}
          <div className="btn-group bg-white p-1 rounded-pill shadow-sm">
            <button
              type="button"
              className={`btn btn-sm rounded-pill px-3 fw-bold ${
                activeMode === 'bus' ? 'btn-danger text-white' : 'btn-light text-dark'
              }`}
              onClick={() => setActiveMode('bus')}
            >
              <i className="bi bi-bus-front-fill me-1"></i>
              RedBus (Bus)
            </button>
            <button
              type="button"
              className={`btn btn-sm rounded-pill px-3 fw-bold ${
                activeMode === 'train' ? 'btn-primary text-white' : 'btn-light text-dark'
              }`}
              onClick={() => setActiveMode('train')}
            >
              <i className="bi bi-train-front-fill me-1"></i>
              IRCTC (Train)
            </button>
          </div>
        </div>
      </div>

      <div className="card-body p-4">
        {/* Route Selector Bar */}
        <div className="bg-light p-3 rounded-3 mb-4 border">
          <div className="row g-2 align-items-center">
            {/* From City */}
            <div className="col-sm-6 col-md-4">
              <label className="form-label small fw-bold mb-1 text-muted">From City</label>
              <div className="input-group">
                <span className="input-group-text bg-white">
                  <i className="bi bi-geo-alt text-danger"></i>
                </span>
                <input
                  type="text"
                  className="form-control fw-bold"
                  value={fromCity}
                  onChange={(e) => setFromCity(e.target.value)}
                  placeholder="Departure city (e.g. Chennai)"
                />
              </div>
            </div>

            {/* To City (Pre-filled with Destination) */}
            <div className="col-sm-6 col-md-4">
              <label className="form-label small fw-bold mb-1 text-muted">Destination (Pre-filled)</label>
              <div className="input-group">
                <span className="input-group-text bg-white">
                  <i className="bi bi-flag-fill text-success"></i>
                </span>
                <input
                  type="text"
                  className="form-control fw-bold bg-white"
                  value={cleanDest}
                  readOnly
                />
              </div>
            </div>

            {/* Date */}
            <div className="col-sm-12 col-md-4">
              <label className="form-label small fw-bold mb-1 text-muted">Journey Date</label>
              <input
                type="date"
                className="form-control"
                value={journeyDate}
                onChange={(e) => setJourneyDate(e.target.value)}
              />
            </div>
          </div>

          {/* Quick Departure City Chips */}
          <div className="d-flex flex-wrap align-items-center gap-1 mt-2 pt-2 border-top">
            <span className="text-muted small me-1">Popular Origins:</span>
            {DEPARTURE_CITIES.map((c) => (
              <button
                key={c}
                type="button"
                className={`btn btn-sm rounded-pill py-0 px-2 small ${
                  fromCity.toLowerCase() === c.toLowerCase() ? 'btn-dark text-white' : 'btn-white border'
                }`}
                onClick={() => setFromCity(c)}
              >
                {c}
              </button>
            ))}
          </div>
        </div>

        {/* ================= BUS BOOKING MODE ================= */}
        {activeMode === 'bus' && (
          <div>
            {!busBookedTicket ? (
              <div>
                <div className="d-flex justify-content-between align-items-center mb-3">
                  <h6 className="fw-bold mb-0">
                    <i className="bi bi-bus-front text-danger me-1"></i>
                    Available RedBus Services ({fromCity} ➔ {cleanDest})
                  </h6>
                  <Link to={`/bus-booking?from=${encodeURIComponent(fromCity)}&to=${encodeURIComponent(cleanDest)}`} className="text-decoration-none small fw-bold text-danger">
                    Full RedBus Engine <i className="bi bi-arrow-up-right"></i>
                  </Link>
                </div>

                <div className="d-flex flex-column gap-3 mb-3">
                  {SAMPLE_BUSES.map((b) => (
                    <div key={b.id} className={`card border rounded-3 p-3 transition-all ${selectedBus?.id === b.id ? 'border-danger bg-danger-subtle' : 'bg-white'}`}>
                      <div className="d-flex flex-wrap justify-content-between align-items-center gap-2">
                        <div>
                          <div className="d-flex align-items-center gap-2 mb-1">
                            <h6 className="fw-bold mb-0 text-dark">{b.operator}</h6>
                            <span className="badge bg-success text-white small">{b.rating}★</span>
                          </div>
                          <p className="text-muted small mb-0">{b.type}</p>
                          <p className="small text-dark mb-0 mt-1">
                            <strong>{b.deptTime}</strong> ({fromCity}) ➔ <strong>{b.arrTime}</strong> ({cleanDest}) · <span className="text-muted">{b.duration}</span>
                          </p>
                        </div>

                        <div className="text-end">
                          <h4 className="fw-bold text-danger mb-0">₹{b.fare}</h4>
                          <span className="badge bg-light text-success border small mb-2 d-inline-block">
                            {b.seatsAvailable} Seats Left
                          </span>
                          <div>
                            <button
                              type="button"
                              className={`btn btn-sm rounded-pill px-3 fw-bold ${selectedBus?.id === b.id ? 'btn-danger text-white' : 'btn-outline-danger'}`}
                              onClick={() => {
                                setSelectedBus(b)
                                setSelectedSeats(['L4']) // Auto select 1 seat
                              }}
                            >
                              {selectedBus?.id === b.id ? '✓ Selected' : 'Select Seat'}
                            </button>
                          </div>
                        </div>
                      </div>

                      {/* In-Card Seat Selector & Booking Form */}
                      {selectedBus?.id === b.id && (
                        <div className="mt-3 pt-3 border-top bg-white p-3 rounded-3">
                          <h6 className="fw-bold text-dark mb-2">
                            💺 Pick Seat(s) for {selectedBus.operator}
                          </h6>
                          <div className="d-flex flex-wrap gap-2 mb-3">
                            {['L1 (W)', 'L2', 'L3', 'L4 (W)', 'L5', 'U1 (W)', 'U2', 'U3 (W)'].map((seat) => (
                              <button
                                key={seat}
                                type="button"
                                className={`btn btn-sm rounded-pill px-3 fw-bold ${
                                  selectedSeats.includes(seat) ? 'btn-danger text-white' : 'btn-outline-secondary'
                                }`}
                                onClick={() => toggleSeat(seat)}
                              >
                                {seat}
                              </button>
                            ))}
                          </div>

                          <form onSubmit={handleConfirmBusBooking} className="row g-2 align-items-center">
                            <div className="col-sm-5">
                              <input
                                type="text"
                                className="form-control form-control-sm"
                                placeholder="Passenger Name"
                                value={passengerName}
                                onChange={(e) => setPassengerName(e.target.value)}
                                required
                              />
                            </div>
                            <div className="col-sm-3">
                              <input
                                type="number"
                                className="form-control form-control-sm"
                                placeholder="Age"
                                value={passengerAge}
                                onChange={(e) => setPassengerAge(e.target.value)}
                                required
                              />
                            </div>
                            <div className="col-sm-4">
                              <button type="submit" className="btn btn-danger btn-sm w-100 rounded-pill fw-bold">
                                Confirm & Pay ₹{selectedSeats.length * selectedBus.fare}
                              </button>
                            </div>
                          </form>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            ) : (
              /* Bus Ticket Confirmation Voucher */
              <div className="alert alert-success border-2 p-4 rounded-3 shadow-sm">
                <div className="d-flex justify-content-between align-items-start mb-3">
                  <div>
                    <span className="badge bg-success px-3 py-1 rounded-pill mb-1">
                      ✓ Bus Ticket Confirmed
                    </span>
                    <h5 className="fw-bold text-dark mb-0">
                      {busBookedTicket.bus.operator}
                    </h5>
                    <p className="text-muted small mb-0">
                      PNR: <strong className="text-dark">{busBookedTicket.pnr}</strong> · Booked on {busBookedTicket.bookedAt}
                    </p>
                  </div>
                  <button
                    type="button"
                    className="btn btn-sm btn-outline-secondary rounded-pill"
                    onClick={() => {
                      setBusBookedTicket(null)
                      setSelectedBus(null)
                    }}
                  >
                    Book Another Bus
                  </button>
                </div>

                <div className="row g-2 bg-white p-3 rounded-3 border mb-3">
                  <div className="col-6 col-md-3">
                    <span className="text-muted small">Route:</span>
                    <p className="fw-bold mb-0">{busBookedTicket.from} ➔ {busBookedTicket.to}</p>
                  </div>
                  <div className="col-6 col-md-3">
                    <span className="text-muted small">Date:</span>
                    <p className="fw-bold mb-0">{busBookedTicket.date}</p>
                  </div>
                  <div className="col-6 col-md-3">
                    <span className="text-muted small">Seats:</span>
                    <p className="fw-bold mb-0 text-danger">{busBookedTicket.seats.join(', ')}</p>
                  </div>
                  <div className="col-6 col-md-3">
                    <span className="text-muted small">Total Paid:</span>
                    <p className="fw-bold mb-0 text-success">₹{busBookedTicket.totalFare}</p>
                  </div>
                </div>

                <div className="d-flex gap-2">
                  <button type="button" className="btn btn-sm btn-success rounded-pill px-3" onClick={() => window.print()}>
                    <i className="bi bi-printer me-1"></i> Print / Save Ticket
                  </button>
                </div>
              </div>
            )}
          </div>
        )}

        {/* ================= TRAIN BOOKING MODE ================= */}
        {activeMode === 'train' && (
          <div>
            {!trainBookedTicket ? (
              <div>
                <div className="d-flex justify-content-between align-items-center mb-3">
                  <h6 className="fw-bold mb-0">
                    <i className="bi bi-train-front text-primary me-1"></i>
                    Available IRCTC Trains ({fromCity} ➔ {cleanDest})
                  </h6>
                  <Link to={`/train-booking?from=${encodeURIComponent(fromCity)}&to=${encodeURIComponent(cleanDest)}`} className="text-decoration-none small fw-bold text-primary">
                    Full IRCTC Engine <i className="bi bi-arrow-up-right"></i>
                  </Link>
                </div>

                <div className="d-flex flex-column gap-3 mb-3">
                  {SAMPLE_TRAINS.map((t) => (
                    <div key={t.trainNumber} className="card border rounded-3 p-3 bg-white">
                      <div className="d-flex flex-wrap justify-content-between align-items-start gap-2 mb-2">
                        <div>
                          <div className="d-flex align-items-center gap-2">
                            <span className="badge bg-primary-subtle text-primary border rounded-pill">
                              #{t.trainNumber}
                            </span>
                            <h6 className="fw-bold mb-0 text-dark">{t.name}</h6>
                          </div>
                          <p className="small text-muted mb-0">
                            Runs: {t.runsOn} · Duration: {t.duration}
                          </p>
                          <p className="small text-dark mb-0 mt-1">
                            <strong>{t.deptTime}</strong> ({fromCity}) ➔ <strong>{t.arrTime}</strong> ({cleanDest})
                          </p>
                        </div>
                      </div>

                      {/* Train Class Chips with Fares & Status */}
                      <div className="d-flex flex-wrap gap-2 mt-2 pt-2 border-top">
                        {t.classes.map((c) => {
                          const isSelected = selectedTrain?.trainNumber === t.trainNumber && selectedClass?.code === c.code
                          return (
                            <button
                              key={c.code}
                              type="button"
                              className={`btn btn-sm rounded-3 text-start p-2 border ${
                                isSelected ? 'btn-primary text-white border-primary' : 'btn-light'
                              }`}
                              onClick={() => {
                                setSelectedTrain(t)
                                setSelectedClass(c)
                              }}
                            >
                              <div className="d-flex justify-content-between align-items-center gap-2">
                                <strong className="small">{c.code}</strong>
                                <span className={isSelected ? 'text-white' : 'text-success fw-bold'}>₹{c.fare}</span>
                              </div>
                              <div className="small opacity-75">{c.status}</div>
                            </button>
                          )
                        })}
                      </div>

                      {/* In-Card Train Booking Form */}
                      {selectedTrain?.trainNumber === t.trainNumber && selectedClass && (
                        <div className="mt-3 pt-3 border-top bg-light p-3 rounded-3">
                          <h6 className="fw-bold text-dark mb-2">
                            🚂 Confirm Booking for {selectedTrain.name} ({selectedClass.name} - ₹{selectedClass.fare})
                          </h6>
                          <form onSubmit={handleConfirmTrainBooking} className="row g-2 align-items-center">
                            <div className="col-sm-5">
                              <input
                                type="text"
                                className="form-control form-control-sm"
                                placeholder="Passenger Name"
                                value={passengerName}
                                onChange={(e) => setPassengerName(e.target.value)}
                                required
                              />
                            </div>
                            <div className="col-sm-3">
                              <input
                                type="number"
                                className="form-control form-control-sm"
                                placeholder="Age"
                                value={passengerAge}
                                onChange={(e) => setPassengerAge(e.target.value)}
                                required
                              />
                            </div>
                            <div className="col-sm-4">
                              <button type="submit" className="btn btn-primary btn-sm w-100 rounded-pill fw-bold">
                                Book Ticket (₹{selectedClass.fare})
                              </button>
                            </div>
                          </form>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            ) : (
              /* Train Ticket Confirmation Voucher */
              <div className="alert alert-primary border-2 p-4 rounded-3 shadow-sm">
                <div className="d-flex justify-content-between align-items-start mb-3">
                  <div>
                    <span className="badge bg-primary px-3 py-1 rounded-pill mb-1">
                      ✓ IRCTC Train Confirmed
                    </span>
                    <h5 className="fw-bold text-dark mb-0">
                      {trainBookedTicket.train.name} (#{trainBookedTicket.train.trainNumber})
                    </h5>
                    <p className="text-muted small mb-0">
                      PNR: <strong className="text-dark">{trainBookedTicket.pnr}</strong> · Booked on {trainBookedTicket.bookedAt}
                    </p>
                  </div>
                  <button
                    type="button"
                    className="btn btn-sm btn-outline-secondary rounded-pill"
                    onClick={() => {
                      setTrainBookedTicket(null)
                      setSelectedTrain(null)
                      setSelectedClass(null)
                    }}
                  >
                    Book Another Train
                  </button>
                </div>

                <div className="row g-2 bg-white p-3 rounded-3 border mb-3">
                  <div className="col-6 col-md-3">
                    <span className="text-muted small">Route:</span>
                    <p className="fw-bold mb-0">{trainBookedTicket.from} ➔ {trainBookedTicket.to}</p>
                  </div>
                  <div className="col-6 col-md-3">
                    <span className="text-muted small">Class & Berth:</span>
                    <p className="fw-bold mb-0 text-primary">{trainBookedTicket.selectedClass.code} · Coach {trainBookedTicket.coach} / {trainBookedTicket.berth}</p>
                  </div>
                  <div className="col-6 col-md-3">
                    <span className="text-muted small">Passenger:</span>
                    <p className="fw-bold mb-0">{trainBookedTicket.passenger.name} ({trainBookedTicket.passenger.age}y)</p>
                  </div>
                  <div className="col-6 col-md-3">
                    <span className="text-muted small">Fare Paid:</span>
                    <p className="fw-bold mb-0 text-success">₹{trainBookedTicket.totalFare}</p>
                  </div>
                </div>

                <div className="d-flex gap-2">
                  <button type="button" className="btn btn-sm btn-primary rounded-pill px-3" onClick={() => window.print()}>
                    <i className="bi bi-printer me-1"></i> Print E-Ticket
                  </button>
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  )
}
