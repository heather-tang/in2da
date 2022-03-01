import pandas as pd
df = pd.read_csv('assets/NISPUF17.csv', index_col=0)
df = df.loc[:, ['EDUC1']]
lt12 = len(df[df['EDUC1']==1])/len(df)
twe = len(df[df['EDUC1']==2])/len(df)
gt12 = len(df[df['EDUC1']==3])/len(df)
col = len(df[df['EDUC1']==4])/len(df)

key = ['less than high school',
      'high school',
      'more than high school but not college',
      'college']
value = [lt12, twe, gt12, col]
result = {}
for i in range(4):
    result[key[i]] = value[i]
result



import numpy as np

def average_influenza_doses():
    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)
    new_df = df.rename(mapper=str.strip, axis='columns')
    new_df = df[['CBF_01', 'P_NUMFLU']]
    # new_df.head()
    # new_df['CBF_01'].unique()

    brf_numflu = new_df[new_df['CBF_01'] == 1].dropna()['P_NUMFLU']
    # len(brf_numflu)
    # np.sum(brf_numflu)
    brf_avg = np.sum(brf_numflu) / len(brf_numflu)
    brf_avg

    nbrf_numflu = new_df[new_df['CBF_01'] == 2].dropna()['P_NUMFLU']
    # len(nbrf_numflu)
    # np.sum(nbrf_numflu)
    nbrf_avg = np.sum(nbrf_numflu) / len(nbrf_numflu)
    nbrf_avg

    return (brf_avg, nbrf_avg)
  
  
  
def chickenpox_by_sex():
    import pandas as pd

    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)
    new_df = df.rename(mapper=str.strip, axis='columns')
    new_df = new_df[['SEX', 'HAD_CPOX', 'P_NUMVRC']]

#     len(new_df['HAD_CPOX'])

    # calculate how many children contracted cpx while vaccinated
    con_vcc = new_df[(new_df['P_NUMVRC'] >= 1) & (new_df['HAD_CPOX'] == 1)]

    # calculate how many children vaccinated and didn't contract
    ncon_vcc = new_df[(new_df['P_NUMVRC'] >= 1) & (new_df['HAD_CPOX'] == 2)]
    ncon_vcc_male = ncon_vcc[ncon_vcc['SEX'] == 1]
    ncon_vcc_female = ncon_vcc[ncon_vcc['SEX'] == 2]

    # calculate how many male children contracted cpx while vaccinated
    male_con = con_vcc[con_vcc['SEX'] == 1]
    female_con = con_vcc[con_vcc['SEX'] == 2]
    # len(male_con)

    # alculate the ratio of 'contracted while vaccinated' vs 'vaccinated' in male
    male_ratio = len(male_con) / len(ncon_vcc_male)
    male_ratio
    female_ratio = len(female_con) / len(ncon_vcc_female)
    female_ratio

    result = {'male': male_ratio,
           'female': female_ratio}

    return result

chickenpox_by_sex()

    #raise NotImplementedError()

  
  
def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

#     # this is just an example dataframe
#     df=pd.DataFrame({"had_chickenpox_column":np.random.randint(1,3,size=(100)),
#                    "num_chickenpox_vaccine_column":np.random.randint(0,6,size=(100))})

#     # here is some stub code to actually run the correlation
#     corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])

#     # just return the correlation
#     #return corr

    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)

    # select the two columns containing data we're insterested in
    cpx_inv = df.rename(mapper=str.strip, axis='columns')[['HAD_CPOX', 'P_NUMVRC']].dropna()
    cpx_inv = cpx_inv[(cpx_inv['HAD_CPOX'] == 1)|(cpx_inv['HAD_CPOX'] == 2)]

    # cpx_inv['HAD_CPOX'].unique()
    # cpx_inv.head(20)
    # len(cpx_inv)

    # con_cpx = cpx_inv['HAD_CPOX']
    # con_cpx.head(20)
    # num_vrc = cpx_inv['P_NUMVRC']
    # len(num_vrc)

    corr, pval=stats.pearsonr(cpx_inv['HAD_CPOX'], cpx_inv['P_NUMVRC'])
    return corr

corr_chickenpox()
