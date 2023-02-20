--Which are the top 10 members by spending ?
select 
	t.member_id,
	first_name,
	last_name,
	sum(total_price) as total_spent
from transactions t 
left join members m 
	on t.member_id = m.member_id 
group by 1,2,3
order by 4 desc 
limit 10

--Which are the top 3 items that are frequently brought by members, in terms of quantity ?
select 
	t.item_id,
	item_name,
	sum(quantity) as quantity_bought 
from transactions t 
left join items i 
	on t.item_id = i.item_id 
group by 1,2 
order by 3 desc
limit 3

--Which are the top 3 items that are frequently brought by members, in terms of frequency ?
select 
	t.item_id,
	item_name,
	count(distinct transaction_id) as frequency_bought 
from transactions t 
left join items i 
	on t.item_id = i.item_id 
group by 1,2 
order by 3 desc
limit 3

--which items bring in most revenue ?
select 
	t.item_id,
	item_name,
	sum(total_price) as revenue 
from transactions t 
left join items i 
	on t.item_id = i.item_id 
group by 1,2 
order by 3 desc
limit 5

--Which members transacted the most ?
select 
	t.member_id,
	first_name,
	last_name,
	count(distinct transaction_id) as number_of_transactions
from transactions t 
left join members m 
	on t.member_id = m.member_id 
group by 1,2,3
order by 4 desc 
limit 10
