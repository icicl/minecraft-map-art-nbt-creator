pathtomcsaves = "/Users/admin/Library/Application Support/minecraft/saves/"#path to the minecraft saves folder (this is for mac, if you replace 'admin' with your username
mcworldfolder = "testserv/"#name of the world
image = 'eagle.jpeg'#filepath of image, or image name if it is in the same directory as this file
crop = True# stretches image to fit if false
mapswide = 2#how many maps wide your display will be
mapstall = 2#how many maps tall your display will be

map_id = 14#the id of the first map to be modified. for example, if I am using maps #23 to #28 to make a 3X2 display, this value should be 23

#tags = {'zCenter':20,'xCenter':139,'locked':97,'colors':152,'trackingPosition':64}

'''some of the nbt tags'''
z = 0#zCenter
x = 0#xCenter
locked = True
track = False#trackingPosition

zb = bytes([(z//(256**i))%256 for i in range(3,-1,-1)])
xb = bytes([(x//(256**i))%256 for i in range(3,-1,-1)])
lb = bytes([locked])
tb = bytes([track])

import gzip#https://github.com/python/cpython/blob/3.8/Lib/gzip.py (pip didn't work for me)

with gzip.open('map_template.dat') as f:
    dat = f.read()

#colorbytes = b'\x00'*16384
def mkmap(id_,colorbytes=b'\x00'*16384):
    d2 = dat[:20]+zb+dat[24:64]+tb+dat[65:97]+lb+dat[98:139]+xb+dat[143:152]+colorbytes+dat[-20:]
    with gzip.open(pathtomcsaves+mcworldfolder+'data/map_'+str(id_)+'.dat','wb+') as f:
        f.write(d2)

from colors import colors
#colors = {5:(109,153,48),34:(255,255,255),43:(79,57,40),74:(299,299,51)}
def closest(pix):
    rmod,gmod,bmod = 0,0,0
    modifyer = 2#power to which each pixel difference is ranged - 2 seems fine, maybe experiment with other values on other colorsets
    min_ = (256**modifyer)*3#minimum difference between given pixel and color from set
    minid = 0#empty
#    min_pix = (255,255,255)#white, can be whatever
    for i in colors:
        dist = (pix[0]+rmod-colors[i][0])**modifyer+(pix[1]+gmod-colors[i][1])**modifyer+(pix[2]+bmod-colors[i][2])**modifyer
        if dist < min_:
            min_=dist############## update the min distance
            minid=i#and its id
#            min_pix = colors[i]#### and the corresponding color
    return minid

#for i in range(200):
#    if dat[i:i+16]==b'trackingPosition':print(i+16)
from PIL import Image
im = Image.open(image)
x,y=im.width,im.height
x_,y_=x,y
if crop:
    if x*mapstall > y*mapswide:
        x = y*mapswide//mapstall
    else:
        y = x*mapstall//mapswide
im = im.resize((mapswide*128,mapstall*128),box=((x_-x)//2,(y_-y)//2,(x_+x)//2,(y_+y)//2))
il = im.load()
#for x in range(mapswide*128):
#    for y in range(mapstall*128):
#        il[x,y] = closest(il[x,y])
#im.show()
for xm in range(mapswide):
    for ym in range(mapstall):
        cb = bytes([0,0,64,0])
        for y in range(128*xm,128*xm+128):
            for x in range(128*ym,128*ym+128):
                cb+=bytes([closest(il[x,y])])
        mkmap(map_id,cb)
        print(map_id)
        map_id += 1
