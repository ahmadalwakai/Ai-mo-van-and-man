import React from 'react';

const Sidebar = () => {
  return (
    <div className="w-64 bg-gray-800 text-white h-screen p-4">
      <h2 className="text-xl font-bold mb-4">Menu</h2>
      <ul>
        <li className="mb-2"><a href="/" className="hover:underline">Home</a></li>
        <li className="mb-2"><a href="/orders" className="hover:underline">Orders</a></li>
        <li className="mb-2"><a href="/pricing" className="hover:underline">Pricing</a></li>
        <li className="mb-2"><a href="/tracking" className="hover:underline">Tracking</a></li>
        <li className="mb-2"><a href="/analytics" className="hover:underline">Analytics</a></li>
        <li className="mb-2"><a href="/login" className="hover:underline">Login</a></li>
        <li className="mb-2"><a href="/signup" className="hover:underline">Signup</a></li>
      </ul>
    </div>
  );
};

export default Sidebar;