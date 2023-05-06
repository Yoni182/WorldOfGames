FROM python:alpine
WORKDIR /app
RUN pip install flask
COPY MainScores.py .
COPY Utils.py .
COPY Scores.txt .
EXPOSE 5000
ENTRYPOINT ["python", "/app/MainScores.py"]