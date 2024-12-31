DELIMITER $$

CREATE PROCEDURE AddBooking(IN customer_id INT, IN booking_date DATE)
BEGIN
    INSERT INTO Bookings (CustomerID, BookingDate) VALUES (customer_id, booking_date);
END $$

DELIMITER ;
DELIMITER $$

CREATE PROCEDURE CancelBooking(IN booking_id INT)
BEGIN
    DELETE FROM Bookings WHERE BookingID = booking_id;
END $$

DELIMITER ;
DELIMITER $$

CREATE PROCEDURE UpdateBooking(IN booking_id INT, IN new_date DATE)
BEGIN
    UPDATE Bookings SET BookingDate = new_date WHERE BookingID = booking_id;
END $$

DELIMITER ;
