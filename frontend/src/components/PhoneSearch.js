import React, { useState } from 'react';
import { searchByPhone } from '../services/api';

const PhoneSearch = ({ onResults, onLoading }) => {
  const [phone, setPhone] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!phone.trim()) return;

    onLoading(true);
    try {
      const results = await searchByPhone(phone);
      onResults(results);
    } catch (error) {
      console.error('Search error:', error);
      alert('Error performing phone search. Please try again.');
    } finally {
      onLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Phone Number
        </label>
        <input
          type="tel"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          placeholder="Enter phone number (e.g., +1234567890)"
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          required
        />
      </div>

      <button
        type="submit"
        className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors font-medium"
      >
        Search Phone Number
      </button>
    </form>
  );
};

export default PhoneSearch;

