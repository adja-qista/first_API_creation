from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


# fastapi instance creation
@app.get("/")
def index():
    return {"name": "First Data"}


# add endpoint parameters
students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "Year 12"

    }
}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
    return students[student_id]


# query parameters :
# optional method: inputs  optional
@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


# POST METHOD: add data
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return{"Error this student exists already"}
    students[student_id] = student
    return students[student_id]


# PUT METHOD: update data
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return{"Error this student doesn't exists "}
    students[student_id] = student
    return students[student_id]

# PUT METHOD: update data/ best methods
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return{"Error this student doesn't exists "}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

# DELETE METHODE
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return{"Error this student doesn't exists "}
    del students[student_id]
    return {"Message": "This student has been deleted"}
