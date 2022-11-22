import sys,random,time
try:
    import bext
except ImportError:
    print("This Programme Requires BEXT Module can install by folowing the instructions @ http://pypi.org/project/bext")
    sys.exit()
width,height = bext.size()
width = -1
number_of_logos = 5
pause_time = 0.2
color = ['red','green','yellow','blue','magenta','cyan','white']
up_right = ur
up_left = ul
down_right = dr
down_left = dl
color_1 = 'color'
X = 'x'
Y = 'y'
Dir = 'direction'
def main():
    bext.clear()
    logos = []
    for i in range(number_of_logos):
        logos.append({color_1 = random.choice(color),X:random.radint(1,-4),y:random.radint(1,-4),Dir = random.choice(direction)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1
    cornerbounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X],logo[Y])
            print(' ',end = ' ')
        original_direction = logo[Dir]
        if logo[X] == 0 and logo[Y] == 0:
            logo[Dir] = down_right
            cornerbounces += 1
        elif logo[X] == 0 and log[Y] == height - 1:
            logo[Dir] = up_right
            cornerbounces += 1
        elif logo[X] == weight-3 and logo[Y] == 0:
            logo[Dir] = down_left
            cornerbounces += 1
        elif logo[X] == wight-3 and logo[Y] == height-1:
            logo[Dir] == up_left
            cornerbounces += 1
#Countinue from line 86. Need to read about the code as what it did and why and how it did.
