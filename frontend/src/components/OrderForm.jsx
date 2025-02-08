import React, { useState } from 'react';
import axios from 'axios';

const OrderForm = () => {
  const [formData, setFormData] = useState({
    origin: '',
    destination: '',
    items: '',
    floor_origin: '',
    elevator_origin: false,
    floor_dest: '',
    elevator_dest: false,
    scheduled_time: '',
    special_instructions: '',
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/orders', formData);
      console.log('Order created:', response.data);
    } catch (error) {
      console.error('Error creating order:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label>Origin</label>
        <input
          type="text"
          name="origin"
          value={formData.origin}
          onChange={handleChange}
          className="w-full p-2 border border-gray-300 rounded"
          required
        />
      </div>
      <div>
        <label>Destination</label>
        <input
          type="text"
          name="destination"
          value={formData.destination}
          onChange={handleChange}
          className="w-full p-2 border border-gray-300 rounded"
          required
        />
      </div>
      <div>
        <label>Items</label>
        <input
          type="text"
          name="items"
          value={formData.items}
          onChange={handleChange}
          className="w-full p-2 border border-gray-300 rounded"
          required
        />
      </div>
      <div>
        <label>Floor Origin</label>
        <input
          type="number"
          name="floor_origin"
          value={formData.floor_origin}
          onChange={handleChange}
          className="w-full p-2 border border-gray-300 rounded"
          required
        />
      </div>
      <div>
        <label>
          <input
            type="checkbox"
            name="elevator_origin"
            checked={formData.elevator_origin}
            onChange={handleChange}
          />
          Elevator at Origin
        </label>
      </div>
      <div>
        <label>Floor Destination</label>
        <input
          type="number"
          name="floor_dest"
          value={formData.floor_dest}
          onChange={handleChange}
          className="w-full p-2 border border-gray-300 rounded"
          required
        />
      </div>
      <div>
        <label>
          <input
            type="checkbox"
            name="elevator_dest"
            checked={formData.elevator_dest}
            onChange={handleChange}
          />
          Elevator at Destination
        </label>
      </div>
      <div>
        <label>Scheduled Time</label>
        <input
          type="datetime-local"
          name="scheduled_time"
          value={formData.scheduled_time}
          onChange={handleChange}
          className="w-full p-2 border border-gray-300 rounded"
          required
        />
      </div>
      <div>
        <label>Special Instructions</label>
        <textarea
          name="special_instructions"
          value={formData.special_instructions}
          onChange={handleChange}
          className="w-full p-2 border border-gray-300 rounded"
        ></textarea>
      </div>
      <button type="submit" className="bg-blue-500 text-white p-2 rounded">
        Create Order
      </button>
    </form>
  );
};

export default OrderForm;