import pymysql.cursors
import pandas as pd

def fetch(ticker_symbol, start_date, end_date):
    # Connect to the database
    connection = pymysql.connect(host='rcdbdev.cv7if3pihnbt.us-west-2.rds.amazonaws.com',
                                 user='test',
                                 password='t4studacity',
                                 db='rcdb',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        # Read a single record
        sql = """SELECT price_date, adj_close_price FROM securities
                INNER JOIN daily_prices on securities.security_id = daily_prices.security_id
                WHERE securities.ticker_symbol=%s AND price_date >= %s AND price_date <= %s
                ORDER BY daily_prices.price_date ASC"""
        cursor.execute(sql, (ticker_symbol, start_date, end_date))
        result = cursor.fetchall()

        connection.close()

        prices = [d['adj_close_price'] for d in result]
        dates = [d['price_date'] for d in result]
        return prices, dates

def fetch_multi(tickers, start_date, end_date):
    """Load daily data from web"""
    # dates = pd.date_range(start_date, end_date)
    # df = pd.DataFrame(index=dates)

    prices, dates = fetch('SPY', start_date, end_date)
    df = pd.DataFrame(prices, index=dates, columns=['SPY'])

    for ticker in tickers:
        prices, dates = fetch(ticker, start_date, end_date)
        df_temp = pd.DataFrame(prices, index=dates, columns=[ticker])
        df = df.join(df_temp)

    return df


if __name__ == '__main__':
    print fetch('GOOG', '2010-01-01', '2016-01-04')
