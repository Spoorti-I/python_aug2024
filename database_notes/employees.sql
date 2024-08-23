


 
 use spoorti_db;
 
 select * for employees; 
 
 create table employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(40) not null, technology varchar(30) not null, phone_num bigint unique, commission int, salary float default 0, years_of_exp int);
 
insert into employees(name,designation,technology, phone_num, commission, salary, years_of_exp) values('soumya','grafic_engg','project',9897562652,14,3455,23);
 insert into employees(name,designation,technology, phone_num, commission, salary, years_of_exp) values('srujana','disign_engg','c',9897532352,12,34567,20);
insert into employees(name,designation,technology, phone_num, commission, salary, years_of_exp) values('sam','disign_engg','c++',9897552652,12,3456347,20);
insert into employees(name,designation,technology, phone_num, commission, salary, years_of_exp) values('shivam','disign_engg','java',9897582652,12,3454,20);
insert into employees(name,designation,technology, phone_num, commission, salary, years_of_exp) values('spoorti','disign_engg','project',9897593652,12,34544,20);
insert into employees(name,designation,technology, phone_num, commission, salary, years_of_exp) values('shreya','manager','project',9895534652,12,34533,20);
insert into employees(name,designation,technology, phone_num, years_of_exp) values('spoorti','disign_engg','project',9895526552,20);
insert into employees(name,designation,technology) values('spoorti','disign_engg','project');
insert into employees(name,designation,technology,  phone_num, commission, salary, years_of_exp) values('spoorti','jfgd','te',9897522652,12,34567,20);
insert into employees(name) values('spoorti');
insert into employees(name,designation,technology, phone_num, commission, salary, years_of_exp) values('spoorti','disign_engg','project',9897532452,12,34567,20);

select * from employees;
