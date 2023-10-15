from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse
from starlette.requests import Request
from typing import List

from src.database.models import Offer
# from src.dependencies import is_authenticated
from src.repositories import OfferRepository
from src.types import OfferBasic, OfferInput

router = APIRouter(
    prefix="/offers",
    # dependencies=[is_authenticated],
    default_response_class=ORJSONResponse,
    tags=["offers (авторизция временно отключена)"],
)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=List[OfferBasic],
    name="Получение списка всех предложений работы",
)
async def list_offers():
    offers = OfferRepository.all().order_by(Offer.id)
    return [OfferBasic.model_validate(obj=offer, from_attributes=True) for offer in offers]


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=OfferBasic,
    name="Размещение предложения о работе",
)
async def add_new_offer(request: Request, form: OfferInput):
    # form = OfferBasic(**form.model_dump() | {'owner': request.user.identity})
    form = OfferBasic(**form.model_dump())
    offer = Offer(**form.model_dump())
    OfferRepository.add(offer)
    return form
