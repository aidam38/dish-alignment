class Caltech6m:
    def __init__(self):
        self.az = 0
        self.el = 0
    
    def point(self, az, el):
        self.az = az
        self.el = el

    def status(self):
        return self.az, self.el