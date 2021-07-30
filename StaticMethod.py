class Math:

    ## create functions that are not instances
    @staticmethod
    def add5(x):
        return x + 5 

    @staticmethod
    def add10(x):
        return x + 10

print(Math.add10(2)) 

