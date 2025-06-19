
# Recursive Capacity Predictor

A lightweight symbolic ML system that estimates a user’s **recursive cognitive capacity** from Big Five personality traits using a linear regression model. Includes a CLI interface and an API server with symbolic interpretation.

---

## Project Structure

```
/simple_linreg/
├── cli/                           # Command-line interface tools
│   └── recursive_capacity_cli_v2.py
├── api/                           # FastAPI-based REST server
│   └── app.py
├── data/
│   ├── trait_data.csv             # Synthetic trait dataset
│   └── README.md                  # Dataset explanation
├── scripts/
│   ├── generate_data.py           # Data synthesis
│   ├── model.py                   # Model training logic
│   ├── main.py                    # Entry point
│   └── test.py                    # Test cases
├── notebooks/                     # (placeholder for EDA/expansion)
└── requirements.txt
```

---

## What It Does

- Accepts five trait inputs: `openness`, `conscientiousness`, `extraversion`, `agreeableness`, and `neuroticism`
- Predicts a **recursive capacity score** (0.0 to 1.0)
- Returns a **symbolic category** such as “Archetypal Master” or “Surface Symbolic”
- CLI and API available for flexible integration

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Using the CLI

```bash
python cli/recursive_capacity_cli_v2.py \
  --openness 0.75 \
  --conscientiousness 0.65 \
  --extraversion 0.45 \
  --agreeableness 0.60 \
  --neuroticism 0.22
```

**Output:**
```
Predicted Recursive Capacity: 0.72
Symbolic Category: Archetypal Master — Peak Recursive Expression
```

---

## Using the API

### Start the server:
```bash
uvicorn api.app:app --reload
```

### Access via Swagger:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Example Request:
**POST** `/predict/`

```json
{
  "openness": 0.78,
  "conscientiousness": 0.63,
  "extraversion": 0.52,
  "agreeableness": 0.64,
  "neuroticism": 0.18
}
```

**Response:**
```json
{
  "recursive_capacity": 0.71,
  "symbolic_category": "Archetypal Master — Peak Recursive Expression"
}
```

---

## Symbolic Categories

| Score Range | Symbolic Category |
|-------------|-------------------|
| ≥ 0.70      | Archetypal Master  
| 0.60–0.69   | Recursive Practitioner  
| 0.50–0.59   | Emerging Recursor  
| 0.35–0.49   | Surface Symbolic  
| < 0.35      | Fragmented or Unrooted  

---

## Philosophy

This tool sits at the intersection of:
- Cognitive simulation  
- Symbolic reasoning  
- Machine learning infrastructure  

