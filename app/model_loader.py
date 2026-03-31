import pickle

MODEL_PATH = "model/churn_model.pkl"
ENCODER_PATH = "model/encoders.pkl"


def load_model():
    try:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        raise RuntimeError(f"Error loading model: {e}")


def load_encoders():
    try:
        with open(ENCODER_PATH, "rb") as f:
            encoders = pickle.load(f)
        return encoders
    except Exception as e:
        raise RuntimeError(f"Error loading encoders: {e}")