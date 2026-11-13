from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello world"}

@app.get("/about")
def about():
    return {"message": "This is About page"}





class Student(BaseModel):
  name : str
  age : int
  email : str
@app.post("/students")
def create_Student(student:Student):
    return{
        "message":"student created",
        "student":student
    }
    
    
class Teacher(BaseModel):
    name : str
    subject : str
    lecture : int 
@app.post("/Teacher")
def create_Teacher(teacher:Teacher):
    return{
        "message":"Teacher created",
        "teacher":teacher
    }

class Book(BaseModel):
    name: str
    author: str
    chapter: int
@app.post("/Book")
def create_Book(book:Book):
    return{
        "message":"my favourite Book",
        "book":book
    }
    
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
posts = []

class Post(BaseModel):
    title : str
    content : str

 
@app.post("/posts")
def create_post(post:Post):
     posts.append(post)
     return{
         "message":"post created",
         "post": post
     }

from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI()
posts =[]
class Post(BaseModel):
    title : str
    content : str
    
@app.post("/posts")
def create_post(post:Post):
    posts.append(post)
    return{
        "message":" post created",
        "post":post
    }

     
     
     
     