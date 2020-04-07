# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ppicavez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/05 10:26:31 by ppicavez          #+#    #+#              #
#    Updated: 2020/03/05 14:15:50 by ppicavez         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import argparse
import sys
import os

from utils import readCsv, dropColumns  

from statistics import count, mean, std, quantile, minimum, maximum  

def describe(fileName):
    
    datas = readCsv(fileName)
    datas = dropColumns(datas, ["Index", "Hogwarts House", "First Name",
                           "Last Name", "Birthday", "Best Hand"])
    result = pd.DataFrame(
        columns=datas.columns,
        index=["Count","Mean","Std","Min","25%","50%","75%","Max"
        ]
    )

    result.iloc[0] = count(datas)
    result.iloc[1] = mean(datas)
    result.iloc[2] = std(datas)
    result.iloc[3] = minimum(datas)
    result.iloc[4] = quantile(datas, 0.25)
    result.iloc[5] = quantile(datas, 0.50)
    result.iloc[6] = quantile(datas, 0.75)
    result.iloc[7] = maximum(datas)

    print(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise "Usage: {} data_file".format(sys.argv[0])
    describe(sys.argv[1])
