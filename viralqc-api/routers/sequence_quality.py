import json
import os
from fastapi import APIRouter, Depends, HTTPException, status
from http import HTTPStatus
from fastapi import Header
from schemas.sequence_quality import SequenceQualityInput

from crud.sequence_quality import run_sequence_quality_pipeline


router = APIRouter(tags=["Sequence Quality"])

def verify_viralqc_api_key(x_api_key: str = Header(None)):
    expected_key = os.getenv("VIRALQC_API_KEY")
    if not x_api_key or x_api_key != expected_key:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid or missing API key.")

@router.post("/", response_model=dict, status_code=status.HTTP_200_OK)
def evaluate_sequences(payload: SequenceQualityInput,
                       _: None = Depends(verify_viralqc_api_key)):
    """
    Run the sequence quality evaluation pipeline and return the results.
    """

    # Convert Pydantic objects to plain dictionaries
    seq_list = [{"id": s.id, "sequence": s.sequence} for s in payload.sequences]

    try:
        # Run ViralQC pipeline
        results = run_sequence_quality_pipeline(seq_list)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}')

    return {"results": results}