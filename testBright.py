from Brightness import *

def main():
    light=Brightness()
    while True:
        lightLevel=light.getValue()
        print("Light Level : " + format(lightLevel,'.2f') + " lx")
        time.sleep(0.5)


if __name__=="__main__":
   main()
