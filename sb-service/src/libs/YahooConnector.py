import requests
from interfaces import IConnector
from settings.settings import PATH_TO_DATA


class YahooConnector(IConnector):

    __connection = {}
    __url = 'http://ichart.finance.yahoo.com/table.csv?s=%s&g=abo'

    @classmethod
    def connect(self, args):
        if args not in self.__connection:
            target_url = self.__url % args
            csv = requests.get(target_url)
            self.__connection[args] = csv.content

        return self.__connection[args]
