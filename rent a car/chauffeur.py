import sqlite3 as sql

class Chauffeur:
    chauffeur_number = 0
    def __init__(self, name, surname, gender, foreign_language, chauffeur_price) -> None:
        """
        constructor of chauffeur
        
        Args:
            name (str): name of chauffeur
            surname (str): surname of chauffeur
            gender (str): gender of chauffeur
            foreign_language (str): foreign language of chauffeur
            chauffeur_price (str): price of chauffeur
        """
        self.name = name
        self.surname = surname
        self.gender = gender
        self.foreign_language = foreign_language
        self.chauffeur_price = chauffeur_price
        self.change_id()
        self.create()
    
    def create(self):
        with sql.connect("database.db") as db:
            cursor = db.cursor()
            mylist = cursor.execute("""SELECT * FROM chauffeur WHERE name = '{}' AND surname = '{}' AND gender = '{}'""".format(self.name, self.surname, self.gender)).fetchall()
            if mylist:
                print("This chauffeur is already exists.")
            else:
                cursor.execute("""INSERT INTO chauffeur VALUES({},'{}','{}','{}','{}', {})""".format(Chauffeur.chauffeur_number,self.name, self.surname, self.gender, self.foreign_language, self.chauffeur_price))
                Chauffeur.chauffeur_number += 1
    @classmethod   
    def change_id(cls):
        with sql.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("""SELECT id FROM chauffeur""")
            try:
                id = cursor.fetchall()[-1][0]
                cls.chauffeur_number = id + 1
            except(IndexError):
                cls.chauffeur_number = 0
        
    def display_chauffeur_info(self):
        """
            display chauffeur info
            
        Returns:
            str: chauffeur info
        """
        return f"Chauffeur Name: {self.name}\nChauffeur Surname: {self.surname}\nChauffeur Gender: {self.gender}\nChauffeur Foreign Language: {self.foreign_language}\nChauffeur Price: {self.chauffeur_price}\nChauffeur Available: {self.case}"
    
    def change_chauffeur_case(self, l):
        """
            change chauffeur case
            
        Args:
            l (str): new chauffeur case
        """
        self.case = l
    
    def display_chauffeur_case(self):
        """
            display chauffeur case
            
        Returns:
            str: chauffeur case
        """
        return self.case
    
    def add_chauffeur_salary(self, s):
        """
            increase of chauffeur salary
            
        Args:
            s (int): new salary of chauffeur
        """
        self.chauffeur_price = s
        
    def display_chauffeur_salary(self):
        """
            display of chauffeur salary
            
        Returns:
            int: chauffeur salary
        """
        return self.chauffeur_price