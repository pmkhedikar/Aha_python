class computer:  # defining the class

    # def __init__(self, ram, cpu, processor):  # ram & cpu are arrguments
    #     self.ram = ram
    #     self.cpu = cpu
    #     self.processor = processor
    #     #print("Initialization")
    def __init__(self):
        self.ram = "1gb"
        self.cpu = "1000 gb"
        self.processor = "i1"

    def config(self):  # method inside the class (behaviour)
        print("Config is :", self.ram, self.cpu, self.processor)


#comp1 = computer('16gb ', 'asus','i3')
#comp2 = computer('RAM: 32gb ', 'CPU:nvidea')
#parag_comp = computer('16Gb:RAM','500gb=HD' , 'i5')
empty_comp = computer()

# computer.config(comp1)
#comp1.config()  # object & method
#comp2.config()
#parag_comp.config()

empty_comp.config()



# #Program 2
# class talentica:    # class
#
#     def __init__(self,ht,wd):
#         self.ht=ht
#         self.wd=wd
#
#     def floor(self):  #method to get ht & width
#         print("height:{0} & width:{1}".format(self.ht,self.wd))
#
#
# floor_4th = talentica(10,20)    # 4th & 5th floor are objects
# floor_5th =  talentica(50,100)
#
# talentica.floor(floor_4th)
# floor_5th.floor()

