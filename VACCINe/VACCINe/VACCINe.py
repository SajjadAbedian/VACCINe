def geo_to_fips(dataframe, latitude, longitude):
    fips = []
    for index, value in enumerate(dataframe.iloc[:,0]):
        url = "https://geo.fcc.gov/api/census/block/find?latitude=" + str(dataframe[latitude][index]) + "&longitude="+ str(dataframe[longitude][index]) + "&format=json"
        obj = json.load(urlopen(url))
        fips.append(obj['Block']['FIPS'])
    dataframe["FIPS"] = fips
    print("FIPS code converted")
    return  dataframe


def fips_check(df, col):
    tract = []
    for n in df[col]:
        tract.append(len(str(n)))
    return max(tract)



def fips_11(df, column_list = []):
    selected_columns = column_list
    df_new = df.loc[:, selected_columns].reset_index(drop=True)
    df_new[column_list[0]] = df_new[column_list[0]].apply(lambda x: str(x)[:11])
    df_new.rename(columns={df_new.columns[0]:'FIPS'}, inplace=True)
    return df_new



def fips_12(df, column_list = []):
    selected_columns = column_list
    df_new = df.loc[:, selected_columns].reset_index(drop=True)
    df_new[column_list[0]] = df_new[column_list[0]].apply(lambda x: str(x)[:12])
    df_new.rename(columns={df_new.columns[0]:'FIPS'}, inplace=True)
    return df_new