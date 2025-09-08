import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
    <p>Welcome</p>
      <Link to="/">🏠 Home</Link>
      <Link to="/about">ℹ️ About</Link>
      <Link to="/contact">📞 Contact</Link>
    </nav>
  );
}

export default Navbar;