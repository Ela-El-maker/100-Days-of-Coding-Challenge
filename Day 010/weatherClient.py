import requests
import bs4

def main():
    # print the header
    # get zipcode from user
    # get html from web
    # parse the html
    # display for the forecast
    print("Hello from main")

    printHeader()
    code = input('What zipcode do you want the Weather for (97201) :- ')

    html = getHtmlWeb(code)

    getHtmlWebsiteFrom(html)



def printHeader():
    print('------------------------------------------------')
    print('---------------    Weather App  ---------------')
    print('------------------------------------------------')
    print()

def getHtmlWeb(zipcode):
    url = 'https://www.weather.com/weather/today/l/{}'.format(zipcode)
    # print(url)
    response = requests.get(url)
    # print(response.status_code)
    print(response.text[250])

    return response.text

def getHtmlWebsiteFrom(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    


if __name__ == '__main__':
    main()