import matplotlib
from matplotlib.axes import Axes
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.image import imread
import os
import os.path
import numpy

######################################################
# Method to make scatter plot using images as marker #
# images are stored in icons/{shape}-{index}         #
######################################################

icon_path = os.path.join(os.path.dirname(__file__), "icons/")
size = {"o": 380,
        "s": 340}

# Patch the Axes instance!
old_init = Axes.__init__
def new_init(self, fig, rect, facecolor=None, frameon=True, sharex=None,
                  sharey=None, label="", xscale=None, yscale=None, axisbg=None, **kwargs):
    old_init(self,fig, rect, facecolor=facecolor, frameon=frameon, sharex=sharex,
                  sharey=sharey, label=label, xscale=xscale, yscale=yscale, axisbg=axisbg, **kwargs)
    self.scatter_img_counter = 0


def _scatter_img(self, x, y, s=100,
                 marker="o", index=None, label=None):
    if index is None:
        index = self.scatter_img_counter % 10 +1
        self.scatter_img_counter = index
        
    img_icon = os.path.join(icon_path,
                            "{}-{}.png".format(marker,
                                               index))
    img = imread(img_icon, format="png")
    # Copied from original scatter mathod
    # self._process_unit_info(xdata=x, ydata=y)
    # x = self.convert_xunit(x)
    # y = self.convert_yunit(y)
    x_size, y_size = self.figure.get_size_inches()
    zoom = s ** 0.5 / size[marker]
    img_inst = OffsetImage(img, zoom=zoom)
    artists = []
    for x_, y_ in zip(x, y):
        ab = AnnotationBbox(img_inst, (x_, y_),
                            xycoords="data",
                            pad=0,
                            frameon=False,
                            annotation_clip=True
        )
        artists.append(self.add_artist(ab, ))
    self.update_datalim(numpy.column_stack([x, y]))
    self.autoscale()

    # Mimicing the behavior of legend
    if label is not None:
        self.plot(x, y, label=label)
        
    return artists
Axes.__init__ = new_init
Axes.scatter_img = _scatter_img

# TODO patch the legend
