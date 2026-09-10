# Robotat DevOps Homework — Starter Kit

This is the starter code for the "Build Your First Pipeline" homework
that follows the *DevOps Foundations: From Code to Production* lecture.

## What's in here

| File | Purpose |
|---|---|
| `robot.py` | A tiny command interpreter (your "application") |
| `test_robot.py` | Unit tests — this is what CI runs automatically |
| `Dockerfile` | Packages the app into a container image |
| `requirements.txt` | Python dependencies |
| `.github/workflows/ci.yml` | The CI pipeline definition (GitHub Actions) |

## Quick start

1. Create a new **private** GitHub repository and push these files to it
   (or use "Import repository" if your instructor gave you a URL).
2. Go to the **Actions** tab of your repo — you should see the `CI`
   workflow run automatically and pass (green check).
3. Now follow the homework instructions to make your change.

## Running things locally (optional but recommended)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the tests
pytest -v

# Run the script directly
python robot.py

# Build and run the Docker image
docker build -t robotat-robot .
docker run --rm robotat-robot
```

Full instructions and grading criteria are in the homework document
provided separately.
