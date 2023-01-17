import decimal
from datetime import date
from decimal import Decimal
from typing import Union

from fastapi import APIRouter
from sqlalchemy import select, delete

from app.connection_db import Session

from app.models import Statistics
from app.statistics.schemas import Statistic, ResponseSet, ResponseGet, StatisticsGet, StatusCode, ResponseError

router = APIRouter(
    prefix='/static',
    tags=['Operation']
)


@router.post("/set", response_model=ResponseSet)
async def set_statistic(statistics: Statistic):
    statistics.cost = statistics.cost.quantize(Decimal('1.00'), decimal.ROUND_DOWN)
    cpc = set_cpc(cost=statistics.cost, clicks=statistics.clicks)
    cpm = set_cpm(cost=statistics.cost, views=statistics.views)

    async with Session() as session:
        session.add(Statistics(
            date=statistics.date,
            views=statistics.views,
            clicks=statistics.clicks,
            cost=statistics.cost,
            cpc=cpc,
            cpm=cpm
        ))
        await session.commit()
    return ResponseSet(status=200, data=statistics)


def set_cpc(cost: Decimal, clicks: int) -> Decimal:
    cpc = cost / clicks if clicks != 0 and clicks is not None else 0
    if cpc == 0:
        return cpc
    return Decimal(cpc).quantize(Decimal('1.00'), decimal.ROUND_DOWN)


def set_cpm(cost: Decimal, views: int) -> Decimal:
    cpm = cost / views * 1000 if views != 0 and views is not None else 0
    if cpm == 0:
        return cpm
    return Decimal(cpm).quantize(Decimal('1.00'), decimal.ROUND_DOWN)


@router.get("/get", response_model=Union[ResponseGet, ResponseError])
async def get_statistic(from_: date, to: date, order_field: str = '-date'):
    try:
        order_field = sort(order_field)
    except AttributeError:
        return ResponseError(error=f"I can not find such a concept for sorting {order_field}")

    if from_ <= to:
        from_, to = to, from_

    query = select(Statistics).filter(Statistics.date <= from_).filter(Statistics.date >= to).order_by(order_field)
    async with Session() as session:
        statistics = await session.execute(query)
        statistics = statistics.scalars()

    return ResponseGet(statistics=[StatisticsGet.from_orm(statistic) for statistic in statistics])


def sort(order: str) -> Statistics:
    descending = False
    if order[0] == '-':
        order = order[1:]
        descending = True

    if descending:
        return Statistics.__getattribute__(Statistics, order).desc()
    return Statistics.__getattribute__(Statistics, order)


@router.delete("/delete", response_model=StatusCode)
async def delete_statistic():
    async with Session() as session:
        await session.execute(delete(Statistics))
        await session.commit()
    return StatusCode(status=200)
