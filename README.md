# StarCraft 2 Training System (SC2T)

The **StarCraft 2 Training System (SC2T)** is a web-based application that allows StarCraft 2 players to train and improve their gameplay by competing against an AI. This system provides features for tracking performance, analyzing gameplay, and enhancing strategy through repeated practice.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
  - [Starting the Application](#starting-the-application)
  - [Accessing the Application](#accessing-the-application)
  - [User Features](#user-features)
  - [Admin Features](#admin-features)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

SC2T offers StarCraft 2 players a structured way to improve their gameplay through AI-based training and performance tracking. The application allows users to review their match history, evaluate progress, and refine strategies.

## Features

- **AI Training**: Compete against a custom AI to develop StarCraft 2 skills.
- **Performance Tracking**: Review match history, performance metrics, and results.
- **User Management**: Secure registration, login, and session management.
- **Admin Controls**: Update AI capabilities and view user performance across matches.

## Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Login
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **AI Development**: python-sc2 library

## Installation

### Prerequisites

- **Python 3.6+** is required.
- **Git** for cloning the repository.

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jodayyy/StarCraft-2-Training-System-SC2T.git
   cd StarCraft-2-Training-System-SC2T

2. **Set Up Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Set Up Environment Variables**
- Create a **.env** file in the root directory with the following content:
  ```plaintext
  SECRET_KEY=YourSecretKeyHere

5. **Set Up the Database**
- Run the application once to automatically create the database:
  ```bash
  python main.py

## Usage

### Starting the Application
- Start the Flask application with:
  ```bash
  python main.py 

### Accessing the Application

Open a browser and go to **http://127.0.0.1:5000**.

### User Features

- **Train against AI:** Play against a custom AI to practice skills and strategies.
- **View Performance:** ccess a history of matches with results and timestamps to analyze gameplay.

### Admin Features

- **Update AI:** Modify and enhance AI for improved training experiences.
- **Review User Performance:** Access performance data for all users, including match results and progress metrics.






