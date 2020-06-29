select * from project1overhillwnerydw.customer_dimension;
select * from project1overhillwnerydw.date_dimension;
select * from project1overhillwnerydw.product_dimension;
select * from project1overhillwnerydw.sales_agent_dimension;
select * from project1overhillwnerydw.salesprofit_fact;
select * from project1overhillwnerydw.salesprofit_fact a join project1overhillwnerydw.date_dimension b on a.Date_Dimension_Date = b.Date;
