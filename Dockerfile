FROM python:3.11
WORKDIR /app
COPY backend ./backend
COPY frontend ./frontend
RUN pip install -r backend/requirements.txt
CMD python backend/app.py