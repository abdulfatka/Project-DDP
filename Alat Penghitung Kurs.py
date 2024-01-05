import tkinter as tk

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Alat Konvert Kurs")

        # Dictionary untuk menyimpan nilai tukar mata uang
        self.exchange_rates = {
            "USD": 0.000070,  # 1 IDR = 0.000070 USD
            "JPY": 0.0077,    # 1 IDR = 0.0077 JPY
            "EUR": 0.000059,  # 1 IDR = 0.000059 EUR
            "SAR": 0.00026    # 1 IDR = 0.00026 SAR
        }

        # Label dan Entry untuk input jumlah uang
        self.amount_label = tk.Label(master, text="Amount (IDR):")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label dan OptionMenu untuk mata uang tujuan
        self.to_currency_label = tk.Label(master, text="To Currency:")
        self.to_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.to_currency_var = tk.StringVar()
        self.to_currency_combobox = tk.OptionMenu(master, self.to_currency_var, *self.exchange_rates.keys())
        self.to_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

        # Label dan Entry untuk menampilkan hasil konversi
        self.result_label = tk.Label(master, text="Result:")
        self.result_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(master, state="readonly", textvariable=self.result_var)
        self.result_entry.grid(row=2, column=1, padx=10, pady=10)

        # Button untuk menghitung konversi
        self.convert_button = tk.Button(master, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

    def convert_currency(self):
        try:
            amount_idr = float(self.amount_entry.get())
            to_currency = self.to_currency_var.get()

            # Menghitung nilai tukar
            rate = self.exchange_rates[to_currency]
            result = round(amount_idr * rate, 2)

            # Menampilkan hasil konversi
            self.result_var.set(f"{amount_idr} IDR = {result} {to_currency}")
        except ValueError:
            self.result_var.set("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
