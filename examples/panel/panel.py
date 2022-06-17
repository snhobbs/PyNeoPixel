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

    led_set = []

    x = 0
    while x < width*height:
        print(x)
        strand.setPixelColor(x, 0, 255, 255)
        strand.show()

        resp = input("%d?"%x)
        if resp.lower() == "y":
            led_set.append(x)
            x+=1
        elif resp.lower() == 'n':
            strand.setPixelColor(x, 0, 0, 0)
            strand.show()
            x+=1
        elif 'b' in resp.lower():
            strand.setPixelColor(x, 0, 0, 0)
            if x > 0:
                x-=1
                if len(led_set):
                    led_set.pop()
                    strand.setPixelColor(x, 0, 0, 0)
        print(led_set)

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
