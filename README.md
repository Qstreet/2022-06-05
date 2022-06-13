# 2022-06-05
RealPython Data Cleaning

Data sets here: 
https://github.com/realpython/python-data-cleaning

`# %%`
interactive Jupyter kernel to right
SHIFT + ENTER or CTRL + ENTER runs

`^SPACE` 
brings up intelliSense
also info on method

User Settings - Settings that apply globally to any instance of VS Code you open.
Workspace Settings - Settings stored inside your workspace and only apply when the workspace is opened.

type 'code .' in any folder to start editing files in that folder.

## `.assign()`
`data.assign(day= lambda df: df.loc[:,"day"] > 9 )` # T or F if > 9

##  drop columns
```
.drop(
    columns=[
        "col1",
        "date",
        "univ"
    ]
)
```

# How To Select Rows From Pandas DataFrame Based on Column Values
### Exploring how to select rows based on conditions in pandas DataFrames

`import numpy as np`
```
df = pd.DataFrame(
 [
  (73, 15, 55, 33, 'foo'),
  (63, 64, 11, 11, 'bar'),
  (56, 72, 57, 55, 'foo'),
 ],
 columns=['A', 'B', 'C', 'D', 'E'],
)
```
`print(df)`

```
#     A   B   C   D    E
# 0  73  15  55  33  foo
# 1  63  64  11  11  bar
# 2  56  72  57  55  foo
```

### Select rows whose column value is equal to a scalar or string

`(df.loc[df['B'] == 64])`
```
    A   B   C   D    E
1  63  64  11  11  bar
```

### omit loc and provide the boolean condition when indexing the pandas df:
`(df[df['B'] == 64])`
```
    A   B   C   D    E
1  63  64  11  11  bar
```

### instead of df['B'] you can also ref col B using df.B
`(df[df.B == 64])`

### Python, may name such boolean conditions as mask that we then pass to DataFrame when indexing it.

`(mask = df.B == 64)`

`(df[mask])`
```
    A   B   C   D    E
1  63  64  11  11  bar
```
### Select rows whose column value is not equal to a scalar

`(df.loc[df['B'] != 64])`
```
    A   B   C   D    E
0  73  15  55  33  foo
2  56  72  57  55  foo
```

### Select rows show column value is greater or less than a scalar

`(df.loc[df['B'] >= 64])`

```
    A   B   C   D    E
1  63  64  11  11  bar
2  56  72  57  55  foo
```

### Select rows whose column value contains a string
### to filter a DataFrame so that you only keep rows containing a specific (sub)string in a particular column.

`(df.loc[df['E'].str.contains('oo')])`

```
    A   B   C   D    E
0  73  15  55  33  foo
2  56  72  57  55  foo
```

### Select rows whose column value is in an iterable
### to select only those rows whose values in a specific column are included in a list.

`(df.loc[df['B'].isin([64, 15])])`
```
    A   B   C   D    E
0  73  15  55  33  foo
1  63  64  11  11  bar
```

### Select rows whose column value is not in an iterable
### to select rows whose value is not in an iterable (e.g. a list), then you can simply use the negation character ~ :

`(df.loc[~df['B'].isin([64, 15])])`
```
    A   B   C   D    E
2  56  72  57  55  foo
```
### Multiple Conditions
### to combine multiple conditions together when selecting rows from a pandas DataFrame.
### make use of the & operator

`(df.loc[(df['A'] >= 59) & (df['E'].isin(['foo', 'boo']))])`

```
    A   B   C   D    E
0  73  15  55  33  foo
```
#
# How to Count NaN Values of a Pandas DataFrame Column
```
import pandas as pd 

df = pd.DataFrame(
    [
        (1, 100, None, 'A'),
        (2, None, True, 'B'),
        (3, 150, None, None), 
        (4, 100, None, 'B'),
        (5, None, False, 'B'),
        (6, 120, False, 'A'),
        (7, 45, True, 'C'),
    ], 
    columns=['colA', 'colB', 'colC', 'colD']
)
print(df)
   colA   colB   colC  colD
0     1  100.0   None     A
1     2    NaN   True     B
2     3  150.0   None  None
3     4  100.0   None     B
4     5    NaN  False     B
5     6  120.0  False     A
6     7   45.0   True     C
```

Count the NaN values in a specific column

## To count the number of rows containing NaN values in a specific column, you can use pandas.Series.isna

`(df['colB'].isna().sum())`
2

`(df['colA'].isna().sum())`
0

`(df['colB'].isnull().sum())`
2

## Count NaN values for each individual column
To get the count of missing values for each individual column, you can use the pandas.DataFrame.isna() method followed by sum(). The output will be a Series object containing the counts for each column in the original DataFrame:

`(df.isna().sum())`
```
colA    0
colB    2
colC    3
colD    1
dtype: int64
```

## Count NaN values in a subset of columns
If you want the counts for just a subset of the columns within the original DataFrame, you can perform the same operation as the one we used in the previous section, but this time slicing the DataFrame:

`(df[['colA', 'colD']].isna().sum())`
```
colA    0
colD    1
dtype: int64
```

## Count rows having only NaN values in the specified columns
To count the number of rows that have missing values in all columns specified you can use the notation below. For example, to count how many rows have missing values in both colC and colD:

`(df[['colC', 'colD']].isna().all(axis=1).sum())` 1

## Count rows containing only NaN values in every column
To count the number of rows containing only missing values in every column across the whole DataFrame, you can use the expression shown below. Note that in our example DataFrame, no such row exists and thus the output will be 0.

`(df.isnull().all(axis=1).sum())`
0

## Count the NaN values within the whole DataFrame
To count how many missing values the whole DataFrame contains across every single column, you can use the following expression:

`(df.isna().sum().sum())`
6

#
# DATA CLEANING
#
```
import pandas as pd
import numpy as np
olympics = pd.read_csv("olympics.csv")
olympics.head()
```

## Finding the right header
```
olympics = pd.read_csv("olympics.csv", header=1)
olympics.head()
```

## Renaming the columns
```
col_names = {'Unnamed: 0': 'Country',
               '? Summer': 'Summer Olympics',
               '01 !': 'Gold',
               '02 !': 'Silver',
               '03 !': 'Bronze',
               '? Winter': 'Winter Olympics',
               '01 !.1': 'Gold.1',
               '02 !.1': 'Silver.1',
               '03 !.1': 'Bronze.1',
               '? Games': '# Games',
               '01 !.2': 'Gold.2',
               '02 !.2': 'Silver.2',
               '03 !.2': 'Bronze.2'}
olympics.rename(columns=col_names, inplace=True)
```

## Getting rid of extra tails in the texts
The ‘applymap’ function takes a function that should be applied on the column or columns we intend to perform the changes. Here we define the function that will take a string as a parameter and remove everything after it finds the first bracket ‘(‘.
```
def get_country(st):
    if ' (' in st:
        return st[:st.find(' (')]  # string start : char before (
    else:
        return st
```

Use this function as a parameter in the ‘applymap’ function.
`pd.DataFrame(olympics['Country']).applymap(get_country)`


## Dealing with the null values
To deal with null values. One way is to drop all the null values using this code that deletes all the rows with any null values:
`df.dropna()`
The problem is, in this way you may be left with only a few rows of data.

Or fill up all the null values with zeros like this:
`df.fillna(0)`
This will fill up all the null values with zeros.

The null values can also be filled with the value immediately before that:
`df.fillna(method = "bfill")`

Or you can fill the null values with the value exactly after that:
`df.fillna(method="ffill")`

Or I fill the null values with the median. It is also common to fill up the null values with mean or standard normal values. We loop through the columns and fill the null values of all the columns using their median.
```
for i in df.columns:
    df[i].fillna(df[i].median(), inplace=True)
```
 
## Removing the duplicate data

Get rid of duplicate rows
```
people = people.drop_duplicates(subset="Name")  # if the Name col has the same data
```

## Getting four-digit year data
The ‘Year’ column has values not a 4 digit year
### regex
`year_ex = people["Year"].str.extract(r'^(\d{4})',expand=False)`
```
year_ex
Output:
0    1980
1    1978
2    1982
3    1992
4    1987
Name: Year, dtype: object
```

## Evaluating the income in plain numeric values w string values that contain ‘K’, ‘M’
### 'K’, and ‘M’ needs to be replaced by three zeros and six zeros:
```
people["Income"].replace({"K": "*1e3", "M": "*1e6"}, regex=True).map(pd.eval).astype(int)
Output:
0     2000000
1       40000
2      120000
3    10000000
4     6000000
Name: Income, dtype: int32
```

In the edu column, the words Harvard, Stanford or Oxford comes with some extra words or characters. To use this data in analysis, two Harvard data will be considered as 2 different data. So, we need to get rid of those extra characters and only have exactly the same strings for the same university.

First, make three boolean variables for three different Universities.
```
edu = people["Education"]
harvard = edu.str.contains("Harvard")
stanford = edu.str.contains("Stanford")
oxford = edu.str.contains("Oxford")
```

Now, we will use ‘Harvard’ if the string contains “Harvard” use “Stanford” where the string contains “Stanford” and so on with nested np.where() functions.
```
people["Education"] = np.where(harvard, "Harvard",
                              np.where(stanford, "Stanford",
                                      np.where(oxford, "Oxford", people["Education"])))
Output:
0     Harvard
1      Oxford
2      Oxford
3    Stanford
4     Harvard
Name: Education, dtype: object
```

## Converting the time series data to DateTime format
To analyze the time or date data in pandas, it is useful to have ‘datetime’ format.
```
pd.to_datetime(people['Graduation'])
Output:
0   2020-03-12
1   2020-04-14
2   2020-08-01
3   2020-05-18
4   2021-05-10
Name: Graduation, dtype: datetime64[ns]
```

Mmake all the strings lower case. That way ‘Low’ and ‘low’ will not be different.

`people["Standing"] = people["Standing"].str.lower()`

Get rid of all the numbers and other characters using a simple regular expression:
```
people["Standing"].map(lambda x: re.sub('([^a-z]+)', '', x))
Output:
0       medium
1          low
2    excellant
3          low
4    excellant
Name: Standing, dtype: object
```
