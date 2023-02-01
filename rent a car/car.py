from vehicle import Vehicle
import sqlite3 as sql

class Car(Vehicle):
    car_number = 0 # number of car
    """car class inherited from vehicle"""
    
    def __init__(self, brand, price, piece, car_type, plate, model, color, segment):
        """
            car constructor

        Args:
            car_type (str): type of car
            plate (str): plate of car
            model (str): model of car
            color (str): color of car
            segment (str): segment of car
        """
        super().__init__(brand, price, piece)
        self.car_type = car_type
        self.plate = plate
        self.model = model
        self.color = color
        self.segment = segment
        self.change_id()
        self.create()
        
    def create(self):
        with sql.connect("database.db") as db:
            cursor = db.cursor()
            mylist = cursor.execute("""SELECT * FROM car WHERE plate = '{}' """.format(self.plate)).fetchall()
            if mylist:
                print("This car is already exists.")
            else:
                cursor.execute("""INSERT INTO car VALUES({},'{}',{},{},'{}','{}','{}','{}','{}')""".format(Car.car_number,self.brand, self.price, self.piece, self.car_type, self.plate, self.model, self.color, self.segment))
                Car.car_number += 1

    @classmethod
    def change_id(cls):
        with sql.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("""SELECT id FROM car""")
            try:
                id = cursor.fetchall()[-1][0]
                cls.car_number = id + 1
            except(IndexError):
                cls.car_number = 0
    
    def display_car_info(self):
        """
            display car info
            
        Returns:
            str: car info
        """
        return f"Car Brand: {self.brand}\nCar Price: {self.price}\nCar Piece: {self.piece}\nCar Type: {self.car_type}\nCar Model: {self.model}\nCar Color: {self.color}\nCar Segment: {self.segment}"
        
    def add_car_piece(self, p):
        """
            increase of car piece
            
        Args:
            int (p): new piece of car
        """
        self.piece += p
        
    def display_car_piece(self):
        """
            display of car piece
            
        Returns:
            int: car piece
        """
        return self.piece
    
    def increase_car_price(self, i):
        """
            increase of car price
            
        Args:
            int (i): new price of car
        """
        self.price += i
    
    def display_car_price(self):
        """
            display of car price
            
        Returns:
            int: car price
        """
        return self.price
        
    def discount_car_price(self, d):
        """
            discount of car price
            
        Args:
            int (d): discount rate of price
        """
        self.price -= self.price*d
        
    @classmethod
    def display_car_number(cls):
        """
            display of car number
            
            it is a class method
            
        Returns:
            int: number of car
        """
        return cls.car_number