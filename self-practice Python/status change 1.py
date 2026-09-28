class Trip:
    def __init__(self,distance,fare):
        self.distance=distance
        self.fare=fare
        self.status=None
    def complete_trip(self):
        if self.distance>100:
            self.status="Too long"
            return self.status
        elif self.distance>0 and self.fare>0:
            print("Trip complete")
            self.status="complete"
            return self.status
        else:
            print("trip unsuccessful")
            self.status="failed"
            return self.status
    def check_status(self):
        if self.status is None:
            return "Trip pending"
        elif self.status=="complete":
            return"Trip complete"
        elif self.status=="Too long":
            return "Too long"
        else:
            return"Trip failed"

my_trip=Trip(0,5)
print(my_trip.complete_trip())
print(my_trip.check_status())
            
            
        