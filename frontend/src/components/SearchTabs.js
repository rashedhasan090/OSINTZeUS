import React, { useState } from 'react';
import NameSearch from './NameSearch';
import ImageSearch from './ImageSearch';
import PhoneSearch from './PhoneSearch';
import EmailSearch from './EmailSearch';
import WiFiSearch from './WiFiSearch';

const SearchTabs = ({ onResults, onLoading }) => {
  const [activeTab, setActiveTab] = useState('name');

  const tabs = [
    { id: 'name', label: 'Name/Username', icon: '👤' },
    { id: 'image', label: 'Image Search', icon: '🖼️' },
    { id: 'phone', label: 'Phone', icon: '📞' },
    { id: 'email', label: 'Email', icon: '📧' },
    { id: 'wifi', label: 'WiFi', icon: '📶' },
  ];

  return (
    <div>
      <div className="flex border-b border-gray-200 mb-4">
        {tabs.map(tab => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`px-6 py-3 font-medium text-sm transition-colors ${
              activeTab === tab.id
                ? 'border-b-2 border-blue-500 text-blue-600'
                : 'text-gray-600 hover:text-gray-800'
            }`}
          >
            <span className="mr-2">{tab.icon}</span>
            {tab.label}
          </button>
        ))}
      </div>

      <div className="mt-4">
        {activeTab === 'name' && (
          <NameSearch onResults={onResults} onLoading={onLoading} />
        )}
        {activeTab === 'image' && (
          <ImageSearch onResults={onResults} onLoading={onLoading} />
        )}
        {activeTab === 'phone' && (
          <PhoneSearch onResults={onResults} onLoading={onLoading} />
        )}
        {activeTab === 'email' && (
          <EmailSearch onResults={onResults} onLoading={onLoading} />
        )}
        {activeTab === 'wifi' && (
          <WiFiSearch onResults={onResults} onLoading={onLoading} />
        )}
      </div>
    </div>
  );
};

export default SearchTabs;

