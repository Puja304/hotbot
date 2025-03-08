import React from "react";
import ReactDOM from "react-dom/client";
import Welcome from "./Welcome"
import MainInterface from "./MainInterface";
import CaseDetails from "./CaseDetails";

import './style.css';  

const App = () => {
    return (
        <div className="app-frame">
            <h1>Blank pages</h1>
        </div>
    );
};


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App/>)