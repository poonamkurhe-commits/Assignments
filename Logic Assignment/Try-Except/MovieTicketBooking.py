# Question 13: Movie Ticket Booking
# Description: Handle invalid seat number input.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
try:
    seat = int(input("Enter seat number: "))
    if seat <= 0:
        raise ValueError
    print("Seat booked successfully")
except ValueError:
    print("Invalid seat number")