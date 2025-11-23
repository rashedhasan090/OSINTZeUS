import React, { useState } from 'react';
import { searchByEmail } from '../services/api';

const EmailSearch = ({ onResults, onLoading }) => {
  const [email, setEmail] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!email.trim()) return;

    onLoading(true);
    try {
      const results = await searchByEmail(email);
      onResults(results);
    } catch (error) {
      console.error('Search error:', error);
      alert('Error performing email search. Please try again.');
    } finally {
      onLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Email Address
        </label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Enter email address..."
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          required
        />
      </div>

      <button
        type="submit"
        className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors font-medium"
      >
        Search Email
      </button>
    </form>
  );
};

export default EmailSearch;

