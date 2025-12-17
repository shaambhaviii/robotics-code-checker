# Robotics Internship Assignment

This project implements a complete robotic simulation validation system consisting of:
1. A Simulation Runner using ROS and Gazebo
2. A Python-based Code Checker backend
3. A lightweight Web Interface for user interaction

The system validates robot control code before simulation and evaluates simulation results programmatically.

---

## System Architecture

User Code → Web Interface → Code Checker → Simulation Evaluator → Result

---

## 1. Simulation Runner

### Tools Used
- Ubuntu 20.04 (WSL)
- ROS Noetic
- Gazebo Simulator
- Universal Robots UR5 (6-DOF)

### Implementation Details
- The UR5 robotic arm was successfully loaded in Gazebo using the `ur_gazebo` package.
- ROS topics such as `/joint_states` were verified and recorded.
- Joint motion data was logged into `joint_states.log`.

### Simulation Evaluation
A Python script (`simulation_evaluator.py`) evaluates the simulation by:
- Parsing joint motion data
- Detecting actual robot movement
- Verifying joint values against configurable limits
- Producing a structured JSON PASS/FAIL result

Both failure (strict joint limits) and success (realistic UR5 limits) cases were demonstrated.

### Notes on Object Spawn
A cube spawn was attempted using `gazebo_ros spawn_model`.  
Under WSL, Gazebo could not resolve `model://cube` due to model database limitations.  
The spawn logic and error handling were verified through logs.

---

## 2. Code Checker Backend

### Description
The Code Checker is a Python-based backend that validates robot control code before simulation.

### Features
- Python syntax validation (AST-based)
- Safety checks for forbidden system commands
- Joint limit constraint validation
- Machine-readable JSON output
- Callable via CLI and backend services

### Example Output
```json
{
  "status": "PASS",
  "errors": [],
  "checks": {
    "syntax": true,
    "safety": true,
    "joint_limits": true
  }
}
