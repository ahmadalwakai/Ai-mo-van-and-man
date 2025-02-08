import React from 'react';

const Tracking = () => {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">Track Your Order</h1>
      <p className="mb-4">Enter your order tracking number to get real-time updates on your order status.</p>
      <form className="space-y-4">
        <div>
          <label>Tracking Number</label>
          <input
            type="text"
            name="tracking_number"
            className="w-full p-2 border border-gray-300 rounded"
            required
          />
        </div>
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
          Track Order
        </button>
      </form>
    </div>
  );
};

export default Tracking;