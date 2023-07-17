from fastapi import FastAPI

app = FastAPI() # create a FastAPI "instance"


#  this decorator tells FastAPI that the function below corresponds to the path / with an operation get.
# It is the "path operation decorator".

@app.get("/") # tells FastAPI that the function right below is in charge of handling requests that go to:
            # * the path /
#           # * using a get operation
async def root():
    return {"message": "Hello World"}