import React from 'react';

const Home = () => {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">Welcome to AI-Powered Moving Service</h1>
      <p className="mb-4">We provide the best moving services using advanced AI technologies to ensure a seamless experience.</p>
      <p className="mb-4">Our services include:</p>
      <ul className="list-disc list-inside mb-4">
        <li>Real-time order tracking</li>
        <li>Dynamic pricing based on various factors</li>
        <li>Fraud detection to ensure secure transactions</li>
        <li>AI-powered chatbot for customer support</li>
      </ul>
      <p>Get started by creating an order or tracking your existing orders.</p>
    </div>
  );
};

export default Home;