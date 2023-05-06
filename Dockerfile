FROM python:alpine
WORKDIR /app
RUN pip install flask
COPY ScoreFile/MainScores.py .
COPY ScoreFile/Utils.py .
COPY ScoreFile/Scores.txt .
EXPOSE 5000
ENTRYPOINT ["python", "/app/MainScores.py"]