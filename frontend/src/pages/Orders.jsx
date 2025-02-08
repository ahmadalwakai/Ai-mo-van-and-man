import React from 'react';
import OrderForm from '../components/OrderForm';

const Orders = () => {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">Create a New Order</h1>
      <OrderForm />
    </div>
  );
};

export default Orders;