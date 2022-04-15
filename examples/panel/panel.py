from neopixel import NeoPixel
from time import sleep
strand = NeoPixel('/dev/ttyACM0', baudrate=115200)

width = 16
height = 16
def main():
    # clear panel
    for x in range(width*height):
        print(x)
        strand.setPixelColor(x, 0, 0, 0)
        #sleep(1)
    strand.show()

    set = []

    for x in range(width*height):
        print(x)
        strand.setPixelColor(x, 0, 255, 255)
        strand.show()

        while True:
            resp = input("%d?"%x)
            if resp.lower() == "y":
                set.append(x)
                break
            elif resp.lower() == 'n':
                strand.setPixelColor(x, 0, 0, 0)
                strand.show()
                break
    print(set)

    '''
    for x in range(5):
        strand.setPixelColor(x, 255, 0, 0)
        strand.show()
        time.sleep(1)
        strand.setPixelColor(x, 0, 255, 0)
        strand.show()
        time.sleep(1)
        strand.setPixelColor(x, 0, 0, 255)
        strand.show()
        time.sleep(1)
    '''


if __name__ == "__main__":
    main()
