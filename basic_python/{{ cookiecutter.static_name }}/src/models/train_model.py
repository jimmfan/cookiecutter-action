# model_config.yaml: Contains general configurations for the model, such as the type of model (model_type), evaluation metrics (evaluation_metrics), and training setup (like test_split and cross_validation settings).
# hyperparameters.yaml: Specifies the hyperparameters for various models. For example, it might contain hyperparameter sets for a random forest model, a gradient boosting model, and others.
import yaml


def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


model_config = load_yaml("model_config.yaml")
hyperparameters = load_yaml("hyperparameters.yaml")

# Based on model_config, initialize the ML model. For example, if model_config['model_type'] is 'random_forest', you would initialize a RandomForest model.

from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier


# Example function to initialize a model
def initialize_model(model_config, hyperparameters):
    model_type = model_config["model_type"]
    if model_type == "random_forest":
        model = RandomForestClassifier(**hyperparameters["random_forest"])
    elif model_type == "gradient_boosting":
        model = GradientBoostingClassifier(**hyperparameters["gradient_boosting"])
    # Add other model initializations as needed...
    else:
        raise ValueError(f"Unsupported model type: {model_type}")
    return model


model = initialize_model(model_config, hyperparameters)

# Step 4: Training
# Use the model configuration to set up the training process, including splitting the data, applying cross-validation, and using the specified evaluation metrics.

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import cross_val_score, train_test_split

# Additional imports as needed...

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=model_config["training"]["test_split"]
)

# Training the model
model.fit(X_train, y_train)

# Optionally, use cross-validation based on model_config
if "cross_validation" in model_config["training"]:
    scores = cross_val_score(
        model, X, y, cv=model_config["training"]["cross_validation"]["k_folds"]
    )
    print(f"Cross-validation scores: {scores.mean()} +/- {scores.std()}")

# Step 5: Evaluation
# After training, evaluate the model using the metrics specified in model_config.

# Example function to evaluate the model
def evaluate_model(model, X_test, y_test, metrics):
    predictions = model.predict(X_test)
    results = {}
    for metric in metrics:
        if metric == "accuracy":
            results["accuracy"] = accuracy_score(y_test, predictions)
        elif metric == "precision":
            results["precision"] = precision_score(y_test, predictions)
        elif metric == "recall":
            results["recall"] = recall_score(y_test, predictions)
        elif metric == "f1_score":
            results["f1_score"] = f1_score(y_test, predictions)
        # Add other metrics as needed...
    return results


evaluation_results = evaluate_model(
    model, X_test, y_test, model_config["evaluation_metrics"]
)
print(evaluation_results)
