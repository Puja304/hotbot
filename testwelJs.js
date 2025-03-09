import React, { useEffect, useState } from "react";
import "./style.css"; // Ensure the path is correct for your setup

function GameStart() {
  return (
    <div>
      <h2>Game Started!</h2>
      {/* Add additional game logic or navigation here */}
    </div>
  );
}

export default function Welcome() {
  const [showStart, setShowStart] = useState(false);

  // Create stars in the background on component mount
  useEffect(() => {
    createStars();
  }, []);

  const createStars = () => {
    const welcomePage = document.querySelector(".welcome-page");
    if (!welcomePage) return;

    // Clear any existing stars
    const stars = document.querySelectorAll(".star");
    stars.forEach((star) => star.remove());

    // Generate 100 random stars
    for (let i = 0; i < 100; i++) {
      const star = document.createElement("div");
      star.classList.add("star");

      // Random size between 1-3px
      const size = Math.random() * 2 + 1;
      star.style.width = `${size}px`;
      star.style.height = `${size}px`;

      // Random position
      star.style.left = `${Math.random() * 100}%`;
      star.style.top = `${Math.random() * 100}%`;

      // Random animation delay
      star.style.animationDelay = `${Math.random() * 3}s`;

      welcomePage.appendChild(star);
    }
  };

  const handleStartClick = () => {
    setShowStart(true);
  };

  if (showStart) {
    return <GameStart />;
  }

  return (
    <div className="welcome-page">
      <div className="welcome-story-box">
        <p className="welcome-text">KILLSWITCH</p>
        <button className="welcome-start-button" onClick={handleStartClick}>
          START
        </button>
      </div>
    </div>
  );
}
