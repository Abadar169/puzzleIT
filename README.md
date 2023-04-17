
# PuzzleIt

The website is an interactive puzzle game designed to test participants Soft Skills. The game is presented as an escape room adventure in which participants assume the role of a falsely accused prisoner who is attempting to escape from prison.
The escape room is designed to test and analyze various soft skills, such as critical thinking, problem-solving, and attention to detail, among others.

Participants must solve a series of challenging clues and puzzles cleverly hidden throughout the prison to find a way out. The puzzles involve decoding messages, searching for specific items, and putting together clues to unlock doors and discover hidden passageways.

Overall, the website and escape room are a fun and engaging way to test and improve participants' soft skills, such as critical thinking, problem-solving, and attention to detail.



## Technologies Used

- React - Frontend framework
- Redux - State management tool
- AntD  - Design Library
- Node.js - Backend runtime environment
- Express.js - Backend routing purpose
- MongoDB - Database


## Installation

Clone the repository: You can clone the repository using Git by running the following command in your terminal or command prompt:

```bash
  git clone https://github.com/Abadar169/puzzleIT.git

```

Install dependencies: Navigate to the project directory and install the required dependencies by running the following command:

```bash
    npm install
```

Navigate to the project directory and Run the project: you can start the project by running the following command:
```bash
    cd client
    npm start
```




    
## Escape Room Puzzle 
Intro : 
Welcome to the Escape Room experience of a lifetime! In this immersive adventure, you will step into the shoes of a falsely accused prisoner who has been wrongly convicted and sent to prison. But you're not going to just sit around and wait for someone to come to your rescue - you're going to take matters into your own hands and escape from prison!

But beware, there is a catch. One wrong move, one misstep, and you could find yourself in a dead-end with no way out. This game will put your skills, patience and intelligence to the ultimate test, and only the most resourceful players will emerge victorious.

But escaping won't be easy. You'll need to solve a series of challenging clues and puzzles that have been cleverly hidden throughout the prison and note it down.

With every twist and turn, you'll find yourself getting closer to freedom and closer to the truth. But you'll need to stay sharp and use your wits if you want to make it out in time. Are you ready to take on the challenge and prove your innocence? The clock is ticking, and the escape room awaits!

### Solution
- To solve this question, you need to examine the image of the note that slipped out of the guard's pocket. The note contains a series of letters that are arranged in a specific pattern which spells out the word "KEY". This means that you need to search for a key that will help you escape the prison.

- To solve the second question in the escape room, you need to carefully observe your surroundings and look for any potential clues that could help you escape.

- You are given a link to a jigsaw puzzle in the third question. After solving the puzzle, you will see the phrase "For The Party" in which "For The" is in green color and "Party" is in red color, which represents danger. Therefore, you should consider "For The" as the answer that will help you decode the last question.

- You're in the final stretch of your escape plan, but there is some crucial information to be decrypted to choose from in terms of your escape route. (Hint: escape party = guecrg rctva) Code given: hktg gzkv. It decodes to Fire Exit.

- The fifth question in the Escape Room requires the player to use all the clues collected so far to find a solution to unlock the exit door and escape. The previous answers and clues must be carefully analyzed and pieced together to find the correct combination or solution to unlock the door and escape the prison. Answer - Key for the fire exit 42211

### Dead-ends of Escape Room
- To avoid getting stuck in the escape room, it's important to stay alert and on the lookout for any potential clues, especially in the second question. The user must precisely count the pens and arrange them in accordance with the provided solution; otherwise, they won't be able to decipher the key to unlock the final exit door.
- The second dead end is that in the third question, the user is required to solve a jigsaw puzzle to decrypt the hint. The puzzle says "For The Party," where "For The" is in green color and "Party" is in red color, representing danger. So, the phrase in green is to be considered as the answer because it helps in finding the answer to the final hint. This can be confusing and time-consuming for users who are not familiar with jigsaw puzzles.

## Features
- The website provides authentication, allowing individuals to create an account with their email address and password in order to participate in the game.
- A dashboard for the admin where the progress of all the users can be tracked & analyzed
- The admin dashboard that offers multiple functionalities, such as presenting the results of all users who took the exam, including exam name, username, exam date, total clues, required clues, clues found, and verdict.
- The admin has the ability to add new exams that assess different soft skills. The current categories available for assessment include critical thinking, time management, and teamwork.
- The admin has the authority to make changes to the exam questions, such as adding or removing questions based on their preferences.
- There is a separate reports page available for the admin, the admin has the option to sort the results based on either the name of the exam or the username of the user who took the exam.
- There is a dedicated page for exams which shows complete information about each puzzle including its name, duration in seconds, category, total number of clues and clues required to solve it.
- The user's report page shows the results of both the current puzzle and previously solved puzzles.
- The website includes a timer for each puzzle, and if the exam is not completed within the given time, it is automatically submitted. The timer can also be used to assess the user's accuracy.
- The website has a testing directory that contains all the Selenium scripts utilized to test different pages of the website, including the Login Page, Register Page, Admin reports page, and more.
