import decimal
from datetime import date
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, Field, validator


class StatusCode(BaseModel):
    status: int


class Statistic(BaseModel):
    date: date
    views: int = Field(ge=0, default=None)
    clicks: int = Field(ge=0, default=None)
    cost: Decimal = Field(ge=0, default=None)

    class Config:
        orm_mode = True


class ResponseSet(StatusCode):
    data: Statistic


class StatisticsGet(Statistic):
    cpc: Decimal
    cpm: Decimal


class ResponseGet(BaseModel):
    statistics: list[StatisticsGet]

    class Config:
        orm_mode = True


class ResponseError(BaseModel):
    error: str
