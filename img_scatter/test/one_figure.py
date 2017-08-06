import matplotlib
import matplotlib.pyplot as plt
import img_scatter
import numpy

a = numpy.linspace(-3.14*3, 3.14*3, 50)
b = numpy.sin(a)
c = numpy.cos(a)

matplotlib.style.use("science")
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)

ax.scatter_img(x=a, y=b, s=200, marker="o")
ax.scatter_img(x=a, y=c, s=200, marker="s")

fig.savefig("one_figure.svg")
fig.savefig("one_figure.png")
fig.savefig("one_figure.pdf")




