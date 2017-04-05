import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gspec

fig = plt.figure()

n = 1000
a = 2-math.sqrt(3)
b = 2+math.sqrt(3)

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
# Mean is 2 in all cases. Standard variation is 1 in normal and gamma. standard deviation of the expontential is 2.
# standard deviation of uniform is 1.333.
x1 = np.random.normal(2, 1, n)
x2 = np.random.gamma(2, 1, n)
x3 = np.random.exponential(2, n)
x4 = np.random.uniform(0, 4, n)

def update(curr):
    # check if animation is at the last frame, and if so, stop the animation a
    if curr == n: 
        a.event_source.stop()
    plt.cla()
    bins = np.arange(-3, 15, .5)
    plt.hist(x1[:curr], bins=bins, histtype = 'step', color = 'b', label = 'Normal')
    plt.hist(x2[:curr], bins=bins, histtype = 'step', color = 'g', label = 'Gamma')
    plt.hist(x3[:curr], bins=bins, histtype = 'step', color = 'm', label = 'Exponential')
    plt.hist(x4[:curr], bins=bins, histtype = 'step', color = 'y', label = 'Uniform')
    plt.axis([-3,15,0,250])
    plt.gca().set_title('4 Probability Distributions with Mean = 2')
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n = {}'.format(curr), [-1.8,240])
    plt.legend()
    
    

a = animation.FuncAnimation(fig, update, interval = 100, repeat = False)
plt.show()