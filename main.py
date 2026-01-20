from fastapi import FastAPI

app = FastAPI()

images_data = [
    {
        "name": "1.jpg",
        "size": ""
    },
    {
        "name": "2.jpg",
        "size": ""
    }
]

@app.get("/")
def home():
    return {"message": "Hello, gallery!"}

@app.get("/images")
def images():
    return images_data