from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


from isp_monitor.isps.railwire.railwire_raw import raw_input

class Item(BaseModel):
    service: str
    state: Union[str, None] = None
    url: str
    userid: str
    password: str
    output_type: Union[str, None] = None


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/raw/")
async def raw_info(item: Item):
    response = raw_input(item.userid, item.password, item.url, item.output_type)
    return response