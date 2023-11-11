import numpy as np
import pandas as pd
from scipy.stats import norm

def create_dist(data):
    mu = np.mean(data)
    std = np.std(data)

    return norm(mu,std)


def prob_of_class(prior, dists, data):
    prob = prior
    for i in range(len(dists)):
        prob *= dists[i].pdf(data[i])

    return prob

def predict(p_w, dists_win, data):
    p_winning = prob_of_class(p_w, dists_win, data)
    p_losing = 1 - p_winning

    answer = 0
    if p_winning > p_losing:
        answer = 1
    
    return answer

def calc_acc(p_w, dists_win, win, lost):
    correct = 0
    total = len(win) + len(lost)
    for d in win:
        guess = predict(p_w, dists_win, d)
        if guess == 1:
            correct += 1
    
    for d in lost:
        guess = predict(p_w, dists_win, d)
        if guess == 0:
            correct += 1

    print(f'Acc: {correct/total}')

#importing the data
monster_df = pd.read_csv("monster_list.csv")

# calculate the prior
winning = monster_df['monster_defeat'].to_numpy()
p_winning = 0
for i in winning:
    if i == 1:
        p_winning +=1

p_winning = p_winning / len(winning)

#split the data
data = monster_df.drop(columns=['monster_name', 'monster_defeated']).to_numpy()
train_win = data[winning==1]
train_lost = data[winning=0]

col_data = []
for i in range(len(train_win)):
    col_data.append(train_win[i][0])
win_p1 = create_dist(col_data)

col_data = []
for i in range(len(train_win)):
    col_data.append(train_win[i][1])
win_p2 = create_dist(col_data)

col_data = []
for i in range(len(train_win)):
    col_data.append(train_win[i][2])
win_p3 = create_dist(col_data)

col_data = []
for i in range(len(train_win)):
    col_data.append(train_win[i][3])
win_p4 = create_dist(col_data)

col_data = []
for i in range(len(train_win)):
    col_data.append(train_win[i][4])
win_p4 = create_dist(col_data)



win_pdfs = [win_p1, win_p2, win_p3, win_p4, win_p4


test_monsters = pd.read_csv('monster_list_test.csv')
test_data = test_monsters.drop(columns=['monster_name', 'monster_defeated']).tolist()
test_winning = test_monsters['monster_defeated'].to_numpy()

test_win = test_data[test_winning==1]
test_lost = test_data[test_winning==0]

#test it out
calc_acc(
    p_w=p_winning,
    dists_win=win_pdfs,
    win=test_win,
    lost=test_lost
)
