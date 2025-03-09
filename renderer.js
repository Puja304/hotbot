import React from "react";
import ReactDOM from "react-dom/client";
import Welcome from "./Welcome"
import MainInterface from "./MainInterface";
import CaseDetails from "./CaseDetails";
import "./welcome.css"

import './style.css';  

const App = () => {
    return (
        <div className="app-frame">
            <Welcome/>
        </div>
    );
};


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App/>)