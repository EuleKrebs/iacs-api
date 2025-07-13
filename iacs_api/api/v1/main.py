

from fastapi import APIRouter
from fastcrud.paginated import PaginatedListResponse, paginated_response

router = APIRouter(tags=["main"])

@router.get("/echo")
def test_router(
    text: str,
) -> str:
    
    return text