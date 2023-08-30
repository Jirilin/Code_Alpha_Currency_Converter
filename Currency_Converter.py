import tkinter as tk
from forex_python.converter import CurrencyRates

# Create a CurrencyConverter object
c = CurrencyRates()

# Function to perform currency conversion
def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

    converted_amount = c.convert(from_currency, to_currency, amount)
    result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create labels
amount_label = tk.Label(root, text="Enter Amount:")
from_label = tk.Label(root, text="From Currency:")
to_label = tk.Label(root, text="To Currency:")
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))

# Create entry fields
amount_entry = tk.Entry(root)
from_currency_var = tk.StringVar(root)
to_currency_var = tk.StringVar(root)

from_currency_var.set("USD")  # Default 'From' currency
to_currency_var.set("EUR")    # Default 'To' currency

from_currency_menu = tk.OptionMenu(root, from_currency_var, "USD", "EUR", "GBP", "JPY")
to_currency_menu = tk.OptionMenu(root, to_currency_var, "USD", "EUR", "GBP", "JPY")

# Create the conversion button
convert_button = tk.Button(root, text="Convert", command=convert_currency)

# Organize the widgets using the grid layout
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry.grid(row=0, column=1, padx=10, pady=10)
from_label.grid(row=1, column=0, padx=10, pady=10)
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)
to_label.grid(row=2, column=0, padx=10, pady=10)
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)
convert_button.grid(row=3, columnspan=2, padx=10, pady=20)
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
