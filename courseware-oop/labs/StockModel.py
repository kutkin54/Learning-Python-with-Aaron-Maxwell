class StockModel:
    def __init__(self, symbol, open_price, close_price,
                 volume, average_volume):
        self.symbol = symbol
        self.open_price = open_price
        self.close_price = close_price
        self.volume = volume
        self.average_volume = average_volume

    def is_bullish(self):
        price_ratio = self.close_price / self.open_price
        volume_ratio = self.volume / self.average_volume
        return price_ratio == volume_ratio
