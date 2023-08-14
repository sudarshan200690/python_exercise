class pyCharm:
    def execute(self):
        print('compiling')
        print('running')
class Laptop:
    def code(self,ide):
        ide.execute()

ide = pyCharm()
lap = Laptop()
lap.code(ide)
