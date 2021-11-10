from datetime import datetime
from typing import List
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
from schemas.currency import Currency
import helpers
import itertools

class Model:
    def __init__(self):
        """
        1. Get all datasets
        2. process all datasets
        3. build scalers for each dataset
        4. build models for each dataset
        """
        self.eth_df = pd.read_csv("~/Desktop/dmdw-project/server/data/ethereum/ETH.csv", index_col="Date")
        self.eth_df['Price'] = self.eth_df['Price'].replace(',','', regex=True)
        self.eth_df['Price'] = self.eth_df['Price'].astype(float, errors = 'raise')

        self.mon_df = pd.read_csv("~/Desktop/dmdw-project/server/data/monero/Monero.csv", index_col="Date")
        self.mon_df['Price'] = self.mon_df['Price'].replace(',','', regex=True)
        self.mon_df['Price'] = self.mon_df['Price'].astype(float, errors = 'raise')

        self.btc_df = pd.read_csv("~/Desktop/dmdw-project/server/data/bitcoin/BTC.csv", index_col="Date")
        self.btc_df['Price'] = self.btc_df['Price'].replace(',','', regex=True)
        self.btc_df['Price'] = self.btc_df['Price'].astype(float, errors = 'raise')
        
        self.eth_scaler = self.__get_eth_scaler(self.eth_df)
        self.eth_model = self.__get_eth_model()

        self.mon_scaler = self.__get_mon_scaler(self.mon_df)
        self.mon_model = self.__get_mon_model()

        self.btc_scaler = self.__get_btc_scaler(self.btc_df)
        self.btc_model = self.__get_btc_model()

    def __get_eth_scaler(self, eth_df):
        values = eth_df['Price'][::-1].values.reshape(-1,1)
        values = values.astype('float32')
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler.fit_transform(values)
        return scaler

    def __get_mon_scaler(self, mon_df):
        values = mon_df['Price'][::-1].values.reshape(-1,1)
        values = values.astype('float32')
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler.fit_transform(values)
        return scaler

    def __get_btc_scaler(self, btc_df):
        values = btc_df['Price'][::-1].values.reshape(-1,1)
        values = values.astype('float32')
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler.fit_transform(values)
        return scaler

    def __get_eth_model(self):
        return load_model("/Users/saifkazi/Desktop/dmdw-project/server/app/models/eth_model.h5")

    def __get_mon_model(self):
        return load_model("/Users/saifkazi/Desktop/dmdw-project/server/app/models/mon_model.h5")

    def __get_btc_model(self):
        return load_model("/Users/saifkazi/Desktop/dmdw-project/server/app/models/btc_model.h5")

    def get_predictions(self, currency: Currency, forecast_date: str) -> List[float]:
        if currency == Currency.eth:
            return self.__get_eth_predictions(forecast_date)
        elif currency == Currency.mon:
            return self.__get_mon_predictions(forecast_date)
        elif currency == Currency.btc:
            return self.__get_btc_predictions(forecast_date)

    def __get_eth_predictions(self, forecast_date: str):
        a = helpers.convert_str_to_date("11/10/2021")
        b = helpers.convert_str_to_date(forecast_date)
        yhat = []
        prev=0.8503466
        days = (b-a).days
        for i in range(0, days):
            x=self.eth_model.predict([[[prev]]])
            yhat.append(x[0][0])
            prev=x[0][0].item()
        yhat = np.array(yhat)
        yhat_inverse = self.eth_scaler.inverse_transform(yhat.reshape(-1, 1))
        return list(itertools.chain.from_iterable(yhat_inverse))

    def __get_mon_predictions(self, forecast_date: str):
        a = helpers.convert_str_to_date("11/10/2021")
        b = helpers.convert_str_to_date(forecast_date)
        yhat = []
        prev=0.571195185
        days = (b-a).days
        for i in range(0, days):
            x=self.mon_model.predict([[[prev]]])
            yhat.append(x[0][0])
            prev=x[0][0].item()
        yhat = np.array(yhat)
        yhat_inverse = self.mon_scaler.inverse_transform(yhat.reshape(-1, 1))
        return list(itertools.chain.from_iterable(yhat_inverse))

    def __get_btc_predictions(self, forecast_date: str):
        a = helpers.convert_str_to_date("11/10/2021")
        b = helpers.convert_str_to_date(forecast_date)
        yhat = []
        prev=0.9040159
        days = (b-a).days
        for i in range(0, days):
            x=self.btc_model.predict([[[prev]]])
            yhat.append(x[0][0])
            prev=x[0][0].item()
        yhat = np.array(yhat)
        yhat_inverse = self.btc_scaler.inverse_transform(yhat.reshape(-1, 1))
        return list(itertools.chain.from_iterable(yhat_inverse))

    def get_data(self, currency: Currency):
        if currency == Currency.eth:
            return [x for x in self.eth_df['Price'][:284][::-1]]
        elif currency == Currency.mon:
            return [x for x in self.mon_df['Price'][:284][::-1]]
        elif currency == Currency.btc:
            return [x for x in self.btc_df['Price'][:284][::-1]]