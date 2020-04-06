# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    statistics.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ppicavez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/05 10:26:31 by ppicavez          #+#    #+#              #
#    Updated: 2020/03/05 14:15:50 by ppicavez         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import math

def count(dataframe):
    count = []
    for _, serie in dataframe.iteritems():
        nb = 0
        for _, value in serie.iteritems():
            if not pd.isna(value):
                nb = nb +1
        count.append(nb)
    return count


def maximum(dataframe):
    
    maximum = []
    for _, serie in dataframe.iteritems():
        newSerie = serie.dropna()
        maxiSerie =newSerie[0]
        for _,nb in newSerie.iteritems():
            if nb > maxiSerie:
                maxiSerie = nb
        maximum.append(maxiSerie)
    return maximum

def meanSerie(serie):
    newSerie = serie.dropna()
    length = len(newSerie)
    sum = 0.0
    try:
        for _, value in newSerie.iteritems():
            sum = sum + value
    except TypeError:
        return (float('NaN'))
    finally:
        return (sum / length)


def mean(dataframe):
    mean = [
        meanSerie(serie)
    for _, serie in dataframe.iteritems()]
    return mean

def minimum(dataframe):
    minimum = []
    for _, serie in dataframe.iteritems():
        newSerie = serie.dropna()
        miniSerie =newSerie[0]
        for _,nb in newSerie.iteritems():
            if nb <miniSerie:
                miniSerie = nb
        minimum.append(miniSerie)
    return minimum

def serieQuantile(serie, q):
    newSerie = serie.dropna()
    sortedSerie = newSerie.sort_values(ascending=True)
    length = len(sortedSerie)
    observation = q * (length - 1)
    fraction = observation % 1
    if fraction:
        i = sortedSerie.iloc[math.floor(observation)]
        j = sortedSerie.iloc[math.ceil(observation)]
        return i + (j - i) * fraction
    return observation


def quantile(dataframe, q):
    quantile = [
        serieQuantile(serie, q)
        for _, serie in dataframe.iteritems()
    ]
    return quantile

def serieStd(serie):
    newSerie = serie.dropna()
    length = len(newSerie)
    mean = meanSerie(newSerie)
    sum = 0.0
    try:
        for _, value in newSerie.iteritems():
            sum = sum + ((value - mean) ** 2)
    except TypeError:
        return (float('NaN'))
    finally:
        variance = (1 / length) * sum
        return (np.sqrt(variance))


def std(dataframe):
    
    std = [
        serieStd(serie)
        for _, serie in dataframe.iteritems()
    ]
    return std
