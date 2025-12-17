

import ast
import json
import sys

JOINT_MIN = -3.14
JOINT_MAX = 3.14

FORBIDDEN_KEYWORDS = [
    "os.system",
    "subprocess",
    "rm -rf",
    "shutdown",
    "reboot"
]


def check_syntax(code):
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)


def check_forbidden(code):
    for word in FORBIDDEN_KEYWORDS:
        if word in code:
            return False, f"Forbidden command detected: {word}"
    return True, None


def check_joint_limits(code):
    for line in code.splitlines():
        if "joint_angle" in line and "=" in line:
            try:
                value = float(line.split("=")[1])
                if value < JOINT_MIN or value > JOINT_MAX:
                    return False, f"Joint angle {value} out of range"
            except ValueError:
                return False, "Invalid joint angle format"
    return True, None


def run_checker(filename):
    result = {
        "status": "PASS",
        "errors": [],
        "checks": {
            "syntax": True,
            "safety": True,
            "joint_limits": True
        }
    }

    try:
        with open(filename, "r") as f:
            code = f.read()
    except FileNotFoundError:
        result["status"] = "FAIL"
        result["errors"].append("File not found")
        print(json.dumps(result, indent=2))
        return

    ok, err = check_syntax(code)
    if not ok:
        result["status"] = "FAIL"
        result["checks"]["syntax"] = False
        result["errors"].append(err)

    ok, err = check_forbidden(code)
    if not ok:
        result["status"] = "FAIL"
        result["checks"]["safety"] = False
        result["errors"].append(err)

    ok, err = check_joint_limits(code)
    if not ok:
        result["status"] = "FAIL"
        result["checks"]["joint_limits"] = False
        result["errors"].append(err)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({
            "status": "FAIL",
            "errors": ["Usage: python3 code_checker.py <code_file.py>"]
        }, indent=2))
    else:
        run_checker(sys.argv[1])
