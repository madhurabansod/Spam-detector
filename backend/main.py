
from fastapi.middleware.cors import CORSMiddleware

import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Load the model and vectorizer
# We load them at the top level so they stay in memory while the app runs
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

# 3. Define the Input Format using Pydantic
class SpamRequest(BaseModel):
    message: str

# 4. Create the POST endpoint
@app.post("/predict")
async def predict_spam(request: SpamRequest):
    # Transform the input text using the loaded vectorizer
    text_vectorized = vectorizer.transform([request.message])
    
    # Predict (0 = ham, 1 = spam)
    prediction = model.predict(text_vectorized)
    
    # Convert prediction to human-readable label
    result = "spam" if prediction[0] == 1 else "This message is NOT SPAM"
    
    # 5. Return JSON response
    return {
        "message": request.message,
        "prediction": result,
        "is_spam": bool(prediction[0])
    }

# Root endpoint for testing
@app.get("/")
def home():
    return {"status": "Spam Detector API is running!"}