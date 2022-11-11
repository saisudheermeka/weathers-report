import matplotlib.pyplot as plt
import pandas as pd

def convert(arr):
    """This function converts oject data type to float data type"""
    l = []
    for i in arr:
        l.append(float(i))
    return l

def linePlot(report):
     """Line plot generator function"""
    date = weather_report[0][1:]
    temp = convert(weather_report[3][1:])
    plt.figure(figsize=(20,10))
    plt.title("Variations in Temperature in the month of October",size="30")
    plt.xlabel("Date",size="30")
    plt.ylabel("Temperature",size="30")
    plt.plot(date,temp,c="r",marker=".",mfc="b",mec="b",lw=3,ms="15")  
    plt.show()
    plt.close()


def barPlot(report):
    """Bar plot generator function"""
    plt.figure(figsize=(20, 10))
    date = weather_report[0][1:]
    windspeed = convert(weather_report[6][1:])
    plt.bar(date,windspeed,width=0.3)
    plt.title("Wind Speed over a month",size="30")
    plt.xlabel("Date",size="30")
    plt.ylabel("Wind Speed",size="30")
    plt.show()
    plt.close()

def scatterPlot(report):
    """Scatter plot generator function"""
    humidity = convert(weather_report[5][1:])
    temp = convert(weather_report[3][1:])
    plt.figure(figsize=(15, 10))
    plt.scatter(temp,humidity,c="b",s=50)
    plt.xlim([8,20])
    plt.title("Temperature vs Humidity",size="30")
    plt.xlabel("Temperature",size="30")
    plt.ylabel("Humidity",size="30")
    plt.show()
    plt.close()

def piechart(report):
    """Pie Chart generator function"""
    temp = convert(weather_report[3][1:])
    cold = 0
    moderate = 0
    hot = 0
    for i in temp:
        if i<11:
            cold+=1
        if i>=11 and i<15:
            moderate += 1
        if i>=15:
            hot += 1
    weatherCondition = ["Cold("+str(cold)+")","Moderate("+str(moderate)+")","Hot("+str(hot)+")"]
    arr = [cold,moderate,hot]
    plt.pie(arr,labels=weatherCondition,colors=["blue","green","orange"])
    plt.title("Weather Condition in New York in October",size="30")
    plt.show()

#Weather report data extraction
weather_report = pd.read_csv("Weather data.csv",header = None)

#Graphs generation using the data
linePlot(weather_report)
barPlot(weather_report)
scatterPlot(weather_report)
piechart(weather_report)
