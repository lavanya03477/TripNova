import { useEffect, useRef, useState } from 'react'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

// Fix standard Leaflet default icon issues in bundled React
delete L.Icon.Default.prototype._getIconUrl
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-shadow.png',
})

const createCustomPin = (label, color = '#0f766e', isMain = false) => {
  return L.divIcon({
    className: 'custom-leaflet-marker',
    html: `
      <div style="
        background: ${color};
        color: #fff;
        border: 2px solid #fff;
        border-radius: ${isMain ? '12px' : '50%'};
        width: ${isMain ? '34px' : '28px'};
        height: ${isMain ? '34px' : '28px'};
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: ${isMain ? '14px' : '11px'};
        box-shadow: 0 4px 10px rgba(0,0,0,0.35);
        transform: translate(-50%, -50%);
        transition: transform 0.2s ease;
      ">
        ${label}
      </div>
    `,
    iconSize: [isMain ? 34 : 28, isMain ? 34 : 28],
    iconAnchor: [isMain ? 17 : 14, isMain ? 17 : 14],
  })
}

export default function InteractiveMapModal({ place, lat, lng, itinerary, onClose, isInline = false }) {
  const mapContainerRef = useRef(null)
  const mapInstanceRef = useRef(null)
  const markersRef = useRef([])
  const [selectedSpot, setSelectedSpot] = useState(null)

  const centerLat = lat || 20.5937
  const centerLng = lng || 78.9629

  // Flatten all places from the itinerary with day labels
  const allSpots = []
  if (itinerary && Array.isArray(itinerary)) {
    itinerary.forEach((dayItem) => {
      if (dayItem.places && Array.isArray(dayItem.places)) {
        dayItem.places.forEach((p, idx) => {
          allSpots.push({
            ...p,
            day: dayItem.day,
            dayTitle: dayItem.title || `Day ${dayItem.day}`,
            spotIdx: idx + 1,
            lat: p.lat || centerLat + (Math.random() - 0.5) * 0.05,
            lng: p.lng || centerLng + (Math.random() - 0.5) * 0.05,
          })
        })
      }
    })
  }

  useEffect(() => {
    if (!mapContainerRef.current) return

    // Initialize Leaflet map if not created yet
    if (!mapInstanceRef.current) {
      const map = L.map(mapContainerRef.current, {
        center: [centerLat, centerLng],
        zoom: 12,
        zoomControl: true,
      })

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors | TripNova Maps',
        maxZoom: 19,
      }).addTo(map)

      mapInstanceRef.current = map
    }

    const map = mapInstanceRef.current
    map.invalidateSize()

    // Clear previous markers
    markersRef.current.forEach((m) => map.removeLayer(m))
    markersRef.current = []

    const bounds = L.latLngBounds()

    // 1. Add Main Destination Marker
    const mainIcon = createCustomPin('★', '#e85d04', true)
    const mainMarker = L.marker([centerLat, centerLng], { icon: mainIcon })
      .addTo(map)
      .bindPopup(`
        <div style="font-family: Outfit, sans-serif; padding: 4px;">
          <h6 style="margin: 0 0 4px 0; color: #0b1d36; font-weight: bold;">📍 ${place || 'Selected Destination'}</h6>
          <p style="margin: 0; font-size: 12px; color: #5b6b7c;">Primary Journey Destination</p>
          <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(place || 'India')}" target="_blank" rel="noopener noreferrer" style="display: inline-block; margin-top: 6px; font-size: 11px; color: #0f766e; text-decoration: underline; font-weight: 600;">
            Open in Google Maps ↗
          </a>
        </div>
      `)

    bounds.extend([centerLat, centerLng])
    markersRef.current.push(mainMarker)

    // 2. Add Itinerary Attraction Markers
    const colors = ['#0f766e', '#2563eb', '#7c3aed', '#db2777', '#ea580c']

    allSpots.forEach((spot, index) => {
      const dayColor = colors[(spot.day - 1) % colors.length]
      const spotIcon = createCustomPin(`D${spot.day}`, dayColor, false)

      const spotMarker = L.marker([spot.lat, spot.lng], { icon: spotIcon })
        .addTo(map)
        .bindPopup(`
          <div style="font-family: Outfit, sans-serif; min-width: 180px; padding: 2px;">
            <span style="background: ${dayColor}; color: #fff; font-size: 10px; font-weight: 600; padding: 2px 6px; border-radius: 99px;">
              Day ${spot.day} Spot
            </span>
            <h6 style="margin: 6px 0 2px 0; font-size: 13px; font-weight: bold; color: #122033;">${spot.name}</h6>
            <p style="margin: 0 0 4px 0; font-size: 11px; color: #475569;">${spot.highlight || ''}</p>
            <div style="font-size: 10px; color: #64748b; margin-bottom: 6px;">
              ⏱️ ${spot.duration || '2 hours'} &nbsp;|&nbsp; ☀️ ${spot.bestTime || 'Morning'}
            </div>
            <a href="https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(spot.name + ', ' + place)}" target="_blank" rel="noopener noreferrer" style="display: inline-block; font-size: 11px; color: #0f766e; font-weight: 600; text-decoration: underline;">
              Get Directions ↗
            </a>
          </div>
        `)

      spotMarker.on('click', () => {
        setSelectedSpot(spot)
      })

      bounds.extend([spot.lat, spot.lng])
      markersRef.current.push(spotMarker)
    })

    if (bounds.isValid()) {
      map.fitBounds(bounds, { padding: [40, 40], maxZoom: 14 })
    }

    setTimeout(() => {
      map.invalidateSize()
    }, 200)

    return () => {
      // Keep map reference if inline, or cleanup on unmount
    }
  }, [centerLat, centerLng, place, itinerary])

  const focusOnSpot = (spot) => {
    setSelectedSpot(spot)
    if (mapInstanceRef.current && spot.lat && spot.lng) {
      mapInstanceRef.current.flyTo([spot.lat, spot.lng], 15, { duration: 1 })
      // Find matching marker and open popup
      const marker = markersRef.current.find((m) => {
        const pos = m.getLatLng()
        return Math.abs(pos.lat - spot.lat) < 0.0001 && Math.abs(pos.lng - spot.lng) < 0.0001
      })
      if (marker) marker.openPopup()
    }
  }

  const focusMain = () => {
    setSelectedSpot(null)
    if (mapInstanceRef.current) {
      mapInstanceRef.current.flyTo([centerLat, centerLng], 13, { duration: 1 })
      if (markersRef.current[0]) markersRef.current[0].openPopup()
    }
  }

  const content = (
    <div className={`tripnova-map-wrapper ${isInline ? 'inline-mode' : 'modal-mode'}`}>
      <div className="map-header d-flex justify-content-between align-items-center p-3 border-bottom bg-light">
        <div className="d-flex align-items-center gap-2">
          <span className="badge bg-warning text-dark px-2 py-1 rounded-pill">
            <i className="bi bi-geo-alt-fill me-1"></i> Interactive Map
          </span>
          <h5 className="mb-0 fw-bold">{place || 'Destination Map'}</h5>
        </div>
        <div className="d-flex align-items-center gap-2">
          <a
            href={`https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(place || 'India')}`}
            target="_blank"
            rel="noopener noreferrer"
            className="btn btn-outline-primary btn-sm rounded-pill"
          >
            <i className="bi bi-box-arrow-up-right me-1"></i> Open Google Maps
          </a>
          {!isInline && onClose && (
            <button type="button" className="btn-close" onClick={onClose} aria-label="Close"></button>
          )}
        </div>
      </div>

      <div className="row g-0 map-body-row">
        {/* Left Side: Interactive Pin List */}
        <div className="col-md-4 col-lg-3 map-sidebar p-3 border-end bg-white">
          <div className="mb-3">
            <button
              type="button"
              className={`btn btn-sm w-100 text-start d-flex align-items-center justify-content-between p-2 rounded-3 ${
                !selectedSpot ? 'btn-primary' : 'btn-outline-secondary'
              }`}
              onClick={focusMain}
            >
              <span>
                <i className="bi bi-pin-map-fill text-warning me-2"></i>
                <strong>{place} Center</strong>
              </span>
              <span className="badge bg-light text-dark">Pin</span>
            </button>
          </div>

          <h6 className="text-muted small text-uppercase fw-bold mb-2">Itinerary Spots ({allSpots.length})</h6>
          <div className="map-spots-list" style={{ maxHeight: '380px', overflowY: 'auto' }}>
            {allSpots.length === 0 ? (
              <p className="text-muted small">No specific spots loaded yet. Generate itinerary to see attraction pins!</p>
            ) : (
              allSpots.map((spot, idx) => (
                <div
                  key={idx}
                  onClick={() => focusOnSpot(spot)}
                  className={`spot-item-card p-2 mb-2 rounded-3 border cursor-pointer transition-all ${
                    selectedSpot?.name === spot.name ? 'border-primary bg-primary-subtle shadow-sm' : 'bg-light'
                  }`}
                  style={{ cursor: 'pointer' }}
                >
                  <div className="d-flex align-items-center justify-content-between mb-1">
                    <span className="badge bg-dark rounded-pill" style={{ fontSize: '10px' }}>
                      Day {spot.day}
                    </span>
                    <span className="text-muted" style={{ fontSize: '10px' }}>
                      {spot.duration}
                    </span>
                  </div>
                  <div className="fw-semibold text-truncate small">{spot.name}</div>
                  <div className="text-muted text-truncate" style={{ fontSize: '11px' }}>
                    {spot.highlight}
                  </div>
                </div>
              ))
            )}
          </div>
        </div>

        {/* Right Side: Leaflet Map */}
        <div className="col-md-8 col-lg-9 position-relative">
          <div
            ref={mapContainerRef}
            className="tripnova-leaflet-container"
            style={{ width: '100%', height: isInline ? '450px' : '520px', zIndex: 1 }}
          />
        </div>
      </div>
    </div>
  )

  if (isInline) {
    return <div className="card glass-card border-0 mb-4 overflow-hidden">{content}</div>
  }

  return (
    <div
      className="modal d-block"
      tabIndex="-1"
      style={{ backgroundColor: 'rgba(0, 0, 0, 0.65)', zIndex: 1060, backdropFilter: 'blur(4px)' }}
    >
      <div className="modal-dialog modal-xl modal-dialog-centered">
        <div className="modal-content border-0 shadow-lg overflow-hidden rounded-4">{content}</div>
      </div>
    </div>
  )
}
