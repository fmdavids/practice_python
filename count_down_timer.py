import time

# t = int(input('Please, enter how long: '))

def countDown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -=1
        print(t)

print('Countdown completed!!!')

t = int(input('Please, enter how long: '))
countDown(t)
