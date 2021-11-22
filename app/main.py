from fastapi import FastAPI

from .routers import pet

app = FastAPI(
    title="Pet Care API",
    description="",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Kevin Contreras",
        "url": "https://github.com/kvncont",
        "email": "kvncont@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(pet.router)
