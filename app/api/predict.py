from fastapi import APIRouter, HTTPException
from app.services.predict_service import predict_threat

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    try:
        return predict_threat(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")