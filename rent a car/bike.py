from vehicle import Vehicle
import sqlite3 as sql
class Bike(Vehicle):
    """bike class inherited from vehicle"""
    bike_number = 0 # number of bike
    def __init__(self, brand, price, piece, bike_type, frame_size, frame_type, rim_size, gear_number, brake_type) -> None:
        """
            bike constructor
        
        Args: 
            staff_size (str): frame size of bike
            staff_type (str): frame type of bike
            rim_size (str): rim size of bike
            gear_number (str): gear number of bike
            brake_type (str): brake type of bike  
        """
        super().__init__(brand, price, piece)
        self.bike_type = bike_type
        self.frame_size = frame_size
        self.frame_type = frame_type
        self.rim_size = rim_size
        self.gear_number = gear_number
        self.brake_type = brake_type
        self.change_id()
        self.create()
    
      
    def create(self):
        with sql.connect("database.db") as db:
            cursor = db.cursor()
            piece = cursor.execute("""SELECT piece FROM bike WHERE brand = '{}' AND price = {} AND bike_type = '{}' AND  rim_size = {} AND gear_number = {} AND brake_type = '{}'  """.format(self.brand, self.price, self.bike_type, self.rim_size, self.gear_number, self.brake_type)).fetchone()[0]
            piece = int(piece)
            if piece:
                self.piece += piece
                cursor.execute("""UPDATE bike SET piece = {} WHERE brand = '{}' AND price = {} AND bike_type = '{}' AND  rim_size = {} AND gear_number = {} AND brake_type = '{}'  """.format(self.piece, self.brand, self.price, self.bike_type, self.rim_size, self.gear_number, self.brake_type))
            else:
                cursor.execute("""INSERT INTO bike VALUES({},'{}',{},{},'{}',{},'{}',{},{},'{}')""".format(Bike.bike_number,self.brand, self.price, self.piece, self.bike_type, self.frame_size, self.frame_type, self.rim_size, self.gear_number, self.brake_type))
                Bike.bike_number += 1
                
    @classmethod
    def change_id(cls):
        with sql.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("""SELECT id FROM car""")
            try:
                id = cursor.fetchall()[-1][0]
                cls.bike_number = id + 1
            except(IndexError):
                cls.bike_number = 0

    def display_bike_info(self):
        """
            display of bike info
            
        Returns:
            str: info of bike
        """
        return f"Bike Brand: {self.brand}\nBike Price: {self.price}\nBike Piece: {self.piece}\nBike Type: {self.bike_type}\nBike Staff Size: {self.staff_size}\nBike Staff Type: {self.staff_type}\nBike Rim Size: {self.rim_size}\nBike Gear Number: {self.gear_number}\nBike Brake Type: {self.brake_type}"
    
    def add_bike_piece(self, n):
        """
            increase piece of bike
        
        Args:
            n (int): pieces to add  
        """
        self.piece += n
    
    def display_bike_piece(self):
        """
            display bike piece
            
        Returns:
            int: bike piece
        """
        return self.piece
    
    def change_bike_price(self, p):
        """
            change of bike price
            
        Args:
            p (int): new price of bike
        """
        self.price = p
        
    
    def display_bike_price(self):
        """
            display bike price
            
        Returns:
            int: bike price
        """
        return self.price
    
    def discount_bike_price(self, r):
        """
            discount of bike price
            
        Args:
            r (int): rate of discount
        """
        self.price -= self.price*r