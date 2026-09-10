# Small, simple image for the Robotat CI/CD homework exercise.
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY robot.py test_robot.py ./

# Running the container executes the demo sequence in robot.py
CMD ["python", "robot.py"]
