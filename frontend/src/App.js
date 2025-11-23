import React, { useState } from 'react';
import './App.css';
import Header from './components/Header';
import SearchTabs from './components/SearchTabs';
import ResultsPanel from './components/ResultsPanel';
import { SearchProvider } from './context/SearchContext';

function App() {
  const [searchResults, setSearchResults] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <SearchProvider>
      <div className="App min-h-screen">
        <Header />
        <div className="container mx-auto px-4 py-8">
          <div className="max-w-7xl mx-auto">
            <div className="bg-white rounded-lg shadow-2xl p-6 mb-6">
              <h1 className="text-4xl font-bold text-gray-800 mb-2">
                OSINTZeUS 🔍
              </h1>
              <p className="text-gray-600 mb-6">
                Open Source Intelligence Gathering Tool
              </p>
              <SearchTabs 
                onResults={setSearchResults}
                onLoading={setLoading}
              />
            </div>
            
            {searchResults && (
              <ResultsPanel 
                results={searchResults}
                loading={loading}
              />
            )}
          </div>
        </div>
      </div>
    </SearchProvider>
  );
}

export default App;

