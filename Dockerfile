FROM python:alpine
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install flask
COPY MainScores.py .
COPY Utils.py .
COPY Scores.txt .
EXPOSE 5000
CMD ["python", "MainScores.py"]