from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

async def create_app() -> FastAPI:
    app = FastAPI(docs_url="/", redoc_url="/redoc")
        
    origins = [
        "*",
        
    ]

    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  
        allow_credentials=True,
        allow_methods=["*"],  
        allow_headers=["*"],  
    )

    register_views(app=app)
    
    return app

def register_views(app: FastAPI):
    from src.controllers.main_controller import api_router
    app.include_router(api_router, prefix="/api/v1")
