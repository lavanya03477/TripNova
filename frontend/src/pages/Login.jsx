import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { apiPost } from '../api'

export default function Login() {
  const { user, login } = useAuth()
  const navigate = useNavigate()
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [showGoogleModal, setShowGoogleModal] = useState(false)
  const [googleEmail, setGoogleEmail] = useState('')

  useEffect(() => {
    if (user) {
      navigate('/', { replace: true })
    }
  }, [user, navigate])

  const handleLogin = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)
    try {
      const data = await apiPost('/api/auth/login', { username, email })
      login(data)
      navigate('/')
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleRegister = async () => {
    setError('')
    setLoading(true)
    try {
      const data = await apiPost('/api/auth/register', { username, email })
      login(data)
      navigate('/')
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleGoogle = () => {
    setShowGoogleModal(true)
    setGoogleEmail('')
    setError('')
  }

  const handleGoogleSubmit = async (e) => {
    e.preventDefault()
    if (!googleEmail || !googleEmail.includes('@')) {
      setError('Please enter a valid email address')
      return
    }
    setError('')
    setLoading(true)
    try {
      const emailLower = googleEmail.toLowerCase().trim()
      const data = await apiPost('/api/auth/google', {
        email: emailLower,
        username: username || emailLower.split('@')[0] || 'User',
        name: username || 'Google User',
        googleId: 'demo-' + Date.now(),
      })
      if (data && data.id) {
        login(data)
        setShowGoogleModal(false)
        navigate('/')
      } else {
        setError('Failed to create user. Please try again.')
      }
    } catch (err) {
      console.error('Google login error:', err)
      setError('Google sign-in failed: ' + (err.message || 'Unknown error'))
    } finally {
      setLoading(false)
    }
  }

  const closeGoogleModal = () => {
    setShowGoogleModal(false)
    setGoogleEmail('')
  }

  return (
    <div className="login-bg">
      <div className="login-card card">
        <div className="login-header">
          <div className="brand-orb mx-auto mb-3" />
          <div className="login-wordmark mb-1">TRIPNOVA</div>
          <h2 className="fw-bold mb-1">India Travel Planner</h2>
          <p className="mb-0 opacity-75">An interactive studio for journeys across India</p>
        </div>

        <div className="card-body p-4">
          <form onSubmit={handleLogin}>
            <div className="mb-3">
              <label className="form-label fw-semibold">
                <i className="bi bi-person me-1"></i> Username
              </label>
              <input
                type="text"
                className="form-control form-control-lg"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Your name"
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label fw-semibold">
                <i className="bi bi-envelope me-1"></i> Mail ID
              </label>
              <input
                type="email"
                className="form-control form-control-lg"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="you@example.com"
                required
              />
            </div>

            {error && (
              <div className="alert alert-danger py-2 small" role="alert">
                <i className="bi bi-exclamation-circle me-1"></i>{error}
              </div>
            )}

            <button type="submit" className="btn btn-primary btn-lg w-100 mb-3" disabled={loading}>
              {loading ? (
                <>
                  <span className="spinner-border spinner-border-sm me-2"></span>
                  Please wait...
                </>
              ) : (
                <>
                  <i className="bi bi-box-arrow-in-right me-2"></i>
                  Sign In
                </>
              )}
            </button>
          </form>

          <div className="text-center text-muted small mb-3">— or —</div>

          <button
            type="button"
            className="btn btn-outline-secondary btn-lg w-100 mb-3"
            onClick={handleGoogle}
            disabled={loading}
          >
            <i className="bi bi-google me-2"></i>
            Sign in with Google
          </button>

          <p className="text-center text-muted mb-0 small">
            New user?{' '}
            <button type="button" className="btn btn-link p-0 align-baseline" onClick={handleRegister} disabled={loading}>
              Register here
            </button>
          </p>
        </div>
      </div>

      {/* Google Email Modal */}
      {showGoogleModal && (
        <div className="modal d-block" style={{ backgroundColor: 'rgba(0,0,0,0.5)' }}>
          <div className="modal-dialog modal-dialog-centered">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">
                  <i className="bi bi-google me-2"></i>
                  Sign in with Google
                </h5>
                <button type="button" className="btn-close" onClick={closeGoogleModal} disabled={loading}></button>
              </div>
              <form onSubmit={handleGoogleSubmit}>
                <div className="modal-body">
                  <p className="text-muted small mb-3">Enter your email to continue with Google sign-in:</p>
                  <input
                    type="email"
                    className="form-control form-control-lg"
                    value={googleEmail}
                    onChange={(e) => setGoogleEmail(e.target.value)}
                    placeholder="your.email@gmail.com"
                    autoFocus
                    required
                  />
                  {error && (
                    <div className="alert alert-danger mt-3 py-2 small" role="alert">
                      <i className="bi bi-exclamation-circle me-1"></i>{error}
                    </div>
                  )}
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary" onClick={closeGoogleModal} disabled={loading}>
                    Cancel
                  </button>
                  <button type="submit" className="btn btn-primary" disabled={loading}>
                    {loading ? (
                      <>
                        <span className="spinner-border spinner-border-sm me-2"></span>
                        Signing in...
                      </>
                    ) : (
                      <>
                        <i className="bi bi-google me-2"></i>
                        Continue
                      </>
                    )}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
