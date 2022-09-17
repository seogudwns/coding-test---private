import time
num = 1000000

stt_time = time.time()
lst = [i for i in range(num)]
print(time.time()-stt_time)
# ! == 0.1260082721710205 & 0.12100505828857422

stt_time = time.time()
lst2 = []
for i in range(num):
    lst2.append(i)
print(time.time()-stt_time)
# ! == 0.4361860752105713 & 0.4710655212402344

stt_time = time.time()
lst3 = []
for i in range(num):
    lst3 += [i]
print(time.time()-stt_time)
# ! == 0.4895172119140625 & 0.4257373809814453

stt_time = time.time()
lst4 = []
for i in range(num):
    lst4 = lst4 + [i]
print(time.time()-stt_time)
# ! 10초 넘어감.. pass