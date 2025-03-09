import React, { useState } from "react";
import './MainInterface.css';
// import CaseDetails from "./CaseDetails";

export default function MainInterface() {
    const [casebutton, setCaseFiles] = useState(false);

    const toggleCaseFile = () => {
        setCaseFiles(true);
    }

    return (
        <div className="main-interface">
            <button className="case-file" onClick={toggleCaseFile}>Case File</button>
            <h3 className="logo">hotbot</h3>

            {/* 
            <CaseDetails trigger={casebutton}>
                <h3>Popup</h3>
            </CaseDetails> */}

        {casebutton && (
            <div className="casefiles">
                <div className="popup">
                    {/*victim's image*/}
                    <div className="victimImage">
                        
                    </div>
                    {/*victim info: name, age, height, hair color, eye color, unique identification marks*/}
                    <div className="victimInfo">
                        <p>Name: John Doe</p>
                        <p>Age: 30</p>
                        <p>Height: 6'0"</p>
                        <p>Hair Color: Brown</p>
                        <p>Eye Color: Blue</p>
                        <p>Unique Identification Marks: Scar on left cheek</p>
                        <p>Description: Serial Killer Murder</p>
                    </div>
                    {/* carousel of relatives of this suspect available */}
                    <div className="victimSuspects">
                        <div className="carousel">

                        </div>
                    </div>
                </div>
            </div>
        )}

        </div>
    );
}