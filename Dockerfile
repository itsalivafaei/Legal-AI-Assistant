# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install ffmpeg for audio processing
RUN apt-get update && apt-get install -y ffmpeg

# Copy the rest of the code into the container
COPY . .

# Expose port 7860 for Gradio
EXPOSE 7860

# Set environment variable for the Groq API key
# It's recommended to pass this at runtime for security
ENV GROQ_API_KEY=${GROQ_API_KEY}

# Run the application
CMD ["python", "main.py"]