# SFI-Application
A python code for a gift exchange problem

The premise of the problem: 
Every year around the winter holidays, many groups of people play a gift exchange game. In this game, everyone brings a gift and sits in a circle. The leader of the game reads a story about the Left Family and how they left right away to get right to the store, etc. Every time the word "left" is read, everyone passes the gift they currently have to their left. Every time the word "right" is read, everyone passes the gift they currently have to their right. 
At the end of the story, everyone opens the gift that is in front of them. 
A problem arises when the net number of moves given by the story causes everyone to receive their own gift (the bad case). 
I created this code to rank net move numbers based on their likelihood of producing the case where everyone receives their own gift. 

Some ground rules:
No one plays this game in a group of 1 because they would be guaranteed to get their own gift.
No one plays this game in a group of 2 because they should just exchange with each other. 

Given the above restrictions on number of players, 1 or 2 net moves are guaranteed to work out so that the players do not receive their own gift. If one were writing a story to be used in this game, it would probably be a good idea to have this many net moves. However, this is boring, and I want to see how other numbers compare. 

Some observations and guesses:
If the number of players is a factor of the number of net moves, this produces the bad case.
Therefore, it seems like prime numbers of net moves might be good choices. However, if the number of players is the same as the number of net moves, this also produces the bad case. 
After primes, it seems like prime multiples of primes might be the next best, since they have few factors as well.
While I can rank numbers based on how many factors they have, I also want to know something about what amounts of players are likely in this game so that I can avoid making the net number of moves equal to the number of players. 
I don't know much about the probability distribution that describes the likelihood of each possible number of players. However, I do know that there is a hard upper limit of players at the number of people on Earth. This is still too big because it would be impossible to get everyone to play this game. I would guess that even a number as small as 100 players would be pretty unlikely. 
Since there is a hard limit on the bottom (no 1- or 2-player games allowed), but the upper limit of players is a bit more ambiguous, I would guess that the distribution has a right skew. 

I first did this problem in Excel, where I drew some probability distributions to test the concept of the calculations. When moving to python, I decided it was easiest just to start with a normal distribution, even though I'm pretty convinced this distribution would really have a right skew. 
In the future I would potentially like to try this with more realistic distributions, but the result is always an element-wise multiplication of the vector containing the probabilities with the vector containing the number of bad cases possible for each net number of moves. 
It may be interesting at some point to collect data on group sizes, but this task may not be feasible since this game is typcially only played around winter holidays, and it would be difficult to get enough accurate responses. 

Enjoy!
