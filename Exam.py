class CurrencyConverter:
    def __init__(self, dollar_rate, dollar_amount):
        self.dollar_rate = dollar_rate
        self.dollar_amount = dollar_amount

    def convert_to_uah(self):
        return self.dollar_amount * self.dollar_rate

    def display_result(self):
        uah_amount = self.convert_to_uah()
        print(f"{self.dollar_amount} USD = {uah_amount:.2f} UAH за дуже хорошим курсом 1 USD = {self.dollar_rate} UAH!!!")


def main():
    dollar_rate = 41.50

    try:
        dollar_amount = float(input("Введіть кількість доларів: "))
        converter = CurrencyConverter(dollar_rate, dollar_amount)
        converter.display_result()

    except ValueError:
        print("Будь ласка, введіть правильні числові значення.")

if __name__ == "__main__":
    main()
