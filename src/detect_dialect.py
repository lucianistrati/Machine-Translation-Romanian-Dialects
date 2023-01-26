"""
dialect detection inference
"""
import joblib

vectorizer = joblib.load("checkpoints/vectorizer.joblib")
model = joblib.load("checkpoints/model.joblib")

idx_to_class = {0: "maramuresean",
                1: "banatean",
                2: "ardelean",
                3: "oltean",
                4: "moldovean"
                }


def detect_dialect(text: str, string_label: bool = True):
    vectorized = vectorizer.transform([text])
    prediction = model.predict(vectorized)[0]
    print(prediction)
    if string_label:
        prediction = idx_to_class[prediction]
    return prediction


def main():
    text = "No apăi unde merem amu?"
    print(detect_dialect(text))

    text = "Mă dusei să trec la Olt"
    print(detect_dialect(text))


if __name__ == "__main__":
    main()
