import { Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider, useAuth } from './context/AuthContext'
import Login from './pages/Login'
import Home from './pages/Home'
import PlanMyJourney from './pages/PlanMyJourney'
import PlacesToVisit from './pages/PlacesToVisit'
import BusBooking from './pages/BusBooking'
import TrainBooking from './pages/TrainBooking'
import Hotels from './pages/Hotels'

function ProtectedRoute({ children }) {
  const { user } = useAuth()
  if (!user) return <Navigate to="/login" replace />
  return children
}

export default function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<ProtectedRoute><Home /></ProtectedRoute>} />
        <Route path="/plan-my-journey" element={<ProtectedRoute><PlanMyJourney /></ProtectedRoute>} />
        <Route path="/places-to-visit" element={<ProtectedRoute><PlacesToVisit /></ProtectedRoute>} />
        <Route path="/bus-booking" element={<ProtectedRoute><BusBooking /></ProtectedRoute>} />
        <Route path="/train-booking" element={<ProtectedRoute><TrainBooking /></ProtectedRoute>} />
        <Route path="/bus-train" element={<Navigate to="/bus-booking" replace />} />
        <Route path="/hotels" element={<ProtectedRoute><Hotels /></ProtectedRoute>} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </AuthProvider>
  )
}
