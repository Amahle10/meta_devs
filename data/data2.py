import pandas as pd
# Open as Excel object
xls = pd.ExcelFile('C:/Users/julia/OneDrive/Documents/python assignment/2016 data -EU values.xlsx')
# Get sheet names
sheets_1 = xls.sheet_names

# Dictionary of SheetNames:dfOfSheets
sheet_to_df_map = {}
for sheet_name in xls.sheet_names:
    sheet_to_df_map[sheet_name] = xls.parse(sheet_name)

# create list to store results
resultM1 = []
# Loop over keys and df in dictionary
for key, df in sheet_to_df_map.items():
    # remove top 5 blank rows
    df = df = df.iloc[5:]
    # set column names as first row values
    headers = df.iloc[0]
    df  = pd.DataFrame(df.values[1:], columns=headers)
    #loop over rows in the df and create pd series to store Malta results
    results  =df.loc[df['Country'] == "Malta", 'AirPollutionLevel']
    # Loop over the results for Malta from each sheet and append 'Malta' and then append the value to a list
    for i in results:
        resultM1.append(key)
        resultM1.append(i)

# Convert list to df
df = pd.DataFrame(resultM1) 
# Rename column
df = df.rename({0: 'Sheet'}, axis=1)  
# create two columns
final = pd.DataFrame({'Sheet':df['Sheet'].iloc[::2].values, 'Value':df['Sheet'].iloc[1::2].values})