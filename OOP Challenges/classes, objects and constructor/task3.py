# Task 3: Movie Ticket Booking
# Create a MovieTheater class with theater_name and total_seats. Implement a method
# book_seats(number_of_seats) that checks if seats are available. If yes, decrease the available seats
# and return True. If not, return False.
# EXAMPLE INPUT
# theater = MovieTheater("PVR", 10)
# print(theater.book_seats(6))
# print(theater.book_seats(5))
# EXPECTED OUTPUT
# True
# False
class MovieTheater:
    def __init__(self, theater_name, total_seats):
        self.theater_name = theater_name
        self.available_seats = total_seats

    def book_seats(self, number_of_seats):
        if number_of_seats <= self.available_seats:
            self.available_seats -= number_of_seats
            return True
        else:
            return False
theater = MovieTheater("PVR", 10)
print(theater.book_seats(6))
print(theater.book_seats(5))