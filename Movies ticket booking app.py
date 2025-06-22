
def movie_ticket_booking():
    # Predefined movies with showtimes and seat prices
    movies = {
        "Titanic": {"showtimes": ["10:00 AM", "1:00 PM", "4:00 PM"], "price": 10.00},
        "Avator": {"showtimes": ["11:00 AM", "2:00 PM", "5:00 PM"], "price": 12.00},
        "Terminator": {"showtimes": ["12:00 PM", "3:00 PM", "6:00 PM"], "price": 8.00},
    }

    total_bookings = 0
    total_cost = 0.0

    while True:
        print("\nAvailable Movies:")
        for movie, details in movies.items():
            print(f"{movie}: Showtimes: {', '.join(details['showtimes'])}, Price: ETB{details['price']:.2f}")

        selected_movie = input("Choose a movie: ")
        if selected_movie in movies:
            num_tickets = int(input("How many tickets do you want to book? "))
            price = movies[selected_movie]["price"] * num_tickets
            total_cost += price
            total_bookings += num_tickets
            print(f"Total price for {num_tickets} tickets: ETB{price:.2f}")
        else:
            print("Invalid movie selection. Please try again.")

        another = input("Do you want to book another movie? (yes/no): ").strip().lower()
        if another == "no":
            break

    print(f"\nTotal bookings: {total_bookings}, Total cost: ETB{total_cost:.2f}")

movie_ticket_booking()