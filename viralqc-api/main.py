from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import sequence_quality
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

## Create a FastAPI instance
app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

## CORS settings
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## Include the routers
app.include_router(sequence_quality.router, prefix="/sequence_quality")

@app.get("/")
async def read_root():
    return {"message": "API is working"}