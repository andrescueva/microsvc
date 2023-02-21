"""main module with api endpoints
"""
from fastapi import FastAPI, Header, HTTPException
from microsvc.models import Message

from microsvc.dependencies import (
    is_api_key_valid, create_jwt, is_valid_token,
    invalidate_token)

from microsvc.dependencies import IdGenerator



id_generator = iter(IdGenerator())

app = FastAPI()

@app.post("/DevOps/")
async def send_message(
    message: Message,
    x_parse_rest_api_key: str = Header(...),
    x_jwt_kwy: str = Header(...),
):
    """Post message protected with api key"""
    if not is_api_key_valid(x_parse_rest_api_key):
        raise HTTPException(status_code=401, detail="Invalid x-parse-reset-api-key")

    if not is_valid_token(x_jwt_kwy):
        raise HTTPException(status_code=401, detail="Invalid x-jwt-kwy")


    message_dict = message.dict()
    to_destination = message_dict["to"]
    invalidate_token(x_jwt_kwy)
    return {"message": f"Hello {to_destination} your message will be send"}


@app.get("/DevOps/")
async def get_send_message():
    """Method get not allowed"""
    raise HTTPException(status_code=405, detail="ERROR")


@app.delete("/DevOps/")
async def delete_send_message():
    """Method deleye not allowed"""
    raise HTTPException(status_code=405, detail="ERROR")


@app.put("/DevOps/")
async def put_send_message():
    """Method put not allowed"""
    raise HTTPException(status_code=405, detail="ERROR")


@app.patch("/DevOps/")
async def patch_send_message():
    """Method patch not allowed"""
    raise HTTPException(status_code=405, detail="ERROR")


@app.get("/jwt/")
async def get_token():
    """get jwt token"""
    transaction_id = next(id_generator)
    token = create_jwt(transaction_id)

    return {"token": token}


@app.get("/health/")
async def get_health_status():
    """health status check endpoint"""
    return {"status": "OK"}
