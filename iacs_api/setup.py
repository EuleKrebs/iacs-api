
from typing import Any
import fastapi
from fastapi import APIRouter, FastAPI
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from .models.fields import Fields
from .config import (
    AppSettings,
    DatabaseSettings,
    EnvironmentOption,
    EnvironmentSettings,
    settings,
)
from .database import Base
from .database import engine


# -------------- database --------------
def create_tables() -> None:
    with engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all)

# -------------- application --------------
def create_application(
    router: APIRouter,
    settings: (
        DatabaseSettings
        | AppSettings
    ),
    create_tables_on_start: bool = True,
    **kwargs: Any,
) -> FastAPI:
    
    # --- before creating application ---
    if isinstance(settings, AppSettings):
        to_update = {
            "title": settings.APP_NAME,
            "description": settings.APP_DESCRIPTION,
            "contact": {"name": settings.CONTACT_NAME, "email": settings.CONTACT_EMAIL},
            "license_info": {"name": settings.LICENSE_NAME},
        }
        kwargs.update(to_update)

    if isinstance(settings, EnvironmentSettings):
        kwargs.update({"docs_url": None, "redoc_url": None, "openapi_url": None})

    application = FastAPI(**kwargs)
    application.include_router(router)

    if isinstance(settings, EnvironmentSettings):
        if settings.ENVIRONMENT != EnvironmentOption.PRODUCTION:
            docs_router = APIRouter()

            @docs_router.get("/docs", include_in_schema=False)
            def get_swagger_documentation() -> fastapi.responses.HTMLResponse:
                return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

            @docs_router.get("/openapi.json", include_in_schema=False)
            def openapi() -> dict[str, Any]:
                out: dict = get_openapi(title=application.title, version=application.version, routes=application.routes)
                return out

            application.include_router(docs_router)

    return application