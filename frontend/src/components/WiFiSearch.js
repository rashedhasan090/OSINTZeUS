import React, { useState } from 'react';
import { searchWiFi } from '../services/api';

const WiFiSearch = ({ onResults, onLoading }) => {
  const [location, setLocation] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    onLoading(true);
    try {
      const results = await searchWiFi(location);
      onResults(results);
    } catch (error) {
      console.error('Search error:', error);
      alert('Error performing WiFi scan. Please try again.');
    } finally {
      onLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-4">
        <p className="text-sm text-yellow-800">
          ⚠️ <strong>Warning:</strong> WiFi scanning requires proper authorization and may be restricted. 
          Only use on networks you own or have explicit permission to scan.
        </p>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Location (Optional)
        </label>
        <input
          type="text"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          placeholder="Enter location (optional)..."
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        />
      </div>

      <button
        type="submit"
        className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors font-medium"
      >
        Scan WiFi Networks
      </button>
    </form>
  );
};

export default WiFiSearch;

