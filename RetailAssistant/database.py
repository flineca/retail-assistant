'''
sqlite3 warehouse.db
create table stock(
id      int primary key not null,
place   char(50)        not null,
product char(50)        not null,
brand   char(50)        not null,
code    char(50)        not null,
number  int             not null,
first_cost  real,
reference_price real,
update_date char
);

INSERT INTO stock (id,place,product,brand,code,number,first_cost,reference_price,update_date)
VALUES (1, 'south', 'fan', 'aimeite', '111', 3, 80, 100, '20200202');

create table deal_history(
id      int primary key not null,
time    char(50)        not null,
date    char(8)         not null,
product_id  int         not null,
number      int         not null,
customer    char(50),
deal_price  real,
technician  char(50),
import_channel char(50)
)

INSERT INTO deal_history (id,time,date,product_id,number,customer,deal_price,technician,import_channel)
VALUES (1, '202002020122', '20200202', '1', 'xiaoming', 100, 'laowang', 'shanghai');
'''