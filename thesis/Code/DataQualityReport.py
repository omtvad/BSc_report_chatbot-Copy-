def get_quality_report(dataframe):
    report = pandas.DataFrame()

    report['Data Type'] = dataframe.dtypes
    report['Missing Values'] = dataframe.isnull().sum()
    report['Present Values'] = dataframe.count()
    report['Missing Value Ratio'] = report['Missing Values'] / dataframe.index.size
    report['Unique Values'] = dataframe.apply(lambda x: len(x.unique()))
    report['Min'] = dataframe.min()
    report['Max'] = dataframe.max()
    report['Mean'] = dataframe.mean()
    report['Median'] = dataframe.median()
    report['Std dev'] = dataframe.std()
    report['Var'] = dataframe.var()
    report['25%'] = dataframe.quantile(q=0.25)
    report['50%'] = dataframe.quantile(q=0.5)
    report['75%'] = dataframe.quantile(q=0.75)

    return report