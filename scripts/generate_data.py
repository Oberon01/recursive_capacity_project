import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic Big Five trait scores (0.0 to 1.0)
n_samples = 100
data = {
    "openness": np.round(np.random.uniform(0.2, 0.95, n_samples), 2),
    "conscientiousness": np.round(np.random.uniform(0.3, 0.9, n_samples), 2),
    "extraversion": np.round(np.random.uniform(0.1, 0.85, n_samples), 2),
    "agreeableness": np.round(np.random.uniform(0.2, 0.95, n_samples), 2),
    "neuroticism": np.round(np.random.uniform(0.1, 0.8, n_samples), 2),
}

# Define recursive capacity as a weighted linear combination + noise
weights = {
    "openness": 0.3,
    "conscientiousness": 0.2,
    "extraversion": 0.1,
    "agreeableness": 0.15,
    "neuroticism": -0.25,
}

recursive_capacity = (
    data["openness"] * weights["openness"]
    + data["conscientiousness"] * weights["conscientiousness"]
    + data["extraversion"] * weights["extraversion"]
    + data["agreeableness"] * weights["agreeableness"]
    + data["neuroticism"] * weights["neuroticism"]
    + np.random.normal(0, 0.02, n_samples)  # small noise
)

data["recursive_capacity"] = np.clip(np.round(recursive_capacity, 2), 0.0, 1.0)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_path = "data/trait_data.csv"
df.to_csv(csv_path, index=False)

csv_path
