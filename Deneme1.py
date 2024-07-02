import datetime

print("\n\n")      

class VehicleRent():
    def __init__(self,stock):
        #yarattığım objede ne kadar var demek stock
        self.stock = stock
        self.now = 0 
##########################################################
    def displaystock(self):
        print(self.stock, " vehicle available to rent.")
        return self.stock
 #########################################################   
    def renthourly(self,n):
        #n saatlik olarak kiralanmak istenen araç sayısı
        self.n = n
        if n<0:
            print("Number should be positive")
            return None
        elif n>self.stock:
            print("Sorry ", self.stock, " vehicle available")
            return None
        else:
            self.now = datetime.datetime.now()
            #kiraladığım zamanı anında alacağım
            print("Rented ",n," vehicle for hourly at ", self.now.hour, " hours")
            #self.now.hour şu anın saatini return ediyor
            self.stock -= n
            return self.now
############################################################
    def rentdaily(self,n):
        self.n = n
        if n<0:
            print("Number should be positive")
            return None
        elif n>self.stock:
            print("Sorry ", self.stock, " vehicle available")
            return None
        else:
            self.now = datetime.datetime.now()
            #kiraladığım zamanı anında alacağım
            print("Rented ",n," vehicle for hourly at ", self.now.hour, " hours")
            #self.now.hour şu anın saatini return ediyor
            self.stock -= n
            return self.now
###################################################################        
    def returnvehicle(self,request, brand):
        carhprice = 10
        cardprice = carhprice * 8/10 * 24
        bikehprice = 5
        bikedprice = bikehprice * 7/10 *24

        rentalTime, rentalBasis, numOfVehicle = request

        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()#self now ve now farklı şeyler burda herhangi bir local var tanımladım
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*carhprice*numOfVehicle
                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/(3600*24)*cardprice*numOfVehicle

                if (2 <= numOfVehicle):
                    print("You have %20 discount")
                    bill = bill*0.8
                print("Thank you for returning car")
                print("Price: $ ",bill)
                return bill
            
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()#self now ve now farklı şeyler burda herhangi bir local var tanımladım
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*bikehprice*numOfVehicle
                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/(3600*24)*bikedprice*numOfVehicle

                if (4 <= numOfVehicle):
                    print("You have %20 discount")
                    bill = bill*0.8
                print("Thank you for returning bike")
                print("Price: $ ",bill)
                return bill
        else:
            print("You do not rent a vehicle")

class Car(VehicleRent):
    global discount_rate
    discount_rate = 15
    def __init__(self,stock):
        super().__init__(stock)
    def discount(self, b):
        bill = b - (b*discount_rate)/100
        return bill


class Bike(VehicleRent):
    def __init__(self,stock):
        super().__init__(stock)

#customer
class Customer():
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0

        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0
        self.bill = 0

    def requestVehicle(self,brand):
        if brand == "car":
            cars = input("How many cars would you like to rent")
            try:
                cars = int(cars)
            except ValueError:
                print("It should be number")
                return -1
            if cars < 0:
                print("Number of cars should be positive")
                return -1
            else:
                self.cars = cars
                return self.cars
        elif brand == "bike":
            bikes = input("How many cars would you like to rent")
            try:
                bikes = int(bikes)
            except ValueError:
                print("It should be number")
                return -1
            if bikes < 0:
                print("Number of bikes should be positive")
                return -1
            else:
                self.bikes = bikes
                return self.bikes
        else:
            print("Request vehicle error")

        
    def returnVehicle(self, brand):
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b , self.rentalBasis_b , self.bikes
            else:
                return 0,0,0
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c , self.rentalBasis_c , self.cars
            else:
                return 0,0,0
        else:
            print("Return vehicle error")


bike = Bike(100)
car = Car(10)
customer = Customer()

main_menu = True

while True:
    
    if main_menu:
        print("****Vehicle Rental Shop****")
        print("A. Bike Menu\nB.Car Menu\nQ.Exit")
        main_menu = False

        choice = input("Enter a choice")

    if choice == "A" or choice == "a":
        print("*****Bike Menu****")
        print("1.Display available bikes\n2.Request a bike on hourly basis $ 5")
        print("3.Request a bike on daily basis $ 84")
        print("4.Main menu")
        print("6.Exit")
        print("*************")
        choice = input("Enter a choice")
        try:
            choice = int(choice)
        except ValueError:
            print("It is not an integer")
            continue
        if choice == 1:
            bike.displaystock()
            choice = "A"
        elif choice == 2:
            customer.rentalTime_b =bike.renthourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_b =bike.rentdaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill = bike.returnvehicle(customer.returnVehicle("bike"))
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter a number between 1-6")
            main_menu = True

    elif choice == "B" or choice == "b":
        print("*****Car Menu****")
        print("1.Display available cars\n2.Request a cars on hourly basis $ 10")
        print("3.Request a cars on daily basis $ 192")
        print("4.Main menu")
        print("6.Exit")
        print("*************")
        choice = input("Enter a choice")
        try:
            choice = int(choice)
        except ValueError:
            print("It is not an integer")
            continue
        if choice == 1:
            car.displaystock()
            choice = "B"
        elif choice == 2:
            customer.rentalTime_c =car.renthourly(customer.requestVehicle("Car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_c =car.rentdaily(customer.requestVehicle("Car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill =car.returnvehicle(customer.returnVehicle("bike"))
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter a number between 1-6")
            main_menu = True
    elif choice == "Q" or choice == "q":
        break
    else:
        print("Invalid input. Please enter A-B-Q ")
        main_menu = True
    print("Thanks")


print("\n\n")
    




