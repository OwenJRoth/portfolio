import React from 'react';

const Hero = () => {
  return (
    <section
      id="hero"
      className="min-h-screen flex items-center justify-center relative overflow-hidden"
      style={{
        backgroundImage: 'url("https://images.unsplash.com/photo-1591439657848-9f4b9ce436b9")',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat'
      }}
    >
      {/* Overlay */}
      <div className="absolute inset-0 bg-black/70"></div>
      
      {/* Content */}
      <div className="relative z-10 text-center px-6 max-w-4xl mx-auto">
        <h1 className="text-5xl md:text-7xl font-bold text-white mb-6">
          Owen Roth's
          <span className="block text-blue-400">Portfolio</span>
        </h1>
        <p className="text-xl md:text-2xl text-gray-300 mb-8 max-w-2xl mx-auto">
          Full-Stack Developer & Game Developer specializing in Python, JavaScript, and Unity
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <button
            onClick={() => document.getElementById('projects').scrollIntoView({ behavior: 'smooth' })}
            className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold transition-colors duration-200"
          >
            View Projects
          </button>
          <button
            onClick={() => document.getElementById('contact').scrollIntoView({ behavior: 'smooth' })}
            className="border-2 border-blue-600 text-blue-600 hover:bg-blue-600 hover:text-white px-8 py-3 rounded-lg font-semibold transition-colors duration-200"
          >
            Get In Touch
          </button>
        </div>
      </div>

      {/* Scroll Indicator */}
      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
        <svg
          className="w-6 h-6 text-white"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M19 14l-7 7m0 0l-7-7m7 7V3"
          />
        </svg>
      </div>
    </section>
  );
};

export default Hero;