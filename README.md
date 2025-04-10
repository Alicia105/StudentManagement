# StudentManagement

## **Description**  
A simple studenet management system with a Command Line Interface (CLI) to manage student accounts, administartor accounts and course registration. This project comes with a REST API to interact with a SQLite database.

## **Table of Contents**  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)
- [How to run](#How-to-run)
- [How to use](#How-to-use)

## **Features**  
- Possibility to **sign in or log in** with a **student or administrator account**.  
- Possibility for **student to modfy their account, register or unregister from a course**.  
- Posibilty for **administrators to add, remove or modify students account or courses**.
- Possibility for **administrator to modify or delete their own account**.
- Possibility for **an administrator to delete another administrator account**.

## **Requirements**  
- **Python 3** 
- **Flask** 
- **SQLAlchemy** 

## **Installation**  
- Clone or download the repository
<pre> git clone https://github.com/Alicia105/StudentManagement.git </pre>
- Install Flask and SQLAlchemy
<pre> pip install Flask SQLAlchemy</pre>

## **How to run** 
1. Navigate to the project directory
<pre> cd StudentManagement</pre>
2. Launch the REST API first
<pre> python app.py</pre>
3. Navigate to the source code directory (preferrably in a different terminal)
<pre>cd StudentManagement/src </pre>
4. Run main script
<pre>python main.py</pre>


## **How to use** 
The app is pretty straightforward to use. You just have to follow along the indications on the terminal 
![Main menu](images/mainMenu.jpg)