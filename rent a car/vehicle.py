class Vehicle:
    def __init__(self, brand, price, piece):
        """
            vehicle constructor
            
        Args:
            brand (str): brand of vehicle
            price (int): price of vehicle
            piece (int): piece of vehicle
        """
        self.brand = brand
        self.price = price
        self.piece = int(piece)