import React from "react";
import ReactDOM from "react-dom/client";
import Body from "./Body"
import './style.css';  

const App = () => {
    return (
        <div>
            <Body/>
            <div className="song-picture">
                <img src="https://static.vecteezy.com/system/resources/thumbnails/002/723/534/small_2x/abstract-paint-pastel-purple-background-free-vector.jpg"/>
            </div>
        </div>
    );
};


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App/>)