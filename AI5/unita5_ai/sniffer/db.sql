create database monitoraggio_db;

create table tls (
    ID serial not null,
    ip_client varchar(15) not null,
    ip_server varchar(15) not null,
    tcp_src int not null,
    tcp_dst int not null,
    data_richiesta date default null,
    ora_richiesta time default null,
    primary key (ID)
);