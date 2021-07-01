class Vehicle:

	def __init__(self,vehicle_id,type,cost,amount=0):
		self.__vehicle_id=vehicle_id
		self.__type=type
		self.__cost=cost
		self.__premium_amount=amount


	def set_vehicle_id(self,id):
		self.__vehicle_id=id 

	def get_vechicle_id(self):
		print(self.__vehicle_id)

	def set_type(self,type):
		if type == "Two Wheeler" || "Four Wheeler":
			self.__type=type 
		else:
			print("Type is not suport.")

	def get_type(self):
		print(self.__type)

	def set_cost(self,cost):
		self.__cost=cost 

	def get_cost(self):
		print(self.__cost)

	def set_premimum_amount(self,premium_amount):
		self.__premium_amount=premium_amount 

	def get_premium_amount(self):
		print(self.__premium_amount)

	def calculate_premium(self):
		if self.__type == "Two Wheeler":
			self.__premium_amount = self.__cost*(2/100)

		if self.type == "Four Wheeler":
			self.__premium_amount = self.__cost*(6/100)


	def display_vehicle_details(self):
		print(self.__vehicle_id)
		print(self.__type)
		print(self.__cost)
		print(self.__premium_amount)


bmw = Vehicle(25,"Four Wheeler",1000000,200)
bmw.display_vehicle_details()