import requests
from bs4 import BeautifulSoup

def parse_steam_market(item_name):
    url = f"https://steamcommunity.com/market/search?q={item_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        item_listings = soup.find_all('div', class_='market_listing_row')
        
        for listing in item_listings:
            item_title = listing.find('span', class_='market_listing_item_name').text.strip()
            item_price = listing.find('span', class_='normal_price').text.strip()
            print(f"Item: {item_title}, Price: {item_price}")
    else:
        print("Error: Failed to retrieve data from Steam Market.")

if __name__ == "__main__":
    item_name = input("Enter item name: ")
    parse_steam_market(item_name)
