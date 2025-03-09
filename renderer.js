import React from "react";
import ReactDOM from "react-dom/client";
import Welcome from "./Welcome"
import MainInterface from "./MainInterface";
import CaseDetails from "./CaseDetails";
import "./welcome.css"

import './style.css';  

const bgMusic = new Audio("./assets/music.mp3");
bgMusic.loop = true;
bgMusic.volume = 0.5;
bgMusic.play();

const App = () => {
    return (
        <div className="app-frame">
            <Welcome/>
        </div>
    );
};


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App/>)