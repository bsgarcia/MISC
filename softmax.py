import numpy as np
import matplotlib.pyplot as plt


def softmax(x, beta):
    return 1/(1+np.exp(beta-x))

def main():
    # x = np.linspace(-10, 10, 20)
    x = np.linspace(0, 1, 20)
    plt.plot(x, x**.2, color='black', lw=8)
    plt.plot(x, -x**.2, color='black', lw=8, alpha=.5)
    plt.plot(x, [0, ] * len(x), color='black', lw=5, ls='--')
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('values.png')



if __name__ == '__main__':
    main()
