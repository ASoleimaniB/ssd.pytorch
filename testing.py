import argparse
parser = argparse.ArgumentParser(description='Single Shot MultiBox Detector Training')
args = parser.parse_args()
class SSDAugmentation(object):
    m=1
    def __init__(self, size=300, mean=(104, 117, 123)):
        self.mean = mean
        self.size = size
        self.augment = 'asd'


(v1, v2)[args.version == 'v2']


a=SSDAugmentation()
print(a.mean)
print(SSDAugmentation.mean)