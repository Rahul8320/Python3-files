# duck typing


class Pycharm:
    def execute(self):
        print("Execute code")
        print("output")


class Spider:
    def execute(self):
        print("Execute code")
        print("Compile code")
        print("Output")


class Anaconda:
    def execute(self):
        print("Execute code")
        print("Compile code")
        print("Check errors")
        print("Output")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = Anaconda()

lap1 = Laptop()
lap1.code(ide)
