class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0

    def repair(self):
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0


class Car(Vehicle):
    def __init__(self, make, model, year, weight):
        super(Car, self).__init__(make, model, year, weight)
        self.isDriving = False

    def drive(self):
        self.isDriving = True
        self.tripsSinceMaintenance += 1

        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True

    def stop(self):
        self.isDriving = False


honda = Car('Honda','Civic','2007','2800 LBS')
toyota = Car('Toyota','Tundra','2015','5400 LBS')
ford = Car('Ford','Raptor','2020','6800 LBS')

honda.drive()
honda.drive()
honda.drive()
toyota.drive()
toyota.drive()
toyota.drive()
toyota.drive()
ford.drive()
ford.drive()

sentence = 'The {} {} was built in {}, weighing in at {}.\nIt was used {} times since its last maintenance and it is {} that it needs to be serviced currently.\n\n'

print(sentence.format(honda.make,honda.model,honda.year,honda.weight,honda.tripsSinceMaintenance,str(honda.needsMaintenance).lower()))
print(sentence.format(toyota.make,toyota.model,toyota.year,toyota.weight,toyota.tripsSinceMaintenance,str(toyota.needsMaintenance).lower()))
print(sentence.format(ford.make,ford.model,ford.year,ford.weight,ford.tripsSinceMaintenance,str(ford.needsMaintenance).lower()))

ford.tripsSinceMaintenance = 100
ford.drive()

print(f'The Raptor is a work tuck and is used quite frequently. It is {str(ford.needsMaintenance).lower()} that it needs to be serviced.')

