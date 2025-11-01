# 1. Start from the Python 3.10-slim base image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy our project files into the /app directory
COPY . .

# 4. Install our Python libraries
RUN pip install -r requirements.txt

# 5. Set the default command to run when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]