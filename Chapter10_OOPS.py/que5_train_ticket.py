class Train:
    def __init__(self,name,price,seat,game):
        self.name=name
        self.price=price
        self.seat=seat
        self.game=game

    def Status(self):
        print("*************")
        print("Train name :",self.name)
        print("Seat available :",self.seat)
        print("*************")

    def Fare(self):
        print("Ticket price :",self.price)
        print("*************")

    def Book(self):
        if(self.seat>=0):
            if(self.seat>0 and self.game==0):
                print(f"Your seat confirmed & seat number is {self.seat}")
                self.list.remove(self.seat)
                self.seat=self.seat-1
                print(f"Now available seat number :{self.list}\n")
                

            elif(self.seat!=0 and self.game!=0):
                print(f"Your's seat confirmed & seat number is {self.game}")
                self.list.remove(self.game)
                self.seat=self.seat-1
                self.cali.remove(self.game)
                print("Now available seat number :",self.list,"\n")
                self.game=self.cali[self.last]

            else:
                print("Sorry,No seat vacant.Go for Tatkal\n")
    
    def Cancel(self,seat_no):
       self.cali.append(seat_no)
       self.list.append(seat_no)
       self.game=self.cali[self.last]
       self.seat=self.seat+1
       print(f"Succesfully cancel ticket seat number :{seat_no}\n")
       

hw=Train("Hawda 143120",50,4,0)

hw.list=[]
hw.cali=[0]
hw.last=-1
for i in range(1,hw.seat+1):
    hw.list.append(i)
hw.Status()
hw.Book()
hw.Book()
hw.Book()
hw.Book()
hw.Status()
hw.Book()
hw.Cancel(3)
hw.Status()
hw.Book()



