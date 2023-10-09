import decimal
from datetime import datetime

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    Text, Boolean, DateTime, ForeignKey,Numeric

#
# # установка соединения с postgres
# connection = psycopg2.connect(user="postgres", password = "1212")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
# # создаем курсор для выполнения операции с базой данных
# cursor = connection.cursor()
#
# # # Создаем базу данных "sqldz"
# sql_create_database = 'CREATE DATABASE sqldz'
# cursor.execute(sql_create_database)
#
# # закрываем соединение
#
# cursor.close()
# connection.close()

engine = create_engine("postgresql+psycopg2://postgres:1212@localhost/sqldz")
engine.connect()
print(engine)

metadata = MetaData()




customers = Table('customers', metadata,
                  # первичный ключ
             Column('id',Integer(), primary_key=True),

                  # имя покупателя
             Column('first_name', String(100), nullable=False),

                  # фамилия покупателя
             Column('last_name', String(100), nullable=False),

                  # уникальное имя покупателя
             Column('username', String(50), nullable=False),

                  # уникальный адрес электронной почты
             Column('email', String(200), nullable=False),

                  # адрес
             Column('address', String(200), nullable=False),

                  # город
             Column('town', String(50), nullable=False),

                  # дата и время создания аккаунта
             Column('created_on', DateTime(),default=datetime.now),

                  # дата и время обновления аккаунта
             Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now),
             )



items = Table('items', metadata,
              # первичный ключ
             Column('id',Integer(), primary_key = True),

              # название
             Column('name',String(200),nullable=False),

              # себестоимость товара
             Column('cost_price',Numeric(10, 2), nullable=False),

              # цена продажи
             Column('selling_price', Numeric(10, 2), nullable=False),

              # количество товаров в наличии
             Column('quantity',Integer(), default=False),
             )

posts = Table('orders',metadata,
                # первичный ключ
              Column('id',Integer(),primary_key=True),

                # внешний ключ, указывающий на колонку id таблицы customers
              Column('customer_id',ForeignKey('customers.id')),

                # дата и время отгрузки заказа  ТУТ НЕМНОГО НЕ ПОНЯТНО В КАКОМ ФОРМАТ ЭТО ДЕЛАТЬ
              Column('date_placed',DateTime(),default=datetime.now),

                # дата и время отгрузки заказа  ТУТ НЕМНОГО НЕ ПОНЯТНО В КАКОМ ФОРМАТ ЭТО ДЕЛАТЬ
              Column('date_shipped ',DateTime(),default=datetime.now),
              )

tags = Table('order_lines', metadata,
                # первичный ключ
              Column('id',Integer(),primary_key=True),

                # внешний ключ, указывающий на id таблицы orders
              Column('order_id',ForeignKey('orders.id')),

                # внешний ключ, указывающий на id таблицы items
              Column('item_id',ForeignKey('items.id')),

                # количество товаров в заказе
              Column('quantity',Integer(), default=False),
             )



metadata.create_all(engine)

