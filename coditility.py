# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(predicted, observed):
    # write your code in Python 3.6
    sqdeviations = []
    for obs, pre in zip(observed, predicted):
        sqdeviations.append((obs-pre)**2)

    mse = (sum(sqdeviations))/len(sqdeviations)
    rmse = mse ** 0.5
    return rmse
predicted = [4, 25,  0.75, 11]
observed  = [3, 21, -1.25, 13]

solution(predicted, observed)
