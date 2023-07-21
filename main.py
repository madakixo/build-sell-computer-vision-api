import os

from ultralytics import YOLO
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np


class Image(BaseModel):
    img_url: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = YOLO('./ship_classifier.pt')


@app.post("/classify")
def classify(image: Image):

    img_url = image.img_url

    output = model(img_url)[0]

    pred = output.probs.data.tolist()

    os.remove(img_url.split('/')[-1])

    return {'img_url': img_url,
           'score': np.amax(pred),
           'class': output.names[np.argmax(pred)]}
