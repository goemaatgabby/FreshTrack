from datetime import datetime

class GroceryItem:
    def __init__(self, item_id, name, quantity, expiration_date):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.expiration_date = datetime.strptime(
            expiration_date, "%Y-%m-%d"
        ).date()

    def __str__(self):
        return (
            f"ID: {self.item_id}, "
            f"Name: {self.name}, "
            f"Quantity: {self.quantity}, "
            f"Expires: {self.expiration_date}"
        )
