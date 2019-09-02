def transformTable(sourceDf, tableKey):
    print('--- read data for table ' + tableKey +' ---')

    snakeKey = tableKey # En_Cn , for example E3_C6
    kebabKey = tableKey.replace('_', '-') # En-Cn , for example E3-C6

    # Filter column name ends with end with tableKey (En_Cn) and copy( allow for white space at the end of the col name)
    tableFilterRegEx = '.*' + snakeKey + '$'
    dfTrans = sourceDf.filter(regex=tableFilterRegEx, axis=1).copy()

    # Add 'ID' column to the front of dataframe
    dfTrans.insert(0, 'ID', sourceDf.filter(items=['Study Subject ID']))

    # Add 'E1-C6' suffix to 'ID' cells
    dfTrans['ID'] = dfTrans['ID'].astype(str) + '-' + kebabKey
    dfTrans.rename(columns=lambda x: x.replace(('_' + snakeKey), ''), inplace=True)
    
    return dfTrans
