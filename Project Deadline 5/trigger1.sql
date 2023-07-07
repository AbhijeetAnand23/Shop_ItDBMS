# When a customer add product to cart then this trigger change the availabilty of stock 

DELIMITER $$
CREATE TRIGGER update_product_stock 
AFTER INSERT ON cart_item
FOR EACH ROW
BEGIN
  UPDATE product
  SET stock = stock - NEW.quantity
  WHERE product_id = NEW.product_id;
END $$
DELIMITER ;