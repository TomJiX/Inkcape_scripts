import numpy as np


def rgb_to_hex(grey):
    return '#{:02x}{:02x}{:02x}'.format(grey, grey, grey)

def draw_snake(L,W,pw,ps,grey):   #all dimensions are [x,y]
    
    rect((0,0),(W,L), fill=rgb_to_hex(grey),stroke_width=0)

    rect((0,0),(W,5), fill="black",stroke_width=0)
    rect((0,L-5),(W,L), fill="black",stroke_width=0)
    repeat_l=(2*(ps+pw))
    n,r=divmod(L-10-2*ps-pw,repeat_l)
    for i in range(int(n)):
        if i==0:
            rect((0,5),(pw,5+r/2+i*repeat_l+pw+ps), fill="black",stroke_width=0)
        else:
            rect((0,5+r/2.+i*repeat_l),(pw,5+r/2.+i*repeat_l+pw+ps), fill="black",stroke_width=0)
        
        rect((W-pw,ps+5+r/2.+i*repeat_l),(W,ps+5+r/2.+i*repeat_l+pw+ps), fill="black",stroke_width=0)
        
        rect((0,5+r/2.+i*repeat_l+ps),(W,5+r/2.+i*repeat_l+ps+pw), fill="black",stroke_width=0)
        rect((0,ps+pw+5+r/2.+i*repeat_l+ps),(W,ps+pw+5+r/2.+i*repeat_l+ps+pw), fill="black",stroke_width=0)

    i+=1
    rect((0,5+r/2.+i*repeat_l),(pw,5+r/2.+i*repeat_l+pw+ps), fill="black",stroke_width=0) 
    rect((W-pw,ps+5+r/2.+i*repeat_l),(W,L-5), fill="black",stroke_width=0)
    rect((0,5+r/2.+i*repeat_l+ps),(W,5+r/2.+i*repeat_l+ps+pw), fill="black",stroke_width=0)

draw_snake(50,10,0.5,0.2,150)

