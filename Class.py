import requests
from config import keys
class ConvertionExeptions(Exception): #Класс для обработки ошибок
    pass

class CryptoConverter: #Обработка ошибок
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionExeptions(f'Нельзя конвертировать одинаковые валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeptions(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeptions(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeptions(f'Не удалось обработать кол-во {amount}')

        #Получение данных с сайта
        api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={base_ticker}&have={quote_ticker}&amount={amount}'
        response = requests.get(api_url, headers={'X-Api-Key': '0h+iHZhUolyFh/ElhjIw6A==6iPO2HW0R2vqPsD7'})

        if response.status_code == requests.codes.ok:
            json_data = response.json()
            total_base = json_data["new_amount"]
        return total_base