import requests
from src.libs.interfaces.IConnector import IConnector
from src.configs.settings import PATH_TO_DATA


class YahooConnector(IConnector):

    __connection = {}
    __url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=nsl1opc1p2&e=.csv'

    @classmethod
    def connect(cls, args):

        if args not in cls.__connection:
            try:
                target_url = cls.__url % args
                csv = requests.get(target_url)
                cls.__connection[args] = csv.content
            except Exception as ex:
                raise Exception("Erro ao conectar", "Não foi possível realizar conexão")

        return cls.__connection[args]
