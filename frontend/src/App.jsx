import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Home from './pages/Home.jsx'
import Navbar from './pages/navbar.jsx'

function App() {

  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  )
}

export default App
