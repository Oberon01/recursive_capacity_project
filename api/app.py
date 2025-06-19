from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Recursive Capacity API")

# Define input schema
class TraitProfile(BaseModel):
    openness: float
    conscientiousness: float
    extraversion: float
    agreeableness: float
    neuroticism: float

# Load static model parameters
COEFFICIENTS = [0.3285, 0.2090, 0.0922, 0.1293, -0.2474]
INTERCEPT = -0.0059

def predict_capacity(traits: list[float]) -> float:
    score = sum(trait * coef for trait, coef in zip(traits, COEFFICIENTS)) + INTERCEPT
    return round(max(0.0, min(1.0, score)), 2)

def interpret(score: float) -> str:
    if score >= 0.70:
        return "Archetypal Master — Peak Recursive Expression"
    elif score >= 0.60:
        return "Recursive Practitioner — High Symbolic Awareness"
    elif score >= 0.50:
        return "Emerging Recursor — Developing Pattern Fluency"
    elif score >= 0.35:
        return "Surface Symbolic — Partial Pattern Recognition"
    else:
        return "Fragmented or Unrooted — Low Recursive Integration"

# Define prediction route
@app.post("/predict/")
def predict(profile: TraitProfile):
    traits = [
        profile.openness,
        profile.conscientiousness,
        profile.extraversion,
        profile.agreeableness,
        profile.neuroticism,
    ]
    score = predict_capacity(traits)
    category = interpret(score)
    return {
        "recursive_capacity": score,
        "symbolic_category": category
    }

# Optional: dev entry point
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
