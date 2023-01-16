import decimal
from datetime import date
from decimal import Decimal

from fastapi import APIRouter
from sqlalchemy import insert, select, delete

from app.connection_db import async_session
from app.statistics.models import statistic
from app.statistics.schemas import Statistics, ResponseSet, ResponseGet, StatisticsGet, StatusCode

router = APIRouter(
    prefix='/static',
    tags=['Operation']
)


@router.post("/set", response_model=ResponseSet)
async def set_statistic(statistics: Statistics):
    async with async_session() as session:
        stmt = insert(statistic).values(
            date=statistics.date,
            views=statistics.views,
            clicks=statistics.clicks,
            cost=statistics.cost.quantize(Decimal('1.00'), decimal.ROUND_DOWN),
        )
        await session.execute(stmt)
        await session.commit()
    return ResponseSet(status=200, data=statistics)


@router.get("/get", response_model=ResponseGet)
async def get_statistic(from_: date, to: date):
    query = select(statistic).filter(statistic.c.date <= from_).filter(statistic.c.date >= to).order_by(
        statistic.c.date.desc())
    async with async_session() as session:
        objs = await session.execute(query)
        objs = objs.all()

    list_statistics = []
    for obj in objs:
        cpc = set_cpc(cost=obj[4], clicks=obj[3])
        cpm = set_cpc(cost=obj[4], clicks=obj[2])
        list_statistics.append(
            StatisticsGet(
                date=obj[1],
                views=obj[2],
                clicks=obj[3],
                cost=obj[4],
                cpc=cpc,
                cpm=cpm
            )
        )
    return ResponseGet(statistics=list_statistics)


@router.delete("/delete", response_model=StatusCode)
async def delete_statistic():
    async with async_session() as session:
        await session.execute(delete(statistic))
        await session.commit()
    return StatusCode(status=200)


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
