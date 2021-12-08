import matplotlib.pyplot as plt
import yfinance as yf

start = ''
end = ''

# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data10y = yf.download('AAPL AIR BP BUD CRM CSCO', start='2010-12-31', end='2020-12-31')
data5y = yf.download('AAPL AIR BP BUD CRM CSCO', start='2015-12-31', end='2020-12-31')
data3y = yf.download('AAPL AIR BP BUD CRM CSCO', start='2017-12-31', end='2020-12-31')
data1y = yf.download('AAPL AIR BP BUD CRM CSCO', start='2019-12-31', end='2020-12-31')

closing = data10y['Close']


tickerList = ['AAPL', 'AIR', 'BP', 'BUD', 'CRM', 'CSCO']


# tickerPrices = {'APPL': [], 'AIR' : [], 'BP' : [], 'DUB': [], 'CRM' : [], 'CSCO' : []}


for ticker in tickerList:
    stock = closing[ticker]

    valueList = []
    dayCountList = []

    value = 10000
    count = 0
    for pctChange in stock:
        if count == 0:
            print("SKIPPING NAN ROW")
            count = count + 1
        else:
            value = value + (value * pctChange)
            dayCountList.append(count)
            valueList.append(value)
            count = count + 1

    plt.plot(dayCountList, valueList)
    plt.show()

    print("Final Value After 10 Years: " + str(value) + " For the stock: " + ticker)




# tickerList = ['AAPL', 'AIR', 'BP', 'BUD', 'CRM', 'CSCO']
