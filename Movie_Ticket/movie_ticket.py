"""
Movie Ticket - A simple movie ticket booking system
"""

from datetime import datetime


class MovieTicket:
    """Movie Ticket booking system."""

    def __init__(self):
        """Initialize the movie booking system."""
        self.movies = {
            1: {"title": "Inception", "duration": "2h 28m", "rating": "PG-13"},
            2: {"title": "The Dark Knight", "duration": "2h 32m", "rating": "PG-13"},
            3: {"title": "Interstellar", "duration": "2h 49m", "rating": "PG-13"},
            4: {"title": "Avengers: Endgame", "duration": "3h 1m", "rating": "PG-13"},
            5: {"title": "The Matrix", "duration": "2h 16m", "rating": "R"}
        }

        self.show_times = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"]

        self.ticket_prices = {
            "regular": 12.00,
            "premium": 18.00,
            "vip": 25.00
        }

        # Theater with 5 rows (A-E) and 10 seats per row
        self.seats = {}
        self._initialize_seats()

        self.bookings = []
        self.booking_counter = 1000

    def _initialize_seats(self):
        """Initialize available seats."""
        rows = ["A", "B", "C", "D", "E"]
        for row in rows:
            for seat_num in range(1, 11):
                seat_id = f"{row}{seat_num}"
                self.seats[seat_id] = {"available": True, "type": "regular"}

        # Premium seats (rows C and D)
        for seat_num in range(1, 11):
            self.seats[f"C{seat_num}"]["type"] = "premium"
            self.seats[f"D{seat_num}"]["type"] = "premium"

        # VIP seats (row E)
        for seat_num in range(1, 11):
            self.seats[f"E{seat_num}"]["type"] = "vip"

    def get_movies(self):
        """Get list of available movies."""
        return self.movies

    def get_show_times(self):
        """Get available show times."""
        return self.show_times

    def display_seat_map(self):
        """Display the seat map."""
        result = ["\n       🎬 SCREEN 🎬       \n"]
        result.append("-" * 35)

        rows = ["A", "B", "C", "D", "E"]
        for row in rows:
            row_display = f"  {row} | "
            for seat_num in range(1, 11):
                seat_id = f"{row}{seat_num}"
                seat = self.seats[seat_id]
                if seat["available"]:
                    if seat["type"] == "vip":
                        row_display += "👑 "
                    elif seat["type"] == "premium":
                        row_display += "⭐ "
                    else:
                        row_display += "🟢 "
                else:
                    row_display += "❌ "
            result.append(row_display)

        result.append("-" * 35)
        result.append("  Legend: 🟢 Regular  ⭐ Premium  👑 VIP  ❌ Taken")
        return "\n".join(result)

    def book_ticket(self, movie_id, show_time, seat_id, customer_name):
        """Book a ticket."""
        if movie_id not in self.movies:
            return False, "Invalid movie selection."

        if show_time not in self.show_times:
            return False, "Invalid show time."

        seat_id = seat_id.upper()
        if seat_id not in self.seats:
            return False, "Invalid seat selection."

        if not self.seats[seat_id]["available"]:
            return False, "Seat is already taken."

        seat_type = self.seats[seat_id]["type"]
        price = self.ticket_prices[seat_type]

        self.seats[seat_id]["available"] = False
        self.booking_counter += 1

        booking = {
            "booking_id": f"TKT{self.booking_counter}",
            "customer": customer_name,
            "movie": self.movies[movie_id]["title"],
            "show_time": show_time,
            "seat": seat_id,
            "seat_type": seat_type,
            "price": price,
            "booking_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.bookings.append(booking)

        return True, booking

    def cancel_booking(self, booking_id):
        """Cancel a booking."""
        for booking in self.bookings:
            if booking["booking_id"] == booking_id:
                seat_id = booking["seat"]
                self.seats[seat_id]["available"] = True
                self.bookings.remove(booking)
                return True, "Booking cancelled successfully."
        return False, "Booking not found."

    def get_booking_details(self, booking_id):
        """Get details of a booking."""
        for booking in self.bookings:
            if booking["booking_id"] == booking_id:
                return True, booking
        return False, "Booking not found."

    def print_ticket(self, booking):
        """Print a formatted ticket."""
        return f"""
╔══════════════════════════════════════════╗
║          🎬 MOVIE TICKET 🎬              ║
╠══════════════════════════════════════════╣
║  Booking ID: {booking['booking_id']:<25} ║
║  Customer:   {booking['customer']:<25} ║
║  Movie:      {booking['movie']:<25} ║
║  Show Time:  {booking['show_time']:<25} ║
║  Seat:       {booking['seat']} ({booking['seat_type'].capitalize()}){'':18}║
║  Price:      ${booking['price']:.2f}{'':24}║
║  Date:       {booking['booking_date'][:10]}{'':18}║
╠══════════════════════════════════════════╣
║          Enjoy your movie! 🍿            ║
╚══════════════════════════════════════════╝
"""


def main():
    """Main function to run the movie ticket system."""
    system = MovieTicket()

    print("=" * 50)
    print("       Welcome to Movie Ticket Booking")
    print("=" * 50)

    while True:
        print("\n" + "-" * 50)
        print("1. View Movies")
        print("2. View Show Times")
        print("3. View Seat Map")
        print("4. Book Ticket")
        print("5. Cancel Booking")
        print("6. View Booking")
        print("7. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("\n🎬 Available Movies:")
            for mid, movie in system.get_movies().items():
                print(f"  {mid}. {movie['title']} "
                      f"({movie['duration']}) - {movie['rating']}")

        elif choice == "2":
            print("\n🕐 Show Times:")
            for i, time in enumerate(system.get_show_times(), 1):
                print(f"  {i}. {time}")

        elif choice == "3":
            print(system.display_seat_map())
            print(f"\nPrices: Regular ${system.ticket_prices['regular']:.2f} | "
                  f"Premium ${system.ticket_prices['premium']:.2f} | "
                  f"VIP ${system.ticket_prices['vip']:.2f}")

        elif choice == "4":
            print("\n🎬 Available Movies:")
            for mid, movie in system.get_movies().items():
                print(f"  {mid}. {movie['title']}")

            try:
                movie_id = int(input("\nSelect movie (1-5): "))
                print("\n🕐 Show Times:")
                for i, time in enumerate(system.get_show_times(), 1):
                    print(f"  {i}. {time}")
                time_choice = int(input("Select show time (1-5): "))
                show_time = system.get_show_times()[time_choice - 1]

                print(system.display_seat_map())
                seat_id = input("Enter seat (e.g., A1, B5): ")
                customer_name = input("Enter your name: ")

                success, result = system.book_ticket(
                    movie_id, show_time, seat_id, customer_name
                )
                if success:
                    print("\n✅ Booking Successful!")
                    print(system.print_ticket(result))
                else:
                    print(f"\n❌ {result}")
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

        elif choice == "5":
            booking_id = input("Enter Booking ID to cancel: ")
            success, msg = system.cancel_booking(booking_id)
            print(f"\n{'✅' if success else '❌'} {msg}")

        elif choice == "6":
            booking_id = input("Enter Booking ID: ")
            success, result = system.get_booking_details(booking_id)
            if success:
                print(system.print_ticket(result))
            else:
                print(f"\n❌ {result}")

        elif choice == "7":
            print("\nThank you for using Movie Ticket Booking. Goodbye! 🎬")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
