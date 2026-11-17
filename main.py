from GroceryItem import GroceryItem

def main():
    item1 = GroceryItem(1, "Milk", 1, "2026-11-25")
    item2 = GroceryItem(2, "Eggs", 12, "2026-12-01")
    item3 = GroceryItem(3, "Apples", 5, "2026-11-22")

    print("Welcome to FreshTrack!")
    print("----------------------")

    print(item1)
    print(item2)
    print(item3)

if __name__ == "__main__":
    main()
