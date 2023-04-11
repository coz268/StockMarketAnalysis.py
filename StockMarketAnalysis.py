import requests

def stock_analysis(symbol, start_date, end_date):
    url = f"https://api.example.com/stocks/{symbol}?start={start_date}&end={end_date}"
    response = requests.get(url)
    data = response.json()
    prices = [day['price'] for day in data['history']]
    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / len(prices)
    print(f"Maximum price: ${max_price:.2f}")
    print(f"Minimum price: ${min_price:.2f}")
    print(f"Average price: ${avg_price:.2f}")

symbol = input("Enter stock symbol: ")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD
