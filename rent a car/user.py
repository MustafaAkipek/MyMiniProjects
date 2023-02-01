import sqlite3 as sql

class User:
    user_number = 0 #number of user
    def __init__(self, nick_name, name, surname, gender, tel, driving_licence, remnant, e_posta, password):
        """
            users constructor
        
        Args:
            nick_name (str): nick name of user
            name (str): name of user
            surname (str): surname of user
            gender (str): gender of user
            tel (str): tel number of user
            __driving_licence (str): driving licence of user
            remnant (int): remnant of user
            e_posta (str): e posta of user
            password (str): password of user 
        """
        self.nick_name = nick_name
        self.name = name
        self.surname = surname
        self.gender = gender
        self.tel = tel
        self.__driving_licence = driving_licence
        self.remnant = remnant
        self.e_posta = e_posta
        self.password = password
        User.user_number += 1
        self.create()
        
    def create(self):
        with sql.connect("database.db") as db:
            cursor = db.cursor()
            mylist = cursor.execute("""SELECT * FROM USER WHERE nick_name = '{}' """.format(self.nick_name)).fetchall()
            if mylist:
                print("This user already exists. Please login")
            else:
                cursor.execute("""INSERT INTO user VALUES('{}','{}','{}','{}','{}','{}',{},'{}','{}')""".format(self.nick_name, self.name, self.surname, self.gender, self.tel, self.__driving_licence, self.remnant, self.e_posta, self.password))


    def display_user_info(self):
        """ 
            display user info
    
        Returns:
            str: user info 
        """  
        return f"User Nickname: {self.nick_name}\nUser Name: {self.name}\nUser Surname: {self.surname}\nUser Gender: {self.gender}\nUser Tel: {self.tel}\nUser Driving License: {self.__driving_license}\nUser Remnant: {self.remnant}\nUser e_posta: {self.e_posta}\nUser Password: {self.password}"
    
    def change_nick_name(self, n):
        """
            change nick name
        
        Args:
            n (str): new nick name
        """
        self.nick_name = n
    
    def display_nick_name(self):
        """
            display nick name
            
        Returns:
            str: nick name
        """
        return self.nick_name
    
    def change_tel_no(self, t):
        """
            change tel no
        
        Args:
            t (int): new tel
        """
        self.tel = t
    
    def display_tel_no(self):
        """
            display tel no
            
        Returns:
            str: tel no
        """
        return self.tel
        
    def add_remnant(self, r):
        """
            increase remnant
        
        Args:
            r (int): increase amount of remnant
        """
        self.remnant += r
    
    def display_remnant(self):
        """
            display remnant
            
        Returns:
            int: display remnant
        """
        return self.remnant
    
    def change_eposta(self, e):
        """
            change e posta
        
        Args:
            e (str): new e posta
        """
        self.e_posta = e
    
    def display_eposta(self):
        """
            display e posta
            
        Returns:
            str: e posta
        """
        return self.e_posta
    
    def change_password(self, p):
        """
            change password
        
        Args:
            p (str): new password
        """
        self.password = p
    
    def display_password(self):
        """
            display password
            
        Returns:
            str: password
        """
        return self.password
    
    @property
    def driving_licence(self):
        """
            display driving license
        
        Returns:
            str: driving license
        """
        return self.__driving_licence
    
    
    @driving_licence.setter
    def driving_licence(self, d):
        """
            update driving license
        
        Args:
            d (str): new license
        """
        self.__driving_licence = d
        
    @classmethod
    def display_user_number(cls):
        """
            display of user number
            
            it is a class method
            
        Returns:
            int: number of user
        """
        return cls.user_number