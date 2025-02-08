import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Orders from './pages/Orders';
import Pricing from './pages/Pricing';
import Tracking from './pages/Tracking';
import Analytics from './pages/Analytics';
import Login from './pages/Login';
import Signup from './pages/Signup';

const App = () => {
  return (
    <Router>
      <div className="flex">
        <Sidebar />
        <div className="flex-1">
          <Navbar />
          <main className="p-4">
            <Switch>
              <Route path="/" component={Home} exact />
              <Route path="/orders" component={Orders} />
              <Route path="/pricing" component={Pricing} />
              <Route path="/tracking" component={Tracking} />
              <Route path="/analytics" component={Analytics} />
              <Route path="/login" component={Login} />
              <Route path="/signup" component={Signup} />
            </Switch>
          </main>
          <Footer />
        </div>
      </div>
    </Router>
  );
};

export default App;