select customer.customer_name as CUSTOMER_NAME, customer.customer_id as CUSTOMER_ID, sum(cart.total_price) as Total from customer inner join cart on customer.customer_id = cart.customer_id group by customer_id;

# Total purchase value by all customers