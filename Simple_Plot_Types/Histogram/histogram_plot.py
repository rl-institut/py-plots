import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["font.family"] = "Roboto"
mpl.rcParams["font.weight"] = "bold"

mpl.use("TkAgg")

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 8]
FIGSIZE = (14, 5)
ALPHA = 0.8

### Official Corporate design colors
rli_dblue = (0, 46 / 255, 80 / 255)
rli_green = (68 / 255, 175 / 255, 105 / 255)
rli_orange = (254 / 255, 127 / 255, 45 / 255)
rli_yellow = (241 / 255, 196 / 255, 15 / 255)
rli_lblue = (34 / 255, 116 / 255, 165 / 255)
rli_dgrey = (51 / 255, 88 / 255, 115 / 255)
### Not from official coperate design
rli_red = (192 / 255, 0, 0)
rli_green2 = (0, 176 / 255, 80 / 255)
rli_brown = (132 / 255, 60 / 255, 12 / 255)
rli_black = (0, 0, 0)
rli_colors = [rli_dblue, rli_green, rli_orange, rli_yellow, rli_lblue, rli_dgrey, rli_black,
              rli_red, rli_brown, rli_green2]
###
# Make Plotfonts roboto
FONT_TITLE = {'family': 'Roboto',
              'color': 'black',
              'weight': 'bold',
              'size': 16,
              }
FONT_AX = {'family': 'Roboto',
           'color': 'black',
           'weight': 'bold',
           'size': 12,
           }
n, bins, patches = plt.hist(data, bins=(max(data) - min(data)), density=True, facecolor=rli_dblue,
                            alpha=ALPHA)
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Titel des Plots', fontdict=FONT_TITLE)
plt.grid(True)
plt.show()
