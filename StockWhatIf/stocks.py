import yfinance as yf
from tkinter import * 
from tkinter.ttk import *

def process(symbol, investment, startDate, endDate):
    stockSym = yf.Ticker(symbol)
master = Tk()

symL = Label(master, text = "Stock Symbol:")
investL = Label(master, text = "Initial Investment:")
startD = Label(master, text="Start Date (mm/dd/yy):")
endD = Label(master, text="End Date (mm/dd/yy):")
stockGrowth = Label(master, text="Stock Growth Earnings:")
divGrowth = Label(master, text="Dividend Earnings:")
totalEarnings = Label(master, text="Total Earnings:")
overallValue = Label(master, text="Overall Value:")

symL.grid(row = 0, column = 0, sticky = W, pady = 2)
investL.grid(row = 1, column = 0, sticky = W, pady = 2)
startD.grid(row = 2, column = 0, sticky = W, pady = 2)
endD.grid(row = 3, column = 0, sticky = W, pady = 2)
stockGrowth.grid(row = 4, column = 0, sticky = W, pady = 2)
divGrowth.grid(row = 5, column = 0, sticky = W, pady = 2)
totalEarnings.grid(row = 6, column = 0, sticky = W, pady = 2)
overallValue.grid(row = 7, column = 0, sticky = W, pady = 2)
 
symbol = Entry(master)
investment = Entry(master)
sDate = Entry(master)
eDate = Entry(master)
sGrowth = Entry(master, state='disabled')
dGrowth = Entry(master, state='disabled')
tEarnings = Entry(master, state='disabled')
oValue = Entry(master, state='disabled')
 
symbol.grid(row = 0, column = 1, pady = 2)
investment.grid(row = 1, column = 1, pady = 2)
sDate.grid(row = 2, column = 1, pady = 2)
eDate.grid(row = 3, column = 1, pady = 2)
sGrowth.grid(row = 4, column = 1, pady = 2)
dGrowth.grid(row = 5, column = 1, pady = 2)
tEarnings.grid(row = 6, column = 1, pady = 2)
oValue.grid(row = 7, column = 1, pady = 2)
 
enter = Button(master, text="Enter", pady = 2, command=process)
mainloop()
