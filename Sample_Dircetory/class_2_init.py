# class computer:  # defining the class
#
#     def __init__(self, ram, cpu):  # ram & cpu are arrguments
#         self.ram = ram
#         self.cpu = cpu
#         print("Initialization")
#
#     def config(self):  # method inside the class (behavoiur)
#         print("Config is :", self.ram, self.cpu)
#
#
# comp1 = computer('RAM:16gb ', 'CPU:asus')
# comp2 = computer('RAM: 32gb ', 'CPU:nvidea')
#
# # computer.config(comp1)
#
# comp1.config()  # object & method
# # comp2.config()


#Program 2
class talentica:    # class

    def __init__(self,ht,wd):
        self.ht=ht
        self.wd=wd

    def floor(self):  #method to get ht & width
        print("height:{0} & width:{1}".format(self.ht,self.wd))


floor_4th = talentica(10,20)    # 4th & 5th floor are objects
floor_5th =  talentica(50,100)

talentica.floor(floor_4th)
floor_5th.floor()

