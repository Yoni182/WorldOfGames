FROM python:alpine
WORKDIR /app
ENV FLASK_APP=MainScores.py
RUN pip install flask
COPY MainScores.py .
COPY Utils.py .
COPY Scores.txt .
EXPOSE 5000
CMD ["python", "MainScores.py", "--host", "0.0.0.0"]