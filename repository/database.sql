create database mft_library;

create table mft_library.persons
(
    p_id         int primary key auto_increment,
    name       varchar(30),
    family     varchar(30),
    birth_date date,
    username   varchar(30),
    password   varchar(20)
);


create table mft_library.books
(
    b_id        int primary key auto_increment,
    title     varchar(30),
    writer    varchar(60),
    publisher varchar(50),
    pages     int
);


create table mft_library.borrows
(
    id        int primary key auto_increment,
    borrow_date date,
    return_date date default null,

    person_id int,
    foreign key (person_id) references mft_library.persons(p_id),

    book_id int,
    foreign key (book_id) references mft_library.books(b_id)
);