import React from "react";
import ReactDOM from "react-dom/client";
import Welcome from "./Welcome"
import MainInterface from "./MainInterface";
import CaseDetails from "./CaseDetails";
import Guess from "./Guess";
import "./welcome.css"

import './style.css';  

const bgMusic = new Audio("./music/haunted-forest-309396.mp3");
bgMusic.loop = true;
bgMusic.volume = 0.3;
bgMusic.play();

const App = () => {
    return (
        <div className="app-frame">
            <Guess
            killer="killer"
            weapon="weapon"
            location="location" />
        </div>
    );
};


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App/>)