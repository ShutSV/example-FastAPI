from src.database import Offer
from src.tasks import log_offer_db
from src.utils import SQLAlchemyRepository


class OfferRepository(SQLAlchemyRepository):
    model = Offer

    @classmethod
    def add(cls, instance):

        with cls.session() as s:
            try:
                s.add(instance)
                s.commit()
                log_offer_db.delay("HTTP_201. Offer добавлен")
            except Exception as e:
                log_offer_db.delay(f"Postgres error: {e}")
                print(f"Error DB - неуникальный offer {e}")
