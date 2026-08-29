import { useEffect, useRef, useState } from 'react'
import { apiPost } from '../api'

const SUGGESTIONS = [
  'Best time to visit Kerala?',
  'Family trip in Rajasthan',
  'Hidden hill stations',
  'Vegetarian food trail',
]

export default function AIAssistant({ title = 'AI Assistant', context = null, placeholder }) {
  const [message, setMessage] = useState('')
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)
  const boxRef = useRef(null)

  useEffect(() => {
    if (boxRef.current) boxRef.current.scrollTop = boxRef.current.scrollHeight
  }, [messages, loading])

  const sendText = async (userMsg) => {
    if (!userMsg.trim() || loading) return
    setMessage('')
    setMessages((prev) => [...prev, { role: 'user', text: userMsg }])
    setLoading(true)
    try {
      const data = await apiPost('/api/ai/chat', { message: userMsg, context })
      setMessages((prev) => [...prev, { role: 'assistant', text: data.answer }])
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: 'assistant', text: 'Sorry, something went wrong. Please try again.' },
      ])
    } finally {
      setLoading(false)
    }
  }

  const send = (e) => {
    e.preventDefault()
    sendText(message)
  }

  return (
    <div className="card glass-card border-0 mb-4">
      <div className="card-header bg-transparent border-0 py-3">
        <h5 className="mb-0">
          <i className="bi bi-stars text-warning me-2"></i>
          {title}
        </h5>
      </div>
      <div className="card-body pt-0">
        <div className="d-flex flex-wrap gap-2 mb-3">
          {SUGGESTIONS.map((s) => (
            <button key={s} type="button" className="quick-chip" onClick={() => sendText(s)} disabled={loading}>
              {s}
            </button>
          ))}
        </div>
        <div className="chat-box mb-3" ref={boxRef}>
          {messages.length === 0 && (
            <p className="text-muted mb-0 small">
              <i className="bi bi-chat-dots me-1"></i>
              {placeholder || 'Ask me anything about travelling in India!'}
            </p>
          )}
          {messages.map((m, i) => (
            <div key={i} className={`chat-bubble ${m.role}`}>
              {m.text}
            </div>
          ))}
          {loading && (
            <div className="chat-bubble assistant">
              <span className="spinner-border spinner-border-sm me-2" role="status"></span>
              Mapping ideas...
            </div>
          )}
        </div>
        <form onSubmit={send} className="input-group">
          <input
            type="text"
            className="form-control"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your question..."
            disabled={loading}
          />
          <button type="submit" className="btn btn-success" disabled={loading || !message.trim()}>
            <i className="bi bi-send-fill"></i>
          </button>
        </form>
      </div>
    </div>
  )
}
