import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = list()

        for quote in quotes:
            price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], price))
            prices.append(price)

        ratio = getRatio(prices[0], prices[1])
        check = float(prices[0] / prices[1])
        self.assertEqual(ratio, check)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = list()

        for quote in quotes:
            price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], price))
            prices.append(price)

        ratio = getRatio(prices[0], prices[1])
        check = float(prices[0] / prices[1])
        self.assertEqual(ratio, check)

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_calculatePriceBidSmallerThanAsk(self):

        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 115.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        prices = list()

        for quote in quotes:
            price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], price))
            prices.append(price)

        ratio = getRatio(prices[0],prices[1])
        check = float(prices[0]/prices[1])
        self.assertEqual(ratio,check)


    '''--- edge case when price_b is 0 ---'''
    def test_getDataPoint_edgeCase(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 4}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        prices = list()

        for quote in quotes:
            price = (quote['top_bid']['price'] +quote['top_ask']['price'])/2
            self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], price))
            prices.append(price)


        self.assertIsNone(getRatio(prices[0], prices[1]))




if __name__ == '__main__':
    unittest.main()
