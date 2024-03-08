import tkinter as tk
from tkinter import messagebox

class OnlineStoreApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Flare Games Online Store")

        # Create labels for item names, prices, and images
        self.game_label = tk.Label(self.root, text="Game", font=("Helvetica", 12))
        self.remote_label = tk.Label(self.root, text="Game Remote", font=("Helvetica", 12))
        self.headphones_label = tk.Label(self.root, text="Headphones", font=("Helvetica", 12))

        # Create buttons to add items to cart
        self.game_button = tk.Button(self.root, text="Add Game ($50)", command=self.add_to_cart("Game"))
        self.remote_button = tk.Button(self.root, text="Add Remote ($50)", command=self.add_to_cart("Remote"))
        self.headphones_button = tk.Button(self.root, text="Add Headphones ($75)", command=self.add_to_cart("Headphones"))

        # Initialize cart and total cost
        self.cart = []
        self.total_cost = 0

        # Display items
        self.game_label.pack()
        self.game_button.pack()
        self.remote_label.pack()
        self.remote_button.pack()
        self.headphones_label.pack()
        self.headphones_button.pack()

        # Display total cost label
        self.total_cost_label = tk.Label(self.root, text="Total Cost: $0", font=("Helvetica", 12))
        self.total_cost_label.pack()

    def add_to_cart(self, item_name):
        def callback():
            self.cart.append(item_name)
            self.total_cost += self.get_item_price(item_name)
            self.update_total_cost_label()
            messagebox.showinfo("Added to Cart", f"{item_name} added to cart!")
        return callback

    def get_item_price(self, item_name):
        # Define item prices (you can modify these as needed)
        item_prices = {"Game": 50, "Remote": 50, "Headphones": 75}
        return item_prices.get(item_name, 0)

    def update_total_cost_label(self):
        self.total_cost_label.config(text=f"Total Cost: ${self.total_cost}")

    def run(self):
        self.root.mainloop()

# Create an instance of the OnlineStoreApp class and run the application
if __name__ == "__main__":
    app = OnlineStoreApp()
    app.run()
