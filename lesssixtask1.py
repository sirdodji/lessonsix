coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

def make_a_dict():
    new_dict = {coin: code for coin, code in zip(coin, code)}
    print(new_dict)

make_a_dict()