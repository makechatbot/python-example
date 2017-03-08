import numpy as np
import matplotlib.pylab as plt


# plt.plot([1,4, 9, 16])
# plt.show()


# plt.plot([10, 20, 30, 40], [1,4, 9, 16])
# plt.show()


# plt.plot([1,4,9,16], 'rs--')
# plt.show()

# plt.plot([1,4,9,16], c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
# plt.show()

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
# plt.plot(X, C, label="cosine")
# plt.xlabel("time")
# plt.ylabel("amplitude")
# plt.title("Cosine Plot")
# plt.show()


# plt.plot(X, S, label="sine")
# plt.scatter([0], [0], color="r", linewidth=10)
# plt.annotate(r'$(0,0)$', xy=(0, 0), xycoords='data', xytext=(-50, 50),
#              textcoords='offset points', fontsize=16,
#              arrowprops=dict(arrowstyle="->", linewidth=3, color="g"))
# plt.show()


f1 = plt.figure(figsize=(10,2))
plt.plot(np.random.randn(100))
plt.show()