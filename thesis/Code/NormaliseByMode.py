def normalise_by_mode(df):

    # Create a copy of the entered dataframe, to avoid reference to same object problems.
    norm_df = df.copy()

    # Iterates through each mode, and calculates the retrieves the mean and std dev for each column
    for i in range(6):
        mean = (df.loc[df['Operational Mode']==i]).mean()
        std = (df.loc[df['Operational Mode'] == i]).std()

        # Iterates through every column, and normalises the value based on operational mode
        for feature_name in df.columns[0:-1]:
            norm_df[feature_name].loc[norm_df['Operational Mode']==i] = \
                (df[feature_name].loc[df['Operational Mode']==i] - 
                 mean[feature_name])/(std[feature_name])

    # Ensures that a std deviation of 0 does not corrupt the entire dataset. Fill NaN values with 0.
    norm_df = norm_df.fillna(0)

    return norm_df