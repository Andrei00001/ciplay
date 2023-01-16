from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field


class StatusCode(BaseModel):
    status: int


class Statistics(BaseModel):
    date: date
    views: int = Field(ge=0, default=None)
    clicks: int = Field(ge=0, default=None)
    cost: Decimal = Field(ge=0, default=None)

    class Config:
        orm_mode = True


class ResponseSet(StatusCode):
    data: Statistics


class StatisticsGet(Statistics):
    cpc: Decimal
    cpm: Decimal


class ResponseGet(BaseModel):
    statistics: list[StatisticsGet]
