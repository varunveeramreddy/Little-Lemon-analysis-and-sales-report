DELIMITER $$
CREATE PROCEDURE GetAllCustomers()
BEGIN
    SELECT * FROM Customers;
END $$
DELIMITER ;
