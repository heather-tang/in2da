def answer_one():

    Energy = pd.read_excel('assets/Energy Indicators.xls', skiprows = 17,
                          skipfooter = 38, usecols = 'C:G')
    # Energy.columns
    Energy.rename(columns={'Unnamed: 2':'Country', 'Petajoules':'Energy Supply',
                           'Gigajoules':'Energy Supply per Capita', '%':'% Renewable'},
                  inplace=True)
    Energy[Energy['Energy Supply']=='...']=np.nan
    Energy['Energy Supply'] = pd.to_numeric(Energy['Energy Supply'])
    Energy['Energy Supply'] = Energy['Energy Supply'] *1000000
    # Energy['Energy Supply']

    Energy = Energy.replace({'Country':{'United States of America20':'United States',
                                        'United Kingdom of Great Britain and Northern Ireland19':'United Kingdom',
                                        'China, Hong Kong Special Administrative Region3':'Hong Kong'}})

    Energy['Country'] = Energy['Country'].replace('\(.*\)$', '', regex=True)
    Energy['Country'] = Energy['Country'].replace('\d', '', regex=True)
#     Energy.tail(5)

    GDP = pd.read_csv('assets/world_bank.csv', skiprows = 4)
    # GDP.head()
    GDP = GDP.replace({'Country Name': {"Korea, Rep.": "South Korea",
                                        "Iran, Islamic Rep.": "Iran",
                                        "Hong Kong SAR, China": "Hong Kong"}})
    # GDP.head()
    cols = ['Country Name']
    years = ['2006', '2007', '2008', '2009', '2010',
            '2011', '2012', '2013', '2014', '2015']
    cols = cols + years

    GDP = GDP[cols]
    GDP[GDP['Country Name']=='Iran']
    GDP[GDP['Country Name']=='South Korea']

    ScimEn = pd.read_excel('assets/scimagojr-3.xlsx')
#     ScimEn.head()

    ScimEn = ScimEn.set_index('Rank')
    ScimEn = ScimEn.iloc[:15]
    ScimEn = ScimEn.reset_index()
#     ScimEn.head(15)

    t1 = pd.merge(ScimEn, GDP, how='inner', left_on='Country', right_on='Country Name')
    t1.set_index('Rank').head(15)
    summary = t1.merge(Energy, how='left', on='Country')
    summary.set_index('Rank')
    summary.columns
    cols_to_keep = ['Rank', 'Country', 'Documents', 'Citable documents', 'Citations',
           'Self-citations', 'Citations per document', 'H index',
           '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
           '2015', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    summary = summary[cols_to_keep]
    summary = summary.set_index('Rank')

    return summary

answer_one()
#     raise NotImplementedError()
