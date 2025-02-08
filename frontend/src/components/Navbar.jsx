import { Link } from "react-router-dom";
import { FaTruckMoving } from "react-icons/fa";

const Navbar = () => {
  return (
    <nav className="bg-blue-600 text-white p-4 shadow-md flex justify-between items-center">
      <div className="flex items-center gap-2">
        <FaTruckMoving size={28} />
        <Link to="/" className="text-xl font-bold">MO VAN AND MAN</Link>
      </div>
      <ul className="hidden md:flex gap-6">
        <li><Link to="/" className="hover:text-gray-200">Home</Link></li>
        <li><Link to="/orders" className="hover:text-gray-200">Orders</Link></li>
        <li><Link to="/pricing" className="hover:text-gray-200">Pricing</Link></li>
        <li><Link to="/tracking" className="hover:text-gray-200">Tracking</Link></li>
      </ul>
      <button className="md:hidden p-2 rounded bg-white text-blue-600">☰</button>
    </nav>
  );
};

export default Navbar;
