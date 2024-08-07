import pandas as pd
from datetime import datetime

def process_SOH(SOH_file_path):
    columns_to_select = ('GroupBy1', 'textbox6', 'textbox19')
    df = pd.read_csv(SOH_file_path, usecols=columns_to_select)

    df = df.query('textbox131 in ["INS", "DRG", "PSC","SPY", "VOX"]')

    current_date = datetime.now().strftime('%Y-%m-%d')
    df['CurrentDate'] = current_date
    df['keterangan'] = 'SOH'
    df = df.rename(columns={
        'GroupBy1': 'Store',
        'textbox162': 'ItemCode',
        'textbox12': 'Qty',
        'textbox168': 'Date'
    })    
    return df
path_SOH = r'D:\IDam\try\update SOH, SALES, PO & TO OPEN 31\inv-hos-laststock(21).csv'
df_SOH = process_SOH(path_SOH)
df_SOH.head()

def process_PO_TO(TO_file_path):
    columns_to_select = ('GroupBy2', 'textbox162', 'textbox12', 'textbox168')
    df = pd.read_csv(TO_file_path, usecols=columns_to_select)
    df['keterangan'] = 'TO / PO Open'
    df = df.rename(columns={
        'GroupBy2': 'Store',
        'textbox162': 'ItemCode',
        'textbox12': 'Qty',
        'textbox168': 'Date'
    })
    return df

path_TO = r'D:\IDam\try\update SOH, SALES, PO & TO OPEN 31\inv-hos-tovsti-det(13) (1).csv'
df_TO = process_PO_TO(path_TO)


path_PO = r'D:\IDam\try\update SOH, SALES, PO & TO OPEN 31\inv-hos-povsgr-det(11).csv'
df_PO = process_PO_TO(path_PO)

def process_Sales(Sales_file_path):
    columns_to_select = ('GroupBy1', 'textbox5', 'txtPrice', 'txtStock')
    df = pd.read_csv(Sales_file_path, usecols=columns_to_select)
    df['keterangan'] = 'Sales'
    df = df.rename(columns={
        'GroupBy1': 'Store',
        'textbox5': 'ItemCode',
        'txtPrice': 'Date',
        'txtStock': 'Qty'
    })

    return df
path_sales = r'D:\IDam\try\update SOH, SALES, PO & TO OPEN 31\sal-hos-det-lv2(13) (1).csv'
df_sales = process_Sales(path_sales)

#print(df_PO.head())
print(df_sales.head())