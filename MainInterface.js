import React, { useState } from "react";
import Slider from "react-slick";
import './MainInterface.css';
import CaseData from './case_data.json';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

export default function MainInterface() {
    const [selectedCase, setSelectedCase] = useState(1);

    const selectCase = (caseId) => {
        setSelectedCase(caseId);
    };

    const buttons = [
        { id: 1, label: 'Case 1' },
        { id: 2, label: 'Case 2' },
        { id: 3, label: 'Case 3' },
        { id: 4, label: 'Case 4' }
    ];

    const settings = {
        dots: true,
        infinite: false,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        arrows: true,
        pauseOnHover: true,
    };

    // Retrieve victim data for the selected case (assuming case IDs are 1-indexed)
    const victimData = CaseData.victims[selectedCase - 1];

    return (
        <div className="main-interface">
                <div className="casefiles">
                    <div className="popup">
                        <div className="bookmarks">
                            {buttons.map(button => (
                                <div className="button-wrapper" key={button.id}>
                                    <div className="button-item">
                                        <button 
                                            className="buttons" 
                                            onClick={() => selectCase(button.id)}
                                        >
                                            {button.label}
                                        </button>
                                    </div>
                                </div>
                            ))}
                        </div>
                        {victimData && (
                            <div>
                                <div className="caseNumber">Case {selectedCase}</div>
                                <div className="victimDetails">
                                    <div className="victimImage"></div>
                                    <div className="victimInfo">
                                        <p>Name: {victimData.victim_name}</p>
                                        <p>Age: {victimData.victim_age}</p>
                                        <p>Height: {victimData.victim_height}</p>
                                        <p>Hair Color: {victimData.victim_hair}</p>
                                        <p>Eye Color: {victimData.victim_eye}</p>
                                        <p>Identification: {victimData.victim_identification}</p>
                                        <p>Description: {victimData.victim_desc}</p>
                                    </div>
                                </div>
                                <div className="victimSuspects">
                                    <div className="suspects">Suspects</div>
                                    <Slider {...settings} className="carousel">
                                        <div>
                                            <p>{(victimData.victim_relation_desc1)}</p>
                                        </div>
                                        <div>
                                            <p>{victimData.victim_relation_desc2}</p>
                                        </div>
                                        <div>
                                            <p>{victimData.victim_relation_desc3}</p>
                                        </div>
                                    </Slider>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
        </div>
    );
}
