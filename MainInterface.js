import React, { useState } from "react";
import './MainInterface.css';
// import CaseDetails from "./CaseDetails";

export default function MainInterface() {
    const [casebutton, setCaseFiles] = useState(false);

    const toggleCaseFile = () => {
        setCaseFiles(true);
    }

    const buttons = [
        { id: 1, label: 'Case 1' },
        { id: 2, label: 'Case 2' },
        { id: 3, label: 'Case 3' },
        { id: 4, label: 'Case 4 ' }
    ];

    return (
        <div className="main-interface">
            <button className="case-file" onClick={toggleCaseFile}>Case File</button>
            <h3 className="logo">hotbot</h3>


            {casebutton && (
                <div className="casefiles">
                    <div className="popup">
                        {/* <div className="othercasebuttons">
                        {buttons.map(button => (<button key={button.id} className="buttons"> {button.label}</button>
                    ))} */}
                        <div className={`othercasebuttons ${casebutton ? 'visible' : ''}`}>
                            {buttons.map(button => (
                                <button key={button.id} className="buttons">{button.label}</button>
                            ))}
                            {/* <button className="button1">Case1</button> */}
                        </div>
                        {/*victim's image*/}
                        <div className="caseNumber">Case 1</div>
                        <div className="victimDetails">
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