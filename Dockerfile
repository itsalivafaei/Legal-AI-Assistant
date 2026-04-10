FROM python:3.9-slim

WORKDIR /app

# Install system dependency for audio processing
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure the static directory exists for audio output
RUN mkdir -p app/static

EXPOSE 7860

# Pass GROQ_API_KEY at runtime: docker run -e GROQ_API_KEY=... <image>
ARG GROQ_API_KEY
ENV GROQ_API_KEY=${GROQ_API_KEY}

CMD ["python", "app/main.py"]
