import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import ProfileForm from './components/ProfileForm'
import Dashboard from './components/Dashboard'
import DailyCheckIn from './components/DailyCheckIn'

function App() {
    const [userId, setUserId] = useState(null)

    return (
        <Router>
            <nav style={{ display: 'flex', gap: '20px', marginBottom: '20px', justifyContent: 'center' }}>
                <Link to="/" style={{ color: 'white', textDecoration: 'none' }}>Dashboard</Link>
                <Link to="/profile" style={{ color: 'white', textDecoration: 'none' }}>Profile</Link>
                <Link to="/checkin" style={{ color: 'white', textDecoration: 'none' }}>Daily Check-in</Link>
            </nav>

            <Routes>
                <Route path="/" element={<Dashboard userId={userId} />} />
                <Route path="/profile" element={<ProfileForm setUserId={setUserId} />} />
                <Route path="/checkin" element={<DailyCheckIn userId={userId} />} />
            </Routes>
        </Router>
    )
}

export default App
