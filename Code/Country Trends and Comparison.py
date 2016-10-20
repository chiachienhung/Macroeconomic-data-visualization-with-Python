import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
import shutil
import os
from datetime import datetime

# Read all the needed data files.
data1 = pd.read_csv("GDP.csv")
data2 = pd.read_csv("CPI.csv")
data3 = pd.read_csv("Net_debt.csv")
data4 = pd.read_csv("population.csv")
data5 = pd.read_csv("employment.csv")
data6 = pd.read_csv("unemployment_rate.csv")

def country_trend():
    # Let the user input the name of the country.
    input_country = raw_input("Please enter a country you want to know about:")

    # Give out the list of data type.
    print "-" * 25
    print "Data Type list:"
    print "1. GDP\n2. CPI\n3. Net_debt\n4. population\n5. employment\n6. unemployment_rate\n"
    input_type = raw_input("Please choose a type of trend you want to know from the list:")
    print "-" * 25

    # The function gives out the particular trend of one country.
    def single_trend(data):
        # Show the first 10 rows of the chosen data type
        print "The first 10 rows of data in the database"
        print data[['DATE', input_country]][:10]

        # Create a figure
        fig = plt.figure()

        # Create a subplot
        ax = fig.add_subplot(1, 1, 1)

        # Get the data to be drawn
        px = data[input_country]

        # Set the plot style
        px.plot(ax=ax, style='k-')

        # Set the title of the figure
        title = str(input_type + " of " + input_country)
        ax.set_title(title)

        # Set x-label for the figure
        ax.set_xlabel('Date')

        # Set y-label for the figure
        ax.set_ylabel(input_type)

        ax.set_xticklabels(range(1980, 2016, 4), rotation=30, fontsize='small')

        # Judge the data type and decide the corresponding file name for the figure
        if input_type == "GDP":
            save_name = str(input_country + " GDP.png")
        elif input_type == "CPI":
            save_name = str(input_country + " CPI.png")
        elif input_type == "Net_debt":
            save_name = str(input_country + " Net_debt.png")
        elif input_type == "population":
            save_name = str(input_country + " Population.png")
        elif input_type == "employment":
            save_name = str(input_country + " Employment.png")
        elif input_type == "unemployment_rate":
            save_name = str(input_country + " Unemployment_rate.png")

        # Save the figure to the right place, in the wanted style
        plt.savefig(save_name, dpi=400, bbox_inches='tight')

        # Open result folder if it's not exist  AND move the result to result folder
        newpath = r'./result'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        shutil.move('%s %s.png' % (input_country, input_type), "result/%s %s.png" % (input_country, input_type))
        # Show and close the figure
        plt.show()
        plt.close()

    # This function judges the input data type and returns different figure result.
    def judge(input_type):

        if input_type == "GDP":
            data = data1
            single_trend(data)
        elif input_type == "CPI":
            data = data2
            single_trend(data)
        elif input_type == "Net_debt":
            data = data3
            single_trend(data)
        elif input_type == "population":
            data = data4
            single_trend(data)
        elif input_type == "employment":
            data = data5
            single_trend(data)
        elif input_type == "unemployment_rate":
            data = data6
            single_trend(data)

    judge(input_type)

#Call the country_trend function
country_trend()


# This function returns a figure comparing several countries' situations chosen by the user
def comparison():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    # Get the chosen type of data
    print "-"*25
    print "Data Type list:"
    print "1. GDP\n2. CPI\n3. Net_debt\n4. population\n5. employment\n6. unemployment_rate\n"
    print "-"*25

    chosen_type = raw_input("Please enter the type of data you want to compare:")

    if chosen_type == "GDP":
        data = data1
    elif chosen_type == "CPI":
        data = data2
    elif chosen_type == "Net_debt":
        data = data3
    elif chosen_type == "population":
        data = data4
    elif chosen_type == "employment":
        data = data5
    elif chosen_type == "unemployment_rate":
        data = data6
    else:
        chosen_type = raw_input("Sorry, but the type you put in is not in our database, please re-enter a type.")

    # Get the chosen countries
    chosen_countries = raw_input("Please enter several countries you want to compare, split by ','/like 'China,United States'. Please do not input blanks, Upper case counts!:")

    # split the string user inputs
    chosen = chosen_countries.split(",")

    # Create a list for the maximum and minimum numbers of each country's data
    y_maxes = []
    y_mins = []

    # Print the chosen countries' situations and get the upper limit and lower limit for the figure
    for country in chosen:
        print "Last ten years'",chosen_type,"of",country
        print "*" * 25
        print data[['DATE', country]][-10:]
        print "*" * 25

        # put the maximum and minimum of each country's data into the original list
        y_maxes.append(max(data[country]))
        y_mins.append(min(data[country]))

        # Draw each country's line
        ax.plot(data[country], 'o-', label = country)

    # Get the maximum among all the country's max and decide the upper limit
    max_y = str(max(y_maxes))
    len_max = 0
    for num in max_y:
        if num.isdigit() is True:
            len_max += 1
        else:
            break
    upp_lim = (int(max_y[0])+1) * 10 ** (len_max - 1)

    # Get the minimum among all the country's min and decide the lower limit
    min_y = str(min(y_mins))
    len_min = 0
    for num in min_y:
        if num.isdigit() is True:
            len_min += 1
        else:
            break
    low_lim = int(max_y[0]) * 10 ** (len_min - 1)

    # Set the title of the figure
    ax.set_title('Country Comparison')

    # Set the y label of the figure
    ax.set_ylabel(chosen_type)

    # Set the x label of the figure
    ax.set_xlabel('DATE')

    # Set the x tick labels as every year
    ax.set_xticklabels(range(1980, 2016, 4), rotation = 30, fontsize = 'small')

    # Set the y limits with low_lim and upp_lim we get before
    ax.set_ylim(low_lim, upp_lim)

    # Put the legend at the best place
    plt.legend(loc = 'best')

    # Judge the data type and decide the corresponding file name for the figure
    if chosen_type == "GDP":
        save_name = "result\GDP Comparison.jpg"
    elif chosen_type == "CPI":
        save_name = "result\CPI Comparison.jpg"
    elif chosen_type == "Net_debt":
        save_name = "result\Net Debt Comparison.jpg"
    elif chosen_type == "population":
        save_name = "result\Population Comparison.jpg"
    elif chosen_type == "employment":
        save_name = "result\Employment Comparison.jpg"
    elif chosen_type == "unemployment_rate":
        save_name = "result\Unemployment Rate Comparison.jpg"

    plt.show()
    plt.savefig(save_name)

comparison()
