from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sentry_sdk
sentry_sdk.init(
    dsn="https://6ac061156e754dbb94b9e9f2ce4b881b@o4503935339397120.ingest.sentry.io/4503935340707840",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

app = FastAPI()

origins = [
    "http://localhost:3333",
    "http://127.0.0.1:3333",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0
#uvicorn hello:app --reload