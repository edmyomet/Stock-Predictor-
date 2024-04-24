import numpy as np
import pandas as pd

import yfinance as yf
from pandas_datareader import data as pdr
from datetime import date
yf.pdr_override()

class SetupStock:
    def __init__(self):
        self.company_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
        #self.companies = [AAPL, GOOG, MSFT, AMZN]
        self.companies = {
            'AAPL' : None, 
            'GOOG' : None, 
            'MSFT' : None,
            'AMZN' : None
        }
        
    def __get_data(self):
        self.start = '2021-04-28'
        self.end = str(date.today())
        for index in range(len(self.company_list)):
            company = self.company_list[index]
            self.companies[company]= pdr.get_data_yahoo(company, start=self.start, end=self.end, auto_adjust=True)
            self.companies[company].to_csv(fr'datasets/{company}.csv')
        
        
    
    def data_setup(self):
        self.__get_data()
        
        
    def main(self):
        self.data_setup()

if __name__ == '__main__':
    ss = SetupStock()
    ss.main()
