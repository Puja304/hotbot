import React, {useState, useEffect, useRef} from "react";
import "./guess.css"
import Victory from "./Victory";

export default function Guess({killer, weapon, location}) {

    const [guessButton, setGuessButton] = useState(false);
    const [isOn, setIsOn] = useState(true);
    const isFirstRun = useRef(true); // Track initial renderx

    const toggleGuess = () => 
    {
      setGuessButton(!guessButton);
    }

    const toggleOn = () => 
    {
      setIsOn(!isOn);
    }

    useEffect(() => {
      if (isFirstRun.current) {
        isFirstRun.current = false; // Mark first run as done
        return; // Prevent execution on first render
      }
  
      // Here is your effect for toggling guess
      toggleGuess();
      toggleGuess();
    }, [isOn]); // Runs only when `isOn` is changed after the first time

    useEffect(() => {
        let guess_button = document.getElementsByClassName("guess-open")[0];
        if (guessButton) {
          guess_button.style.display = "none";
          // You can call any function here or run any side effects
        }

        if(!guessButton)
        {
            guess_button.style.display = "block";
        }
      }, [guessButton]); // The useEffect will run every time guessButton changes

    const [userKiller, setKiller] = useState("");
    const [userWeapon, setWeapon] = useState("");
    const [userLocation, setLocation] = useState("");
    const [notification, setNotification] = useState(false);

    const showNotification = (message) => {
      setNotification(message);
      setTimeout(() => {
        setNotification(false);
      }, 1000); // Hide after 5 seconds
    };

    const closeForm = () => {
      setGuessButton(false);
      setKiller("");
      setWeapon("");
      setLocation("");
      setTime("");
      setAlibi("");
    };

    const declareVictory = () => 
    {
      return (
          <Victory/>
      )
    }
    const assessVictory = () => 
    {
      if ((userKiller == killer) &&
      (userWeapon == weapon) &&
      (userLocation == location)
      )
      {
        toggleGuess();
        toggleOn();
        declareVictory();
      }
      else{
        showNotification("Wrong Guess! Try Again.");
      }
    }

    const handleSubmit = (e) => {
      e.preventDefault(); // Prevent page refresh
      assessVictory()
      // Close the pop-up after submission
      closeForm();
  };

    return (
    <div className='guess-main-body'>
      <button className="guess-open" onClick={toggleGuess}>Guess</button>
      {guessButton && isOn && (
        <div className='guess-pop-up'>
            {notification && (
              <div className={`notification ${notification ? "show" : ""}`}>
                {notification}
              </div>
      )}
         <div className="guess-close-div"> 
          <button className="guess-close" onClick={closeForm}>❌</button>
        </div>
          <h2 className="guess-title">details about the killer</h2>
          <form className='guess-form'>
            <div className="guess-form-pair">
                <label for="Name">Name:</label>
                <input type='text' id="Name" value={userKiller} onChange={(e) => setKiller(e.target.value)} ></input>
            </div>
            <div className="guess-form-pair">
                <label for="Name">Weapon:</label>
                <input type='text' id="Weapon" value={userWeapon} onChange={(e) => setWeapon(e.target.value)}></input>
            </div>
            <div className="guess-form-pair">
                <label for="Name">Location:</label>
                <input type='text' id="Location" value={userLocation} onChange={(e) => setLocation(e.target.value)}></input>
            </div>
          </form>
          <button type="submit" className="guess-submit" onClick={assessVictory}>Submit</button>
        </div>
      )
      }

    </div>
  )
}