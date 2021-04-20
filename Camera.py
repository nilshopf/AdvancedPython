import threading


new_timer = 1

def Camera_picture():
    global new_timer
    print("Hello Camera")
    new_timer = 1

def Timer_Camera():
    global new_timer

    t = threading.Timer(5, Camera_picture)
    t.start()
    new_timer = 0

def NeedNewTimer():
    if new_timer == 1:
        Timer_Camera()