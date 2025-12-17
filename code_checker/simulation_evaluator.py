
import json
import sys

JOINT_MIN = -6.28
JOINT_MAX = 6.28


def evaluate_joint_log(filename):
    result = {
        "simulation_status": "PASS",
        "reason": "",
        "joint_motion_detected": False
    }

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        result["simulation_status"] = "FAIL"
        result["reason"] = "joint_states log not found"
        print(json.dumps(result, indent=2))
        return

    positions = []

    for line in lines:
        if "position:" in line:
            try:
                values = line.strip().split("[")[1].split("]")[0]
                values = [float(v) for v in values.split(",")]
                positions.append(values)
            except:
                continue

    if len(positions) < 2:
        result["simulation_status"] = "FAIL"
        result["reason"] = "No sufficient joint motion detected"
        print(json.dumps(result, indent=2))
        return

    if positions[0] != positions[-1]:
        result["joint_motion_detected"] = True

    for snapshot in positions:
        for v in snapshot:
            if v < JOINT_MIN or v > JOINT_MAX:
                result["simulation_status"] = "FAIL"
                result["reason"] = "Joint limit violation detected"
                print(json.dumps(result, indent=2))
                return

    if result["joint_motion_detected"]:
        result["reason"] = "Joint motion valid and within limits"
    else:
        result["simulation_status"] = "FAIL"
        result["reason"] = "Robot did not move"

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({
            "simulation_status": "FAIL",
            "reason": "Usage: python3 simulation_evaluator.py joint_states.log"
        }, indent=2))
    else:
        evaluate_joint_log(sys.argv[1])
