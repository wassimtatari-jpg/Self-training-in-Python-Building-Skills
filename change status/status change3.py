class Booking:
    def __init__(self,guests,days):
        self.guests=guests
        self.days=days
        self.status=None
    def confirm_booking(self):
        if self.guests>6:
            self.status="too many guests"
            return self.status
        elif self.guests>0 and self.days>0:
            self.status="confirmed"
            return self.status
        else:
            self.status="failed"
            return self.status
    def check_booking(self):
        if self.status is None:
            return"booking pending"
        elif self.status=="confirmed":
            return"booking confirmed"
        elif self.status=="too many guests":
            return"too many guestds"
        else:
            return"boking failed"
my_book=Booking(2,3)
print(my_book.confirm_booking())
print(my_book.check_booking())