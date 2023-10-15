from pydantic import Field, field_validator, model_validator
from slugify import slugify
from typing import Self

from src.repositories import OfferRepository
from src.types import DTO


class OfferBasic(DTO):
    title: str
    text: str
    city: str
    cost: float
    owner: str
    slug: str = Field(
        default=None,
        min_length=4,
        max_length=64,
        title='Offer slug'
    )


class OfferInput(OfferBasic):

    @model_validator(mode="after")
    def validator(self) -> Self:
        if self.title.isnumeric():
            raise ValueError("field does not contain letters")

        if self.cost <= 0:
            raise ValueError("value expected greater than zero")

        if self.slug is None:
            self.slug = slugify(self.text, max_length=64)
        elif len(self.slug) > 64 or len(self.slug) < 4:
            raise ValueError(f"4 < the value 'slug' should be < 64")

        if OfferRepository.filter(slug=self.slug).first():
            raise ValueError(f"field 'slug' already exists. Maybe the field 'text' needs to be changed first 64 lett")

        return self

    @field_validator('text', mode='after')
    def text_validator(cls, text: str) -> str:
        if OfferRepository.filter(text=text).first():
            raise ValueError(f"field 'text' already exists")
        return text
