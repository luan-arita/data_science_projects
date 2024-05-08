import pandas as pd

df = pd.read_excel('default_of_credit_card_clients__courseware_version_1_21_19.xls')

#counts returns a count of unique values in ID column
id_counts = df['ID'].value_counts()
#head returns the first five rows by default
#print(id_counts.head())

#dupe mask has the IDs and a boolean value stating if they're duplicates or not
dupe_mask = id_counts == 2

dupe_ids = id_counts.index[dupe_mask]
dupe_ids = list(dupe_ids)
#print(dupe_ids)
print(len(dupe_ids))

#print(df.loc[df['ID'].isin(dupe_ids[0:3]), :])

#dataframe containing boolean values.
#basically, this holds the table with replacing cells with zeroes with boolean values
df_zero_mask = df == 0

#this is a boolean series that identifies every row where all elements starting from the second column are 0.
feature_zero_mask = df_zero_mask.iloc[:, 1:].all(axis = 1)
print(sum(feature_zero_mask))

df_clean_1 = df.loc[~feature_zero_mask, :].copy()

print(df_clean_1['ID'].nunique())

df_clean_1.to_csv('./df_clean_1.csv', index=False)