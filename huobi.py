
import ccxt

def huobi():
    return  ccxt.huobipro({
        # 'apiKey': apikey,
        # 'secret': secretkey,
        'rateLimit': 10000,  # 统一的交易所属性
        'options': {
            'adjustForTimeDifference': True,  # 特定交易所的属性
        }
    })
