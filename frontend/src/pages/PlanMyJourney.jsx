import { useState } from 'react'
import { Link } from 'react-router-dom'
import Navbar from '../components/Navbar'
import { OptionGroup, CLIMATE, TRAVEL_WITH, EXPERIENCE, BUDGET } from '../components/FormOptions'
import { apiPost } from '../api'

export default function PlanMyJourney() {
  const [climate, setClimate] = useState('')
  const [travelWith, setTravelWith] = useState('')
  const [experience, setExperience] = useState('')
  const [budget, setBudget] = useState('')
  const [recommendations, setRecommendations] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const preferences = { climate, travelWith, experience, budget }
  const isComplete = climate && travelWith && experience && budget

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!isComplete) {
      setError('Please select an option for every question.')
      return
    }
    setError('')
    setLoading(true)
    try {
      const data = await apiPost('/api/ai/plan-journey', preferences)
      setRecommendations(data.places)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page-bg">
      <Navbar />
      <main className="container py-4">
        <div className="mb-4">
          <h1 className="fw-bold">Plan My Journey</h1>
          <p className="text-muted">Answer a few questions and our AI will recommend the top 3 places for you.</p>
        </div>

        <div className="card glass-card border-0 mb-4">
          <div className="card-body p-4">
            <div className="progress-pills" aria-hidden="true">
              <span className={climate ? 'on' : ''} />
              <span className={travelWith ? 'on' : ''} />
              <span className={experience ? 'on' : ''} />
              <span className={budget ? 'on' : ''} />
            </div>
            <form onSubmit={handleSubmit}>
              <OptionGroup label="1) Climate do you prefer?" options={CLIMATE} value={climate} onChange={setClimate} name="climate" />
              <OptionGroup label="2) Who are you travelling with?" options={TRAVEL_WITH} value={travelWith} onChange={setTravelWith} name="travelWith" />
              <OptionGroup label="3) What type of experience do you want?" options={EXPERIENCE} value={experience} onChange={setExperience} name="experience" />
              <OptionGroup label="4) What is your approximate budget?" options={BUDGET} value={budget} onChange={setBudget} name="budget" />

              {error && (
                <div className="alert alert-danger py-2 small">
                  <i className="bi bi-exclamation-circle me-1"></i>{error}
                </div>
              )}

              <button type="submit" className="btn btn-warm btn-lg w-100" disabled={loading || !isComplete}>
                {loading ? (
                  <>
                    <span className="spinner-border spinner-border-sm me-2"></span>
                    Getting recommendations...
                  </>
                ) : (
                  <>
                    <i className="bi bi-magic me-2"></i>
                    Submit
                  </>
                )}
              </button>
            </form>
          </div>
        </div>

        {recommendations && (
          <div className="mb-4">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <h5 className="mb-0 fw-bold">
                <i className="bi bi-trophy text-warning me-2"></i>
                Top 3 Recommended Destinations for You
              </h5>
              <span className="badge bg-success-subtle text-success border border-success-subtle px-3 py-2 rounded-pill">
                <i className="bi bi-check2-circle me-1"></i> Click any place to plan your days
              </span>
            </div>
            <div className="row g-3">
              {recommendations.map((p, i) => (
                <div className="col-md-4" key={i}>
                  <div className="card place-card h-100 p-3 shadow-sm border-0 d-flex flex-column justify-content-between">
                    <div>
                      <div className="d-flex align-items-center justify-content-between gap-2 mb-2">
                        <div className="d-flex align-items-center gap-2">
                          <span className="rank-orb">{i + 1}</span>
                          <h6 className="fw-bold mb-0 text-dark">{p.name}</h6>
                        </div>
                        {p.tag && (
                          <span className="badge bg-warning-subtle text-dark border border-warning-subtle rounded-pill">
                            {p.tag}
                          </span>
                        )}
                      </div>
                      <p className="text-muted small mb-3">{p.reason}</p>
                    </div>
                    <div>
                      <Link
                        className="btn btn-warm w-100 d-flex align-items-center justify-content-center gap-2 text-decoration-none shadow-sm"
                        to={`/places-to-visit?place=${encodeURIComponent(p.name)}&travelWith=${encodeURIComponent(travelWith)}`}
                      >
                        <i className="bi bi-calendar2-range"></i>
                        <span>Plan {p.name.split(',')[0]} Itinerary</span>
                        <i className="bi bi-arrow-right"></i>
                      </Link>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        <PlanDoubtAssistant preferences={preferences} hasSubmitted={!!recommendations} />
      </main>
    </div>
  )
}

function PlanDoubtAssistant({ preferences, hasSubmitted }) {
  const [message, setMessage] = useState('')
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)

  const send = async (e) => {
    e.preventDefault()
    if (!message.trim() || loading) return

    const userMsg = message.trim()
    setMessage('')
    setMessages((prev) => [...prev, { role: 'user', text: userMsg }])
    setLoading(true)

    try {
      let answer
      if (hasSubmitted) {
        const data = await apiPost('/api/ai/unsuitable-place', { preferences, place: userMsg })
        answer = data.answer
      } else {
        const data = await apiPost('/api/ai/chat', { message: userMsg, context: { page: 'plan-my-journey' } })
        answer = data.answer
      }
      setMessages((prev) => [...prev, { role: 'assistant', text: answer }])
    } catch {
      setMessages((prev) => [...prev, { role: 'assistant', text: 'Sorry, please try again.' }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="card glass-card border-0 mb-4">
      <div className="card-header bg-transparent border-0 py-3">
        <h5 className="mb-0">
          <i className="bi bi-robot me-2"></i>
          AI Assistant
        </h5>
      </div>
      <div className="card-body">
        <p className="text-muted small mb-3">
          {hasSubmitted
            ? 'Ask about a different place — the AI will explain why it may not suit your preferences.'
            : 'Submit the form first, then ask about places that might not fit your preferences.'}
        </p>
        <div className="chat-box mb-3">
          {messages.map((m, i) => (
            <div key={i} className={`chat-bubble ${m.role}`}>{m.text}</div>
          ))}
          {loading && (
            <div className="chat-bubble assistant">
              <span className="spinner-border spinner-border-sm me-2"></span>
              Thinking...
            </div>
          )}
        </div>
        <form onSubmit={send} className="input-group">
          <input
            type="text"
            className="form-control"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder={hasSubmitted ? 'e.g. Why is Goa not suitable for me?' : 'Ask a travel question...'}
            disabled={loading}
          />
          <button type="submit" className="btn btn-primary" disabled={loading || !message.trim()}>
            <i className="bi bi-send-fill"></i>
          </button>
        </form>
      </div>
    </div>
  )
}
