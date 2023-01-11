#Christmas Gift Exchange Problem

#import packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Create Normal Distribution
NUM_ROLLS = 100000
np.random.seed(3)
sample = np.random.normal(loc=19.5, scale=3.5, size=NUM_ROLLS)
sample = np.round(sample).astype(int)
side, count = np.unique(sample, return_counts=True)
probs = count / len(sample)

# Plot the results
sns.displot(sample, binwidth=1, stat="density")
plt.title(
    f"Discrete Normal Distribution (sample size {NUM_ROLLS})")
plt.ylabel("Probability")
plt.xlabel("Number of Game Players")
plt.show()

#Create Array with true/false for factors
#each row is a number of moves
#each column is a number of players and whether it is a factor of the number of moves
amountofplayernumbers = max(sample)-min(sample) + 1 #not sure if I need this line anymore
factors = np.zeros((amountofplayernumbers,amountofplayernumbers))
k = 0
for i in range(min(sample), max(sample)+1):
    l = 0
    for j in range(min(sample),max(sample)+1):
        if i % j == 0:
            factors[k,l] = 1
        l=l+1
    k = k+1

#Calculate the expected value of amount of playernumbers that will be bad
E = np.zeros((amountofplayernumbers,amountofplayernumbers))
for i in range(amountofplayernumbers):
    E[i,:] = factors[i,:] * probs

Etotals = np.sum(E, axis = 1)
 
#plot the expected values vs the number of net moves   
movenumbers = np.arange(min(sample),max(sample)+1,1)
plt.scatter(x=movenumbers,y=Etotals)

#sort the number of net moves in order of best to worst 
tupleList = []
for i in range (0,len(Etotals)):
    tupleList.append((Etotals[i], movenumbers[i]))
#print("unsorted: ", tupleList)
tupleList.sort()
#print("Sorted: ", tupleList)

besttoworstMoveNumbers = []
for i in tupleList:
    besttoworstMoveNumbers.append(i[1])
    
print(besttoworstMoveNumbers)
