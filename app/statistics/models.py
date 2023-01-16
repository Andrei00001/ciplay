from sqlalchemy import Column, Integer, Float, MetaData, Table, Date

metadata = MetaData()

statistic = Table(
    'statistic',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('date', Date),
    Column("views", Integer, nullable=True),
    Column("clicks", Integer, nullable=True),
    Column("cost", Float, nullable=True),
)
