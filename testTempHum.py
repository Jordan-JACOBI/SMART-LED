from TempHum import *

def main():
    tempHumValue = TempHum()
    while True:
        (x,y)=tempHumValue.getValue()
        print("Temperature: " + format(x,'.2f')+" C" +'\n' +"Humidite: " +format (y,'.2f'))
        time.sleep(0.5)


if __name__=="__main__":
   main()

