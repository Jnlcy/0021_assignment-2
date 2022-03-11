from noisyPattern import noisyPattern
import numpy as np
import random
import matplotlib.pyplot as plt

def main():
    pattern = noisyPattern()
    pattern.setLines()
    pattern.addnoise()
    pattern.removeNoise()
    pattern.filter1()



if __name__ == "__main__":
    main() 