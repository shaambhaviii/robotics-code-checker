# Robotics Code Checker

## Overview
This project implements a robotic simulation validation system consisting of:
- A simulation runner using ROS and Gazebo
- A Python-based code checker
- A minimal Flask web interface

The system validates robot control code before simulation and reports PASS/FAIL results.

---

## Setup Instructions
1. Install Python 3
2. Install Flask:
   pip install flask
3. Run the web interface:
   python app.py
4. Open browser at:
   http://127.0.0.1:5000/

---

## How to Run the Tool
1. Start the Flask server
2. Upload robot control code
3. View validation result on the web page

---

## Test Packages
- `sample_robot_code.py`  
  Correct robot control code that passes all checks.

- `faulty_robot_code.py`  
  Contains forbidden system calls and fails validation.

---

## Simulation Notes
- UR5 robot simulated in Gazebo
- Joint motion recorded and evaluated programmatically
- Strict joint limits correctly trigger failure
- Realistic joint limits result in successful validation

---

## Logs and Testing Notes
- Joint states logged via ROS
- Simulation evaluator outputs structured JSON results
- Web interface verified end-to-end
