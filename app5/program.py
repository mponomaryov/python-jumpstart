import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond temp scale loc')

def main():
    print_header()
    zipcode = input('Enter your zip code (e.g. 91910): ')
    html = get_html_from_web(zipcode)
    report = get_weather_from_html(html)
    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

def print_header():
    print('-------------------')
    print('    WEATHER APP')
    print('-------------------')
    print()

def get_html_from_web(zipcode):
    url = 'http://wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    cond = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    cond = cleanup_text(cond)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    return WeatherReport(cond=cond, temp=temp, scale=scale, loc=loc)

def cleanup_text(text):
    if text:
        text = text.strip()
    return text

if __name__ == '__main__':
    main()
