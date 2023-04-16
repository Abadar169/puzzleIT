import React from "react";

function Instructions({ examData, setView, startTimer }) {
  return (
    <div className="flex flex-col items-center gap-5">
      <h1 className="text-2xl underline login">Introduction</h1>

      <div className="flex">
        <p className="text-xl text-center">
          Welcome to the Escape Room experience of a lifetime! In this immersive
          adventure, you will step into the shoes of a falsely accused prisoner
          who has been wrongly convicted and sent to prison. But you're not
          going to just sit around and wait for someone to come to your rescue -
          you're going to take matters into your own hands and escape from
          prison!<br />
          But beware, there is a catch. One wrong move, one misstep, and
          you could find yourself in a dead-end with no way out. This game will
          put your skills, patience and intelligence to the ultimate test, and
          only the most resourceful players will emerge victorious.<br /> But escaping
          won't be easy. You'll need to solve a series of challenging clues and
          puzzles that have been cleverly hidden throughout the prison and note
          it down. <br />With every twist and turn, you'll find yourself getting
          closer to freedom and closer to the truth. But you'll need to stay
          sharp and use your wits if you want to make it out in time. Are you
          ready to take on the challenge and prove your innocence? The clock is
          ticking, and the escape room awaits!
        </p>
      </div>

      <div className="flex">
        <button
          className="primary-outlined-btn flex flex-col"
          type="submit"
          onClick={() => {
            // window.localStorage.setItem("secondsLeft",examData.duration);
            startTimer();
            setView("questions");
            window.localStorage.setItem("view", "questions");
          }}
        >
          Start Puzzle
        </button>
      </div>
    </div>
  );
}

export default Instructions;
