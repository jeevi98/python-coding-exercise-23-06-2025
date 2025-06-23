import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert"
    params = {
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": amount
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("success", True):
            result = data["result"]
            print(f"\n {amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
        else:
            print(" Conversion failed. Check currency codes.")
    except Exception as e:
        print(f" Error fetching rates: {e}")

def main():
    print(" Currency Converter CLI")
    print("-" * 30)

    try:
        from_currency = input("From Currency (e.g. USD): ").strip()
        to_currency = input("To Currency (e.g. INR): ").strip()
        amount = float(input("Amount to convert: "))
        convert_currency(from_currency, to_currency, amount)
    except ValueError:
        print(" Please enter a valid amount.")

if __name__ == "__main__":
    main()
