import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import csv
from collections import defaultdict
import datetime


class Dot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


dots = defaultdict(list)

with open('coordinates.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            dots[row[0]] = Dot(row[1], row[2])
            line_count += 1

title_input = input("Enter figure title (ex: 'Routing Result-001'): ")
routes_input = [
    "0 - 57 - 63 - 61 - 66 - 42 - 87 - 33 - 5 - 0",
    "0 - 78 - 77 - 56 - 19 - 38 - 1 - 64 - 80 - 79 - 0",
    "0 - 44 - 25 - 9 - 16 - 3 - 30 - 39 - 52 - 26 - 85 - 0",
    "0 - 100 - 28 - 62 - 82 - 14 - 20 - 68 - 36 - 4 - 0",
    "0 - 70 - 47 - 35 - 31 - 18 - 48 - 6 - 37 - 49 - 0",
    "0 - 43 - 98 - 23 - 89 - 67 - 99 - 69 - 2 - 74 - 0",
    "0 - 7 - 65 - 84 - 45 - 40 - 93 - 83 - 8 - 88 - 0",
    "0 - 15 - 13 - 10 - 97 - 34 - 32 - 50 - 90 - 24 - 0",
    "0 - 22 - 53 - 51 - 29 - 94 - 92 - 59 - 60 - 21 - 0",
    "0 - 17 - 81 - 11 - 54 - 76 - 75 - 71 - 58 - 0",
    "0 - 55 - 73 - 41 - 96 - 72 - 12 - 86 - 91 - 0",
    "0 - 95 - 46 - 27 - 0"
]

routes = []

index = 0
for route in routes_input:
    iter_route = []
    for r in route.split(" - "):
        iter_route.append(r)
    routes.append(iter_route)


verts = []
codes = []
fig, ax = plt.subplots()

total_count = 0
for route in routes:
    total_count += 1
    iter_verts = []
    iter_codes = []
    for s in route:
        iter_verts.append((dots[s].x, dots[s].y))
        ax.text(float(dots[s].x), float(dots[s].y) + 1,
                s, size='x-small')
        if len(iter_codes) == 0:
            iter_codes.append(Path.MOVETO)
            plt.scatter(float(dots[s].x), float(dots[s].y), color='green')
        else:
            iter_codes.append(Path.LINETO)
            plt.scatter(float(dots[s].x), float(dots[s].y), color='black', s=7)

    verts.append(iter_verts)
    codes.append(iter_codes)

color_array = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
               '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
               '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
               '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
               '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
               '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
               '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
               '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
               '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
               '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF']
color_index = 0
for index in range(total_count):
    path = Path(verts[index], codes[index])
    patch = patches.PathPatch(path, facecolor='none',
                              lw=0.5, edgecolor=color_array[index])
    ax.add_patch(patch)
    color_index += 1

ax.set_title(title_input)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

dt = datetime.datetime.now().strftime("%Y-%m-%d_%X")

fig.savefig(f'{title_input}_{dt}.png', dpi=500)
