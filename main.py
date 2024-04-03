import pandas as pd

# create dataframes from the CSV files
df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')

# set display options
# pd.set_option('display.max_columns', 84)
# pd.set_option('display.max_rows', 20)

# check the shape of the dataframe 
df.shape

# check the columns present
df.columns

# select a specific row with iloc (integer location)
first_row = df.iloc[0]
multiple_rows = df.iloc[[1, 2, 3]]

# using iloc, select specific rows and columns (by index)
specific_rows_and_columns = df.iloc[[0, 2, 4], [2, 5]]

# select multiple specific columns from the file 
two_columns_data = df[['ResponseId', 'MainBranch']]

# slice the data shown 
two_columns_data[:10]

# select specific rows and columns by label
labeled_rows = df.loc[[1, 2, 3, 4], 'SurveyEase']

# get all data from "CodingActivities" column
activities_column = df['CodingActivities']

# get unique values and count of a column
activities_column.value_counts()