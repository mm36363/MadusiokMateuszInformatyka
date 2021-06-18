import requests

conversion_rates = {}


def get_latest_data(currency_code):
    response = requests.get('https://v6.exchangerate-api.com/v6/8585a50717b367cf5d408875/latest/{}'.format(currency_code[0])).json()
    conversion_rates[currency_code[0]] = {currency_code[1]: response['conversion_rates'][currency_code[1]]}


def get_exchange_symbols():
    currency_from = input('Podaj walute z jakiej chcesz przeliczyc (kod waluty): ')
    currency_to = input('Podaj walute na jaka chcesz przeliczyc (kod waluty): ')

    return currency_from, currency_to


def get_current_value():
    value = input('Podaj kwote: ')

    return value


def calculate_currency(current_value, currency_code):
    exchange_value1 = conversion_rates[currency_code[0]][currency_code[1]]

    value_from_to = float(current_value) * exchange_value1

    return value_from_to


def print_result(values):
    print("\n{} [{}] = {} [{}]".format(values[0], values[1][0], values[2], values[1][1]))

current_currency = get_exchange_symbols()
amount = get_current_value()
get_latest_data(current_currency)
conversion_result = calculate_currency(amount, current_currency)
print_result([amount, current_currency, conversion_result])