# SQL Query: Customer Data by Registration Year

## Objective

Write a SQL query to display the `id`, `name`, and `citizen_id` of customers who registered in the year 2022.

---

## Query

```sql
SELECT id, name, citizen_id
FROM Customers
WHERE registration_date >= '2022-01-01' AND registration_date < '2023-01-01';
```

### Explanation

This query filters the `Customers` table to include only records where the `registration_date` falls within the 2022 calendar year.
