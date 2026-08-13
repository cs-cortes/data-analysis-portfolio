import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    #plt.clf()
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], 
                color = 'lightblue',
                s = 25,
                alpha = 0.6,
                edgecolors = 'royalblue',
                label = 'Historical Data'
                )

    # Create first line of best fit
    regression1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    m1 = regression1.slope
    b1 = regression1.intercept

    projected_year1 = np.arange(df['Year'].min(), 2051)
    predicted_sea_level1 = m1 * projected_year1 + b1
    plt.plot(projected_year1, predicted_sea_level1, 
             color = 'darkorange',
             linewidth = 1.5, 
             label = '1880-2050 fit'

             )
    # plt.legend()
 
    # Create second line of best fit
    df_re = df[df['Year'] >= 2000]
    regression2 = linregress(df_re['Year'], df_re['CSIRO Adjusted Sea Level'])
    m2 = regression2.slope
    b2 = regression2.intercept

    projected_year2 = np.arange(2000, 2051)
    predicted_sea_level2 = m2 * projected_year2 + b2
    plt.plot(projected_year2, predicted_sea_level2, 
             color = 'limegreen', 
             linewidth = 1.5,
             label = '2000-2050 fit')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))

    plt.legend(
        by_label.values(),         
        by_label.keys(),
        fontsize = '10',
        facecolor = '#f5f5dc',
        edgecolor = 'gray',
        framealpha=0.85
    )

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
