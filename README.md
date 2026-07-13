# python
This repository contains python project 
<br>
made by Deep

# project information
# 📝 Python To-Do List

A simple command-line To-Do List application built using Python. This project allows users to create separate task lists, add and view tasks, delete tasks, and mark tasks as completed.

## ✨ Features

* Create multiple To-Do List files
* Add multiple tasks to a list
* View all saved tasks
* Delete a task using its line number
* Mark tasks as completed with a ✔️ symbol
* Automatically create a folder to store task files
* Save tasks permanently in text files

## 🛠️ Technologies Used

* Python 3
* Python File Handling
* Python `os` module

## 📂 Project Structure

```text
To-Do-List/
│
├── to_do_list.py
│
└── To_do_list/
    └── task_file.txt
```

The `To_do_list` folder is automatically created when the program runs.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/deep050601/python.git
```

### 2. Open the repository folder

```bash
cd python
```

### 3. Run the To-Do List program

```bash
python to_do_list.py
```
## 📖 How to Use

After running the program, select an option from the menu:

```text
1 - View tasks
2 - Create a new task list
3 - Delete a task
4 - Mark a task as completed
```

Enter the requested file name and follow the instructions displayed in the terminal.

## 💡 Example

```text
----------Welcome to To_Do_List App----------

1 - View Task
2 - Create New File
3 - Delete Task
4 - Mark Task as Done
```

Completed tasks are displayed like this:

```text
Complete Python project  =  ✔️ complete
```

## 🔮 Future Improvements

* Add an option to edit existing tasks
* Add task numbers automatically
* Add task deadlines and priorities
* Improve input validation
* Add a graphical user interface (GUI)
* Store tasks using a database



### 2. 🧮 GUI Calculator

A simple graphical calculator application built using Python and Tkinter. It provides an easy-to-use interface for performing basic mathematical calculations.

**Features:**

* Perform addition (`+`)
* Perform subtraction (`-`)
* Perform multiplication (`×`)
* Perform division (`÷`)
* Supports decimal numbers
* Clear the display using the `AC` button
* Display calculation results instantly
* Show an error message for invalid calculations
* Simple graphical user interface

**Concepts Used:**

* Python functions
* Tkinter GUI library
* Buttons and entry widgets
* Grid layout management
* Lambda functions
* Exception handling
* Event-driven programming

**Run the project:**

```bash
python claculator.py
```

**Future Improvements:**

* Add percentage calculations
* Add square root functionality
* Add calculation history
* Add keyboard input support
* Improve the user interface
* Add scientific calculator functions

---

### 3. 🎵 YouTube Audio Downloader

A simple command-line Python application that downloads the best available audio from a user-provided YouTube URL using the `yt-dlp` library.

> This project is intended for downloading content you own, content you have permission to download, or content whose license allows downloading.

**Features:**

* Accepts a YouTube URL from the user
* Downloads the best available audio quality
* Automatically uses the original video title as the file name
* Saves the downloaded audio in the current project folder
* Provides a simple command-line interface
* Displays a confirmation message after the download is completed

**Technologies and Libraries Used:**

* Python 3
* `yt-dlp` library
* Python user input

**Installation:**

Install the required `yt-dlp` library before running the project:

```bash
pip install yt-dlp
```

**Run the project:**

```bash
python audiodowlode.py
```

```bash
python audio_downloader.py
```

**How to Use:**

1. Run the Python program.
2. Enter the URL of the YouTube video.
3. Press `Enter`.
4. Wait for the audio download to finish.
5. The downloaded audio file will be saved in the current project folder.

**Future Improvements:**

* Allow users to select the download folder
* Add audio format selection
* Add download progress information
* Add URL validation
* Add better error handling
* Create a graphical user interface using Tkinter

---

### 4. 💧 Drink Water Reminder

A simple Python desktop notification application that reminds users to drink water at regular intervals. The program uses the `plyer` library to display notifications on the computer.

**Features:**

* Sends desktop notifications
* Reminds users to drink water
* Displays a notification title and message
* Sends multiple reminders automatically
* Uses a time delay between notifications
* Simple and easy to use

**Technologies and Libraries Used:**

* Python 3
* Python `time` module
* `plyer` library
* Desktop notifications

**Installation:**

Install the required `plyer` library before running the project:

```bash
pip install plyer
```

**Run the project:**

```bash
python "drink water remainder.py"
```

```bash
python drink_water_reminder.py
```

**How It Works:**

1. Run the Python program.
2. The program waits for a specified amount of time.
3. A desktop notification reminds the user to drink water.
4. The reminder repeats automatically.

**Current Settings:**

* Number of reminders: `5`
* Time between reminders: `10 seconds`
* Notification display time: `10 seconds`

**Future Improvements:**

* Change the reminder interval to one or two hours
* Allow users to select a custom reminder interval
* Run the application automatically in the background
* Add start and stop options
* Add a graphical user interface using Tkinter
* Track daily water intake

---

### 5. 💰 Expense Tracker

A command-line Expense Tracker application built using Python. It allows users to record daily expenses, save expense details in separate text files, calculate total spending, and delete expense entries.

**Features:**

* Create multiple expense files
* Add expense names and spending amounts
* Save expenses permanently in text files
* View all saved expenses
* Automatically calculate the total expense
* Display the total amount in rupees
* Delete an expense using its line number
* Automatically create a folder for storing expense files

**Technologies and Concepts Used:**

* Python 3
* Python file handling
* Python `os` module
* Functions
* Loops
* Conditional statements
* String manipulation
* Exception handling

**Expense Entry Format:**

Enter each expense using the following format:

```text id="4np72k"
Expense Name:Amount
```

Example:

```text id="o1dm8j"
Food:200
Travel:100
Shopping:500
```

The program calculates and displays the total:

```text id="2tp7ms"
Total expense is 800 Rupees
```

**Run the Project:**

```bash id="rb0avh"
python expence_tercker.py
```

```bash id="njl0cw"
python expense_tracker.py
```

**How to Use:**

1. Run the Python program.
2. Select an option from the menu:

```text id="p31u6m"
1 - Open an existing expense file
2 - Create a new expense file
3 - Delete an expense
```

3. Enter expenses in the `Expense Name:Amount` format.
4. Open an expense file to view all expenses and the total amount spent.

**Future Improvements:**

* Add an option to edit existing expenses
* Add expense categories
* Add dates to expense entries
* Add monthly expense reports
* Add input validation
* Support decimal expense amounts
* Store expense information in a database
* Add a graphical user interface using Tkinter
* Add charts for expense analysis

---

### 6. 📂 Automatic File Organizer

A Python automation project that automatically organizes files into separate folders based on their file extensions. It helps keep the Downloads folder clean and organized by moving documents, images, and videos into their respective folders.

**Features:**

* Automatically scans files in the Downloads folder
* Creates folders if they do not already exist
* Organizes PDF and document files
* Organizes JPG and PNG images
* Organizes MKV and MOV video files
* Automatically moves files to their respective folders
* Reduces the need for manual file organization

**Technologies and Modules Used:**

* Python 3
* Python `os` module
* Python `shutil` module
* File and folder handling
* Loops
* Conditional statements
* Python automation

**Supported File Types:**

| File Type | Destination Folder |
| --------- | ------------------ |
| `.pdf`    | `PDFS`             |
| `.docx`   | `PDFS`             |
| `.jpg`    | `PHOTOS`           |
| `.png`    | `PHOTOS`           |
| `.mkv`    | `VIDEOS`           |
| `.mov`    | `VIDEOS`           |

**How It Works:**

1. The program opens the configured Downloads folder.
2. It reads all files inside the folder.
3. It automatically creates the following folders if they do not exist:

```text id="au6epu"
PDFS
PHOTOS
VIDEOS
```

4. It checks the extension of every file.
5. It moves each supported file into the appropriate folder.

**Run the Project:**

```bash id="wmbqxh"
python filehandling.py
```

> Before running the project, change the folder path in the Python code according to the location of your Downloads folder.

Example:

```python id="v55pt4"
os.chdir("D:\\CHROME DOWNLOADS")
```

Replace it with your own folder path if required.

**Future Improvements:**

* Add support for more file types
* Create separate folders for Word documents
* Organize ZIP and RAR files
* Organize audio files
* Allow users to select a folder
* Handle duplicate file names
* Add error handling
* Automatically organize newly downloaded files
* Add a graphical user interface using Tkinter

---

### 7. 🐍💧🔫 Snake, Water, Gun Game

A simple command-line Snake, Water, Gun game built using Python. The player competes against the computer for three rounds, and the program calculates the scores and announces the final winner.

**Game Rules:**

* 🐍 Snake drinks Water → Snake wins
* 💧 Water damages Gun → Water wins
* 🔫 Gun defeats Snake → Gun wins
* If both players select the same option → The round is a draw

**Features:**

* Play against the computer
* Computer choices are generated randomly
* The game contains three rounds
* Displays the computer's choice after every round
* Tracks the player's score
* Tracks the computer's score
* Detects draw rounds
* Announces the final winner after all rounds

**Technologies and Concepts Used:**

* Python 3
* Python `random` module
* User input
* Lists
* `for` loops
* Conditional statements
* Variables and score tracking
* Comparison operators

**Game Choices:**

```text id="i0o26n"
1 - Snake 🐍
2 - Water 💧
3 - Gun 🔫
```

**Run the Project:**

```bash id="ct31wb"
python game.py
```

**How to Play:**

1. Run the Python program.
2. Enter a number according to your choice:

```text id="i0k4ax"
Enter 1 for Snake
Enter 2 for Water
Enter 3 for Gun
```

3. The computer randomly selects Snake, Water, or Gun.
4. The winner of the current round is displayed.
5. The game continues for three rounds.
6. After all rounds, the final winner is announced.

**Example Output:**

```text id="3c1zyb"
Welcome to game!

Welcome in round 1

Enter your choice: 1
Computer choice: 2

You win!
```

**Future Improvements:**

* Add input validation
* Display names instead of numbers for the computer's choice
* Allow users to select the number of rounds
* Add a replay option
* Display the final scores
* Add difficulty levels
* Create a graphical user interface using Tkinter

---

### 8. 🔢 Number Guessing Game

A command-line Number Guessing Game built using Python. The computer randomly selects a number between 0 and 25, and the player must guess the correct number within a limited number of attempts.

The player can select from three difficulty levels. Each difficulty level provides a different number of attempts.

**Features:**

* Generates a random number between 0 and 25
* Provides three difficulty levels
* Gives a different number of attempts based on difficulty
* Displays hints when the guessed number is too high or too low
* Tracks the number of attempts used
* Displays a congratulatory message when the correct number is guessed
* Reveals the correct number when the player runs out of attempts
* Uses short delays to improve the game experience

**Difficulty Levels:**

| Difficulty | Number of Attempts |
| ---------- | -----------------: |
| Easy       |         8 attempts |
| Medium     |         6 attempts |
| Hard       |         4 attempts |

**Technologies and Concepts Used:**

* Python 3
* Python `random` module
* Python `time` module
* User input
* `while` loops
* Conditional statements
* Random number generation
* Variables and attempt tracking

**Run the Project:**

```bash id="ebszr9"
python number_guessing.py
```

**How to Play:**

1. Run the Python program.
2. Press `Enter` to start the game.
3. Select a difficulty level:

```text id="v2q9fa"
1 - Easy
2 - Medium
3 - Hard
```

4. The computer randomly selects a number between `0` and `25`.
5. Enter your guessed number.
6. The game provides a hint:

```text id="6e0qwa"
Guessed high!
```

or:

```text id="oxh91m"
Guessed low!
```

7. Continue guessing until you find the correct number or run out of attempts.

**Example Output:**

```text id="l3t8zu"
Welcome to Number Guessing Game

Choose a difficulty level:

1. Easy
2. Medium
3. Hard

You chose Easy. You have 8 attempts.

Computer is guessing a number...

Enter your guessed number: 15

Guessed high!
```

**Future Improvements:**

* Add input validation
* Prevent invalid difficulty selections
* Display the number of remaining attempts
* Add a replay option
* Allow users to select the number range
* Add a scoring system
* Save the player's highest score
* Create a graphical user interface using Tkinter

---

### 9. 🔐 Secure Password Generator

A command-line password generator built using Python. The program generates a random password using letters, numbers, and special characters. It also allows users to copy the generated password directly to their clipboard.

The program uses Python's `secrets` module to generate secure random characters.

**Features:**

* Generates random passwords
* Allows users to select the password length
* Uses uppercase and lowercase letters
* Uses numbers
* Uses special characters
* Adds a user-provided name at the beginning of the password
* Uses the `secrets` module for secure random generation
* Allows users to copy the generated password to the clipboard

**Technologies and Libraries Used:**

* Python 3
* Python `secrets` module
* Python `string` module
* `pyperclip` library
* User input
* String manipulation

**Installation:**

Install the required `pyperclip` library before running the project:

```bash id="syvrfw"
pip install pyperclip
```

**Run the Project:**

```bash id="8tmv8v"
python password.py
```

**How to Use:**

1. Run the Python program.
2. Enter a name to include at the beginning of the password.
3. Enter the number of random characters you want in the password.
4. The program generates and displays a random password.
5. Enter `yes` if you want to copy the generated password to your clipboard.

**Example Output:**

```text id="r7ydwb"
Enter name to generate password: Deep

Enter the password length: 10

Your password is: Deep@8#kP2!xQ$

If you want to copy your password, enter yes or no: yes

Your password is copied!
```

**Future Improvements:**

* Allow users to generate multiple passwords
* Add password-strength checking
* Allow users to select which character types to include
* Add a minimum password-length requirement
* Add better input validation
* Add an option to regenerate the password
* Create a graphical user interface using Tkinter

---

### 10. 🔊 Voice Shoutout Generator

A simple Python text-to-speech application that automatically gives voice shoutouts to multiple people. The program reads names from a list and uses the Windows Speech API to speak a personalized shoutout for each person.

**Features:**

* Converts text into speech
* Gives automatic voice shoutouts
* Supports multiple names
* Reads names from a Python list
* Generates a personalized shoutout for every name
* Displays messages in the terminal
* Uses the built-in Windows Speech API

**Technologies and Libraries Used:**

* Python 3
* `pywin32` library
* Windows Speech API (`SAPI.SpVoice`)
* Python lists
* `for` loops
* String concatenation
* Text-to-speech technology

**Installation:**

Install the required `pywin32` library before running the project:

```bash
pip install pywin32
```

**Run the Project:**

```bash
python shoutout.py
```

**How It Works:**

1. The program stores multiple names in a Python list.
2. It connects to the Windows Speech API.
3. A `for` loop reads each name from the list.
4. The computer speaks:

```text
Shoutout to Deep
Shoutout to Yug
Shoutout to Manav
```

5. The process continues until every person receives a shoutout.

**Example Code Output:**

```text
Shoutout to Deep

Shoutout to Yug

Shoutout to Manav
```

The computer speaks each shoutout using the system voice.

**System Requirement:**

> This project is designed for Windows because it uses `SAPI.SpVoice` through the `win32com` library.

**Future Improvements:**

* Allow users to enter names from the terminal
* Add a working stop option
* Allow users to add names without changing the code
* Add voice selection
* Add speech-speed controls
* Save names in a text file
* Create a graphical user interface using Tkinter
* Add support for other operating systems

---

## 👨‍💻 Author

**Deep Savani**

GitHub: `deep050601`

