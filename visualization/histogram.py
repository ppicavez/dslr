# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ppicavez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/05 10:26:31 by ppicavez          #+#    #+#              #
#    Updated: 2020/03/05 14:15:50 by ppicavez         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

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

def histogram(fileName):
	
	try:
		datas = readCsv(fileName)
	except FileNotFoundError as e:
		print(e)
		exit(1)
	plt.figure(figsize=(8, 6))
	groupedBy = datas.groupby('Hogwarts House')
	for course in courses:
		groupedBy[course].plot(kind='hist', alpha=0.5)
		plt.title("Histogram of notes frequency by House  \n for " + course + " course")
		plt.legend(loc='upper left')
		print("Notes frequency by House for " + course )
		print("Close graphical windows to see next histogram  or press Ctrl + W \n")
		plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise "Usage: {} data_file".format(sys.argv[0])
    histogram(sys.argv[1])
