create database bank_db;

create table bank_db.persons

(
    p_id       int primary key auto_increment,
    name       varchar(30),
    family     varchar(30),
    birth_date date,
    username       varchar(20),
    password   varchar(10)
);

create table bank_db.cards
(
    c_id        int primary key auto_increment,
    bank_name   varchar(20),
    card_number char(16),
    expire_date int,
    cvv2        char(4),
    password    varchar(10),
    amount      int,

    person_id   int,
    foreign key (person_id) references bank_db.persons(p_id)
);


create table bank_db.transactions
(
    t_id        int primary key auto_increment,

    amount      int,
    date_time   datetime,

    sender_id   int,
    foreign key (sender_id) references bank_db.cards (c_id),

    receiver_id int,
    foreign key (receiver_id) references bank_db.cards (c_id)
);

