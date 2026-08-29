import { useState, useEffect } from 'react'
import { useSearchParams } from 'react-router-dom'
import Navbar from '../components/Navbar'

const SAMPLE_HOTELS = [
  {
    id: 'HT-1',
    name: 'The Grand Heritage Palace Resort',
    city: 'Jaipur',
    location: 'Near City Palace & Lake',
    type: 'Luxury Heritage',
    rating: 4.9,
    reviews: 1850,
    price: 8500,
    originalPrice: 12000,
    image: 'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600&auto=format&fit=crop&q=80',
    amenities: ['Free WiFi', 'Swimming Pool', 'Spa & Wellness', 'Free Breakfast', 'Airport Shuttle'],
    roomsAvailable: 3,
  },
  {
    id: 'HT-2',
    name: 'Himalayan Pine View Retreat & Spa',
    city: 'Manali',
    location: 'Old Manali / Solang Road',
    type: 'Mountain Luxury',
    rating: 4.8,
    reviews: 1230,
    price: 5200,
    originalPrice: 7500,
    image: 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=600&auto=format&fit=crop&q=80',
    amenities: ['Mountain View Balcony', 'Free WiFi', 'Bonfire & BBQ', 'Free Breakfast', 'Heated Rooms'],
    roomsAvailable: 5,
  },
  {
    id: 'HT-3',
    name: 'Taj Coastal Beachfront Villa',
    city: 'Goa',
    location: 'Calangute / Baga Beachfront',
    type: 'Luxury Beach Resort',
    rating: 4.9,
    reviews: 2400,
    price: 11500,
    originalPrice: 16000,
    image: 'https://images.unsplash.com/photo-1582719508461-905c673771fd?w=600&auto=format&fit=crop&q=80',
    amenities: ['Private Beach Access', 'Infinity Pool', 'Cocktail Bar', 'Sea Facing Rooms', 'Free WiFi'],
    roomsAvailable: 2,
  },
  {
    id: 'HT-4',
    name: 'The Royal Residency Boutique Stay',
    city: 'Delhi',
    location: 'Connaught Place / Central Delhi',
    type: 'Mid-range Business',
    rating: 4.5,
    reviews: 940,
    price: 3200,
    originalPrice: 4800,
    image: 'https://images.unsplash.com/photo-1590490360182-c33d57733427?w=600&auto=format&fit=crop&q=80',
    amenities: ['Free WiFi', 'AC Rooms', 'Multi-cuisine Restaurant', 'Fitness Center', 'Room Service'],
    roomsAvailable: 8,
  },
  {
    id: 'HT-5',
    name: 'Backwater Serenity Luxury Houseboat & Resort',
    city: 'Kerala',
    location: 'Alleppey Punnamada Lake',
    type: 'Houseboat Stay',
    rating: 4.8,
    reviews: 1560,
    price: 7800,
    originalPrice: 10500,
    image: 'https://images.unsplash.com/photo-1593693397690-362cb9666fc2?w=600&auto=format&fit=crop&q=80',
    amenities: ['Private Chef Included', 'All Meals Included', 'Sunset Cruise', 'Ayurvedic Massage'],
    roomsAvailable: 4,
  },
  {
    id: 'HT-6',
    name: 'Heritage Temple View Inn',
    city: 'Madurai',
    location: 'Near Meenakshi Amman Temple',
    type: 'Budget-friendly Heritage',
    rating: 4.4,
    reviews: 680,
    price: 1800,
    originalPrice: 2500,
    image: 'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=600&auto=format&fit=crop&q=80',
    amenities: ['Temple View', 'Free WiFi', 'Vegetarian Restaurant', 'AC Rooms'],
    roomsAvailable: 12,
  },
]

export default function Hotels() {
  const [searchParams] = useSearchParams()
  const [destination, setDestination] = useState('Manali')
  const [checkIn, setCheckIn] = useState(new Date().toISOString().split('T')[0])
  const [checkOut, setCheckOut] = useState(
    new Date(Date.now() + 3 * 86400000).toISOString().split('T')[0]
  )
  const [guests, setGuests] = useState('2 Guests, 1 Room')
  const [starFilter, setStarFilter] = useState('ALL')
  const [activeHotel, setActiveHotel] = useState(null)

  // Booking Form State
  const [guestName, setGuestName] = useState('')
  const [guestPhone, setGuestPhone] = useState('')
  const [guestEmail, setGuestEmail] = useState('')
  const [roomType, setRoomType] = useState('Deluxe King Room')
  const [bookingConfirmed, setBookingConfirmed] = useState(null)

  useEffect(() => {
    const destParam = searchParams.get('destination')
    if (destParam) {
      setDestination(destParam.split(',')[0].trim())
    }
  }, [searchParams])

  const openBookModal = (hotel) => {
    setActiveHotel(hotel)
    setBookingConfirmed(null)
  }

  const handleConfirmReservation = (e) => {
    e.preventDefault()
    if (!guestName || !guestPhone) {
      alert('Please fill guest name and phone number.')
      return
    }
    const bookingId = 'TN-HTL-' + Math.floor(100000 + Math.random() * 900000)
    setBookingConfirmed({
      bookingId,
      hotel: activeHotel,
      checkIn,
      checkOut,
      guests,
      roomType,
      guest: { name: guestName, phone: guestPhone, email: guestEmail },
      totalPrice: activeHotel.price * 2, // 2 nights
    })
  }

  const filteredHotels = SAMPLE_HOTELS.filter((h) => {
    if (starFilter === '5STAR') return h.rating >= 4.8
    if (starFilter === 'BUDGET') return h.price < 4000
    return true
  })

  return (
    <div className="page-bg">
      <Navbar />
      <main className="container py-4">
        {/* Hotel Hub Banner */}
        <div className="card glass-card border-0 mb-4 bg-gradient-hotel text-white overflow-hidden shadow-lg">
          <div className="card-body p-4 position-relative">
            <div className="d-flex flex-wrap justify-content-between align-items-center gap-3">
              <div>
                <div className="d-flex align-items-center gap-2 mb-2">
                  <span className="badge bg-warning text-dark px-3 py-1 fw-bold rounded-pill">
                    <i className="bi bi-building-fill me-1"></i> TripNova Hotels Engine
                  </span>
                  <span className="badge bg-white bg-opacity-25 rounded-pill px-3 py-1">
                    Verified Stays & Best Price Guarantee
                  </span>
                </div>
                <h1 className="fw-bold mb-1 display-6">Hotel & Resort Booking</h1>
                <p className="lead mb-0 opacity-90 fs-6">
                  Book luxury palaces, hill station retreats, beach villas, and cozy stays across India inside TripNova.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Search Bar */}
        <div className="card glass-card border-0 mb-4 shadow-sm">
          <div className="card-body p-4">
            <form onSubmit={(e) => e.preventDefault()}>
              <div className="row g-3 align-items-end">
                <div className="col-md-4 col-sm-6">
                  <label className="form-label fw-bold small text-uppercase text-muted">
                    <i className="bi bi-geo-alt-fill text-danger me-1"></i> Destination City
                  </label>
                  <input
                    type="text"
                    className="form-control form-control-lg fw-semibold"
                    value={destination}
                    onChange={(e) => setDestination(e.target.value)}
                    placeholder="e.g. Manali, Goa, Jaipur, Madurai"
                    required
                  />
                </div>

                <div className="col-md-2 col-sm-6">
                  <label className="form-label fw-bold small text-uppercase text-muted">
                    <i className="bi bi-calendar-check text-success me-1"></i> Check In
                  </label>
                  <input
                    type="date"
                    className="form-control form-control-lg"
                    value={checkIn}
                    onChange={(e) => setCheckIn(e.target.value)}
                    required
                  />
                </div>

                <div className="col-md-2 col-sm-6">
                  <label className="form-label fw-bold small text-uppercase text-muted">
                    <i className="bi bi-calendar-x text-danger me-1"></i> Check Out
                  </label>
                  <input
                    type="date"
                    className="form-control form-control-lg"
                    value={checkOut}
                    onChange={(e) => setCheckOut(e.target.value)}
                    required
                  />
                </div>

                <div className="col-md-2 col-sm-6">
                  <label className="form-label fw-bold small text-uppercase text-muted">
                    <i className="bi bi-people-fill text-info me-1"></i> Guests & Rooms
                  </label>
                  <select
                    className="form-select form-select-lg"
                    value={guests}
                    onChange={(e) => setGuests(e.target.value)}
                  >
                    <option value="1 Guest, 1 Room">1 Guest, 1 Room</option>
                    <option value="2 Guests, 1 Room">2 Guests, 1 Room</option>
                    <option value="3 Guests, 1 Room">3 Guests, 1 Room</option>
                    <option value="4 Guests, 2 Rooms">4 Guests, 2 Rooms</option>
                  </select>
                </div>

                <div className="col-md-2 col-sm-12">
                  <button type="button" className="btn btn-info text-white btn-lg w-100 fw-bold shadow-sm">
                    <i className="bi bi-search me-1"></i> Search
                  </button>
                </div>
              </div>

              {/* Star Rating & Budget Filters */}
              <div className="d-flex flex-wrap align-items-center gap-2 mt-3 pt-3 border-top">
                <span className="small fw-bold text-muted me-2">Filter by:</span>
                {[
                  { id: 'ALL', label: 'All Stays' },
                  { id: '5STAR', label: '★ 5-Star & Luxury' },
                  { id: 'BUDGET', label: 'Budget Friendly (< ₹4,000)' },
                ].map((f) => (
                  <button
                    key={f.id}
                    type="button"
                    className={`btn btn-sm rounded-pill px-3 fw-semibold ${
                      starFilter === f.id ? 'btn-dark' : 'btn-outline-secondary'
                    }`}
                    onClick={() => setStarFilter(f.id)}
                  >
                    {f.label}
                  </button>
                ))}
              </div>
            </form>
          </div>
        </div>

        {/* Hotels Grid */}
        <div className="mb-4">
          <div className="d-flex justify-content-between align-items-center mb-3">
            <h5 className="fw-bold mb-0">
              <i className="bi bi-building-check text-info me-2"></i>
              Top Recommended Hotels for {destination}
              <span className="badge bg-light text-dark ms-2 border">
                {filteredHotels.length} verified stays
              </span>
            </h5>
          </div>

          <div className="row g-4">
            {filteredHotels.map((hotel) => (
              <div className="col-lg-4 col-md-6" key={hotel.id}>
                <div className="card glass-card border-0 shadow-sm h-100 overflow-hidden d-flex flex-column justify-content-between hover-lift">
                  <div>
                    {/* Hotel Image with Badge */}
                    <div className="position-relative" style={{ height: '190px', overflow: 'hidden' }}>
                      <img
                        src={hotel.image}
                        alt={hotel.name}
                        className="w-100 h-100"
                        style={{ objectFit: 'cover' }}
                      />
                      <span className="badge bg-dark bg-opacity-75 position-absolute top-0 start-0 m-3 px-3 py-2 rounded-pill">
                        {hotel.type}
                      </span>
                      <span className="badge bg-success position-absolute top-0 end-0 m-3 px-2 py-1 rounded-pill">
                        ★ {hotel.rating} ({hotel.reviews})
                      </span>
                    </div>

                    <div className="p-3">
                      <h5 className="fw-bold mb-1 text-dark text-truncate" title={hotel.name}>
                        {hotel.name}
                      </h5>
                      <p className="text-muted small mb-2">
                        <i className="bi bi-geo-alt text-danger me-1"></i>
                        {hotel.location}
                      </p>

                      {/* Amenities */}
                      <div className="d-flex flex-wrap gap-1 mb-3">
                        {hotel.amenities.slice(0, 3).map((a, idx) => (
                          <span key={idx} className="badge bg-light text-muted border" style={{ fontSize: '10px' }}>
                            ✓ {a}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>

                  <div className="p-3 pt-0 border-top bg-light bg-opacity-50">
                    <div className="d-flex justify-content-between align-items-center mb-2 mt-2">
                      <div>
                        <span className="text-muted text-decoration-line-through small me-1">
                          ₹{hotel.originalPrice}
                        </span>
                        <span className="fs-5 fw-bold text-success">₹{hotel.price}</span>
                        <span className="text-muted small"> / night</span>
                      </div>
                      <span className="badge bg-danger-subtle text-danger border border-danger-subtle rounded-pill">
                        {hotel.roomsAvailable} rooms left
                      </span>
                    </div>

                    <button
                      type="button"
                      className="btn btn-info text-white w-100 rounded-pill fw-bold shadow-sm"
                      onClick={() => openBookModal(hotel)}
                    >
                      <i className="bi bi-door-open me-1"></i> Reserve In-App
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Hotel In-App Reservation Modal */}
        {activeHotel && (
          <div
            className="modal d-block"
            tabIndex="-1"
            style={{ backgroundColor: 'rgba(0,0,0,0.65)', zIndex: 1055, backdropFilter: 'blur(3px)' }}
          >
            <div className="modal-dialog modal-lg modal-dialog-centered">
              <div className="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
                <div className="modal-header bg-info text-white">
                  <div>
                    <h5 className="modal-title fw-bold">
                      <i className="bi bi-building me-2"></i>
                      {activeHotel.name}
                    </h5>
                    <p className="small mb-0 opacity-90">
                      {activeHotel.location} | Check-in: {checkIn} ➔ Check-out: {checkOut}
                    </p>
                  </div>
                  <button
                    type="button"
                    className="btn-close btn-close-white"
                    onClick={() => setActiveHotel(null)}
                    aria-label="Close"
                  ></button>
                </div>

                {!bookingConfirmed ? (
                  <div className="modal-body p-4">
                    <form onSubmit={handleConfirmReservation}>
                      <h6 className="fw-bold mb-3">
                        <i className="bi bi-person-circle text-info me-2"></i>
                        Guest Information & Room Selection
                      </h6>

                      <div className="row g-3 mb-3">
                        <div className="col-md-6">
                          <label className="form-label small fw-bold">Primary Guest Full Name</label>
                          <input
                            type="text"
                            className="form-control"
                            value={guestName}
                            onChange={(e) => setGuestName(e.target.value)}
                            placeholder="e.g. Priya Sharma"
                            required
                          />
                        </div>
                        <div className="col-md-6">
                          <label className="form-label small fw-bold">Phone Number</label>
                          <input
                            type="tel"
                            className="form-control"
                            value={guestPhone}
                            onChange={(e) => setGuestPhone(e.target.value)}
                            placeholder="10-digit mobile number"
                            required
                          />
                        </div>
                        <div className="col-md-6">
                          <label className="form-label small fw-bold">Email for Booking Voucher</label>
                          <input
                            type="email"
                            className="form-control"
                            value={guestEmail}
                            onChange={(e) => setGuestEmail(e.target.value)}
                            placeholder="you@example.com"
                          />
                        </div>
                        <div className="col-md-6">
                          <label className="form-label small fw-bold">Room Category</label>
                          <select
                            className="form-select"
                            value={roomType}
                            onChange={(e) => setRoomType(e.target.value)}
                          >
                            <option value="Deluxe King Room">Deluxe King Room (Complimentary Breakfast)</option>
                            <option value="Executive Mountain/Sea View Suite">Executive View Suite</option>
                            <option value="Heritage Royal Villa">Heritage Royal Villa</option>
                          </select>
                        </div>
                      </div>

                      {/* Pricing Summary */}
                      <div className="card bg-light border-0 p-3 rounded-3 mb-3">
                        <div className="d-flex justify-content-between small mb-1">
                          <span>Room Rate per Night:</span>
                          <span>₹{activeHotel.price}</span>
                        </div>
                        <div className="d-flex justify-content-between small mb-1">
                          <span>Duration (2 Nights):</span>
                          <span>₹{activeHotel.price * 2}</span>
                        </div>
                        <div className="d-flex justify-content-between small mb-1">
                          <span>Taxes & GST (12%):</span>
                          <span className="text-success">Included / Free</span>
                        </div>
                        <div className="d-flex justify-content-between fw-bold fs-6 border-top pt-2 mt-1">
                          <span>Total Payable at Hotel:</span>
                          <span className="text-success">₹{activeHotel.price * 2}</span>
                        </div>
                      </div>

                      <button type="submit" className="btn btn-info text-white btn-lg w-100 fw-bold shadow-sm">
                        <i className="bi bi-check2-circle me-1"></i>
                        Confirm Hotel Reservation (In-App)
                      </button>
                    </form>
                  </div>
                ) : (
                  /* Reservation Confirmation Voucher */
                  <div className="modal-body p-4 text-center">
                    <div className="alert alert-success d-inline-block rounded-circle p-3 mb-3 shadow-sm">
                      <i className="bi bi-check-lg display-5 text-success"></i>
                    </div>
                    <h4 className="fw-bold text-success mb-1">Hotel Reservation Confirmed!</h4>
                    <p className="text-muted small mb-3">Your hotel voucher is confirmed via TripNova In-App Engine.</p>

                    <div className="card border-2 border-info bg-light text-start p-3 rounded-4 mx-auto mb-3" style={{ maxWidth: '440px' }}>
                      <div className="d-flex justify-content-between border-bottom pb-2 mb-2">
                        <div>
                          <span className="badge bg-info text-white">TripNova Hotel Voucher</span>
                          <h6 className="fw-bold mb-0 mt-1">{bookingConfirmed.hotel.name}</h6>
                        </div>
                        <div className="text-end">
                          <span className="small text-muted">Booking Ref:</span>
                          <strong className="d-block text-dark">{bookingConfirmed.bookingId}</strong>
                        </div>
                      </div>

                      <div className="row g-2 small mb-2">
                        <div className="col-6">
                          <span className="text-muted">Check-In: </span>
                          <strong>{bookingConfirmed.checkIn}</strong>
                        </div>
                        <div className="col-6">
                          <span className="text-muted">Check-Out: </span>
                          <strong>{bookingConfirmed.checkOut}</strong>
                        </div>
                        <div className="col-12">
                          <span className="text-muted">Room: </span>
                          <strong>{bookingConfirmed.roomType}</strong>
                        </div>
                        <div className="col-12">
                          <span className="text-muted">Guest: </span>
                          <strong>{bookingConfirmed.guest.name} ({bookingConfirmed.guest.phone})</strong>
                        </div>
                      </div>

                      <div className="border-top pt-2 d-flex justify-content-between align-items-center">
                        <span className="small text-muted">Status: Confirmed (Free Cancellation)</span>
                        <span className="fw-bold text-success fs-6">Total: ₹{bookingConfirmed.totalPrice}</span>
                      </div>
                    </div>

                    <button
                      type="button"
                      className="btn btn-outline-dark rounded-pill px-4"
                      onClick={() => setActiveHotel(null)}
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
