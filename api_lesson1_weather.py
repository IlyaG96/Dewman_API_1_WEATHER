import requests


def show_forecast(cities: list,
                  forecast_params: str,
                  forecast_language: str) -> None:
    """shows weather forecast for cities from cities-list in the terminal
       the description of forecast_params variable and all supported languages
       can be found at https://wttr.in/:help"""
    for city in cities:
        payload = {forecast_params: "", "lang": forecast_language}
        url = f'https://wttr.in/{city}'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    forecast_params = 'nTqm'
    forecast_language = 'ru'
    cities = ['Лондон',
              'Череповец',
              'Шереметьево'
              ]

    show_forecast(cities, forecast_params, forecast_language)
