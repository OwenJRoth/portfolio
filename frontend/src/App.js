import React from "react";
import "./App.css";
import Header from "./components/Header";
import Hero from "./components/Hero";
import ProjectSection from "./components/ProjectSection";
import Contact from "./components/Contact";

function App() {
  return (
    <div className="App bg-gray-900 min-h-screen">
      <Header />
      <Hero />
      <ProjectSection />
      <Contact />
    </div>
  );
}

export default App;
