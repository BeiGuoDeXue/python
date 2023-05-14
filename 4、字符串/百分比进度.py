import time

for i in range(101):
# end=' ',避免换行
    print("\r{:3}%".format(i),end=' ')
    time.sleep(0.05)