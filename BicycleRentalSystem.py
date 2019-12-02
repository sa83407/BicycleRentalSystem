import datetime


class BikeAndBoatRental:
    def __init__(self, large_swan_boat=0, small_swan_boat=0, surrey=0, double_surrey=0, deuce_coupe=0, chopper=0,
                 quad_sport=0, cruiser_bike=0, tandem_bike=0, kids_bike=0, tag_a_long=0, kids_trailer=0, kayak=0, double_kayak=0):
        self.large_swan_boat = large_swan_boat
        self.small_swan_boat = small_swan_boat
        self.surrey = surrey
        self.double_surrey = double_surrey
        self.deuce_coupe = deuce_coupe
        self.chopper = chopper
        self.quad_sport = quad_sport
        self.cruiser_bike = cruiser_bike
        self.tandem_bike = tandem_bike
        self.kids_bike = kids_bike
        self.tag_a_long = tag_a_long
        self.kids_trailer = kids_trailer
        self.kayak = kayak
        self.double_kayak = double_kayak

    def display_stock(self):
        print("Current stock available:\n")
        print("A.NEW-Large Swan Boat: {} \n\t@ Adult-Hourly Rate:$11 or Child (17yrs and Under) - Hourly: $6 ".format(self.large_swan_boat))
        print("B.NEW-Small Swan Boat: {} \n\t@ Adult - Hourly Rate: $11 or Child (17yrs and Under) - Hourly: $6 ".format(self.small_swan_boat))
        print("C.Surrey: {}\n\t@ Hourly Rate: $27".format(self.surrey))
        print("D.Double Surrey: {}\n\t@ Hourly Rate: $37 ".format(self.double_surrey))
        print("E.Deuce Coupe: {}\n\t@ Hourly Rate: $27".format(self.deuce_coupe))
        print("F.Chopper: {}\n\t@ Hourly Rate: $13".format(self.chopper))
        print("G.Quad Sport: {}\n\t@ Hourly Rate: $13".format(self.quad_sport))
        print("H.Cruiser Bike: {}\n\t@ Hourly Rate: $12 or Half Day: $26 or Full Day: $32".format(self.cruiser_bike))
        print("I.Tandem Bike: {}\n\t@ Hourly Rate: $20 or Half Day: $35 or Full Day: $47".format(self.tandem_bike))
        print("J.Kids Bike: {}\n\t@ Hourly Rate: $8 or Half Day: $18 or Full Day: $25".format(self.kids_bike))
        print("K.Tag-A-Long: {}\n\t@ Hourly Rate: $8 or Half Day: $18 or Full Day: $25".format(self.tag_a_long))
        print("L.Kids Trailer: {}\n\t@ Hourly Rate: $10 or Half Day: $24 or Full Day: $32".format(self.kids_trailer))
        print("M.Kayak: {}\n\t@ Hourly Rate: $16".format(self.kayak))
        print("N.Double Kayak: {}\n\t@ Hourly Rate: $21".format(self.double_kayak))

    def rental_on_hourly_basis(self, n, t):
        """
        Hourly eligible items: C. Surrey Hourly Rate: $27", D.Double Surrey: Hourly Rate: $37,
        E.Deuce Coupe: Hourly Rate: $27
        F.Chopper: Hourly Rate: $13, G.Quad Sport: Hourly Rate: $13, H.Cruiser Bike: Hourly Rate: $12 ,
        I.Tandem Bike: Hourly Rate: $20 J.Kids Bike: Hourly Rate: $8 , K.Tag-A-Long: Hourly Rate: $8,
         L.Kids Trailer: Hourly Rate: $10, M.Kayak: Hourly Rate: $16,
        N.Double Kayak: Hourly Rate: $21

        """
        if t == 'C' or t == 'c':
            if n < self.surrey:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.surrey:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Surrey rental(s). ".format(now.hour,now.minute,now.month,
                                                                                                                 now.day,now.year,n))
                self.surrey -= n
                return now
                self.surrey_hourly_rate()
        elif t == 'D' or t == 'd':
            if n < self.double_surrey:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.double_surrey:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Double Surrey rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.double_surrey -= n
                return now
                self.double_surrey_hourly_rate()
        elif t == 'E' or t == 'e':
            if n < self.deuce_coupe:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.deuce_coupe:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Deuce Coupe rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.deuce_coupe -= n
                return now
                self.surrey_hourly_rate()

        elif t == 'F' or t == 'f':
            if n < self.chopper:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.chopper:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Chopper rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.chopper -= n
                return now
                self.chopper_hourly_rate()
        elif t == 'G' or t == 'g':
            if n < self.quad_sport:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.quad_sport:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Quad Sport rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.quad_sport -= n
                return now
                self.chopper_hourly_rate()
        elif t == 'H' or t == 'h':
            if n < self.cruiser_bike:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.cruiser_bike:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Cruiser Bike rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.cruiser_bike -= n
                return now
                self.cruiser_bike_hourly_rate()
        elif t == 'I' or t == 'i':
            if n < self.tandem_bike:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.tandem_bike:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Tandem Bike rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.tandem_bike -= n
                return now
                self.tandem_bike_hourly_rate()

        elif t == 'J' or t == 'j':
            if n < self.kids_bike:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.kids_bike:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Kids Bike rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.kids_bike -= n
                return now
                self.kids_bike_hourly_rate()
        elif t == 'K' or t == 'k':
            if n < self.tag_a_long:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.tag_a_long:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Tag-A-Long rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.tag_a_long -= n
                return now
                self.kids_bike_hourly_rate()
        elif t == 'L' or t == 'l':
            if n < self.kids_trailer:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.kids_trailer:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Kids Trailer rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.kids_trailer -= n
                return now
                self.kids_trailer_hourly_rate()
        elif t == 'M' or t == 'm':
            if n < self.kayak:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.kayak:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Kayak rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.kayak -= n
                return now
                self.kayak_hourly_rate()
        elif t == 'N' or t == 'n':
            if n < self.double_kayak:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_hourly_basis()
            elif n > self.double_kayak:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Double Kayak rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.double_kayak -= n
                return now
                self.double_kayak_hourly_rate()

    def rental_on_adult_hourly_basis(self, n, t):

        """
        Adult hourly eligible items: A. NEW-Large Swan Boat, B. NEW-Small Swan Boat
        """

        if t == 'A' or t == 'a':
            if n < self.large_swan_boat:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_adult_hourly_basis()
            elif n > self.large_swan_boat:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_adult_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Large Swan Boat rental(s). ".format(now.hour,now.minute,now.month,
                                                                                                                 now.day,now.year,n))
                self.large_swan_boat -= n
                return now
                self.adult_hourly_rate()
        elif t == 'B' or t == 'b':
            if n < self.small_swan_boat:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_adult_hourly_basis()
            elif n > self.small_swan_boat:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_adult_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Small Swan Boat rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.small_swan_boat -= n
                return now
                self.adult_hourly_rate()

    def rental_on_child_hourly_basis(self, n, t):

        """
        Child hourly eligible items: A. NEW-Large Swan Boat, B. NEW-Small Swan Boat
        """

        if t == 'A' or t == 'a':
            if n < self.large_swan_boat:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_adult_hourly_basis()
            elif n > self.large_swan_boat:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_child_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Small Swan Boat rental(s). ".format(now.hour,
                                                                                                               now.minute,
                                                                                                               now.month,
                                                                                                               now.day,
                                                                                                               now.year,
                                                                                                               n))
                self.large_swan_boat -= n
                return now
                self.child_hourly_rate()
        elif t == 'B' or t == 'b':
            if n < self.small_swan_boat:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_adult_hourly_basis()
            elif n > self.small_swan_boat:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_adult_hourly_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Small Swan Boat rental(s). ".format(now.hour,
                                                                                                               now.minute,
                                                                                                               now.month,
                                                                                                               now.day,
                                                                                                               now.year,
                                                                                                               n))
                self.small_swan_boat -=n
                return now
                self.child_hourly_rate()

    def adult_hourly_rate(self):
        print("At an adult hourly rate of $11.")

    def child_hourly_rate(self):
        print("At a child hourly rate of $6.")

    def surrey_hourly_rate(self):
        print("At an hourly rate of $27.")

    def double_surrey_hourly_rate(self):
        print("At an hourly rate of $37.")

    def chopper_hourly_rate(self):
        print("At an hourly rate of $13.")

    def cruiser_bike_hourly_rate(self):
        print("At an hourly rate of $12.")

    def tandem_bike_hourly_rate(self):
        print("At an hourly rate of $20.")

    def kids_bike_hourly_rate(self):
        print("At an hourly rate of $8.")

    def kids_trailer_hourly_rate(self):
        print("At an hourly rate of $10")

    def kayak_hourly_rate(self):
        print("At an hourly rate of $16.")

    def double_kayak_hourly_rate(self):
        print("At an hourly rate of $21.")

    def rental_on_half_day_basis(self, n, t):
        """
        Half-Day rate items:  H.Cruiser Bike: Hourly Rate: $12 or Half Day: $26 or Full Day: $32"
        I.Tandem Bike: Hourly Rate: $20 or Half Day: $35 or Full Day: $47
        J.Kids Bike: Hourly Rate: $8 or Half Day: $18 or Full Day: $25
        K.Tag-A-Long: Hourly Rate: $8 or Half Day: $18 or Full Day: $25
        L.Kids Trailer: Hourly Rate: $10 or Half Day: $24 or Full Day: $32
        :param n:
        :param t:
        :return:
        """
        if t == 'H' or t == 'h':
            if n < self.cruiser_bike:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_half_day_basis()
            elif n > self.cruiser_bike:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_half_day_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Cruiser Bike rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.cruiser_bike -= n
                return now
        elif t == 'I' or t == 'i':
            if n < self.tandem_bike:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_half_day_basis()
            elif n > self.tandem_bike:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_half_day_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Tandem Bike rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.tandem_bike -= n
                return now

        elif t == 'J' or t == 'j':
            if n < self.kids_bike:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_half_day_basis()
            elif n > self.kids_bike:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_half_day_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Kids Bike rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.kids_bike -= n
                return now

        elif t == 'K' or t == 'k':
            if n < self.tag_a_long:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_half_day_basis()
            elif n > self.tag_a_long:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rental_on_half_day_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Tag-A-Long rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.tag_a_long -= n
                return now

        elif t == 'L' or t == 'l':
            if n < self.kids_trailer:
                print("\nQuantity is invalid! Please enter a positive number.")
                self.rental_on_half_day_basis()
            elif n > self.kids_trailer:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                self.rrental_on_half_day_basis()
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Kids Trailer rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.kids_trailer -= n
                return now

    def rental_on_full_day_basis(self ,n, t):
        """
        Full-Day Rental items: print("H.Cruiser Bike: {}\n\t@ Hourly Rate: $12 or Half Day: $26 or Full Day: $32".format(self.cruiser_bike))
        print("I.Tandem Bike: {}\n\t@ Hourly Rate: $20 or Half Day: $35 or Full Day: $47".format(self.tandem_bike))
        print("J.Kids Bike: {}\n\t@ Hourly Rate: $8 or Half Day: $18 or Full Day: $25".format(self.kids_bike))
        print("K.Tag-A-Long: {}\n\t@ Hourly Rate: $8 or Half Day: $18 or Full Day: $25".format(self.tag_a_long))
        print("L.Kids Trailer: {}\n\t@ Hourly Rate: $10 or Half Day: $24 or Full Day: $32".format(self.kids_trailer))

        :param self:
        :param n:
        :param t:
        :return:
        """
        if t == 'H' or t == 'h':
            if n < self.cruiser_bike:
                print("\nQuantity is invalid! Please enter a positive number.")
                return -1
            elif n > self.cruiser_bike:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                return -1
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Cruiser Bike rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.cruiser_bike -= n
                return now
        elif t == 'I' or t == 'i':
            if n < self.tandem_bike:
                print("\nQuantity is invalid! Please enter a positive number.")
                return -1
            elif n > self.tandem_bike:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                return -1
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Tandem Bike rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.tandem_bike -= n
                return now


        elif t == 'J' or t == 'j':
            if n < self.kids_bike:
                print("\nQuantity is invalid! Please enter a positive number.")
                return -1
            elif n > self.kids_bike:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                return -1
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Kids Bike rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.kids_bike -= n
                return now

        elif t == 'K' or t == 'k':
            if n < self.tag_a_long:
                print("\nQuantity is invalid! Please enter a positive number.")
                return -1
            elif n > self.tag_a_long:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                return -1
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Tag-A-Long rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.tag_a_long -= n
                return now

        elif t == 'L' or t == 'l':
            if n < self.kids_trailer:
                print("\nQuantity is invalid! Please enter a positive number.")
                return -1
            elif n > self.kids_trailer:
                print("Sorry! We don't have enough in stock! Please review the amount available:\n")
                self.display_stock()
                return -1
            else:
                now = datetime.datetime.now()
                print("\nYour rental has started at {}:{} on {}/{}/{} for {} Kids Trailer rental(s). ".format(now.hour, now.minute,
                                                                                                                 now.month, now.day, now.year,
                                                                                                                 n))
                self.kids_trailer -= n
                return now

    def return_rental(self, request):

        rental_time, rental_rate, num_of_bikes, type_of_bike = request
        bill = 0

        if rental_time and rental_rate and num_of_bikes and type_of_bike:
            if type_of_bike == 'A' or type_of_bike == 'a':
                self.large_swan_boat += numOfBikes
                now = datetime.datetime.now()
                rental_period = now - rental_time

                # hourly adult/ child bill calculation
                if rental_rate == 1:
                    bill = round(rental_period.seconds / 3600) * 11 * numOfBikes
                elif rental_rate == 2:
                    bill = round(rental_period.seconds / 3600) * 6 * numOfBikes
                return bill

            else:
                print("Are you sure you rented a bike with us?")
                return None


class Customer:
    def __init__(self):
        self.type_of_bike = 0
        self.bike = 0
        self.rental_rate = 0
        self.rental_time = 0
        self.bill = 0

    def request_bike(self):
        type_of_bike = input("\nWhich bike would you like to rent (Enter a letter A-N or Q to quit): ")
        if type_of_bike == 'A' or type_of_bike == 'a':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'B' or type_of_bike == 'b':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'C' or type_of_bike == 'c':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'D' or type_of_bike == 'd':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'E' or type_of_bike == 'e':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'F' or type_of_bike == 'f':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'G' or type_of_bike == 'g':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'H' or type_of_bike == 'h':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'I' or type_of_bike == 'i':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'J' or type_of_bike == 'j':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'K' or type_of_bike == 'k':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'L' or type_of_bike == 'l':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'M' or type_of_bike == 'm':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'N' or type_of_bike == 'n':
            self.type_of_bike = type_of_bike
        elif type_of_bike == 'Q' or type_of_bike == 'q':
            return -1
        else:
            print("Invalid input! Please enter a letter A-G or Q to quit.")
            if input == '0':
                return -1
            else:
                self.request_bike()

    def number_of_bikes(self):
        bike = input("\nHow many would you like to rent?" )

        try:
            bike = int(bike)
        except ValueError:
            print("\nPlease enter a positive number!")
            self.number_of_bikes()

        if bike < 1:
            print("\nInvalid input!")
            return -1
        else:
            self.bike = bike
            return self.bike

    def choose_rate(self):
        rental_rate = input("\nWhat type of rate would you like? (Enter A for Adult or C for Child): ")

        if rental_rate == 'A' or rental_rate == 'a':
            self.rental_rate = rental_rate
            return rental_rate
        elif rental_rate == 'C' or rental_rate == 'c':
            self.rental_rate = rental_rate
            return rental_rate
        else:
            print("\nError! Please enter A for Adult rate or C for Child rate.")
            self.choose_rate()

    def return_rental(self):
        if self.rental_rate and self.rental_time and self.bike and self.type_of_bike:
            return self.rental_rate, self.rental_time, self.bike, self.type_of_bike
        else:
            return 0, 0, 0, 0