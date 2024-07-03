from tkinter import * #type: ignore
import tkinter.messagebox
from tkinter import ttk
import requests


class Currency_converter:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x400+0+0")
        self.root.title("Currency Converter")

        self.from_country = StringVar()
        self.to_country = StringVar()


#=========================Heading===========================================
        self.heading = Label(self.root, text="Currency Converter", fg="Black", bg="White", font=("Times new roman", 30, "bold"))
        self.heading.pack(side=TOP, fill=X)

#=========================Main Frame========================================
        self.main_frame = Frame(self.root, bg="grey")
        self.main_frame.pack(fill=BOTH, expand=1)

#======================Box for input====================================
        self.input_currency = Entry(self.main_frame, width=20, font=("Times new roman", 25))
        self.input_currency.grid(row=0, columnspan=2, padx=225, pady=20)

#================Option for from and to conversion==============================
        self.from_currency = Label(self.main_frame, text="From:", fg="White", font=("Times new roman", 15, "bold"))
        self.from_currency.grid(row=1, column=0)
        self.from_currencyEntry = ttk.Combobox(self.main_frame, width=10, textvariable=self.from_country, font=("Times new roman", 15), state="readonly")
        self.from_currencyEntry['values'] = ('Australian Dollar', 'Bulgarian Lev', 'Brazilian Real', 'Canadian Dollar', 'Swiss Franc', 'Chinese Renminbi Yuan', 'Czech Koruna', 'Danish Krone', 'Euro', 'British Pound', 'Hong Kong Dollar', 'Hungarian Forint', 'Indonesian Rupiah', 'Israeli New Sheqel', 'Indian Rupee', 'Icelandic Króna', 'Japanese Yen', 'South Korean Won', 'Mexican Peso', 'Malaysian Ringgit', 'Norwegian Krone', 'New Zealand Dollar', 'Philippine Peso', 'Polish Złoty', 'Romanian Leu', 'Swedish Krona', 'Singapore Dollar', 'Thai Baht', 'Turkish Lira', 'United States Dollar', 'South African Rand')
        self.from_currencyEntry.grid(row=2, column=0, pady=4)

        self.to_currency = Label(self.main_frame, text="To:", fg="White", font=("Times new roman", 15, "bold"))
        self.to_currency.grid(row=1, column=1)
        self.to_currencyEntry = ttk.Combobox(self.main_frame, width=10, textvariable=self.to_country, font=("Times new roman", 15), state="readonly")
        self.to_currencyEntry['values'] = ('Australian Dollar', 'Bulgarian Lev', 'Brazilian Real', 'Canadian Dollar', 'Swiss Franc', 'Chinese Renminbi Yuan', 'Czech Koruna', 'Danish Krone', 'Euro', 'British Pound', 'Hong Kong Dollar', 'Hungarian Forint', 'Indonesian Rupiah', 'Israeli New Sheqel', 'Indian Rupee', 'Icelandic Króna', 'Japanese Yen', 'South Korean Won', 'Mexican Peso', 'Malaysian Ringgit', 'Norwegian Krone', 'New Zealand Dollar', 'Philippine Peso', 'Polish Złoty', 'Romanian Leu', 'Swedish Krona', 'Singapore Dollar', 'Thai Baht', 'Turkish Lira', 'United States Dollar', 'South African Rand')
        self.to_currencyEntry.grid(row=2, column=1, pady=4)

#==================convert button==================================================
        self.convert_button = Button(self.main_frame, text="Convert", fg="black", bg="white", height=3, width=10, font=("Times new roman", 20, "bold"), command=self.convert)
        self.convert_button.grid(row=3, columnspan=2, pady=5)
#=====================output box============================================
        self.output_currency = Entry(self.main_frame, width=20, font=("Times new roman", 25))
        self.output_currency.grid(row=4, columnspan=2, pady=10)



    def convert(self):
        self.output_currency.delete(0, END)
        country_dict = {'Australian Dollar': 'AUD', 'Bulgarian Lev': 'BGN', 'Brazilian Real': 'BRL', 'Canadian Dollar': 'CAD', 'Swiss Franc': 'CHF', 'Chinese Renminbi Yuan': 'CNY', 'Czech Koruna': 'CZK', 'Danish Krone': 'DKK', 'Euro': 'EUR', 'British Pound': 'GBP', 'Hong Kong Dollar': 'HKD', 'Hungarian Forint': 'HUF', 'Indonesian Rupiah': 'IDR', 'Israeli New Sheqel': 'ILS', 'Indian Rupee': 'INR', 'Icelandic Króna': 'ISK', 'Japanese Yen': 'JPY', 'South Korean Won': 'KRW', 'Mexican Peso': 'MXN', 'Malaysian Ringgit': 'MYR', 'Norwegian Krone': 'NOK', 'New Zealand Dollar': 'NZD', 'Philippine Peso': 'PHP', 'Polish Złoty': 'PLN', 'Romanian Leu': 'RON', 'Swedish Krona': 'SEK', 'Singapore Dollar': 'SGD', 'Thai Baht': 'THB', 'Turkish Lira': 'TRY', 'United States Dollar': 'USD', 'South African Rand': 'ZAR'}

        if(self.input_currency.get() == ""):
            tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")

        elif(self.from_country.get() == "" or self.to_country.get() == ""):
            tkinter.messagebox.showinfo("Error !!","Currency Not Selected.\n Please select FROM and TO Currency form menu.")

        elif(self.from_country.get() == self.to_country.get()):
            tkinter.messagebox.showinfo("Error !!","\n Please select different country.")

        else:
            input_curr = self.input_currency.get()
            from_country = country_dict[self.from_country.get()]
            to_country = country_dict[self.to_country.get()]
            response = requests.get(f"https://api.frankfurter.app/latest?amount={input_curr}&from={from_country}&to={to_country}")

            value = response.json()['rates'][to_country]
            self.output_currency.insert(0, str(value))



if __name__ == "__main__":
    root = Tk()
    obj = Currency_converter(root)
    root.mainloop()