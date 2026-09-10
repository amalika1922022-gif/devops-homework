"""
test_robot.py — Unit tests for robot.py

This is what your CI pipeline runs automatically on every push.
When you add a new command to robot.py, add a matching test here too.
"""

from robot import run_command, run_sequence


def test_forward():
    assert run_command("FORWARD") == "Moving forward"


def test_backward():
    assert run_command("BACKWARD") == "Moving backward"


def test_left():
    assert run_command("LEFT") == "Turning left"


def test_right():
    assert run_command("RIGHT") == "Turning right"


def test_stop():
    assert run_command("STOP") == "Stopping"


def test_case_insensitive():
    assert run_command("forward") == "Moving forward"


def test_unknown_command():
    assert run_command("DANCE") == "Unknown command: DANCE"
    
def test_spin():
    assert run_command("SPIN") == "Robot is spinning in circles!"

def test_sequence():
    result = run_sequence(["forward", "left", "stop"])
    assert result == ["Moving forward", "Turning left", "Stopping"]
    



# ---------------------------------------------------------------
# TODO (your homework task): add a test for your new command here
# ---------------------------------------------------------------
