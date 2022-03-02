from faker import Faker
from collections import defaultdict
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn_pandas import DataFrameMapper
import names


def anonymizeL1(df):
    'Anonymizes the given original data to anonymized form'
    # Load the faker and its providers
    df_out = pd.DataFrame(df)

    # creationg dictionary of functions
    functions = {'PN': anon_PN, 'EML': anon_EML, 'GEN': anon_GEN, 'ADRS': anon_ADRS,
                 'TL': anon_TL}
    df_in = df[df.columns[::-1]]
    headers = df_in.head()

    for column in headers:
        df_out[column] = functions[column](df_in[column])
    print("---------------------------------------------------------------------")
    print("Anonymised Data:")
    print(df_out)


def anon_PN(df):
    df1 = pd.DataFrame(df)
    for row in df1:
        faker = Faker("en_US")
        names = defaultdict(faker.name)
        df1[row] = names[row]
    return df1


"""def anon_PN_F(df):
    df1 = pd.DataFrame(df)
    for row in range(len(df.index)):
        rand_name = names.get_first_name()
        print("***********", rand_name)
        df1[row] = rand_name
        df1['PN_F'] = df1[row]
    return df1

def anon_PN_L(df):
    df1 = pd.DataFrame(df)
    for row in df1:
        rand_name = names.get_last_name()
        df1[row] = rand_name
    return df"""


def anon_EML(df):
    faker = Faker()
    emails = defaultdict(faker.email)
    df1 = emails[df[0]]
    return df1


def anon_COM(df):
    df1 = pd.DataFrame(df)
    encoders = [(["company_name"], LabelEncoder())]
    mapper = DataFrameMapper(encoders, df_out=True)
    label_col = mapper.fit_transform(df1.copy())
    df1 = label_col
    return df1


def anon_GEN(df):
    # df['GEN'] = np.where(df['GEN'] == "Female", 0, 1)
    return df


def anon_ADRS(df):
    df = np.random.permutation(df)
    return df


def anon_TL(df):
    fake1 = Faker('en_US')
    df = fake1.phone_number()
    return df


def anonymizeL3(df):
    'Anonymize the given original data to anonymized form'
    df_in = pd.DataFrame(df)
    print(df_in)
    df_out = pd.DataFrame(df_in)

    for row in range(len(df_in.index)):
        for column in df_in.columns:
            if column == 'TL':
                df_out = np.random.permutation(df)
            else:
                df_out.values[row, column] = column + ' ' + str(df_in.index[row][column])[0]
    print("Anonymised Data")
    print(df_out)


def anonymizeData(df, level):
    df_in = pd.DataFrame(df)
    if level == "L1":
        anonymizeL1(df_in)
    elif level == "L3":
        anonymizeL3(df_in)
    return df

# if __name__ == '__main__':
#     df = pd.read_csv(r"C:\Users\megha\Documents\Python Programming\Input Testdata\test.csv")
#     print("Actual DF: ", df)
#     anonymizeData(df, "L1")
