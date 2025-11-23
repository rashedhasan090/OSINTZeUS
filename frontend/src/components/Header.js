import React from 'react';

const Header = () => {
  return (
    <header className="bg-white shadow-md">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <h1 className="text-2xl font-bold text-gray-800">OSINTZeUS</h1>
            <span className="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">
              Educational Use Only
            </span>
          </div>
          <nav className="flex space-x-4">
            <a href="#about" className="text-gray-600 hover:text-gray-800">
              About
            </a>
            <a href="#docs" className="text-gray-600 hover:text-gray-800">
              Docs
            </a>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;

