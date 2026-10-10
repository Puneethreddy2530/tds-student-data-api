# TDS Student Data API

FastAPI service for serving `students.csv` as JSON.

## Files

- `main.py` — FastAPI application
- `students.csv` — provided 2-column CSV (`studentId`, `class`)
- `requirements.txt` — Python dependencies

## Local run

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Try:

- `http://127.0.0.1:8000/api`
- `http://127.0.0.1:8000/api?class=1A`
- `http://127.0.0.1:8000/api?class=1A&class=1B`
- `http://127.0.0.1:8000/docs`

The `/api` response is shaped as `{"students": [{"studentId": 1, "class": "3A"}, ...]}`. Filtering keeps the original CSV row order. CORS is enabled for GET requests from any origin.

## Render deployment

Create a new Render Web Service connected to a GitHub repository containing these three files in the repository root.

- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

After deployment, submit `https://YOUR-RENDER-SERVICE.onrender.com/api` to the assignment (replace the hostname with your actual service URL).
