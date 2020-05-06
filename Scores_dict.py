import numpy as np
import matplotlib.pyplot as plt
scores = {"Day 1": 100, "Day 2": 108, "Day 3":112, "Day 4":115, "Day 5":150,
          "Day 6":178, "Day 7": 143, "Day 8": 132, "Day 9":190, "Day 10": 235,
          "Day 11":253, "Day 12": 298, "Day 13": 328, "Day 14":390, "Day 15": 257,
          "Day 16":288, "Day 17": 393, "Day 18": 425, "Day 19":458, "Day 20": 450,
          "Day 21":473, "Day 22": 333, "Day 23": 452, "Day 24":490, "Day 25": 495,
          "Day 26":488, "Day 27": 543, "Day 28": 532, "Day 29":590, "Day 30": 605}



Scores=np.array(list(scores.values()))
#kk1=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
Days=np.arange(1,31,1)

print("mean score:")
print(np.mean(Scores))
print("median score:")
print(np.median(Days))

print("minimum score:")
print(np.min(Scores))
print("maximum score:")
print(np.max(Scores))

plt.plot(Scores,Days)

plt.ylabel('days')
plt.xlabel('score')