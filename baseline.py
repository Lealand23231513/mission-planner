import matplotlib.pyplot as plt
import progressbar
from galogic import * 
pbar = progressbar.ProgressBar()

# Add Dustbins
for i in range(numNodes):
    RouteManager.addDustbin(Dustbin())

random.seed(seedValue)
yaxis = [] # Fittest value (distance)
xaxis = [] # Generation count

pop = Population(populationSize, True)
globalRoute = pop.getFittest()
print ('Initial minimum distance: ' + str(globalRoute.getDistance()))

# Start evolving
for i in pbar(range(numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)

print ('Global minimum distance: ' + str(globalRoute.getDistance()))
print ('Final Route: ' + globalRoute.toString())

fig = plt.figure()

plt.plot(xaxis, yaxis, 'r-')
plt.xlabel('Iterations')
plt.ylabel('Shortest Path Distance')
plt.title('Ant Colony Optimization')
fig.savefig(f'baseline_nodes-{numNodes}_drones-{numTrucks}.png')
plt.show()
