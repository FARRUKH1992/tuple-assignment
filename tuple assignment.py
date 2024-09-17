# lesson 1





def format_itineraries(flight_list):
    formatted_itineraries = []
    
    for index, (traveler_name, origin, destination) in enumerate(flight_list, start=1):
        itinerary = f"Itinerary {index}: {traveler_name} - From {origin} to {destination}"
        formatted_itineraries.append(itinerary)
    
    return "\n".join(formatted_itineraries)


flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
result = format_itineraries(flights)
print(result)







# lesson 2  


def add_book(library, new_book):
    """
    Add a new book to the library if it does not already exist.

    Parameters:
    - library (list of tuples): The current list of books in the library.
    - new_book (tuple): The new book to add, in the format ("Book Title", "Author").

    Returns:
    - list of tuples: The updated list of books.
    """
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        library.append(new_book)
        print(f"Added '{new_book[0]}' by {new_book[1]} to the library.")

    return library

# library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# usage:
new_book = ("To Kill a Mockingbird", "Harper Lee")
library = add_book(library, new_book)  # Should add the new book

# add a duplicate book
duplicate_book = ("1984", "George Orwell")
library = add_book(library, duplicate_book)  # Should print a message about the duplicate


# lesson 3 

def process_orders(orders):
    """
    Process a list of customer orders and print the details in a user-friendly format.

    Parameters:
    - orders (list of tuples): Each tuple contains (customer_name, product, quantity).
    """
    for order in orders:
        customer_name, product, quantity = order
        print(f"Customer: {customer_name}")
        print(f"Product: {product}")
        print(f"Quantity: {quantity}")
        print("-" * 20)  # Separator for readability

# data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3)
]


process_orders(orders)