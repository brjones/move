import sys
try:
        xclick=int(sys.argv[1])
        yclick=int(sys.argv[2])
        try:
                delay=int(sys.argv[3])
        except:
                delay=0
except:
        print "USAGE mouseclick [int x] [int y] [optional delay in seconds]"
        exit()
print "mouse click at ", xclick, ",", yclick," in ", delay, "seconds"

import time
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap

def mouseEvent(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
        mouseEvent(kCGEventMouseMoved, posx,posy);

def mouseclick(posx,posy):
        mouseEvent(kCGEventLeftMouseDown, posx,posy);
        mouseEvent(kCGEventLeftMouseUp, posx,posy);

while True:
        time.sleep(delay);
        mousemove(xclick, yclick);
        time.sleep(delay);
        mousemove(yclick, xclick);
