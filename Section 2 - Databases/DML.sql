
-- members
INSERT INTO members (member_id, first_name, last_name, email, phone, above_18)
VALUES 
('smith_c7677', 'Patty', 'Smith', 'Patty_Smith@ross.com', '59428759', true),
('wang_04168', 'Sean', 'Wang', 'Sean_Wang@gibson-calderon.com', '25595367', true),
('estrada_0bf5b', 'Richard', 'Estrada', 'Richard_Estrada@malone.com', '22821527', true),
('cline_825fb', 'Jackson', 'Cline', 'Jackson_Cline@hudson.net', '48056519', true),
('williams_3e726', 'Allen', 'Williams', 'Allen_Williams@sanchez.net', '77991519', true),
('flores_f6828', 'Eric', 'Flores', 'Eric_Flores@dillon-patterson.com', '36641663', true),
('richardson_ef158', 'Anna', 'Richardson', 'Anna_Richardson@perry.com', '64083047', true),
('smith_9625b', 'Benjamin', 'Smith', 'Benjamin_Smith@christian-contreras.com', '95835639', true),
('gomez_876bf', 'Taylor', 'Gomez', 'Taylor_Gomez@johnston.com', '24007567', true),
('rodriguez_93ac7', 'Jeremy', 'Rodriguez', 'Jeremy_Rodriguez@roth.com', '32567967', true),
('garcia_26b55', 'April', 'Garcia', 'April_Garcia@hall.com', '24650447', true),
('garza_40199', 'Sharon', 'Garza', 'Sharon_Garza@duran.com', '59411567', true),
('sanchez_364a7', 'Lori', 'Sanchez', 'Lori_Sanchez@hardin-warner.net', '76989167', true),
('reed_3bc34', 'Joseph', 'Reed', 'Joseph_Reed@kelley.com', '18798163', true),
('armstrong_e2fb8', 'Jason', 'Armstrong', 'Jason_Armstrong@curtis.com', '68514503', true),
('allison_0c21b', 'Jessica', 'Allison', 'Jessica_Allison@harper.com', '66821135', true),
('hall_5eccd', 'Arthur', 'Hall', 'Arthur_Hall@gonzalez.com', '65493407', true),
('meza_5bcfa', 'Sherry', 'Meza', 'Sherry_Meza@west.com', '33491119', true),
('turner_0303a', 'Matthew', 'Turner', 'Matthew_Turner@martinez.com', '73291455', true),
('bauer_18f68', 'Jeffrey', 'Bauer', 'Jeffrey_Bauer@garza.com', '51154803', true),
('randolph_76c7a', 'Sophia', 'Randolph', 'Sophia_Randolph@leonard-ramirez.com', '94510479', true),
('matthews_2a414', 'Marissa', 'Matthews', 'Marissa_Matthews@graves.com', '20636447', true);

-- items
INSERT INTO items (item_id, item_name, manufacture_name, cost, weight_kg) VALUES (1, 'T-shirt', 'Nike', 29.99, 0.3);
INSERT INTO items (item_id, item_name, manufacture_name, cost, weight_kg) VALUES (2, 'Hoodie', 'Adidas', 49.99, 0.6);
INSERT INTO items (item_id, item_name, manufacture_name, cost, weight_kg) VALUES (3, 'Jeans', 'Levi', 89.99, 0.8);
INSERT INTO items (item_id, item_name, manufacture_name, cost, weight_kg) VALUES (4, 'Sneakers', 'Puma', 59.99, 0.5);

-- transaction
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (1, 4, 2, 200, 1.0, '2023-02-10 12:34:56', 'matthews_2a414');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (1, 2, 1, 80, 0.6, '2023-02-10 12:34:56', 'matthews_2a414');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (2, 3, 3, 240, 2.4, '2023-02-09 10:22:33', 'allison_0c21b');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (3, 1, 5, 200, 1.5, '2023-02-08 14:44:55', 'bauer_18f68');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (4, 4, 1, 100, 0.5, '2023-02-10 12:34:56', 'randolph_76c7a');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (5, 3, 3, 360, 2.4, '2023-02-09 10:22:33', 'randolph_76c7a');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (6, 1, 7, 280, 2.1, '2023-02-08 14:44:55', 'matthews_2a414');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (7, 1, 1, 40, 0.3, '2023-02-08 14:44:55', 'flores_f6828');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (8, 1, 1, 40, 0.3, '2023-02-09 14:44:55', 'flores_f6828');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (9, 1, 1, 40, 0.3, '2023-02-10 14:47:55', 'sanchez_364a7');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (10, 2, 1, 80, 0.6, '2023-02-11 15:44:55', 'reed_3bc34');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (11, 2, 2, 160, 1.2, '2023-02-08 19:44:55', 'meza_5bcfa');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (12, 3, 2, 200, 1.6, '2023-02-11 14:11:23', 'turner_0303a');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (13, 3, 1, 100, 0.8, '2023-02-02 11:43:55', 'turner_0303a');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (14, 4, 1, 80, 0.5, '2023-02-04 20:20:55', 'cline_825fb');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (15, 4, 2, 160, 1.0, '2023-02-14 10:02:55', 'garza_40199');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (16, 3, 2, 200, 1.6, '2023-02-05 15:15:55', 'wang_04168');
INSERT INTO transactions (transaction_id, item_id, quantity, total_price, total_weight, transaction_datetime, member_id) VALUES (17, 3, 1, 100, 0.8, '2023-02-03 12:57:55', 'wang_04168');
