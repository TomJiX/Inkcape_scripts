import numpy as np


def rgb_to_hex(grey):
    return '#{:02x}{:02x}{:02x}'.format(grey,grey,grey)


def zig_zag(width,length,pw,angle,grey):   #all dimensions are [x,y]
    
    grey=rgb_to_hex(grey)
    angle=np.pi*angle/180
    rect((0,0),(width,5), fill="black",stroke_width=0)
    rect((0,length-5),(width,length), fill="black",stroke_width=0)

    rect((0,5),(width,length-5), fill=grey,stroke_width=0)
    
    border=rect((0,0),(width,length),stroke_width=0)
    pts=[(1,4)]
    i=0
    while pts[-1][1]<length-5:
        i+=1
        pts.append((1+(width-2)*(i%2),4+i*np.tan(angle)*width))
    polyline(pts,stroke_width=pw,clip_path=border)
    
zig_zag(10,40,0.5,15,70)
