from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Hello Passcodes!!",
        "url": "https://github.com/PasscodesApp", 
        "maintainer": "https://github.com/jainil63"
    }

@app.get("/password")
def get_password():
    return {
        "password": "YourSecurePassword123!"
    }