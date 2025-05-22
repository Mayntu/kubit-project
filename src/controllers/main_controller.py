from fastapi import APIRouter, Body, BackgroundTasks, HTTPException, Depends, status
from fastapi.responses import JSONResponse

api_router : APIRouter = APIRouter()

@api_router.get("/check")
def check():
    return 200