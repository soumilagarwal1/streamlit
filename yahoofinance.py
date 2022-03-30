import streamlit as st
import yfinance as yf

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Apple!
""")#markdown language to be used here

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='3y')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
