import imageio.v2 as iio

filenames = ['starry night1.jpg', 'starry night2.jpg', 'starry night3.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))
  
iio.mimsave('starry_night.gif', images, duration=500, loop=0)

print("starry_nigt is ready!")


