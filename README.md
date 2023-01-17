# ciplay

func set_cpc(cost: Decimal, clicks: int)
Необходима для вычисления cpc каждой записи
на сход получает стоимость и количество кликов, на выход число с 2 знаками поле запятой
set_cpc(1.25: Decimal, 1: int) -> 1.25

func set_cpm(cost: Decimal, views: int)
Необходима для вычисления cpm каждой записи
на сход получает стоимость и количество просмотров, на выход число с 2 знаками поле запятой
set_cpc(1.25: Decimal, 1: int) -> 1250.0

func sort(order: str)
Необходима для получиния объектов сортировки запроса
sort(-date: str) -> Statistics.date.desc()
sort(date: str) -> Statistics.date
sort(cpc: str) -> Statistics.cpc

func set_statistic(statistics: Statistic)
функция записывает данные в БД
На вход получает данные по схеме 
{
date:2023-01-17
views:1
clicks:1
cost:1.00
}
Вычисляет cpc, cpm с пощью функций описанных выше и записывает всё в бд
в Ответ получает 
{
status:200
data:{
    date:2023-01-17
    views:1
    clicks:1
    cost:1.00
}
}


func get_statistic(from_: date, to: date, order_field: str = '-date')
Выводит данные за период 
на вход получает 
from_:2023-01-18
to:2023-01-16
order_field:'-date' - необходимо для определения по какому полю сортировать


на выходе
{
  "statistics": [
    {
      "date": "2023-01-18",
      "views": 0,
      "clicks": 0,
      "cost": 0,
      "cpc": 0,
      "cpm": 0
    },
    {
      "date": "2023-01-17",
      "views": 0,
      "clicks": 0,
      "cost": 0,
      "cpc": 0,
      "cpm": 0
    },
    {
      "date": "2023-01-17",
      "views": 1000,
      "clicks": 100,
      "cost": 1.25,
      "cpc": 0.01,
      "cpm": 1.25
    },
    {
      "date": "2023-01-16",
      "views": 0,
      "clicks": 0,
      "cost": 0,
      "cpc": 0,
      "cpm": 0
    },
    {
      "date": "2023-01-16",
      "views": 1000,
      "clicks": 100,
      "cost": 1.35,
      "cpc": 0.01,
      "cpm": 1.35
    },
    {
      "date": "2023-01-16",
      "views": 1000,
      "clicks": 100,
      "cost": 1.45,
      "cpc": 0.01,
      "cpm": 1.45
    }
  ]
}


на вход получает 
from_:2023-01-16
to:2023-01-18
order_field:'-cpm'

на выходе
{
  "statistics": [
    {
      "date": "2023-01-16",
      "views": 1000,
      "clicks": 100,
      "cost": 1.45,
      "cpc": 0.01,
      "cpm": 1.45
    },
    {
      "date": "2023-01-16",
      "views": 1000,
      "clicks": 100,
      "cost": 1.35,
      "cpc": 0.01,
      "cpm": 1.35
    },
    {
      "date": "2023-01-17",
      "views": 1000,
      "clicks": 100,
      "cost": 1.25,
      "cpc": 0.01,
      "cpm": 1.25
    },
    {
      "date": "2023-01-17",
      "views": 0,
      "clicks": 0,
      "cost": 0,
      "cpc": 0,
      "cpm": 0
    },
    {
      "date": "2023-01-16",
      "views": 0,
      "clicks": 0,
      "cost": 0,
      "cpc": 0,
      "cpm": 0
    },
    {
      "date": "2023-01-18",
      "views": 0,
      "clicks": 0,
      "cost": 0,
      "cpc": 0,
      "cpm": 0
    }
  ]
}

func delete_statistic()
Ничего не принимает , очищает всю БД