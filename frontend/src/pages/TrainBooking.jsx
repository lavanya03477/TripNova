import { useState, useEffect } from 'react'
import { useSearchParams } from 'react-router-dom'
import Navbar from '../components/Navbar'

const POPULAR_STATIONS = [
  { code: 'NDLS', name: 'New Delhi (NDLS)' },
  { code: 'CSTM', name: 'Mumbai CSMT (CSTM)' },
  { code: 'SBC', name: 'KSR Bengaluru (SBC)' },
  { code: 'MAS', name: 'Chennai Central (MAS)' },
  { code: 'HWH', name: 'Howrah Junction (HWH)' },
  { code: 'JP', name: 'Jaipur Junction (JP)' },
  { code: 'MDU', name: 'Madurai Junction (MDU)' },
  { code: 'BSB', name: 'Varanasi Junction (BSB)' },
  { code: 'ERS', name: 'Ernakulam South / Kochi (ERS)' },
  { code: 'MAO', name: 'Madgaon Goa (MAO)' },
  { code: 'KLK', name: 'Kalka / Shimla (KLK)' },
  { code: 'CDG', name: 'Chandigarh / Manali (CDG)' },
]

const SAMPLE_TRAINS = [
  {
    trainNumber: '12002',
    trainName: 'Bhopal Shatabdi Express',
    fromStation: 'New Delhi (NDLS)',
    toStation: 'Agra Cantt (AGC)',
    deptTime: '06:00',
    arrTime: '07:50',
    duration: '1h 50m',
    runsOn: 'M T W T F S S',
    classes: [
      { code: 'CC', name: 'AC Chair Car', fare: 640, status: 'AVAILABLE - 84', color: 'success' },
      { code: 'EC', name: 'Exec Chair Car', fare: 1220, status: 'AVAILABLE - 16', color: 'success' },
    ],
  },
  {
    trainNumber: '22691',
    trainName: 'Bengaluru Rajdhani Express',
    fromStation: 'New Delhi (NDLS)',
    toStation: 'KSR Bengaluru (SBC)',
    deptTime: '19:50',
    arrTime: '05:20 (+2d)',
    duration: '33h 30m',
    runsOn: 'M T W T F S S',
    classes: [
      { code: '3A', name: '3 Tier AC', fare: 2450, status: 'AVAILABLE - 42', color: 'success' },
      { code: '2A', name: '2 Tier AC', fare: 3580, status: 'AVAILABLE - 12', color: 'success' },
      { code: '1A', name: '1st Class AC', fare: 5980, status: 'RAC 4', color: 'warning' },
    ],
  },
  {
    trainNumber: '20608',
    trainName: 'Vande Bharat Express',
    fromStation: 'Chennai Central (MAS)',
    toStation: 'Madurai Junction (MDU)',
    deptTime: '05:45',
    arrTime: '11:45',
    duration: '6h 00m',
    runsOn: 'M T W T F S',
    classes: [
      { code: 'CC', name: 'Chair Car', fare: 1140, status: 'AVAILABLE - 110', color: 'success' },
      { code: 'EC', name: 'Executive CC', fare: 2150, status: 'AVAILABLE - 28', color: 'success' },
    ],
  },
  {
    trainNumber: '12626',
    trainName: 'Kerala Superfast Express',
    fromStation: 'New Delhi (NDLS)',
    toStation: 'Ernakulam Junction (ERS)',
    deptTime: '20:10',
    arrTime: '14:20 (+2d)',
    duration: '42h 10m',
    runsOn: 'M T W T F S S',
    classes: [
      { code: 'SL', name: 'Sleeper', fare: 860, status: 'AVAILABLE - 68', color: 'success' },
      { code: '3A', name: '3 Tier AC', fare: 2280, status: 'AVAILABLE - 34', color: 'success' },
      { code: '2A', name: '2 Tier AC', fare: 3340, status: 'RAC 8', color: 'warning' },
    ],
  },
  {
    trainNumber: '12952',
    trainName: 'Mumbai Tejas Rajdhani',
    fromStation: 'New Delhi (NDLS)',
    toStation: 'Mumbai CSMT (CSTM)',
    deptTime: '16:55',
    arrTime: '08:35',
    duration: '15h 40m',
    runsOn: 'M T W T F S S',
    classes: [
      { code: '3A', name: '3 Tier AC', fare: 2140, status: 'AVAILABLE - 56', color: 'success' },
      { code: '2A', name: '2 Tier AC', fare: 3120, status: 'AVAILABLE - 18', color: 'success' },
      { code: '1A', name: '1st Class AC', fare: 5240, status: 'AVAILABLE - 6', color: 'success' },
    ],
  },
]

export default function TrainBooking() {
  const [searchParams] = useSearchParams()
  const [activeTab, setActiveTab] = useState('search') // 'search' | 'pnr'
  const [fromStation, setFromStation] = useState('NDLS')
  const [toStation, setToStation] = useState('MDU')
  const [date, setDate] = useState(new Date().toISOString().split('T')[0])
  const [trainClass, setTrainClass] = useState('ALL')
  const [quota, setQuota] = useState('GN')
  const [searched, setSearched] = useState(true)

  // Booking Modal State
  const [selectedTrain, setSelectedTrain] = useState(null)
  const [selectedClass, setSelectedClass] = useState(null)
  const [passengerName, setPassengerName] = useState('')
  const [passengerAge, setPassengerAge] = useState('')
  const [berthPreference, setBerthPreference] = useState('No Preference')
  const [ticketConfirmed, setTicketConfirmed] = useState(null)

  // PNR State
  const [pnrInput, setPnrInput] = useState('')
  const [pnrResult, setPnrResult] = useState(null)

  useEffect(() => {
    const toParam = searchParams.get('to')
    if (toParam) {
      // Check if station code matches
      const match = POPULAR_STATIONS.find((s) => s.name.toLowerCase().includes(toParam.toLowerCase()))
      if (match) setToStation(match.code)
    }
  }, [searchParams])

  const handleSearch = (e) => {
    e.preventDefault()
    setSearched(true)
    setSelectedTrain(null)
  }

  const openBookModal = (train, cls) => {
    setSelectedTrain(train)
    setSelectedClass(cls)
    setTicketConfirmed(null)
  }

  const handleConfirmTicket = (e) => {
    e.preventDefault()
    if (!passengerName) {
      alert('Please enter passenger name.')
      return
    }
    const pnr = '28' + Math.floor(10000000 + Math.random() * 90000000)
    setTicketConfirmed({
      pnr,
      train: selectedTrain,
      trainClass: selectedClass,
      date,
      quota,
      passenger: { name: passengerName, age: passengerAge || '30', berth: berthPreference },
      coach: selectedClass.code + '2',
      seatNumber: Math.floor(1 + Math.random() * 64),
    })
  }

  const handleCheckPNR = (e) => {
    e.preventDefault()
    if (!pnrInput || pnrInput.length < 8) {
      alert('Please enter a valid 10-digit PNR number.')
      return
    }
    setPnrResult({
      pnr: pnrInput,
      trainNumber: '12002 / Shatabdi Express',
      from: 'New Delhi (NDLS)',
      to: 'Agra Cantt (AGC)',
      dateOfJourney: date,
      bookingStatus: 'CNF (Confirmed)',
      coach: 'C3',
      berth: '42 (Window Seat)',
      chartStatus: 'Chart Not Prepared',
    })
  }

  return (
    <div className="page-bg">
      <Navbar />
      <main className="container py-4">
        {/* IRCTC In-App Header Banner */}
        <div className="card glass-card border-0 mb-4 bg-gradient-irctc text-white overflow-hidden shadow-lg">
          <div className="card-body p-4 position-relative">
            <div className="d-flex flex-wrap justify-content-between align-items-center gap-3">
              <div>
                <div className="d-flex align-items-center gap-2 mb-2">
                  <span className="badge bg-warning text-dark px-3 py-1 fw-bold rounded-pill">
                    <i className="bi bi-train-front-fill me-1"></i> IRCTC In-App Engine
                  </span>
                  <span className="badge bg-white bg-opacity-25 rounded-pill px-3 py-1">
                    Official Railway Gateway
                  </span>
                </div>
                <h1 className="fw-bold mb-1 display-6">Indian Railways Train Booking</h1>
                <p className="lead mb-0 opacity-90 fs-6">
                  Check live seat availability, fare chart, and instant ticket booking in TripNova.
                </p>
              </div>

              {/* Navigation Tabs */}
              <div className="btn-group rounded-pill p-1 bg-black bg-opacity-25 shadow-sm">
                <button
                  type="button"
                  className={`btn btn-sm rounded-pill px-3 fw-bold ${
                    activeTab === 'search' ? 'btn-light text-dark' : 'btn-outline-light'
                  }`}
                  onClick={() => setActiveTab('search')}
                >
                  <i className="bi bi-search me-1"></i> Train Search
                </button>
                <button
                  type="button"
                  className={`btn btn-sm rounded-pill px-3 fw-bold ${
                    activeTab === 'pnr' ? 'btn-light text-dark' : 'btn-outline-light'
                  }`}
                  onClick={() => setActiveTab('pnr')}
                >
                  <i className="bi bi-card-checklist me-1"></i> Live PNR Status
                </button>
              </div>
            </div>
          </div>
        </div>

        {activeTab === 'search' ? (
          <>
            {/* Search Form */}
            <div className="card glass-card border-0 mb-4 shadow-sm">
              <div className="card-body p-4">
                <form onSubmit={handleSearch}>
                  <div className="row g-3 align-items-end">
                    <div className="col-md-3 col-sm-6">
                      <label className="form-label fw-bold small text-uppercase text-muted">
                        <i className="bi bi-record-circle text-primary me-1"></i> Origin Station
                      </label>
                      <select
                        className="form-select form-select-lg fw-semibold"
                        value={fromStation}
                        onChange={(e) => setFromStation(e.target.value)}
                      >
                        {POPULAR_STATIONS.map((st) => (
                          <option key={st.code} value={st.code}>
                            {st.name}
                          </option>
                        ))}
                      </select>
                    </div>

                    <div className="col-md-3 col-sm-6">
                      <label className="form-label fw-bold small text-uppercase text-muted">
                        <i className="bi bi-geo-alt-fill text-success me-1"></i> Destination Station
                      </label>
                      <select
                        className="form-select form-select-lg fw-semibold"
                        value={toStation}
                        onChange={(e) => setToStation(e.target.value)}
                      >
                        {POPULAR_STATIONS.map((st) => (
                          <option key={st.code} value={st.code}>
                            {st.name}
                          </option>
                        ))}
                      </select>
                    </div>

                    <div className="col-md-2 col-sm-6">
                      <label className="form-label fw-bold small text-uppercase text-muted">
                        <i className="bi bi-calendar-date text-info me-1"></i> Date
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
                      <label className="form-label fw-bold small text-uppercase text-muted">
                        <i className="bi bi-shield me-1"></i> Quota
                      </label>
                      <select
                        className="form-select form-select-lg"
                        value={quota}
                        onChange={(e) => setQuota(e.target.value)}
                      >
                        <option value="GN">General (GN)</option>
                        <option value="TQ">Tatkal (TQ)</option>
                        <option value="PT">Premium Tatkal</option>
                        <option value="LD">Ladies Quota</option>
                      </select>
                    </div>

                    <div className="col-md-2 col-sm-12">
                      <button type="submit" className="btn btn-primary btn-lg w-100 fw-bold shadow-sm">
                        <i className="bi bi-search me-1"></i> Find Trains
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </div>

            {/* Train Search Results */}
            {searched && (
              <div className="mb-4">
                <div className="d-flex justify-content-between align-items-center mb-3">
                  <h5 className="fw-bold mb-0">
                    <i className="bi bi-train-front text-primary me-2"></i>
                    Trains from {fromStation} to {toStation} on {date}
                    <span className="badge bg-light text-dark ms-2 border">
                      {SAMPLE_TRAINS.length} trains available
                    </span>
                  </h5>
                </div>

                <div className="row g-3">
                  {SAMPLE_TRAINS.map((train) => (
                    <div className="col-12" key={train.trainNumber}>
                      <div className="card glass-card border-0 shadow-sm p-4 hover-lift">
                        <div className="row align-items-center g-3">
                          {/* Train Info */}
                          <div className="col-lg-4 col-md-5">
                            <div className="d-flex align-items-center gap-2 mb-1">
                              <span className="badge bg-primary rounded-pill px-2 py-1">
                                #{train.trainNumber}
                              </span>
                              <h5 className="fw-bold text-dark mb-0">{train.trainName}</h5>
                            </div>
                            <p className="text-muted small mb-1">Runs On: <strong className="text-dark">{train.runsOn}</strong></p>
                            <span className="badge bg-light text-muted border">IRCTC Certified Superfast</span>
                          </div>

                          {/* Timings */}
                          <div className="col-lg-3 col-md-3">
                            <div className="d-flex align-items-center justify-content-between text-center">
                              <div>
                                <div className="fs-5 fw-bold text-dark">{train.deptTime}</div>
                                <div className="text-muted small">{train.fromStation.split('(')[0]}</div>
                              </div>
                              <div className="px-2">
                                <span className="badge bg-light text-muted border mb-1">{train.duration}</span>
                                <div style={{ height: '2px', background: '#0284c7', width: '50px' }}></div>
                              </div>
                              <div>
                                <div className="fs-5 fw-bold text-dark">{train.arrTime}</div>
                                <div className="text-muted small">{train.toStation.split('(')[0]}</div>
                              </div>
                            </div>
                          </div>

                          {/* Classes & Availability */}
                          <div className="col-lg-5 col-md-4">
                            <div className="d-flex flex-wrap gap-2 justify-content-lg-end">
                              {train.classes.map((cls) => (
                                <button
                                  key={cls.code}
                                  type="button"
                                  onClick={() => openBookModal(train, cls)}
                                  className="btn btn-outline-dark p-2 text-start rounded-3 bg-white border flex-grow-1"
                                  style={{ minWidth: '120px' }}
                                >
                                  <div className="d-flex justify-content-between align-items-center mb-1">
                                    <strong className="badge bg-dark">{cls.code}</strong>
                                    <span className="fw-bold text-primary">₹{cls.fare}</span>
                                  </div>
                                  <div className={`small fw-bold text-${cls.color}`}>
                                    {cls.status}
                                  </div>
                                  <div className="text-muted" style={{ fontSize: '10px' }}>
                                    Click to Book In-App
                                  </div>
                                </button>
                              ))}
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </>
        ) : (
          /* Live PNR Status Check Tab */
          <div className="card glass-card border-0 shadow-sm p-4 mb-4">
            <h4 className="fw-bold mb-3 d-flex align-items-center gap-2">
              <i className="bi bi-card-checklist text-primary"></i>
              Live PNR Status Tracker
            </h4>
            <p className="text-muted">Enter your 10-digit Railway PNR number to check current booking and confirmation status.</p>

            <form onSubmit={handleCheckPNR} className="mb-4">
              <div className="row g-2 align-items-center">
                <div className="col-md-8">
                  <input
                    type="text"
                    className="form-control form-control-lg fw-bold"
                    placeholder="Enter 10-Digit PNR (e.g. 2847192840)"
                    maxLength="10"
                    value={pnrInput}
                    onChange={(e) => setPnrInput(e.target.value)}
                    required
                  />
                </div>
                <div className="col-md-4">
                  <button type="submit" className="btn btn-primary btn-lg w-100 fw-bold">
                    Check Live Status
                  </button>
                </div>
              </div>
            </form>

            {pnrResult && (
              <div className="card bg-light border-2 border-primary p-4 rounded-4 shadow-sm">
                <div className="d-flex justify-content-between align-items-center border-bottom pb-3 mb-3">
                  <div>
                    <span className="badge bg-primary px-3 py-1">IRCTC Verified</span>
                    <h5 className="fw-bold mb-0 mt-1">{pnrResult.trainNumber}</h5>
                  </div>
                  <div className="text-end">
                    <span className="small text-muted">PNR Number:</span>
                    <h5 className="fw-bold text-primary mb-0">{pnrResult.pnr}</h5>
                  </div>
                </div>

                <div className="row g-3 mb-3">
                  <div className="col-md-3">
                    <span className="text-muted small d-block">From:</span>
                    <strong>{pnrResult.from}</strong>
                  </div>
                  <div className="col-md-3">
                    <span className="text-muted small d-block">To:</span>
                    <strong>{pnrResult.to}</strong>
                  </div>
                  <div className="col-md-3">
                    <span className="text-muted small d-block">Date of Journey:</span>
                    <strong>{pnrResult.dateOfJourney}</strong>
                  </div>
                  <div className="col-md-3">
                    <span className="text-muted small d-block">Booking Status:</span>
                    <strong className="badge bg-success fs-6">{pnrResult.bookingStatus}</strong>
                  </div>
                </div>

                <div className="p-3 bg-white rounded-3 border d-flex justify-content-between align-items-center">
                  <div>
                    <span className="small text-muted">Allocated Coach & Berth:</span>
                    <div className="fs-5 fw-bold text-dark">{pnrResult.coach} - Berth #{pnrResult.berth}</div>
                  </div>
                  <div>
                    <span className="badge bg-info-subtle text-info border border-info-subtle rounded-pill">
                      {pnrResult.chartStatus}
                    </span>
                  </div>
                </div>
              </div>
            )}
          </div>
        )}

        {/* Train In-App Booking Modal */}
        {selectedTrain && selectedClass && (
          <div
            className="modal d-block"
            tabIndex="-1"
            style={{ backgroundColor: 'rgba(0,0,0,0.65)', zIndex: 1055, backdropFilter: 'blur(3px)' }}
          >
            <div className="modal-dialog modal-lg modal-dialog-centered">
              <div className="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
                <div className="modal-header bg-primary text-white">
                  <div>
                    <h5 className="modal-title fw-bold">
                      <i className="bi bi-train-front me-2"></i>
                      {selectedTrain.trainNumber} - {selectedTrain.trainName} ({selectedClass.code})
                    </h5>
                    <p className="small mb-0 opacity-90">
                      {selectedTrain.fromStation} ➔ {selectedTrain.toStation} | {date} | Quota: {quota}
                    </p>
                  </div>
                  <button
                    type="button"
                    className="btn-close btn-close-white"
                    onClick={() => {
                      setSelectedTrain(null)
                      setSelectedClass(null)
                    }}
                    aria-label="Close"
                  ></button>
                </div>

                {!ticketConfirmed ? (
                  <div className="modal-body p-4">
                    <form onSubmit={handleConfirmTicket}>
                      <h6 className="fw-bold mb-3">
                        <i className="bi bi-person-bounding-box text-primary me-2"></i>
                        Passenger Details
                      </h6>

                      <div className="row g-3 mb-3">
                        <div className="col-md-6">
                          <label className="form-label small fw-bold">Passenger Name (as per Govt ID)</label>
                          <input
                            type="text"
                            className="form-control"
                            value={passengerName}
                            onChange={(e) => setPassengerName(e.target.value)}
                            placeholder="e.g. Ramesh Kumar"
                            required
                          />
                        </div>
                        <div className="col-md-3">
                          <label className="form-label small fw-bold">Age</label>
                          <input
                            type="number"
                            className="form-control"
                            value={passengerAge}
                            onChange={(e) => setPassengerAge(e.target.value)}
                            placeholder="Age"
                            min="5"
                            max="100"
                            required
                          />
                        </div>
                        <div className="col-md-3">
                          <label className="form-label small fw-bold">Berth Preference</label>
                          <select
                            className="form-select"
                            value={berthPreference}
                            onChange={(e) => setBerthPreference(e.target.value)}
                          >
                            <option value="No Preference">No Preference</option>
                            <option value="Lower Berth">Lower Berth</option>
                            <option value="Middle Berth">Middle Berth</option>
                            <option value="Upper Berth">Upper Berth</option>
                            <option value="Side Lower">Side Lower</option>
                          </select>
                        </div>
                      </div>

                      {/* Fare Card */}
                      <div className="card bg-light border-0 p-3 rounded-3 mb-3">
                        <div className="d-flex justify-content-between small mb-1">
                          <span>Base Fare ({selectedClass.code}):</span>
                          <span>₹{selectedClass.fare}</span>
                        </div>
                        <div className="d-flex justify-content-between small mb-1">
                          <span>IRCTC Service Fee:</span>
                          <span>₹15.00</span>
                        </div>
                        <div className="d-flex justify-content-between fw-bold fs-6 border-top pt-2 mt-1">
                          <span>Total Ticket Amount:</span>
                          <span className="text-primary">₹{selectedClass.fare + 15}</span>
                        </div>
                      </div>

                      <button type="submit" className="btn btn-primary btn-lg w-100 fw-bold shadow-sm">
                        <i className="bi bi-ticket-detailed me-1"></i>
                        Confirm & Issue Ticket (In-App)
                      </button>
                    </form>
                  </div>
                ) : (
                  /* Generated E-Ticket */
                  <div className="modal-body p-4 text-center">
                    <div className="alert alert-success d-inline-block rounded-circle p-3 mb-3 shadow-sm">
                      <i className="bi bi-check-lg display-5 text-success"></i>
                    </div>
                    <h4 className="fw-bold text-success mb-1">IRCTC E-Ticket Confirmed!</h4>
                    <p className="text-muted small mb-3">Your electronic reservation slip is issued.</p>

                    <div className="card border-2 border-primary bg-light text-start p-3 rounded-4 mx-auto mb-3" style={{ maxWidth: '440px' }}>
                      <div className="d-flex justify-content-between border-bottom pb-2 mb-2">
                        <div>
                          <span className="badge bg-primary">IRCTC E-Ticket</span>
                          <h6 className="fw-bold mb-0 mt-1">{ticketConfirmed.train.trainName}</h6>
                        </div>
                        <div className="text-end">
                          <span className="small text-muted">PNR:</span>
                          <strong className="d-block text-primary">{ticketConfirmed.pnr}</strong>
                        </div>
                      </div>

                      <div className="row g-2 small mb-2">
                        <div className="col-6">
                          <span className="text-muted">Coach/Berth: </span>
                          <strong className="text-success">{ticketConfirmed.coach} - #{ticketConfirmed.seatNumber} ({ticketConfirmed.passenger.berth})</strong>
                        </div>
                        <div className="col-6">
                          <span className="text-muted">Class: </span>
                          <strong>{ticketConfirmed.trainClass.code} ({ticketConfirmed.quota})</strong>
                        </div>
                        <div className="col-6">
                          <span className="text-muted">From: </span>
                          <strong>{ticketConfirmed.train.fromStation}</strong>
                        </div>
                        <div className="col-6">
                          <span className="text-muted">To: </span>
                          <strong>{ticketConfirmed.train.toStation}</strong>
                        </div>
                        <div className="col-12">
                          <span className="text-muted">Passenger: </span>
                          <strong>{ticketConfirmed.passenger.name} ({ticketConfirmed.passenger.age} yrs)</strong>
                        </div>
                      </div>

                      <div className="border-top pt-2 d-flex justify-content-between align-items-center">
                        <span className="small text-muted">Status: Confirmed (CNF)</span>
                        <span className="fw-bold text-primary fs-6">Paid: ₹{ticketConfirmed.trainClass.fare + 15}</span>
                      </div>
                    </div>

                    <button
                      type="button"
                      className="btn btn-outline-dark rounded-pill px-4"
                      onClick={() => {
                        setSelectedTrain(null)
                        setSelectedClass(null)
                      }}
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
