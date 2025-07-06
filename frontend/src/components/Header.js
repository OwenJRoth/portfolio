import React, { useState } from 'react';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
    setIsMenuOpen(false);
  };

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-gray-900/90 backdrop-blur-sm border-b border-gray-800">
      <nav className="container mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="text-2xl font-bold text-white">
            Owen Roth
          </div>
          
          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            <button
              onClick={() => scrollToSection('hero')}
              className="text-gray-300 hover:text-white transition-colors duration-200"
            >
              Home
            </button>
            <button
              onClick={() => scrollToSection('projects')}
              className="text-gray-300 hover:text-white transition-colors duration-200"
            >
              Projects
            </button>
            <button
              onClick={() => scrollToSection('contact')}
              className="text-gray-300 hover:text-white transition-colors duration-200"
            >
              Contact
            </button>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            className="md:hidden text-gray-300 hover:text-white"
          >
            <svg
              className="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d={isMenuOpen ? "M6 18L18 6M6 6l12 12" : "M4 6h16M4 12h16M4 18h16"}
              />
            </svg>
          </button>
        </div>

        {/* Mobile Menu */}
        {isMenuOpen && (
          <div className="md:hidden mt-4 py-4 border-t border-gray-800">
            <div className="flex flex-col space-y-4">
              <button
                onClick={() => scrollToSection('hero')}
                className="text-gray-300 hover:text-white transition-colors duration-200 text-left"
              >
                Home
              </button>
              <button
                onClick={() => scrollToSection('projects')}
                className="text-gray-300 hover:text-white transition-colors duration-200 text-left"
              >
                Projects
              </button>
              <button
                onClick={() => scrollToSection('contact')}
                className="text-gray-300 hover:text-white transition-colors duration-200 text-left"
              >
                Contact
              </button>
            </div>
          </div>
        )}
      </nav>
    </header>
  );
};

export default Header;