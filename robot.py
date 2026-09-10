"""
robot.py — A tiny command interpreter for a (simulated) Robotat robot.

This is intentionally simple: it's a stand-in for a real robot control
script, used to practice a CI/CD pipeline, not to teach robotics.

Your task (see the homework instructions) is to add ONE new command
to this interpreter, add a test for it, and push it through the
pipeline defined in .github/workflows/ci.yml and the Dockerfile.
"""


def run_command(command: str) -> str:
    """
    Takes a single text command and returns the robot's response.
    Supported commands: FORWARD, BACKWARD, LEFT, RIGHT, STOP
    """
    command = command.strip().upper()

    if command == "FORWARD":
        return "Moving forward"
    elif command == "BACKWARD":
        return "Moving backward"
    elif command == "LEFT":
        return "Turning left"
    elif command == "RIGHT":
        return "Turning right"
    elif command == "STOP":
        return "Stopping"
    else:
        return f"Unknown command: {command}"


def run_sequence(commands: list[str]) -> list[str]:
    """Runs a list of commands in order and returns all responses."""
    return [run_command(c) for c in commands]


if __name__ == "__main__":
    demo_sequence = ["forward", "left", "stop"]
    for response in run_sequence(demo_sequence):
        print(response)
