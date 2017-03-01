import cv2
from pyheatmap.heatmap import HeatMap
from PIL import Image
from interruptingcow import timeout


def main():
    data = []
    path = 'danklog.asc'
    #f  = open(path)
    #line f.readline().split('\t')
    with open(path, 'r') as f:
        for i, l in enumerate(f):
            if not i%1000 == 0:
                continue
            line = l.split('\t')
            if len(line) != 6:
                continue
            try:
                data.append([int(float(line[1])),int(float(line[2]))])
            except ValueError:
                continue
    print data
    '''hm = HeatMap(data)
    hm.heatmap(save_as="heat.png")

    im1 = Image.open('heat.png')
    im2 = Image.open('KL_007.png')

    im2.paste(im1, (0, 0), mask=im1)
    im2.save("moi.png")'''

with timeout(20, exception=RuntimeError):
    main()
