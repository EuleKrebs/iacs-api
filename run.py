from iacs_api.api import router
from iacs_api.config import settings
from iacs_api.setup import create_application

app = create_application(router=router, settings=settings)
