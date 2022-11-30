import requests
import pandas as pd

# KUCOIN API
api_url = "https://api.kucoin.com"
csv_name = "Kucoin_Market-Pairs"

# API CALL
KuMarketData = requests.get(f"{api_url}/api/v1/symbols",
	headers = {"content-type":"application/json"})

# DATA FRAME 
df = pd.DataFrame(KuMarketData.json()["data"],
    columns = ['symbol', # unique code of a symbol, it would not change after renaming
    'name', # Name of trading pairs, it would change after renaming
    'baseCurrency', # Base currency,e.g. BTC.
    'quoteCurrency', # Quote currency,e.g. USDT.
    'market', # The trading market.
    'baseMinSize', # The minimum order quantity requried to place an order.
    'quoteMinSize', # The minimum order funds required to place a market order.
    'baseMaxSize', # The maximum order size required to place an order.
    'quoteMaxSize', # The maximum order funds required to place a market order.
    'baseIncrement', # The increment of the order size. The value shall be a positive multiple of the baseIncrement.
    'quoteIncrement', # The increment of the funds required to place a market order. The value shall be a positive multiple of the quoteIncrement.
    'priceIncrement', # The increment of the price required to place a limit order. The value shall be a positive multiple of the priceIncrement.
    'feeCurrency', # The currency of charged fees.
    'enableTrading', # Available for transaction or not.
    'isMarginEnabled', # Available for margin or not.
    'priceLimitRate']) # Threshold for price portection

# CSV - INCLUDE THESE COLUMNS ONLY:
df = df[["symbol", "quoteCurrency", "market"]]

# CSV - EXCLUDE EVERY quoteCurrency EXCEPT:
df = df[df['quoteCurrency'].isin(['BTC'])]




# CSV - ORDER ROWS BY
df.sort_values(by='quoteCurrency', inplace=True)

# CSV - EXPORT
df.to_csv(csv_name+'.csv', header=True, index=False)

print("Success...")

PairList=list(df["symbol"])
PairList= [mystring.replace("-", "/") for mystring in PairList]
print(PairList)
import csv


combostring = '","'.join(PairList)
print("testtest")
print(combostring)
# combostring = '["' + combostring +'"]'

print("newtest")
print(combostring)
# for i in PairList:
  
#     # iformat=f'{i},'
#     iformat=str(i)
#     print(iformat)
with open('freqtrade_pairlist.csv', 'w',newline="\n") as f:
        writer = csv.writer(f)
#         # write a row to the csv file
        writer.writerow([combostring])
#     # open the file in the write mode
  
#     # create the csv writer


# #   # open the file in the write mode
# # with open('path/to/csv_file', 'w') as f:
# #     # create the csv writer
# #     writer = csv.writer(f)
# #     for i in PairList:
# #       # write a row to the csv file
# #       writer.writerow(i)
    
import csv

csv.register_dialect('myDialect', delimiter=',', doublequote=False,
                         quoting=csv.QUOTE_NONE, skipinitialspace='True')

f = open("freqtrade_pairlist.csv", 'r')
f = f.read().replace('"', '').replace("['", "'").splitlines()
normal = csv.reader(f, dialect='myDialect')
print
for data in normal:
        print(data)

with open('freqtrade_pairlist.csv', 'w',newline="\n") as f:
        writer = csv.writer(f)
#         # write a row to the csv file
        writer.writerow([data])
#     # open the file in the write mode
  
#     # create the csv writer
       