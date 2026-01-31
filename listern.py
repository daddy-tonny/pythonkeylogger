from pynput.keyboard import Listener

def writetofile(x,y):
    print('position of current mouse [0]'.format((x,y)))


with Listener(on_press= writetofile) as l:
    l.join()