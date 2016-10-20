####Import the packages we need and set the global variables####
import csv
from bs4 import BeautifulSoup
import Image
from PIL import Image
from PIL import ImageDraw
import ImageFont
import svgwrite
import svgutils.transform as st
import string
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from PySide.QtSvg import *
from PySide.QtGui import *
import os
import pylab
import shutil

# Map colors (http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=6)
colors={}
colors["GDP percapita"]=['#e31a1c', '#1f78b4', '#33a02c', '#b2df8a', '#fb9a99', '#a6cee3', '#ffff99', '#CCCCCC']
colors["Unemployment Rate"]= ['#800026', '#e31a1c', '#fc4e2a', '#fd8d3c', '#fed976', '#ffeda0', '#ffffcc', '#CCCCCC']
colors["Population"]= ['#000000', '#081d58', '#225ea8', '#1d91c0', '#41b6c4', '#c7e9b4', '#ffffd9', '#CCCCCC']
colors["Government Net Debt"]=['#67000d', '#cb181d', '#fb6a4a', '#fcbba1', '#fee0d2', '#e5f5e0', '#a1d99b', '#41ab5d', '#006d2c', '#00441b', '#CCCCCC']
threshold={}
threshold["GDP percapita"]=[30000,20000,10000,5000,3000,1000,0,"No data"]
threshold["Unemployment Rate"]=[15,13,10,7.5,5.5,4.5,0,"No data"]
threshold["Population"]=[1000,200,100,75,50,25,0,"No data"]
threshold["Government Net Debt"]=[100,87.5,75,62.5,50,37.5,25,12.5,0,-700,"No data"]

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

####Build 2 methods for 2 inputs: indicator and year####
def input1():
    column = data_dictionary()
    indicator_list = ["GDP percapita", "Unemployment Rate", "Population", "Government Net Debt"]
    print "Indicators: " + str(indicator_list)
    while True:
        input1 = raw_input("Please enter an indicator you want to show on the world map: ")
        if input1 in column.keys():
            break
    return input1
def input2():
    column = data_dictionary()
    year = column['Year']
    while True:
        input2 = raw_input("Please enter a year(2006~2015): ")
        if input2 in year:
            break
    return input2
input1=input1()
input2=input2()

####Edit the world map and save it to .txt format####
def worldmap():
    column = data_dictionary()
    countrycode = column["Country Code"]
    year = column['Year']
    count=[]
    for x in range(len(year)):
        if input2==year[x]:
            count.append(x)
    list = []
    for y in range(len(count)):
        if str(column[str(input1)][count[y]])!='n/a':
            list.append(float(column[str(input1)][count[y]]))
        else:
            list.append(float(-1000))
    my_xticks = countrycode[count[0]:count[len(count) -1]+1]
    indicator = {}
    for x in range(len(my_xticks)):
        try:
            country_id = my_xticks[x]
            index_value=list[x]
            indicator[country_id] = float(index_value)
        except:
            pass
    country=indicator.keys()
    # Load the SVG map
    svg = open('worldmap.svg', 'r').read()
    # Load into Beautiful Soup
    soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])

    if input1=="GDP percapita":
        # Find countries
        paths = soup.findAll('path')
        #  Build the path style
        path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
        # Color the counties based on GDP percapita
        country_list=[]
        for p in paths:
            country_list.append(p['id'])
            if p['id'] in country:
                threshold=indicator[p['id']]
                if threshold > 30000:
                    color_class = 0
                elif threshold > 20000:
                    color_class = 1
                elif threshold > 10000:
                    color_class = 2
                elif threshold > 5000:
                    color_class = 3
                elif threshold > 3000:
                    color_class = 4
                elif threshold > 1000:
                    color_class = 5
                elif threshold > 0:
                    color_class = 6
                else:
                    color_class = 7
                color = colors["GDP percapita"][color_class]
                p['style'] = path_style + color
    elif input1=="Unemployment Rate":
        paths = soup.findAll('path')
        path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
        # Color the counties based on Unemployment Rate
        country_list = []
        for p in paths:
            country_list.append(p['id'])
            if p['id'] in country:
                threshold = indicator[p['id']]
                if threshold > 15:
                    color_class = 0
                elif threshold > 13:
                    color_class = 1
                elif threshold > 10:
                    color_class = 2
                elif threshold > 7.5:
                    color_class = 3
                elif threshold > 5.5:
                    color_class = 4
                elif threshold > 4.5:
                    color_class = 5
                elif threshold > 0:
                    color_class = 6
                else:
                    color_class = 7
                color = colors["Unemployment Rate"][color_class]
                p['style'] = path_style + color
    elif input1=="Population":
        paths = soup.findAll('path')
        path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
        # Color the counties based on Population
        country_list = []
        for p in paths:
            country_list.append(p['id'])
            if p['id'] in country:
                threshold = indicator[p['id']]
                if threshold > 1000:
                    color_class = 0
                elif threshold > 200:
                    color_class = 1
                elif threshold > 100:
                    color_class = 2
                elif threshold > 75:
                    color_class = 3
                elif threshold > 50:
                    color_class = 4
                elif threshold > 25:
                    color_class = 5
                elif threshold > 0:
                    color_class = 6
                else:
                    color_class = 7
                color = colors["Population"][color_class]
                p['style'] = path_style + color
    elif input1=="Government Net Debt":
        paths = soup.findAll('path')
        path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
        # Color the counties based on Government Net Debt
        country_list = []
        for p in paths:
            country_list.append(p['id'])
            if p['id'] in country:
                threshold = indicator[p['id']]
                if threshold > 100:
                    color_class = 0
                elif threshold > 87.5:
                    color_class = 1
                elif threshold > 75:
                    color_class = 2
                elif threshold > 62.5:
                    color_class = 3
                elif threshold > 50:
                    color_class = 4
                elif threshold > 37.5:
                    color_class = 5
                elif threshold > 25:
                    color_class = 6
                elif threshold > 12.5:
                    color_class = 7
                elif threshold > 0:
                    color_class = 8
                elif threshold > -700:
                    color_class = 9
                else:
                    color_class = 10
                color = colors["Government Net Debt"][color_class]
                p['style'] = path_style + color
    # Save the map format in .txt file
    file_index_txt = open('%s_%s.txt' % (input1, input2), 'w')
    file_index_txt.write(soup.prettify().encode('UTF-8'))
    #If wanting to generate an output as a svg file, you need to do some tricks as follow:
    #file_index_svg = open('%s_%s.svg' % (input1, input2), 'w')
    #file_index_svg.write(soup.prettify().encode('UTF-8'))
    # add text in line3 after <svg baseprofile="tiny" height="599px" viewbox="0 0 1360 599" width="1360px" x="0px" y="0px"

worldmap()

####Convert .txt file to .jpg image####
def convert2jpg():
    #Revise the text file, in order to delete the <html>, <body>,</html>, and </body> in order for the QSvgRenderer to read only the text between<svg>to </svg>
    f = open('%s_%s.txt' % (input1, input2), 'r+')
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i.strip() != "<html>" and i.strip() != "<body>" and i.strip() != "</html>" and i.strip() != "</body>":
            f.write(i)
    f.truncate()
    f.close()
    #Open 2 empty image files: jpg and png, whcih can be edited
    pic_png = open("%s_%s.png" % (input1, input2), 'w')
    pic_jpg = open("%s_%s.jpg" % (input1, input2), 'w')
    #Put in the revise text file in QSvgRenderer function from PySide
    r = QSvgRenderer('%s_%s.txt' % (input1, input2))
    #Set the format of the image and save it as a png file
    height = r.defaultSize().height() * 950 / r.defaultSize().width()
    i = QImage(950, height, QImage.Format_ARGB32)
    p = QPainter(i)
    r.render(p)
    i.save("%s_%s.png" % (input1, input2))
    p.end()
    #Reopen the png image
    im = Image.open("%s_%s.png" % (input1, input2))
    # Open a new image, which is the same size as the png image we just saved
    # And set the new image background color: white
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bg.paste(im, im)
    #We past our png image onto the new image and save it as a jpg file.
    bg.save("%s_%s.jpg" % (input1, input2))
    pic_jpg.close()
    pic_png.close()
    #Delete the png file which we're not going to use anymore
    os.remove("%s_%s.png" % (input1, input2))
convert2jpg()

####Build the legend.jpg image####
def legend():
    fig = plt.figure()
    ax  = fig.add_subplot(111)
    ax.set_axis_off()  #turn off the axis
    rate_patch = []
    for k in range(len(colors[input1])):
        if threshold[input1][k]!="No data":
            rate_patch.append(mpatches.Patch(color=colors[input1][k], label='>%s' %threshold[input1][k]))
        else:
            rate_patch.append(mpatches.Patch(color=colors[input1][k], label='No data'))
    ax.legend(handles=rate_patch[0:],loc="lower right")
    fig.savefig('legend.png')
    # create legend as an image
    img = Image.open("legend.png")
    width = img.size[0]
    height = img.size[1]
    # .crop((left, top, right, bottom)
    img2 = img.crop(
        (
            width - 300,
            height - 420, #up
            width - 80,
            height - 30 #down
        )
    )
    # Instruction of image processing (https://yungyuc.github.io/oldtech/python/python_imaging.html)
    img2.save("legendsize.jpg")
    # paste image onto the map
    til = Image.open(("%s_%s.jpg" % (input1, input2)))  # 950x620
    im = Image.open("legendsize.jpg")  # 170x200
    width = 120
    ratio = float(width) / im.size[0]
    height = int(im.size[1] * ratio)
    nim = im.resize((width, height), Image.BILINEAR)
    til.paste(nim, (20, 400))
    til.save("legend.png")

legend()

####Complete the map: add a title and mix 3 elements (world map, legend, title)####
def completemap():
    # Add title
    newfile = Image.new("RGB", (1030, 700), color="#000000")
    newfile.save("world_%s_%s.jpg"% (input1, input2))
    image = Image.open("legend.png")
    newfile.paste(image, (40, 60))
    newfile.save("world_%s_%s.jpg"% (input1, input2))
    font = ImageFont.truetype(".../font/arial.ttf", 30)
    unit={"GDP percapita":"U.S.dollars","Unemployment Rate":"%","Population":"Millions","Government Net Debt":"%GDP"}
    title = "World %s in %s (%s)" %(input1, input2,unit[input1])
    w, h = font.getsize(title)
    draw = ImageDraw.Draw(newfile)
    draw.text(((1030 - w) / 2, 10), title, color="white", font=font)
    newfile.save("world_%s_%s.jpg"% (input1, input2))
    # Create a new folder, and save the result into the folder
    newpath = r'./result'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    shutil.move("world_%s_%s.jpg" % (input1, input2), "result/world_%s_%s.jpg" % (input1, input2))
    shutil.move('%s_%s.txt' % (input1, input2), "result/%s_%s.txt" % (input1, input2))
    # remove the image that we don't need anymore
    os.remove("legendsize.jpg")
    os.remove("legend.png")
    os.remove("%s_%s.jpg" % (input1, input2))
completemap()
