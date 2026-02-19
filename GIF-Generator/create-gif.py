import imageio.v3 as iio
filenames=['freepik1.jpg','freepik2.jpg','freepik3.jpg']
images=[]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('cat.gif',images,duration=500,loop=0)
