#import libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sidetable
from nhanes_data.nhanes_data_api import NHANESDataAPI
import scipy.stats as stats
import researchpy as rp
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import statsmodels.formula.api as smf

#website for instructions
#documentation of nhanes_data - https://pypi.org/project/nhanes-pytool-api/
# github
# https://github.com/kkrusere/NHANES-pyTOOL-API/blob/main/docs/index.md#data-retrieval

############## PROCESS OF CREATING MASTER DATASET FOR ANALYSIS COMMENTED OUT BELOW ########################
# Initialize the NHANESDataAPI object
nhanes_api = NHANESDataAPI()

# List available data categories
data_categories = nhanes_api.list_data_categories()
print("Data Categories:", data_categories)

# List available cycle years
cycle_years = nhanes_api.list_cycle_years()
print("Cycle Years:", cycle_years)

print("########## DEMOGRAPHIC DATA #########")

#list file names
file_names_demo = nhanes_api.list_file_names('demographics', '2017-2018')
print("Unique Demographic Data File Descriptions:", file_names_demo)

#retrieve data
demo = nhanes_api.retrieve_data('demographics', '2017-2018', 'Demographic Variables & Sample Weights')
print(demo)

print("######### DIETARY DATA ############")
file_names_diet = nhanes_api.list_file_names('dietary', '2017-2018')
print("Unique Dietary Data File Descriptions:", file_names_diet)

#retrieve data
dietary = nhanes_api.retrieve_data('dietary', '2017-2018', 'Dietary Interview - Total Nutrient Intakes, First Day')
print(dietary)

print("######### EXAMINATION DATA ###########")
file_names_exam = nhanes_api.list_file_names('examination', '2017-2018')
print("Unique Examination Data File Descriptions:", file_names_exam)

#retrieve data
body_measure = nhanes_api.retrieve_data('examination', '2017-2018', 'Body Measures')
print(body_measure)

print("######## SELF-REPORT CVD DATA #########")
file_names_quest = nhanes_api.list_file_names('questionnaire', '2017-2018')
print("Unique Questionnaire Data File Descriptions:", file_names_quest)

#retrieve data
CVD = nhanes_api.retrieve_data('questionnaire', '2017-2018', 'Medical Conditions')
CVD.drop('year', axis=1, inplace=True) #drop year to avoid error with merge
print(CVD)

print("######## FOOD SECURITY DATA ###########")
#retrieve data
food_security = nhanes_api.retrieve_data('questionnaire', '2017-2018', 'Food Security')
food_security.drop('year', axis=1, inplace=True) #drop year to avoid error with merge
print(food_security)

print("####### JOIN DATASETS BY SEQN ##########")
# apply inner join
demo_diet = pd.merge(demo, dietary, left_on='SEQN',right_on='SEQN', how='inner')
pd.set_option('display.max_columns', None) #show all columns
print(demo_diet)
# apply second inner join
demo_diet_body_measure = pd.merge(demo_diet, body_measure, left_on='SEQN',right_on='SEQN', how='inner')
print(demo_diet_body_measure)
#apply third inner join
demo_diet_body_measure_cvd = pd.merge(demo_diet_body_measure, CVD, left_on='SEQN',right_on='SEQN', how='inner')
print(demo_diet_body_measure_cvd)
#n=338 in demo, diet, and body measure dataset but not in CVD dataset - drop these observations as CVD is our primary outcome
#apply fourth inner join
demo_diet_body_measure_cvd_fs = pd.merge(demo_diet_body_measure_cvd, food_security, left_on='SEQN',right_on='SEQN', how='inner')
print(demo_diet_body_measure_cvd_fs)
#
print("################### EXPORT MASTER DATASET TO CSV #####################")
demo_diet_body_measure_cvd_fs.to_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Project\\master_NHANES.csv", index=False, encoding='latin-1')

print("################## IMPORT MASTER DATASET TO CSV ######################")
master = pd.read_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Project\\master_NHANES.csv",encoding='latin-1')
print(master.head())
print(master.shape)
print(master.dtypes)

print("#### DEMOGRAPHIC DESCRIPTIVE STATS #######")
print(master['RIDAGEYR'].agg(['min','median', 'mean','max']))
print(master['RIDAGEYR'].quantile([0.25, 0.75]))
#drop those less tha 18yr old
master_adult = master[master["RIDAGEYR"] >= 18]
print(master_adult['RIDAGEYR'].agg(['min','median', 'mean','max']))
print(master_adult['RIDAGEYR'].quantile([0.25, 0.75]))
print(master_adult)
#master_adult.to_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Project\\master_NHANES_adult.csv", index=False, encoding='latin-1')


############## PROCESS OF DATA CLEANING / RECODING / IMPUTATION PRIOR TO ANALYSIS COMMENTED OUT BELOW ######################## 
print("################## IMPORT MASTER ADULT DATASET CSV ######################")
#master_adult = pd.read_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Project\\master_NHANES_adult.csv",encoding='latin-1')
print(master_adult.head())
print(master_adult.shape)
print(master_adult.dtypes)

print("################ DEMOGRAPHIC DESCRIPTIVE STATS #############")
# Age
print(master_adult['RIDAGEYR'].agg(['min','median', 'mean', 'std', 'max']))
print(master_adult['RIDAGEYR'].quantile([0.25, 0.75]))

# Sex
print(master_adult.stb.freq(['RIAGENDR']))

# Race -- use RIDRETH1 does not capture non-hispanic Asian
## in ridreth1 other race (value 5) has n=1,081, with the lowest sample size of n=519 for Other hispanic race
## in ridreth3 other race (value 7) has n=288, with the lowest sample size, try both but need to choose 1 for model selection process
print(master_adult.stb.freq(['RIDRETH1']))
print(master_adult.stb.freq(['RIDRETH3']))
#print(master_adult.stb.freq(['RIDRETH1']))

# Education
## DMDEDUC3 - education level yr 0 - 19
print(master_adult.stb.freq(['DMDEDUC3']))
### 0 = never attend, 1 - 12 = highschool no diploma, 13 = hs grad, 14=GED or equiv, 15 = more than hs, 66=less than 9th grade
### recode 0 - 12, 66 to less than highschool, 13 & 14 = highschool graduate/GED, 15 = some college/associate degree
## DMDEDUC2 - education level yr 20+
#print(master_adult.stb.freq(['DMDEDUC2']))
### need to recode to less than highschool (1 or 2), highchool graduate/GED (3), some college/associate degree (4), college grad (5)
### impute n=2 that refused (7) and n=10 that did not know to most frequent response (some college/associate degree)

## create new education var based on DMDEDUC2 for those 20+
def educ_recode(val):
    if val==1.0:
        return 0
    elif val==2.0:
        return 0
    elif val==3.0:
        return 1
    elif val==4.0:
        return 2
    elif val==5.0:
        return 3
    elif val==7.0:
        return 2
    elif val==9.0:
        return 2
master_adult['edu_cat'] = master_adult['DMDEDUC2'].map(educ_recode)
print(master_adult.stb.freq(['edu_cat']))

def educ_recode_b(val):
    if val < 13.0:
        return 0
    elif val==13.0:
        return 1
    elif val==14.0:
        return 1
    elif val==15.0:
        return 2
    elif val==66.0:
        return 0
master_adult['edu_cat_b'] = master_adult['DMDEDUC3'].map(educ_recode_b)
print(master_adult.stb.freq(['edu_cat_b']))

def educ_recode_final(val_a, val_b, age):
    if age < 20:
        return val_a
    if age >= 20:
        return val_b
master_adult['edu_cat'] = master_adult['edu_cat'].fillna(master_adult['edu_cat_b'])
print(master_adult.stb.freq(['edu_cat']))

# Poverty to income ratio
print(master_adult['INDFMPIR'].agg(['min','median', 'mean', 'std', 'max']))
print(master_adult['INDFMPIR'].quantile([0.25, 0.75]))
## bin INDFMPIR -- Poverty to income ratio (PIR) will be collapsed to <= 1.30, 1.31-1.85, 1.86-3.5, and >3.5 as done in Jun et al. (2021)
# A PIR <= 1.30 indicates potential eligibility for SNAP
#create bins
bins = [0, 1.30, 1.85, 3.5001, np.inf]

# create labels for each bin
group = ['=< 1.30', '1.31-1.85', '1.86-3.5', '>3.5']

# convert PIR values to categories
master_adult['PIR_cat'] = pd.cut(master_adult['INDFMPIR'], bins=bins, labels=group)
PIR_cat_res = master_adult.groupby("PIR_cat")[["INDFMPIR"]].agg(["min", "max"])
print(PIR_cat_res)
print(master_adult.stb.freq(['PIR_cat']))
#process worked correctly

# VARIABLES FOR DESCRIPTIVE STATS = biological sex/assumed gender(RIAGENDR), Age in years(RIDAGEYR), Race (most likley will use RIDRETH1, but try also RIDRETH3 with expanded categories),
# education level (edu_cat), poverty to income ratio category (PIR_cat)

#### DIETARY DESCRIPTIVE STATS ######
#total kcal = DR1TKCAL
#total fiber (g) = DR1TFIBE
print(master_adult['DR1TKCAL'].agg(['min','median', 'mean', 'std', 'max']))
print(master_adult['DR1TKCAL'].quantile([0.25, 0.75]))

print(master_adult['DR1TFIBE'].agg(['min','median', 'mean', 'std', 'max']))
print(master_adult['DR1TFIBE'].quantile([0.25, 0.75]))

master_adult['Fiber_1k_kcal'] = (master_adult['DR1TFIBE'] / master_adult['DR1TKCAL']) * 1000
print(master_adult['Fiber_1k_kcal'].agg(['min','median', 'mean', 'std', 'max']))
print(master_adult['Fiber_1k_kcal'].quantile([0.25, 0.75]))

#create bins
bins = [0, 13.9999, np.inf]

# create labels for each bin
group = ['< 14.0', '>= 14.0']

# convert fiber (g) per 1,000kcal values (Fiber_1k_kcal) to >= 14g/1000kcal category
master_adult['fiber_cat'] = pd.cut(master_adult['Fiber_1k_kcal'], bins=bins, labels=group)
Fiber_cat_res = master_adult.groupby("fiber_cat")[["Fiber_1k_kcal"]].agg(["min", "max"])
print(Fiber_cat_res)
print(master_adult.stb.freq(['fiber_cat']))

#### EXAM DESCRIPTIVE STATS ######
# BMI = BMXBMI
print(master_adult['BMXBMI'].agg(['min','median', 'mean', 'std', 'max']))
print(master_adult['BMXBMI'].quantile([0.25, 0.75]))

#create bins
bins = [0, 29.9999, np.inf]

# create labels for each bin
group = ['< 30.0', '>= 30.0']

# convert BMI values (BMXBMI) to >= 30 kg/m2 category
master_adult['obese'] = pd.cut(master_adult['BMXBMI'], bins=bins, labels=group)
obese_res = master_adult.groupby("obese")[["BMXBMI"]].agg(["min", "max"])
print(obese_res)
print(master_adult.stb.freq(['obese']))

#### CVD DESCRIPTIVE STATS #######
# CVD = 1 if yes to MCQ160B (CHF), MCQ160C (CHD), MCQ160D (Angina), MCQ160E (Heart attack), MCQ160F (Stroke)
# 1 = yes, 2 = no, 9 = don't know
print(master_adult.stb.freq(['MCQ160B']))
print(master_adult.stb.freq(['MCQ160C']))
print(master_adult.stb.freq(['MCQ160D']))
print(master_adult.stb.freq(['MCQ160E']))
print(master_adult.stb.freq(['MCQ160F']))

#create CVD variable
master_adult.loc[(master_adult['MCQ160B'] == 1.0) | (master_adult['MCQ160C'] == 1.0) | (master_adult['MCQ160D'] == 1.0) | (master_adult['MCQ160E'] == 1.0) |
(master_adult['MCQ160F'] == 1.0),'CVD'] = 1.0
print(master_adult.stb.freq(['CVD']))
# fill those that did not have a response of "Yes" on any of the conditions to indicate CVD to 0.0 = No
master_adult['CVD'] = master_adult['CVD'].fillna(0.0)
print(master_adult.stb.freq(['CVD']))
# imputed those with missing CVD responses w/ mode = No CVD

#### FOOD SECURITY DESCRIPTIVE STATS #######
# FS Category = FSDAD, 1=High food security, 2=Marginal food security, 3=Low food security, 4=very low food security
print(master_adult.stb.freq(['FSDAD']))
master_adult.loc[(master_adult['FSDAD'] == 3.0) | (master_adult['FSDAD'] == 4.0),'Low_food_security'] = 1.0
print(master_adult.stb.freq(['Low_food_security']))
master_adult['Low_food_security'] = master_adult['Low_food_security'].fillna(0.0)
print(master_adult.stb.freq(['Low_food_security']))
#imputed those missing food security w/ mode = High or marginal food security

#### SUBSET DATASET TO VARIABLES OF INTEREST ########
master_final = master_adult[['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH1', 'RIDRETH3', 'edu_cat', 'INDFMPIR', 'PIR_cat', 'Fiber_1k_kcal', 'fiber_cat', 'BMXBMI', 'obese', 'CVD', 'FSDAD', 'Low_food_security']]
print(master_final.dtypes)
print(master_final.shape)

#### COUNT MISSING DATA FOR VARIABLES OF INTEREST #######
# Count total NaN at each column in a DataFrame
print(" \nCount total NaN at each column in a DataFrame : \n\n",
      master_final.isnull().sum())

#### IMPUTE CATEGORICAL VARIABLES WITH MODE & CONTINUOUS VAR (AGE) W/ MEDIAN ####
# CITATION THAT USED SAME APPROACH WITH CATEGORICAL VARIABLES WITH NHANES DATA -
("""Martin-Morales A, Yamamoto M, Inoue M, Vu T, Dawadi R, Araki M. Predicting Cardiovascular Disease Mortality: 
 Leveraging Machine Learning for Comprehensive Assessment of Health and Nutrition Variables. Nutrients. 2023 Sep 11;15(18):3937. 
doi: 10.3390/nu15183937. PMID: 37764721; PMCID: PMC10534618.""")
# food security category and CVD already imputed using mode
#columns that need imputation = PIR_cat (impute to >3.5), fiber_cat (impute to < 14.0 g/1000kcal), and obese (impute to < 30.0)
print(master_final.stb.freq(['PIR_cat']))
master_final['PIR_cat'] = master_final['PIR_cat'].fillna(master_final['PIR_cat'].mode()[0])
print(master_final.stb.freq(['PIR_cat']))
#imputation done correctly
print(master_final.stb.freq(['fiber_cat']))
master_final['fiber_cat'] = master_final['fiber_cat'].fillna(master_final['fiber_cat'].mode()[0])
print(master_final.stb.freq(['fiber_cat']))
#imputation done correctly
print(master_final.stb.freq(['obese']))
master_final['obese'] = master_final['obese'].fillna(master_final['obese'].mode()[0])
print(master_final.stb.freq(['obese']))

##### EXPORT FINAL DATASET FOR ANALYSIS FOR QUICKER IMPORT MOVING FORWARD #############
#master_final.to_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Project\\master_NHANES_adult_final_analysis.csv", index=False, encoding='latin-1')


##### IMPORT FINAL DATASET FOR ANALYSIS ############
#master_final = pd.read_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Project\\master_NHANES_adult_final_analysis.csv",encoding='latin-1')
print(master_final.dtypes)
print(master_final.shape)
print(" \nCount total NaN at each column in a DataFrame : \n\n",
      master_final.isnull().sum())

# DESCRIPTIVE STATS FOR FINAL VARIABLES
master_final.drop(["SEQN", "RIDRETH3", "INDFMPIR", "Fiber_1k_kcal", "BMXBMI", "FSDAD" ], axis = 1, inplace = True)
print(master_final['RIDAGEYR'].agg(['min','median', 'mean', 'std', 'max']))
print(master_final['RIDAGEYR'].quantile([0.25, 0.75]))

print(master_final.stb.freq(['RIAGENDR']))
print(master_final.stb.freq(['RIDRETH1']))
print(master_final.stb.freq(['edu_cat']))
print(master_final.stb.freq(['PIR_cat']))
print(master_final.stb.freq(['fiber_cat']))
print(master_final.stb.freq(['obese']))
print(master_final.stb.freq(['CVD']))
print(master_final.stb.freq(['Low_food_security']))
# n= 647 outcomes - 8 predictors

#CROSS-TAB ANALYSIS - GENERATE ROW % AND COUNT BY CVD STATUS
#generate row %
print(pd.crosstab(master_final.RIAGENDR, master_final.CVD, normalize='index')) #normalize = 'all' gives total %, normalize = 'columns' gives column %
#genderate counts (n)
print(pd.crosstab(master_final.RIAGENDR, master_final.CVD))
print(pd.crosstab(master_final.RIDRETH1, master_final.CVD, normalize='index'))
print(pd.crosstab(master_final.RIDRETH1, master_final.CVD))
print(pd.crosstab(master_final.edu_cat, master_final.CVD, normalize='index'))
print(pd.crosstab(master_final.edu_cat, master_final.CVD))
print(pd.crosstab(master_final.PIR_cat, master_final.CVD, normalize='index'))
print(pd.crosstab(master_final.PIR_cat, master_final.CVD))
print(pd.crosstab(master_final.fiber_cat, master_final.CVD, normalize='index'))
print(pd.crosstab(master_final.fiber_cat, master_final.CVD))
print(pd.crosstab(master_final.obese, master_final.CVD, normalize='index'))
print(pd.crosstab(master_final.obese, master_final.CVD))
print(pd.crosstab(master_final.Low_food_security, master_final.CVD, normalize='index'))
print(pd.crosstab(master_final.Low_food_security, master_final.CVD))

#CROSS-TAB ANALYSIS - GENERATE MEAN (SD) BY CVD STATUS
AGE_BY_CVD = master_final.groupby("CVD")[["RIDAGEYR"]].agg(["mean", "std"])
print(AGE_BY_CVD)

print("############# UNADJUSTED ANALYSIS TO GET AN IDEA IF PREDICTORS ARE A GOOD FIT ##############")

#CHI-SQUARE ANALYSIS (CATEGORICAL VARIABLES)
print("## GENDER CHI-SQUARE RESULTS ##")
gender_cross = pd.crosstab(master_final['RIAGENDR'], master_final['CVD'])
print(stats.chi2_contingency(gender_cross)) # SIGNIFICANT
print("## RACE CHI-SQUARE RESULTS ##")
race_cross = pd.crosstab(master_final['RIDRETH1'], master_final['CVD'])
print(stats.chi2_contingency(race_cross)) # SIGNIFICANT
print("## EDUCATION CHI-SQUARE RESULTS ##")
education_cross = pd.crosstab(master_final['edu_cat'], master_final['CVD'])
print(stats.chi2_contingency(education_cross)) #SIGNIFICANT
print("## PIR CHI-SQUARE RESULTS ##")
PIR_cross = pd.crosstab(master_final['PIR_cat'], master_final['CVD'])
print(stats.chi2_contingency(PIR_cross)) # SIGNIFICANT
print("## FIBER CHI-SQUARE RESULTS ##")
Fiber_cross = pd.crosstab(master_final['fiber_cat'], master_final['CVD'])
print(stats.chi2_contingency(Fiber_cross)) # not statistically significant
print("## OBESITY CHI-SQUARE RESULTS ##")
Obese_cross = pd.crosstab(master_final['obese'], master_final['CVD'])
print(stats.chi2_contingency(Obese_cross)) # SIGNIFICANT
print("## FOOD SECURITY CHI-SQUARE RESULTS ##")
FS_cross = pd.crosstab(master_final['Low_food_security'], master_final['CVD'])
print(stats.chi2_contingency(FS_cross)) #SIGNIFICANT

## T-TEST FOR AGE - CVD
summary, results = rp.ttest(group1= master_final['RIDAGEYR'][master_final['CVD'] == 0.0], group1_name= "No CVD",
         group2= master_final['RIDAGEYR'][master_final['CVD'] == 1.0], group2_name= "CVD")
print(summary)
print(results)
#significant results

print("############ DATA VISUALIZATION OF RESULTS ############")

################################################################# VISUALIZATIONS FOR EACH PREDICTOR IN RELATION TO CVD #####################
#### CIRCLE BACK TO THIS SECTION AFTER ANALYSIS IS DONE ####
## Categorical data first example ##
data_gen = {
    'Gender': ['Male', 'Female'],
    'CVD Prevalence': [14.2, 9.4]
}
df_gen = pd.DataFrame(data_gen)
sns.barplot(x='Gender', y='CVD Prevalence', data=df_gen)
plt.ylim(0, 20)
plt.title('CVD Prevalence by Gender', size = 18)
plt.xlabel('Gender')
plt.ylabel('CVD Prevalence (%)')
plt.subplots_adjust(bottom=0.2) # this increases the spacing on the bottom
plt.show()

## Continuous data (Age) ##
data_age = {
    'CVD': ['No CVD', 'CVD'],
    'Age': [47.6, 66.6]
}
df_age = pd.DataFrame(data_age)
sns.barplot(x='CVD', y='Age', data=df_age)
plt.ylim(0, 80)
plt.title('Mean Age by Self Report CVD', size = 18)
plt.xlabel('Self Report CVD')
plt.ylabel('Mean Age (years)')
plt.subplots_adjust(bottom=0.2) # this increases the spacing on the bottom
plt.show()

data_race = {
    'Race': ['Mexican American', 'Other Hispanic', 'Non-Hispanic White', 'Non-Hispanic Black', 'Other Race - Including Multiracial'],
    'CVD Prevalence': [6.9, 8.3, 16.8, 11.8, 7.6]
}
df_race = pd.DataFrame(data_race)
sns.barplot(y='Race', x='CVD Prevalence', data=df_race, palette="tab10")
plt.xlim(0, 20)
plt.title('CVD Prevalence by Race', size = 18)
plt.xlabel('CVD Prevalence (%)')
plt.ylabel('Race')
plt.subplots_adjust(left=0.5) # this increases the spacing on the bottom
plt.show()

data_ed = {
    'Education': ['Less than High school', 'High school/GED', 'Some college/Associate degree', 'College graduate'],
    'CVD Prevalence': [15.2, 12.4, 11.6, 7.9]
}
df_ed = pd.DataFrame(data_ed)
sns.barplot(y='Education', x='CVD Prevalence', data=df_ed, palette="tab10")
plt.xlim(0, 20)
plt.title('CVD Prevalence by Education Level', size = 12)
plt.xlabel('CVD Prevalence (%)')
plt.ylabel('Highest Education Attained')
plt.subplots_adjust(left=0.4) # this increases the spacing on the bottom
plt.show()

data_pir = {
    'PIR Cat': ['=< 1.30', '1.31 - 1.85', '1.86 - 3.50', '> 3.50'],
    'CVD Prevalence': [13.5, 16.4, 11.1, 9.2]
}
df_pir = pd.DataFrame(data_pir)
sns.barplot(y='CVD Prevalence', x='PIR Cat', data=df_pir)
plt.ylim(0, 20)
plt.title('CVD Prevalence by Poverty to Income Ratio', size = 12)
plt.ylabel('CVD Prevalence (%)')
plt.xlabel('Poverty to Income Ratio Category')
plt.subplots_adjust(bottom=0.2) # this increases the spacing on the bottom
plt.show()

data_fiber = {
    'Fiber': ['< 14.0', '>= 14.0'],
    'CVD Prevalence': [11.8, 10.5]
}
df_fiber = pd.DataFrame(data_fiber)
sns.barplot(y='CVD Prevalence', x='Fiber', data=df_fiber)
plt.ylim(0, 15)
plt.title('CVD Prevalence by Daily Fiber Intake', size = 12)
plt.ylabel('CVD Prevalence (%)')
plt.xlabel('Daily Fiber Intake (g/1000kcal)')
plt.subplots_adjust(bottom=0.2) # this increases the spacing on the bottom
plt.show()

data_obese = {
    'Obese': ['Not Obese (< 30 kg/m2)', 'Obese (>= 30 kg/m2)'],
    'CVD Prevalence': [10.6, 13.3]
}
df_obese = pd.DataFrame(data_obese)
sns.barplot(y='CVD Prevalence', x='Obese', data=df_obese)
plt.ylim(0, 15)
plt.title('CVD Prevalence by Obesity Status', size = 12)
plt.ylabel('CVD Prevalence (%)')
plt.xlabel('Obese (Y/N)')
plt.subplots_adjust(bottom=0.2) # this increases the spacing on the bottom
plt.show()

data_fs = {
    'FS': ['Low of very low', 'High or marginal'],
    'CVD Prevalence': [15.7, 10.6]
}
df_fs = pd.DataFrame(data_fs)
sns.barplot(y='CVD Prevalence', x='FS', data=df_fs)
plt.ylim(0, 20)
plt.title('CVD Prevalence by Food Security Status', size = 12)
plt.ylabel('CVD Prevalence (%)')
plt.xlabel('Food Security Status')
plt.subplots_adjust(bottom=0.2) # this increases the spacing on the bottom
plt.show()


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')


if __name__ == '__main__':
    # creating data on which bar chart will be plot
    x = ['Low of very low', 'High or marginal']
    y = [15.7, 10.6]

    # setting the y-limit
    plt.ylim(0, 20)

    # making the bar chart on the data
    plt.bar(x, y)

    # calling the function to add value labels
    addlabels(x, y)

    # giving title to the plot
    plt.title("CVD Prevalence by Food Security Status", size = 12)

    # giving X and Y labels
    plt.ylabel('CVD Prevalence (%)')
    plt.xlabel('Food Security Status')

    # visualizing the plot
    plt.show()

print("############ LOGISTIC REGRESSION ANALYSIS #############")
print("\n ### USING STATSMODELS ##\n")
# ANALYSIS USING STATSMODELS -- https://www.andrewvillazon.com/logistic-regression-python-statsmodels/
# Define and fit model
log_reg = smf.logit("CVD ~ RIDAGEYR + C(RIAGENDR, Treatment(reference=2.0)) + C(RIDRETH1, Treatment(reference=3.0)) + C(edu_cat, Treatment(reference=3.0)) + C(PIR_cat, Treatment(reference='>3.5')) + C(fiber_cat, Treatment(reference='>= 14.0')) + obese + Low_food_security", data=master_final).fit()
# Summary of results
print(log_reg.summary())

odds_ratios = pd.DataFrame(
    {
        "OR": log_reg.params,
        "Lower CI": log_reg.conf_int()[0],
        "Upper CI": log_reg.conf_int()[1],
    }
)
odds_ratios = np.exp(odds_ratios)

print(odds_ratios)
#odds_ratios.to_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Project\\odds_ratios.csv", index=False, encoding='latin-1')

print("\n ### USING SKLEARN ##\n")
# ANALYSIS USING SKLEARN -- https://www.statology.org/logistic-regression-python/
# create proper dummy variables prior to logit modeling
master_final.loc[(master_final['RIAGENDR'] == 2.0),'RIAGENDR'] = 0.0
print("\n######### CREATE DUMMY VARIABLES FOR ANALYSIS ##########\n")
df_dummies = pd.get_dummies(master_final, columns=['RIDRETH1', 'edu_cat', 'PIR_cat', 'fiber_cat', 'obese'])
print(df_dummies.dtypes)
print("\n######### DATASET AFTER DROPPING DUMMIES NOT NEEDED (REFERENCE GROUPS) ##########\n")
df_dummies.drop(["RIDRETH1_3.0"], axis = 1, inplace = True)
df_dummies.drop(["edu_cat_3.0"], axis = 1, inplace = True)
df_dummies.drop(["PIR_cat_>3.5"], axis = 1, inplace = True)
df_dummies.drop(["fiber_cat_>= 14.0"], axis = 1, inplace = True)
df_dummies.drop(["obese_< 30.0"], axis = 1, inplace = True)
print(df_dummies.dtypes)

print(df_dummies.stb.freq(['RIAGENDR']))
print(master_final.stb.freq(['RIDRETH1']))
print(df_dummies.stb.freq(['RIDRETH1_1.0']))
print(df_dummies.stb.freq(['RIDRETH1_2.0']))
print(df_dummies.stb.freq(['RIDRETH1_4.0']))
print(df_dummies.stb.freq(['RIDRETH1_5.0']))
print(master_final.stb.freq(['edu_cat']))
print(df_dummies.stb.freq(['edu_cat_0.0']))
print(df_dummies.stb.freq(['edu_cat_1.0']))
print(df_dummies.stb.freq(['edu_cat_2.0']))
print(master_final.stb.freq(['PIR_cat']))
print(df_dummies.stb.freq(['PIR_cat_1.31-1.85']))
print(df_dummies.stb.freq(['PIR_cat_1.86-3.5']))
print(df_dummies.stb.freq(['PIR_cat_=< 1.30']))
print(master_final.stb.freq(['fiber_cat']))
print(df_dummies.stb.freq(['fiber_cat_< 14.0']))
print(master_final.stb.freq(['obese']))
print(df_dummies.stb.freq(['obese_>= 30.0']))
print(df_dummies.stb.freq(['CVD']))
print(df_dummies.stb.freq(['Low_food_security']))

X = df_dummies[['RIAGENDR', 'RIDAGEYR', 'RIDRETH1_1.0', 'RIDRETH1_2.0', 'RIDRETH1_4.0', 'RIDRETH1_5.0', 'edu_cat_0.0', 'edu_cat_1.0', 'edu_cat_2.0', 'PIR_cat_1.31-1.85', 'PIR_cat_1.86-3.5', 'PIR_cat_=< 1.30', 'fiber_cat_< 14.0', 'obese_>= 30.0', 'Low_food_security']]
y = df_dummies['CVD']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.5,random_state=0)
#df_dummies.to_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Project\\master_NHANES_adult_final_analysis_w_dummies.csv", index=False, encoding='latin-1')

#instantiate the model
log_regression = LogisticRegression()

#fit the model using the training data
log_regression.fit(X_train,y_train)

#use model to make predictions on test data
y_pred = log_regression.predict(X_test)

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)

#Confusion matrix results
 #[[2393   22]
 #[ 330   22]]

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#Accuracy: 0.873
# (2393 + 22) = 2415 correct, 22 + 330 = 352 incorrect,
# 2415 / (2415 + 352) = 2415 / 2767 = 0.873

#define metrics
y_pred_proba = log_regression.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)

#create ROC curve
plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.legend(loc=4)
plt.title('ROC Curve of Model', size = 18)
plt.plot([0, 1], [0, 1],'g--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.subplots_adjust(bottom=0.2) # this increases the spacing on the bottom
plt.show()
# AUC = 0.816