import requests
from bs4 import BeautifulSoup

def scrape_weather(soup):
    # Example function to scrape weather; you must adapt it to your specific website.
    try:
        location = soup.find('div', class_='location').get_text().strip()
        temperature = soup.find('span', class_='temp').get_text().strip()
        description = soup.find('div', class_='weather-description').get_text().strip()
        return f"Weather in {location}: {temperature}, {description}"
    except AttributeError:
        return "Weather data not found."

def scrape_sports(soup):
    # Example function to scrape sports scores; you must adapt it to your specific website.
    try:
        team = soup.find('div', class_='team-name').get_text().strip()
        score = soup.find('div', class_='score').get_text().strip()
        return f"Score for {team}: {score}"
    except AttributeError:
        return "Sports data not found."

def fetch_data():
    url = input("Enter the URL of the site you want to scrape: ")
    data_type = input("Enter the type of data to scrape (weather/sports): ")

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        if data_type.lower() == 'weather':
            result = scrape_weather(soup)
        elif data_type.lower() == 'sports':
            result = scrape_sports(soup)
        else:
            result = "Unsupported data type specified."
        
        print(result)

    except requests.RequestException as e:
        print("Error during requests to {0} : {1}".format(url, str(e)))

if __name__ == "__main__":
    fetch_data()
