# Q25 — Vercel POST latency analytics

FastAPI endpoint for the TDS GA0 latency analytics question.

## Deploy

Import the repository `Puneethreddy2530/tds-student-data-api` into Vercel and set **Root Directory** to `q25-vercel-analytics`. Keep the framework preset as Other if Vercel asks. Deploy.

The POST endpoint is the deployed project root URL (for example, `https://YOUR-PROJECT.vercel.app/`). It accepts:

```json
{"regions":["apac","emea"],"threshold_ms":175}
```

It returns a `regions` array with `avg_latency`, `p95_latency`, `avg_uptime`, and `breaches`. CORS permits requests from any origin.

## Local test

Install `requirements.txt` and run `uvicorn api.index:app --reload`. POST the sample payload to `http://127.0.0.1:8000/`.
