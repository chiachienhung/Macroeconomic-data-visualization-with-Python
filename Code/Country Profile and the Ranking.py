####Input and display our data file####
import csv
from scipy.stats import rankdata
import pandas as pd
#Set the format for displaying the table of our data file
pd.set_option('display.height', 2000)
pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)

f = pd.read_csv('worlddata.csv', dtype=str)
#print f.head(190)[f.columns[1:2]]

####Build our dataset dictionary####
def data_dictionary():
    reader = csv.reader(open('worlddata.csv'), delimiter=",")
    #skip header and convert data to map
    headers = reader.next()
    column = {}
    for h in headers:
        column[h] = []
    for row in reader:
        for h, v in zip(headers, row):
            column[h].append(v)
    return column
print sorted(data_dictionary().keys())

####Build a continent catigorized dictionary####
def countrymap():
    column = data_dictionary()
    country = column['Country by IMC'][0:190]
    continent=column["Continent"][0:190]
    print ("All the countries: ")
    for x in range(len(country)):
        print (str(x+1) + ". " + str(country[x]))
    sixcontinent=list(set(continent))
    #continent_map is a dictionary categorizing the coutries into six continents
    continent_map={}
    for k in sixcontinent:
        continent_map[k]=[]
    for s in range(len(continent)):
        for k in sixcontinent:
            if continent[s]==k:
                continent_map[k].append(country[s])
    print continent_map
    print "Total countries: %s" % len(country)
    return continent_map

####Build a ranking method####
def ranking(input_country, input_year, dataset):
    column=data_dictionary()
    country = column['Country by IMC']
    year = column['Year']
    #dataset=column[str(dataset)]
    count = []
    for x in range(len(year)):
        if input_year == year[x]:
            count.append(x)
    list = []
    for y in range(len(count)):
        if str(dataset[count[y]]) != 'n/a':
            list.append(float(dataset[count[y]]))
        else:
            list.append(float(-1000))
    country_list = country[count[0]:count[len(count)-1]+1]
    rank=len(list)+1-rankdata(list,method='max').astype(int)
    for x in range(len(count)):
        if input_country == country_list[x]:
            return rank[x]

####Build a country profile class####
class countryprofile(object):
    __country_classes = countrymap()
    def __init__(self, country, capital, continent, area, rank_area, year, gdppercapita, rank_gdppercapita, unemploymentrate, rank_unemploymentrate, population, rank_population, debt, rank_debt):
        """
            This class instance is created by country, capital, continent, area, rank_area, year, gdppercapita, rank_gdppercapita, unemploymentrate, rank_unemploymentrate, population, rank_population, debt, rank_debt.
            :param country:  name of the country
            :type country: str
            :param capital: capital of the country
            :type capital:  str
            :param continent:: continent of the country
            :type continent: str
            :param area: geographical area of the country
            :type area: int
            :param rank_area: rank of the geographical area among the country
            :type rank_area: int
            :param year: year of the macroeconomics data
            :type year: str
            :param gdppercapita: gdp per capita of the country
            :type gdppercapita: float
            :param rank_gdppercapita: rank of the gdp per capita among the country
            :type rank_gdppercapita: int
            :param unemploymentrate: unemployment rate of the country
            :type unemploymentrate: float
            :param rank_unemploymentrate: rank of the unemploymentrate among the country
            :type rank_unemploymentrate: int
            :param population: population of the country
            :type population: int
            :param rank_population: rank of the population among the country
            :type rank_population: int
            :param debt: government debt per GDP of the country
            :type debt: float
            :param rank_debt: rank of the government debt per GDP among the country
            :type rank_debt: int
            """
        self.__country=country
        self.__capital=capital
        self.__continent = continent
        self.__area = area
        self.__rank_area=rank_area
        self.__year = year
        self.__gdppercapita=gdppercapita
        self.__rank_gdppercapita = rank_gdppercapita
        self.__unemploymentrate=unemploymentrate
        self.__rank_unemploymentrate = rank_unemploymentrate
        self.__population=population
        self.__rank_population = rank_population
        self.__debt=debt
        self.__rank_debt = rank_debt

    '''
    Implement the getter methods
    '''

    @property
    def country(self):
        return self.__country

    @property
    def capital(self):
        return self.__capital

    @property
    def continent(self):
        return self.__continent

    @property
    def area(self):
        return self.__area

    @property
    def rank_area(self):
        return self.__rank_area

    @property
    def year(self):
        return self.__year

    @property
    def gdppercapita(self):
        return self.__gdppercapita

    @property
    def rank_gdppercapita(self):
        return self.__rank_gdppercapita

    @property
    def unemploymentrate(self):
        return self.__unemploymentrate

    @property
    def rank_unemploymentrate(self):
        return self.__rank_unemploymentrate

    @property
    def population(self):
        return self.__population

    @property
    def rank_population(self):
        return self.__rank_population

    @property
    def debt(self):
        return self.__debt

    @property
    def rank_debt(self):
        return self.__rank_debt

    '''
    Implement the setter methods
    '''

    @country.setter
    def country(self, name):
        self.__country = name

    @capital.setter
    def capital(self, name):
        self.__capital = name

    @continent.setter
    def continent(self, name):
        self.__continent = name

    @area.setter
    def area(self, value):
        self.__area = value

    @rank_area.setter
    def rank_area(self, value):
        self.__rank_area = value

    @year.setter
    def year(self, name):
        self.__year=name

    @gdppercapita.setter
    def gdppercapita(self, value):
        self.__gdppercapita = value

    @rank_gdppercapita.setter
    def rank_gdppercapita(self, value):
        self.__rank_gdppercapita = value

    @unemploymentrate.setter
    def unemploymentrate(self, value):
        self.__unemploymentrate = value

    @rank_unemploymentrate.setter
    def rank_unemploymentrate(self, value):
        self.__rank_unemploymentrate = value

    @population.setter
    def population(self, value):
        self.__population = value

    @rank_population.setter
    def rank_population(self, value):
        self.__rank_population = value

    @debt.setter
    def debt(self, value):
        self.__debt = value

    @rank_debt.setter
    def rank_debt(self, value):
        self.__rank_debt = value

    '''
        Implement the deleter methods
        '''

    @country.deleter
    def country(self):
        self.__country = ""

    @capital.deleter
    def capital(self):
        self.__capital = ""

    @continent.deleter
    def continent(self):
        self.__continent = ""

    @area.deleter
    def area(self):
        self.__area = 0

    @rank_area.deleter
    def rank_area(self):
        self.__rank_area = 0

    @year.deleter
    def year(self):
        self.__year = ""

    @gdppercapita.deleter
    def gdppercapita(self):
        self.__gdppercapita = 0

    @rank_gdppercapita.deleter
    def rank_gdppercapita(self):
        self.__rank_gdppercapita = 0

    @unemploymentrate.deleter
    def unemploymentrate(self):
        self.__unemploymentrate = 0

    @rank_unemploymentrate.deleter
    def rank_unemploymentrate(self):
        self.__rank_unemploymentrate = 0

    @population.deleter
    def population(self):
        self.__population = 0

    @rank_population.deleter
    def rank_population(self):
        self.__rank_population = 0

    @debt.deleter
    def debt(self):
        self.__debt = 0

    @rank_debt.deleter
    def rank_debt(self):
        self.__rank_debt = 0


    def __str__(self):
        """
        This function overwrites the built-in __str__ function to give a nice string representation of the class content
        :return: string representation of the class content
        :rtype: str
        """
        return 'Country: {0}\nCapital: {1}\nContinent: {2}\nArea: {3} km2  ({4}/190)\nYear: {5}\nGDP per capita: {6} U.S.dollars  ({7}/190)\nUnemployment Rate: {8}%  ({9}/190)\nPopulation: {10} Millions  ({11}/190)\nGovernment Debt: {12} %GDP ({13}/190)'.format(
            str(self.country),
            str(self.capital),
            str(self.continent),
            str(self.area),
            str(self.rank_area),
            str(self.year),
            str(self.gdppercapita),
            str(self.rank_gdppercapita),
            str(self.unemploymentrate),
            str(self.rank_unemploymentrate),
            str(self.population),
            str(self.rank_population),
            str(self.debt),
            str(self.rank_debt))

####Display the country profile and the ranking among the countries####
if __name__ == "__main__":
    column = data_dictionary()
    country = column['Country by IMC']
    capital = column['Capital']
    continent=column['Continent']
    area = column['Area']
    year = column['Year']
    gdppercapita = column['GDP percapita']
    unemploymentrate = column["Unemployment Rate"]
    population = column["Population"]
    debt = column["Government Net Debt"]
    while True:
        input1 = raw_input("Please enter a country(Uppercase matters!): ")
        if input1 in country:
            break
    while True:
        input2 = raw_input("Please enter a year(2006~2015): ")
        if input2 in year:
            break
    for x in range(len(year)):
        if input2 == year[x]:
            if input1 == country[x]:
                information = countryprofile(country[x], capital[x], continent[x], area[x], ranking(input1,input2,area), year[x],gdppercapita[x], ranking(input1,input2,gdppercapita), unemploymentrate[x], ranking(input1,input2,unemploymentrate),population[x], ranking(input1,input2,population),debt[x], ranking(input1,input2,debt))
                print information