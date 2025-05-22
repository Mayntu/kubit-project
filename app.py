from fastapi import FastAPI
from src.init import create_app
import uvicorn
import asyncio

async def main():
    app = await create_app()
    config = uvicorn.Config(app, host="0.0.0.0", port=5000, workers=3)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
