from typing import Union
from dataclasses import dataclass, asdict
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

@dataclass
class UI:
    number1: float = 0.0
    number2: float = 0.0
    result: float = 0.0

ui = UI()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_json(id:str=""):
    ui.result=ui.number1+ui.number2
    output = asdict(ui)
    return output


@app.put("/")
def update_variable(variable_path: str, value:str):
    if variable_path=="number1":
        ui.number1 = float(value)
    elif variable_path =="number2":
        ui.number2 = float(value)
    return {variable_path: value}