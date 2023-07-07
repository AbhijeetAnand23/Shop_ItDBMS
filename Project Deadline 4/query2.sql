update product set normal_price = 0.9*normal_price, elite_price = 0.9*elite_price, prime_price = 0.9*prime_price where stock>50;

# setting 10% on all products which counts more than 50.