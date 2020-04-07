import pandas as pd
import matplotlib.pyplot as plt
import sys
from utils import readCsv

courses = [
	'Arithmancy',
	'Astronomy',
	'Herbology',
	'Defense Against the Dark Arts',
	'Divination',
	'Muggle Studies',
	'Ancient Runes',
	'History of Magic',
	'Transfiguration',
	'Potions',
	'Care of Magical Creatures',
	'Charms',
	'Flying'
]

houses = ['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff']


def scatter(fileName):
	try:
		datas = readCsv(fileName)
	except FileNotFoundError as e:
		print(e)
		exit()

	groupedBy = datas.groupby('Hogwarts House')

	fig, axes = plt.subplots(13, 13, figsize=(15, 10))
	fig.subplots_adjust(hspace=0, wspace=0)
	i = 0
	for ax, course in zip(axes, courses):
		ax[i].text(0.5, 0.5, course.replace(' ', '\n'), ha='center', va='center', fontsize=8)
		for a in ax:
			a.set_xticklabels([])
			a.set_yticklabels([])
			a.tick_params(axis='both', width=0)
		i += 1

	for i, xi in enumerate(courses):
		for j, yi in enumerate(courses):
			if xi == yi:
				continue
			ravenclowX = groupedBy.get_group('Ravenclaw')[xi]
			slytherinX = groupedBy.get_group('Slytherin')[xi]
			gryffindorX = groupedBy.get_group('Gryffindor')[xi]
			hufflepuffX = groupedBy.get_group('Hufflepuff')[xi]


			ravenclowY = groupedBy.get_group('Ravenclaw')[yi]
			slytherinY = groupedBy.get_group('Slytherin')[yi]
			gryffindorY = groupedBy.get_group('Gryffindor')[yi]
			hufflepuffY = groupedBy.get_group('Hufflepuff')[yi]

			axes[i][j].plot(ravenclowX, ravenclowY, 'v', markersize=.5, color='blue')
			axes[i][j].plot(slytherinX, slytherinY, '^', markersize=.5, color='green')
			axes[i][j].plot(gryffindorX, gryffindorY, 'o', markersize=.5, color='red')
			axes[i][j].plot(hufflepuffX, hufflepuffY, 's', markersize=.5, color='yellow')
	plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise "Usage: {} data_file".format(sys.argv[0])
    scatter(sys.argv[1])
