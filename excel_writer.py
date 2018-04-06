from pandas import ExcelWriter


def save_xls(list_dfs, xls_path):
    writer = ExcelWriter(xls_path)
    for n, df in enumerate(list_dfs):
        df.to_excel(writer, 'sheet%s' % n)
    writer.save()


list_dfs = ['''list of dataframe''']

xls_path = '../data/XP_Distribution.xlsx'
save_xls(list_dfs, xls_path)
