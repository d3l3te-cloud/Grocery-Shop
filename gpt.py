#gpt made billing as follows
items = (
    ("001", "Item 1", 50),
    ("002", "Item 2", 100),
    ("003", "Item 3", 75),
    # Add more items as needed
)

def calculate_total(itemcode, quantity):
    for item in items:
        if item[0] == itemcode:
            price = item[2]  # Fetching price from the tuple based on itemcode
            total = price * quantity
            return total
    return 0  # If itemcode doesn't match, return 0 indicating item not found

# Example usage
while True:
    itemcode = input("Enter item code (or 'exit' to finish): ")
    if itemcode.lower() == "exit":
        break

    quantity = int(input(f"Enter quantity for {itemcode}: "))
    total = calculate_total(itemcode, quantity)
    
    if total:
        print(f"Total for {itemcode}: {total}")
    else:
        print("Item not found!")

# Sample Output:
# Enter item code (or 'exit' to finish): 001
# Enter quantity for 001: 3
# Total for 001: 150
# Enter item code (or 'exit' to finish): exit
