from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import List

from starlette.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse

from groq import AsyncGroq, Groq
from groq.resources import Models
from groq.types import ModelList
from groq.types.chat.completion_create_params import Message

from json import dumps
import async_timeout
import asyncio

GENERATION_TIMEOUT_SEC = 60

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class ChatInput(BaseModel):
    model: str
    messages: List[Message]
    stream: bool
    temperature: float = 0
    max_tokens: int = 100
    user: str = "user"


async def get_groq_response(client: AsyncGroq, req: ChatInput):
    async with async_timeout.timeout(GENERATION_TIMEOUT_SEC):
        try:
            stream = await client.chat.completions.create(
                messages=req.messages,
                model=req.model,
                temperature=req.temperature,
                max_tokens=req.max_tokens,
                stream=req.stream,
            )

            async for chunk in stream:
                yield {"data": dumps(chunk.dict())}

        except asyncio.TimeoutError:
            raise HTTPException(status_code=504, detail="Stream timed out")


@app.get("/models")
async def models(authorization: str = Header()) -> ModelList:
    client = Groq(
        api_key=authorization.split(" ")[-1],
    )
    models = Models(client=client).list()

    return models


@app.post("/chat/completions")
async def completion(req: ChatInput, authorization: str = Header()):
    client = AsyncGroq(
        api_key=authorization.split(" ")[-1],
    )

    if req.stream:
        return EventSourceResponse(get_groq_response(client, req))

    response = await client.chat.completions.create(
        messages=req.messages,
        model=req.model,
        temperature=req.temperature,
        max_tokens=req.max_tokens,
        stream=req.stream,
    )

    return response
