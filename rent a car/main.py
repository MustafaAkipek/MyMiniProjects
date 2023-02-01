from user import User
from car import Car
from bike import Bike
from chauffeur import Chauffeur
import colorama
from colorama import Fore, Style
import time
import sqlite3 as sql
import sys
colorama.init()

with sql.connect("database.db") as db:
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user(
        nick_name text,
        name text,
        surname text,
        gender text,
        tel text,
        driving_license text,
        remnant int,
        e_posta text,
        password text
)""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS car(
        id int,
        brand text,
        price real,
        piece int,
        car_type text,
        plate text,
        model text,
        color text,
        segment text
)""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS bike(
        id int,
        brand text,
        price real,
        piece int,
        bike_type text,
        frame_size int,
        frame_type text,
        rim_size real,
        gear_number int,
        brake_type text
)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS chauffeur(
        id int,
        name text,
        surname text,
        gender text,
        foreign_language text,
        chauffeur_price int
)""")
    
    
def register_user():
    nick_name = input("""Please enter your nickname: """)
    name = input("""Please enter your name: """)
    surname = input("""Please enter your surname: """)
    gender = input("""Please enter your gender: """)
    tel = input("""Please enter your tel: """)
    driving_license = input("""Please enter your driving license: """)
    remnant = input("""Please enter your remnant: """)
    e_posta = input("""Please enter your e posta: """)
    password = input("""Please enter your password: """)
    User(nick_name, name, surname, gender, tel, driving_license, remnant, e_posta, password)
    print_menu()
 
 
 
def register_car():
    brand = input("""Please enter car's brand: """)
    price = input("""Please enter car's rental fee: """)
    car_type = input("""Please enter car's type: """)
    plate = input("""Please enter car's plate: """)
    model = input("""Please enter car's model: """)
    color = input("""Please enter car's color: """)
    segment = input("""Please enter car's segment: """)
    Car(brand, price, 1, car_type, plate, model, color, segment)
    admin_index()
    

def register_bike():
    brand = input("""Please enter bike's brand: """)
    price = input("""Please enter bike's rental fee: """)
    piece = input("""Please enter bike's piece: """)
    bike_type = input("""Please enter bike's type: """)
    frame_size = input("""Please enter bike's frame size: """)
    frame_type = input("""Please enter bike's frame type: """)
    rim_size = input("""Please enter bike's rim size: """)
    gear_number = input("""Please enter bike's gear number: """)
    brake_type = input("""Please enter bike's brake type: """)
    Bike(brand, price, piece, bike_type, frame_size, frame_type, rim_size, gear_number, brake_type)
    admin_index()
    
    
       
def print_menu():
    choice = input("""
    1- Login
    2- Register
    3- Close 
""")
    match choice:
        case "1":
            login_menu()
        case "2":
            register_user()
        case "3":
            sys.exit(0)
        case _:
            print("This case is not available")
            print_menu()
            
def login_menu():
    nick_name = input("""Please enter your nickname: """)
    password = input("""Please enter your password: """)
    with sql.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM user WHERE nick_name = '{}' AND password = '{}' """.format(nick_name, password)) 
        mylist = cursor.fetchall()
        if mylist and nick_name == "Admin":
            print("You have signed in as Admin")
            admin_index()
        elif mylist:
            print("You have signed in")
            index(nick_name)  
        else:
            print("Your username or password is incorrect")
            print_menu()
        
def index(nick_name):
    choice = input("""
    1- Rent a car
    2- Rent a bike
    3- Delete your account
    4- Deposit Money
    5- Logout
""")
    match choice:
        case "1":
            rent_car(nick_name)
        case "2":
            rent_bike(nick_name)
        case "3":
            c = input("Are you sure about deleting your account.(Y/N)")
            match c:
                case "Y":
                    with sql.connect("database.db") as db:
                        cursor = db.cursor()
                        cursor.execute("""DELETE FROM user WHERE nick_name = '{}'""".format(nick_name))
                        print_menu()
                case "N":
                    index(nick_name)
                case _:
                    print("Please enter (Y/N)")
                    index(nick_name)
        case "4":
            deposit(nick_name)
        case "5":
            print_menu()
        case _:
            print("This case is not available")
            print_menu()

def deposit(nick_name):
    value = int(input("Please enter the value of the money you want to deposit: "))
    with sql.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE user SET remnant = remnant + {} WHERE nick_name = '{}'".format(value , nick_name))
        cursor.execute("SELECT remnant FROM user WHERE nick_name = '{}'".format(nick_name))
        remnant = int(cursor.fetchone()[0])
        print("Your new balance is now {}TL".format(remnant))
        time.sleep(2)
    index(nick_name)
    
def admin_index():
    choice = input("""
    1- Add a car
    2- Add a bike
    3- Add Chauffeur
    4- Logout
""")
    match choice:
        case "1":
            register_car()
        case "2":
            register_bike()
        case "3":
            register_chauffeur()
        case "4":
            print_menu()
        case _:
            print("This case is not available")
            print_menu()

def register_chauffeur():
    name = input("""Please enter chauffeur's name: """)
    surname = input("""Please enter chauffeur's surname: """)
    gender = input("""Please enter chauffeurs's gender: """)
    foreign_language = input("""Please enter yes if the chauffeur knows english: """)
    price = input("""Please enter chauffeurs's rent fee: """)
    Chauffeur(name, surname, gender, foreign_language, price)
    admin_index()

def rent_car(nick_name):
    with sql.connect("database.db") as db:
        cars = []
        cursor = db.cursor()
        cursor.execute("""SELECT id FROM car""")
        car_number = cursor.fetchall()[-1][0]
        cursor.execute("SELECT driving_license FROM user WHERE nick_name = '{}'".format(nick_name))
        license = cursor.fetchone()[0]
        chauffeur_hour = None
        if license == "No":
            chauffeurs = []
            cursor.execute("SELECT id FROM chauffeur")
            chauffeur_number = cursor.fetchall()[-1][0]
            for i in range(chauffeur_number + 1):
                cursor.execute("SELECT * FROM chauffeur WHERE id = {}".format(i))
                chlist = cursor.fetchall()[0]
                chauffeurs.append(chlist)
                string = Fore.GREEN + "Chauffeur id: {}, " + Fore.BLUE + "Chauffeur name: {}, " + Fore.LIGHTYELLOW_EX +  "Chauffeur surname: {}, " + Fore.RED+ "Chauffeur gender: {}, " + Fore.MAGENTA + "Foreign Language: {}, " + Fore.YELLOW + "Rental fee: {}TL"
                string = string.format(chlist[0], chlist[1], chlist[2], chlist[3], chlist[4], chlist[5])
                print("\n" + string)
            print(Style.RESET_ALL)
            selected_id = int(input("\nWrite the id of the chauffeur that you want to rent: "))
            if selected_id > car_number or selected_id < 0:
                print("The id you selected is not available.")
            else:
                with sql.connect("database.db") as db:
                    cursor = db.cursor()  
                    cursor.execute("""SELECT remnant FROM user WHERE nick_name = '{}'""".format(nick_name))
                    users_remnant = cursor.fetchone()[0]
                rent_fee = chauffeurs[selected_id][5]
                max_hour = users_remnant / rent_fee
                hour = float(input("How many hours dou you want to rent? (You can rent this chauffeur for {} hours.): ".format(max_hour)))
                if hour > max_hour:
                    print(Fore.RED + "Did you really think you can rent this chauffeur with that much money on you!!" + Style.RESET_ALL)
                    index(nick_name)
                elif hour < 0:
                    print("If you want to be a chauffeur, contact to admin.")
                    index(nick_name)
                else:
                    total_fee = rent_fee * hour
                    remaining_remnant = users_remnant - total_fee
                    with sql.connect("database.db") as db:
                        cursor = db.cursor()
                        cursor.execute("""UPDATE user SET remnant = {} WHERE nick_name = '{}'""".format(remaining_remnant, nick_name))    
                    print("You rented {} {} for {} hours.\n".format(chauffeurs[selected_id][1], chauffeurs[selected_id][2], hour))
                    chauffeur_hour = hour
                    time.sleep(3)  
        if car_number:
            for i in range(car_number + 1):
                cursor.execute("""SELECT * FROM car WHERE id = {}""".format(i))
                clist = cursor.fetchall()[0]
                cars.append(clist)
                string = Fore.GREEN + "Car id: {}, " + Fore.BLUE + "Car's brand: {}, " + Fore.LIGHTYELLOW_EX +  "Car's Model: {}, " + Fore.RED+ "Car's type: {}, " + Fore.MAGENTA + "Car's plate: {}, " + Fore.CYAN + "Car's color: {}, " + Fore.LIGHTGREEN_EX + "Car's segment: {} " + Fore.YELLOW + "Rental fee: {}TL"
                string = string.format(clist[0], clist[1], clist[6], clist[4], clist[5], clist[7], clist[8], clist[2])
                print("\n" + string)
            print(Style.RESET_ALL)
            selected_id = int(input("\nWrite the id of the car that you want to rent: "))
            if selected_id > car_number or selected_id < 0:
                print("The id you selected is not available.")
            else:
                with sql.connect("database.db") as db:
                    cursor = db.cursor()  
                    cursor.execute("""SELECT remnant FROM user WHERE nick_name = '{}'""".format(nick_name))
                    users_remnant = cursor.fetchone()[0]
                rent_fee = cars[selected_id][2]
                if chauffeur_hour:
                    max_hour = chauffeur_hour
                else:
                    max_hour = users_remnant / rent_fee
                hour = float(input("How many hours dou you want to rent? (You can rent the car for {} hours.): ".format(max_hour)))
                if hour > max_hour:
                    print(Fore.RED + "Did you really think you can rent this car with that much money on you!!" + Style.RESET_ALL)
                    index(nick_name)
                elif hour < 0:
                    print("Then you want to rent YOUR car to us huh? Well we don't do that")
                    index(nick_name)
                else:
                    total_fee = rent_fee * hour
                    remaining_remnant = users_remnant - total_fee
                    with sql.connect("database.db") as db:
                        cursor = db.cursor()
                        cursor.execute("""UPDATE user SET remnant = {} WHERE nick_name = '{}'""".format(remaining_remnant, nick_name))    
                    print("You rented {} {} for {} hours.".format(cars[selected_id][1], cars[selected_id][6], hour))
                    time.sleep(3)
                    index(nick_name)        
        else:
            print("There are not any car's available right now.")
            time.sleep(2)
            index(nick_name)

def rent_bike(nick_name):
    with sql.connect("database.db") as db:
        bikes = []
        cursor = db.cursor()
        cursor.execute("""SELECT id FROM bike""")
        try:
            bike_number = cursor.fetchall()[-1][0]
            for i in range(bike_number + 1):
                cursor.execute("""SELECT * FROM bike WHERE id = {}""".format(i))
                blist = cursor.fetchall()[0]
                bikes.append(blist)
                string = Fore.GREEN + "\nBike id: {}, " + Fore.BLUE + "Bike's brand: {}, " + Fore.LIGHTYELLOW_EX +  "Bike's type: {}, " + Fore.RED+ "Bike's Frame type: {}, " + Fore.BLUE + "Bike's Frame size: {}, " + Fore.MAGENTA + "Bike's piece: {}, " + Fore.CYAN + "Bike's rim size: {}, " + Fore.LIGHTGREEN_EX + "\nBike's Brake Type: {} "+ Fore.MAGENTA+ "Bike's Gear Number: {}, " + Fore.YELLOW + "Rental fee: {}TL"
                string = string.format(blist[0], blist[1], blist[4], blist[6], blist[5], blist[3], blist[7], blist[9], blist[8], blist[2])
                print("\n" + string)
            print(Style.RESET_ALL)
            selected_id = int(input("\nWrite the id of the bike that you want to rent: "))
            if selected_id > bike_number or selected_id < 0:
                print("The id you selected is not available.")
            else:
                with sql.connect("database.db") as db:
                    cursor = db.cursor()  
                    cursor.execute("""SELECT remnant FROM user WHERE nick_name = '{}'""".format(nick_name))
                    users_remnant = cursor.fetchone()[0]
                rent_fee = bikes[selected_id][2]
                max_hour = users_remnant / rent_fee
                hour = float(input("How many hours dou you want to rent? (You can rent the bike for {} hours.): ".format(max_hour)))
                if hour > max_hour:
                    print(Fore.RED + "Don't you even have the money to rent a bike!?" + Style.RESET_ALL)
                    time.sleep(3)
                    index(nick_name)
                elif hour < 0:
                    print("Then you want to rent YOUR bike to us huh? Well we don't do that")
                    index(nick_name)
                else:
                    total_fee = rent_fee * hour
                    remaining_remnant = users_remnant - total_fee
                    with sql.connect("database.db") as db:
                        cursor = db.cursor()
                        cursor.execute("""UPDATE user SET remnant = {} WHERE nick_name = '{}'""".format(remaining_remnant, nick_name))    
                    print("You rented {} branded bike for {} hours.".format(bikes[selected_id][1], hour))
                    time.sleep(3)
                    index(nick_name)  
        except(IndexError):
            print("There are not any bike's available right now.")
            time.sleep(2)
            index(nick_name)

print_menu()