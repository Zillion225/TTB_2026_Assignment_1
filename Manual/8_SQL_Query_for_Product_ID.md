# SQL Query: Product and Customer Information by Customer ID

## Objective

Write a SQL query to display the `product_id`, `product_name`, customer `full_name`, and `citizen_id` for a specific customer with `customer_id = '001110001'`.

This query requires joining multiple tables to link customers to the products they have ordered.

---

## Query

```sql
SELECT
    p.product_id,
    p.product_name,
    c.full_name,
    c.citizen_id
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Products p ON o.product_id = p.product_id
WHERE c.customer_id = '001110001';
```

---

## Explanation of Joins

This query uses a series of `JOIN` clauses to link the necessary tables and retrieve the requested information. The `Orders` table serves as a bridge between `Customers` and `Products`.

1.  **`FROM Customers c`**
    -   The query starts with the `Customers` table, aliased as `c`, to filter by the specific `customer_id`.

2.  **`JOIN Orders o ON c.customer_id = o.customer_id`**
    -   This joins `Customers` with the `Orders` table (aliased as `o`). It links a customer to all the orders they have placed, effectively finding all order records belonging to `customer_id = '001110001'`.

3.  **`JOIN Products p ON o.product_id = p.product_id`**
    -   This joins the result with the `Products` table (aliased as `p`). It uses the `product_id` from each order to look up the corresponding product details, such as the `product_name`.
