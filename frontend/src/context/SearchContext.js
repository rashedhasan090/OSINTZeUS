import React, { createContext, useContext, useState } from 'react';

const SearchContext = createContext();

export const useSearch = () => {
  const context = useContext(SearchContext);
  if (!context) {
    throw new Error('useSearch must be used within SearchProvider');
  }
  return context;
};

export const SearchProvider = ({ children }) => {
  const [searchHistory, setSearchHistory] = useState([]);
  const [currentResults, setCurrentResults] = useState(null);

  const addToHistory = (search) => {
    setSearchHistory((prev) => [search, ...prev].slice(0, 50)); // Keep last 50
  };

  return (
    <SearchContext.Provider
      value={{
        searchHistory,
        currentResults,
        setCurrentResults,
        addToHistory,
      }}
    >
      {children}
    </SearchContext.Provider>
  );
};

