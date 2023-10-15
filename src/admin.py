from sqladmin import ModelView
from src.database import User, Offer


class AdminUserDB(ModelView, model=User):
    column_list = [User.id, User.name, User.email, User.password]


class AdminOfferDB(ModelView, model=Offer):
    column_list = [
        Offer.title,
        Offer.text,
        Offer.city,
        Offer.owner,
        Offer.cost,
        Offer.slug,
        Offer.is_activated
    ]
