# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ppicavez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/05 10:26:31 by ppicavez          #+#    #+#              #
#    Updated: 2020/03/05 14:15:50 by ppicavez         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import sys

def read_csv(path):
    parameters = None
    try:
        parameters = pd.read_csv(path)
    except FileNotFoundError:
        print(f'File at path: "{path}" not found')
        sys.exit(1)
    except Exception:
        print(f'An unexpected error occured on read_csv')
        sys.exit(1)
    return parameters

def drop_columns(df=None, columns=[]):
    df.drop(columns, axis=1, inplace=True)
    return df
