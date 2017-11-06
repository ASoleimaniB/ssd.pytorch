class SSDAugmentation(object):
    m=1
    def __init__(self, size=300, mean=(104, 117, 123)):
        self.mean = mean
        self.size = size
        self.augment = 'asd'





a=SSDAugmentation()
print(a.mean)
print(SSDAugmentation.mean)