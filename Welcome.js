import React from "react";
import "./welcome.css"; // Ensure the path is correct in your setup

function gameStart() {
  return (
    <div className="started-game-trial">
      <h1>Started</h1>
    </div>
  );
}

export default function Welcome() {
  return (
    <div className="welcome-page">
      <div className="welcome-story-box">
        {/* The image goes here, pinned to the bottom-right via CSS */}
        <img src="./blood-drop.png" alt="Blood Drop" className="blood-drop" />
        <img src="./blood-left.jpg" alt="Blood Left" className="blood-left" />

        <h1 className="welcome-text">KILLSWITCH</h1>
        <button className="welcome-start-button" onClick={gameStart}>
          start
        </button>
      </div>
    </div>
  );
}