import { Routes, Route, Link } from "react-router-dom";
import Home from "./components/Home";
import Profile from "./components/Profile";
import Shop from "./components/Shop";
import ErrorBoundary from "./components/ErrorBoundary";

function App() {
  return (
    <div className="App">
      <nav>
        <ErrorBoundary>
          <Link to="/">Home</Link>
        </ErrorBoundary>
        <ErrorBoundary>
          <Link to="/profile">Profile</Link>
        </ErrorBoundary>
        <ErrorBoundary>
          <Link to="/shop">Shop</Link>
        </ErrorBoundary>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/shop" element={<Shop />} />
      </Routes>
    </div>
  );
}

export default App;
