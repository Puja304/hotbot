import React from "react";


function gameStart()
{
    return (
        <div className="started-game-trial">
            <h1>Started</h1>
        </div>
    )
}

export default function Welcome()
{

    return (
        <div className="welcome-page">
            <div className="welcome-story-box">
                <h1 className="welcome-text">
                   KILLSWITCH
                </h1>   
                <h3 className="welcome-tagline">
                    a funny and witty tagline
                </h3>
                <button className="welcome-start-button" onClick={gameStart}>start</button>
            </div>
        </div>
    )
}