import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)

# 1
df = pd.read_csv('medical_examination.csv')
print(df.info())
print(df.head())

# 2
imc = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = np.where(imc > 25, 1, 0)

# 3
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
print(df.head())

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars = ['cardio'],
        value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
        # var_name 'variable' by default
        # value_name 'value' by default
    )

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name = 'total')
    

    # 7
    graphic = sns.catplot(
        data = df_cat,
        x = 'variable',
        y = 'total',
        hue = 'value',
        col = 'cardio',
        kind = 'bar'
    )

    # 8
    fig = graphic.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        ((df['ap_lo'] <= df['ap_hi'])) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))

        ]


    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype = bool))

    # 14
    fig, ax = plt.subplots(figsize = (12, 12))

    # 15
    sns.heatmap(
        corr,
        mask = mask,
        annot = True,
        fmt = ".1f",
        center = 0,
        square = True,
        linewidths = .5,
        cbar_kws = {"shrink": .5},
        ax = ax
    )
    
    # 16
    fig.savefig('heatmap.png')
    return fig