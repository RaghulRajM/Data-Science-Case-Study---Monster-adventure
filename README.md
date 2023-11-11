# Data-Science-Case-Study---Monster-adventure

### Introduction
- You are a very inexperienced adventurer, just starting off on your first of what is sure to be many, many adventures! Soon after excitedly leaving your first tavern, you find the flash drive of a past adventurer who met an unfortunate demise.
On it, there is a calculator (privoro_monster_calc.py) that appears to calculate the probability of you winning a fight against a monster, given the monster’s information and the dead adventurer. You also find what appears to be a datasheet containing past examples (monsters_list.csv) on which the calculator was trained.
While you are happy to have come across this data, given how you found this calculator, you decide to give the calculator code a once over before using it for yourself, suspecting that it may have materially contributed to the...deadness of the adventurer you’ve stumbled across.

### Problem
- Your goal is to fix the calculator in any way you see fit. You may change any code and you are permitted to use numpy, pandas, or scipy if you wish. When changing code, you should try to make the code more pythonic and concise where possible, yet also maintain readability.
Please do not use libraries like PyTorch, scikit-learn, or tensorflow here, as they are not needed. Note that there is no single correct answer. The goal is to make the code clean and readable.
Estimated time to complete this problem: 1-2 hours

### Bonus
- Fixing Calculator Logic
Note: Please do not complete this section until the previous part is complete; this is a bonus and not required.
1
The logic behind the calculator is broken. There is a logical error in the way certain probabilities are calculated and after fixing it, the test set (monster_list_test.csv) accu- racy should be 100%. Note that you do not need to compute priors for each type of monster, just the prior for winning overall. Fixing the logical error is sufficient to get 100% accuracy on the test set.
  * Fix the logic in the calculator.
  * Please write a (very) short description of what you changed and why. 2-3 sentences is
sufficient.
- Picking a new classifier
Note: Please do not complete this section until the other parts are complete; this is a bonus and not required.
In this section, suppose you are given the freedom to implement any kind of classifier you wish. All libraries are now fair game, including PyTorch, scikit-learn, and tensorflow.
  * What method would you use to predict your chances of survival against a given monster, and how would you (at a high level) set it up?
  * Why is that method superior to the (attempted) method in the original calculator?
