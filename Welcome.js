// // import React from "react";
// // import "./welcome.css"; // Ensure the path is correct in your setup

// // function gameStart() {
// //   return (
// //     <div className="started-game-trial">
// //       <h1>Started</h1>
// //     </div>
// //   );
// // }

// // export default function Welcome() {
// //   return (
// //     <div className="welcome-page">
// //       <div className="welcome-story-box">
// //         {/* The image goes here, pinned to the bottom-right via CSS */}
// //         <img src="./blood-drop.png" alt="Blood Drop" className="blood-drop" />
// //         <img src="./blood-left.jpg" alt="Blood Left" className="blood-left" />

// //         <h1 className="welcome-text">KILLSWITCH</h1>
// //         <button className="welcome-start-button" onClick={gameStart}>
// //           start
// //         </button>
// //       </div>
// //     </div>
// //   );
// // }

// import React from "react";
// import ReactDOM from "react-dom";
// import "./welcome.css"; // Make sure this path is correct

// function Welcome() {
//   const handleGameStart = () => {
//     // Try different methods to communicate with Streamlit
//     try {
//       // Method 1: Click the hidden Streamlit button
//       const streamlitButton = window.parent.document.querySelector('button[data-testid="baseButton-secondary"]');
//       if (streamlitButton) {
//         streamlitButton.click();
//       } else {
//         console.log("Streamlit button not found");
        
//         // Method 2: Use Streamlit messaging if method 1 fails
//         window.parent.postMessage({
//           type: "streamlit:setComponentValue",
//           value: true
//         }, "*");
//       }
//     } catch (e) {
//       console.error("Error communicating with Streamlit:", e);
//     }
//   };

//   return (
//     <div className="welcome-page">
//       <div className="welcome-story-box">
//         <img src="./blood-drop.png" alt="Blood Drop" className="blood-drop" />
//         <img src="./blood-left.jpg" alt="Blood Left" className="blood-left" />
//         <h1 className="welcome-text">KILLSWITCH</h1>
//         <button className="welcome-start-button" onClick={handleGameStart}>
//           start
//         </button>
//       </div>
//     </div>
//   );
// }

// // Render the Welcome component to the DOM
// const rootElement = document.getElementById("root");
// if (rootElement) {
//   ReactDOM.render(<Welcome />, rootElement);
// } else {
//   console.error("Root element not found");
// }

// export default Welcome;

import React from "react";
import ReactDOM from "react-dom";
import "./welcome.css"; // Make sure this path is correct

function Welcome() {
  const handleGameStart = () => {
    // Try multiple methods to communicate with the parent window
    try {
      // Method 1: Direct message to parent
      window.parent.postMessage('start', '*');
      
      // Method 2: Try to find and click the button directly
      setTimeout(() => {
        try {
          const button = window.parent.document.querySelector('button[data-testid="baseButton-secondary"]');
          if (button) {
            button.click();
            console.log("Button clicked");
          } else {
            console.log("Button not found");
          }
        } catch (e) {
          console.error("Error finding button:", e);
        }
      }, 100);
    } catch (e) {
      console.error("Error communicating with parent:", e);
    }
  };

  return (
    <div className="welcome-page">
      <div className="welcome-story-box">
        {/* Use relative paths - if images are in build folder with bundle.js */}
        <img src="blood-drop.png" alt="Blood Drop" className="blood-drop" />
        <img src="blood-left.jpg" alt="Blood Left" className="blood-left" />
        <h1 className="welcome-text">KILLSWITCH</h1>
        <button className="welcome-start-button" onClick={handleGameStart}>
          start
        </button>
      </div>
    </div>
  );
}

// Check if we're in a browser environment before trying to render
if (typeof document !== 'undefined') {
  const rootElement = document.getElementById("root");
  if (rootElement) {
    ReactDOM.render(<Welcome />, rootElement);
  }
}

export default Welcome;