from typing import List

from src.types import DTO


class Error(DTO):
    msg: str
    input: str


class ValidationError(DTO):
    detail: List[Error]
