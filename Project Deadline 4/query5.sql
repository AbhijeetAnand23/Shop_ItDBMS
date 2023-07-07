update customer set membership = 'prime' where customer_id in (select customer_id from cart group by customer_id having sum(total_price) > 2000 ) and membership = 'Normal';

# upgrading all the normal members to prime members whose purchase is greater than 2000