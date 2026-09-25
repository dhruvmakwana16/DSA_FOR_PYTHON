-- Create database
CREATE DATABASE leetcode_sql;

USE leetcode_sql;


-- Create ProductPurchases table
CREATE TABLE ProductPurchases (
    user_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (user_id, product_id)
);


-- Insert ProductPurchases data
INSERT INTO ProductPurchases
(user_id, product_id, quantity)
VALUES
(1, 101, 2),
(1, 102, 1),
(1, 103, 3),
(2, 101, 1),
(2, 102, 5),
(2, 104, 1),
(3, 101, 2),
(3, 103, 1),
(3, 105, 4),
(4, 101, 1),
(4, 102, 1),
(4, 103, 2),
(4, 104, 3),
(5, 102, 2),
(5, 104, 1);


-- Create ProductInfo table
CREATE TABLE ProductInfo (
    product_id INT PRIMARY KEY,
    category VARCHAR(100),
    price DECIMAL(10,2)
);


-- Insert ProductInfo data
INSERT INTO ProductInfo
(product_id, category, price)
VALUES
(101, 'Electronics', 100),
(102, 'Books', 20),
(103, 'Clothing', 35),
(104, 'Kitchen', 50),
(105, 'Sports', 75);


-- Solution
SELECT
    p1.product_id AS product1_id,
    p2.product_id AS product2_id,
    pi1.category AS product1_category,
    pi2.category AS product2_category,
    COUNT(DISTINCT p1.user_id) AS customer_count
FROM ProductPurchases p1
JOIN ProductPurchases p2
    ON p1.user_id = p2.user_id
    AND p1.product_id < p2.product_id
JOIN ProductInfo pi1
    ON p1.product_id = pi1.product_id
JOIN ProductInfo pi2
    ON p2.product_id = pi2.product_id
GROUP BY
    p1.product_id,
    p2.product_id,
    pi1.category,
    pi2.category
HAVING COUNT(DISTINCT p1.user_id) >= 3
ORDER BY
    customer_count DESC,
    product1_id ASC,
    product2_id ASC;