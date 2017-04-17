create database mht;

CREATE TABLE billProduct(billId int, billProductId int, billProductName varchar(200));

select 	t1.BillId,
		t1.ProductId,
		t1.ProductName
from MhtBillProduct t1;

copy billproduct from '/Users/yao/MyWork/WangJun/bills.csv' with delimiter as ',' csv header;

select t1.billid,string_agg(t1.billproductname,',') from billproduct t1 group by t1.billid

select cast(t1.billid as text) billid,string_agg(t1.billproductname,',') from billproduct t1 group by t1.billid