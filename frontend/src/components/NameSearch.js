import React, { useState } from 'react';
import { searchByName } from '../services/api';

const NameSearch = ({ onResults, onLoading }) => {
  const [name, setName] = useState('');
  const [options, setOptions] = useState({
    social_media: true,
    email: true,
    phone: true,
    address: true,
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name.trim()) return;

    onLoading(true);
    try {
      const results = await searchByName(name, options);
      onResults(results);
    } catch (error) {
      console.error('Search error:', error);
      alert('Error performing search. Please try again.');
    } finally {
      onLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Name or Username
        </label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Enter name or username..."
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          required
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Search Options
        </label>
        <div className="grid grid-cols-2 gap-4">
          {Object.entries(options).map(([key, value]) => (
            <label key={key} className="flex items-center space-x-2">
              <input
                type="checkbox"
                checked={value}
                onChange={(e) =>
                  setOptions({ ...options, [key]: e.target.checked })
                }
                className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
              />
              <span className="text-sm text-gray-700 capitalize">
                {key.replace('_', ' ')}
              </span>
            </label>
          ))}
        </div>
      </div>

      <button
        type="submit"
        className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors font-medium"
      >
        Search
      </button>
    </form>
  );
};

export default NameSearch;

