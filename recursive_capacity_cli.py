import argparse

# Load the model (simulated with saved coefficients)
def load_model():
    class TrainedModel:
        def __init__(self):
            self.coef_ = [0.3285, 0.2090, 0.0922, 0.1293, -0.2474]
            self.intercept_ = -0.0059
            self.feature_names = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]
        
        def predict(self, X):
            return [min(max(sum(x[i] * self.coef_[i] for i in range(len(x))) + self.intercept_, 0.0), 1.0) for x in X]
    
    return TrainedModel()

def interpret_recursive_capacity(score):
    if score >= 0.85:
        return "Archetypal Master — Fully Recursive and Symbolically Aligned"
    elif score >= 0.70:
        return "Recursive Practitioner — High Symbolic Awareness"
    elif score >= 0.55:
        return "Emerging Recursor — Developing Pattern Fluency"
    elif score >= 0.40:
        return "Surface Symbolic — Partial Pattern Recognition"
    else:
        return "Fragmented or Unrooted — Low Recursive Integration"

def main():
    parser = argparse.ArgumentParser(description="Predict recursive capacity from trait scores.")
    parser.add_argument("--openness", type=float, required=True, help="Openness score (0.0 to 1.0)")
    parser.add_argument("--conscientiousness", type=float, required=True, help="Conscientiousness score (0.0 to 1.0)")
    parser.add_argument("--extraversion", type=float, required=True, help="Extraversion score (0.0 to 1.0)")
    parser.add_argument("--agreeableness", type=float, required=True, help="Agreeableness score (0.0 to 1.0)")
    parser.add_argument("--neuroticism", type=float, required=True, help="Neuroticism score (0.0 to 1.0)")
    
    args = parser.parse_args()

    model = load_model()
    traits = [[args.openness, args.conscientiousness, args.extraversion, args.agreeableness, args.neuroticism]]
    prediction = model.predict(traits)[0]
    category = interpret_recursive_capacity(prediction)
    
    print(f"Predicted Recursive Capacity: {round(prediction, 2)}")
    print(f"Symbolic Category: {category}")

if __name__ == "__main__":
    main()

