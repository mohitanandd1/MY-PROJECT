import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('rwl_tel_hr_bihar_999_2021_2025.csv')
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns.to_list)
print(df.describe())
print(df.describe(include='all'))

print(df.duplicated().sum())
print(df.isnull().sum())
print(df['River Water Level Telemetry Hourly (meter)'].isnull().mean()*100)
print(df['River Water Level Telemetry Hourly (meter)'].dtype)
# print(df['Data Acquisition Time'].dtype)
df['Data Acquisition Time'] =pd.to_datetime(df['Data Acquisition Time'],errors='coerce')
print("after conversion: ",df['Data Acquisition Time'].dtype)
print(df['Data Acquisition Time'].head(2))
print("conversion done")

print(df['Data Acquisition Time'].isna().sum())
print(df['Data Acquisition Time'].min())
print(df['Data Acquisition Time'].max())
print(df[['SlNo','Data Acquisition Time']].head())

print(df['Station'].nunique())
print(df['District'].nunique())
print(df[['Station','District']].drop_duplicates().head(17))
print(df['River'].nunique())
print(df['River'].unique())
print(df['Local River'].nunique())
print(df['Local River'].unique())
print(df['Tributary'].nunique())
print(df['Tributary'].unique())
print(df['Subtributary'].nunique())
print(df['Subtributary'].unique())
print(df['SubSubtributary'].nunique())
print(df['SubSubtributary'].unique())

print(df[['Station','Latitude','Longitude']].drop_duplicates().head(17))
print(df['Station'].value_counts())

print(df.groupby('Station')['River Water Level Telemetry Hourly (meter)'].apply(lambda x:x.isnull().sum()))
print(df[df['River Water Level Telemetry Hourly (meter)'].isnull()][['Station','Data Acquisition Time']].head(20))
print(df[(df['Station']=='Arrah Chhapra Bridge') &(df['River Water Level Telemetry Hourly (meter)'].isnull())][['Station','Data Acquisition Time']])
missing = df[
    (df['Station'] == 'Arrah Chhapra Bridge') &
    (df['River Water Level Telemetry Hourly (meter)'].isnull())
]

print(missing['Data Acquisition Time'].min())
print(missing['Data Acquisition Time'].max())
print(len(missing))

ara = df[df['Station'] == 'Arrah Chhapra Bridge'].sort_values('Data Acquisition Time')
print(ara['Data Acquisition Time'].diff().value_counts().head(10))

ara = df[df['Station'] == 'Arrah Chhapra Bridge'].sort_values('Data Acquisition Time')
print(ara['Data Acquisition Time'].diff().value_counts().head(10))

print(ara[ara['Data Acquisition Time'].diff() == pd.Timedelta(0)][
    ['Station', 'Data Acquisition Time']
].head(20))

print(ara['Data Acquisition Time'].duplicated().sum())

print(ara[ara['Data Acquisition Time'].duplicated(keep=False)][
    ['Station', 'Data Acquisition Time',
     'River Water Level Telemetry Hourly (meter)']
].head(10))

print(
    ara.groupby('Data Acquisition Time')['River Water Level Telemetry Hourly (meter)']
    .nunique()
    .value_counts()
)

print(ara[
    (ara['Data Acquisition Time'] >= '2022-02-07') &
    (ara['Data Acquisition Time'] <= '2022-02-10')
][['Data Acquisition Time',
   'River Water Level Telemetry Hourly (meter)']].to_string(index=False))

print(ara['River Water Level Telemetry Hourly (meter)'].isnull().sum())

print(
    ara[ara['River Water Level Telemetry Hourly (meter)'].isnull()]
    [['Data Acquisition Time']]
    .to_string(index=False)
)

print(ara[
    (ara['Data Acquisition Time'].dt.date == pd.Timestamp('2022-02-07').date()) &
    (ara['Data Acquisition Time'].dt.hour.isin([20, 21, 22, 23]))
][['Data Acquisition Time',
   'River Water Level Telemetry Hourly (meter)']].to_string(index=False))

print(ara.duplicated(subset=['Station', 'Data Acquisition Time']).sum())

print(ara['Data Acquisition Time'].value_counts().value_counts())

print(
    ara[ara['Data Acquisition Time'].duplicated(keep=False)]
    [['Data Acquisition Time',
      'River Water Level Telemetry Hourly (meter)']]
    .sort_values('Data Acquisition Time')
    .head(20)
    .to_string(index=False)
)


print(
    ara.groupby('Data Acquisition Time')['River Water Level Telemetry Hourly (meter)']
    .apply(lambda x: (x.notna().sum(), x.isna().sum()))
    .value_counts()
)

print(
    ara.groupby('Data Acquisition Time')['River Water Level Telemetry Hourly (meter)']
    .agg(['min', 'max'])
    .assign(diff=lambda x: x['max'] - x['min'])
    .sort_values('diff', ascending=False)
    .head(10)
)

print(
    ara[ara['Data Acquisition Time'] == pd.Timestamp('2022-07-11 05:00:00')]
    .to_string(index=False)
)

print(df[df['River Water Level Telemetry Hourly (meter)'] > 100][
    ['Station', 'Data Acquisition Time',
     'River Water Level Telemetry Hourly (meter)']
].head(20).to_string(index=False))

print(df['River Water Level Telemetry Hourly (meter)'].describe())

print((ara['River Water Level Telemetry Hourly (meter)'] > 100).sum())


print(
    df[
        (df['Station'] == 'Arrah Chhapra Bridge') &
        (df['Data Acquisition Time'] == pd.Timestamp('2022-07-11 05:00:00'))
    ][[
        'SlNo',
        'Station',
        'Data Acquisition Time',
        'River Water Level Telemetry Hourly (meter)',
        'RL_of_zeroGauge',
        'MeanSeaLevel',
        'Is_DischargeDataAvailable'
    ]].to_string(index=False)
)

print(
    ara[ara['River Water Level Telemetry Hourly (meter)'] > 100]
    [['SlNo',
      'Data Acquisition Time',
      'River Water Level Telemetry Hourly (meter)']]
    .sort_values('Data Acquisition Time')
    .to_string(index=False)
)

for t in ara.loc[
    ara['River Water Level Telemetry Hourly (meter)'] > 100,
    'Data Acquisition Time'
].unique():

    print("\nTIME:", t)

    print(
        ara[ara['Data Acquisition Time'] == t][
            ['SlNo',
             'Data Acquisition Time',
             'River Water Level Telemetry Hourly (meter)']
        ].to_string(index=False)
    )

    print(
    ara['Data Acquisition Time']
    .dt.hour
    .value_counts()
    .sort_index()
)


print(
    ara[ara['Data Acquisition Time'] == pd.Timestamp('2022-07-11 05:00:00')][
        ['SlNo',
         'Data Acquisition Time',
         'River Water Level Telemetry Hourly (meter)']
    ].to_string(index=False)
)


print(
    ara['River Water Level Telemetry Hourly (meter)']
    .describe()
)

ara['Month'] = ara['Data Acquisition Time'].dt.to_period('M')

print(
    ara.groupby('Month')['River Water Level Telemetry Hourly (meter)']
    .agg(['mean', 'max'])
    .tail(20)
)

print(
    ara.assign(Month=ara['Data Acquisition Time'].dt.to_period('M'))
    .groupby('Month')['River Water Level Telemetry Hourly (meter)']
    .apply(lambda x: (x > 100).sum())
)


print(
    ara[ara['River Water Level Telemetry Hourly (meter)'] > 100]
    [['Data Acquisition Time', 'River Water Level Telemetry Hourly (meter)']]
    .sort_values('Data Acquisition Time')
    .to_string(index=False)
)


print(
    ara[
        (ara['Data Acquisition Time'] >= '2022-04-26 20:00:00') &
        (ara['Data Acquisition Time'] <= '2022-04-27 06:00:00')
    ][
        ['Data Acquisition Time',
         'River Water Level Telemetry Hourly (meter)']
    ].to_string(index=False)
)


print(
    ara[
        (ara['Data Acquisition Time'] >= '2022-07-11 02:00:00') &
        (ara['Data Acquisition Time'] <= '2022-07-11 08:00:00')
    ][
        ['Data Acquisition Time',
         'River Water Level Telemetry Hourly (meter)']
    ].to_string(index=False)
)

print(
    ara[
        ara['Data Acquisition Time'].eq('2022-07-11 05:00:00')
    ].to_string(index=False)
)

print(
    ara[ara['River Water Level Telemetry Hourly (meter)'] > 100]
    [['Data Acquisition Time',
      'River Water Level Telemetry Hourly (meter)']]
    .merge(
        ara[['Data Acquisition Time',
             'River Water Level Telemetry Hourly (meter)']],
        on='Data Acquisition Time',
        suffixes=('_extreme', '_same_time')
    )
    .sort_values('Data Acquisition Time')
    .to_string(index=False)
)

print(
    ara[
        (ara['Data Acquisition Time'] >= '2023-08-15 09:00:00') &
        (ara['Data Acquisition Time'] <= '2023-08-15 15:00:00')
    ][
        ['Data Acquisition Time',
         'River Water Level Telemetry Hourly (meter)']
    ].to_string(index=False)
)


print(
    ara[
        (ara['Data Acquisition Time'] == '2023-08-15 12:00:00')
    ][
        ['SlNo',
         'Station',
         'Data Acquisition Time',
         'River Water Level Telemetry Hourly (meter)']
    ].to_string(index=False)
)


print(
    ara[
        ara['Data Acquisition Time'] == '2023-08-15 12:00:00'
    ].to_string(index=False)
)


print(
    ara[ara['River Water Level Telemetry Hourly (meter)'] > 100]
    [['Data Acquisition Time',
      'River Water Level Telemetry Hourly (meter)']]
    .sort_values('Data Acquisition Time')
    .to_string(index=False)
)


print(
    ara.groupby('Month')['River Water Level Telemetry Hourly (meter)']
    .mean()
)

print(
    ara.groupby('Month')['River Water Level Telemetry Hourly (meter)']
    .median()
)


print(
    ara.groupby(ara['Data Acquisition Time'].dt.year)
    ['River Water Level Telemetry Hourly (meter)']
    .median()
)

print(
    ara.groupby(ara['Data Acquisition Time'].dt.to_period('M'))
    ['River Water Level Telemetry Hourly (meter)']
    .median()
    .head(20)
)


print(
    ara.groupby(ara['Data Acquisition Time'].dt.date)
    ['River Water Level Telemetry Hourly (meter)']
    .median()
    .tail(250)
)




# Create a working copy for preprocessing
clean_df = df.copy()

print(clean_df.shape)


# Sort data station-wise and chronologically
clean_df = clean_df.sort_values(
    by=['Station', 'Data Acquisition Time']
).reset_index(drop=True)

print(clean_df[['Station', 'Data Acquisition Time']].head(10))


print(clean_df.isnull().sum())

print(
    clean_df.duplicated(
        subset=['Station', 'Data Acquisition Time']
    ).sum()
)


print(
    clean_df.groupby(
        ['Station', 'Data Acquisition Time']
    ).size().value_counts().sort_index()
)


print(
    clean_df[clean_df['River Water Level Telemetry Hourly (meter)'].isnull()]
    [['Station', 'Data Acquisition Time']]
    .head(20)
)

missing = clean_df[
    clean_df['River Water Level Telemetry Hourly (meter)'].isnull()
]

print(missing.groupby('Station').size())


missing = clean_df[
    clean_df['River Water Level Telemetry Hourly (meter)'].isnull()
]

print(
    missing.groupby('Station')['Data Acquisition Time']
    .agg(['min', 'max'])
)

print(
    clean_df[
        (clean_df['Station'] == 'Arrah Chhapra Bridge') &
        (
            (clean_df['Data Acquisition Time'] == '2022-02-07 04:00:00') |
            (clean_df['Data Acquisition Time'] == '2022-02-09 05:00:00')
        )
    ][
        ['Station', 'Data Acquisition Time',
         'River Water Level Telemetry Hourly (meter)']
    ]
)


clean_df = clean_df.dropna(
    subset=['River Water Level Telemetry Hourly (meter)']
).copy()

print(clean_df.shape)
print(clean_df['River Water Level Telemetry Hourly (meter)'].isnull().sum())