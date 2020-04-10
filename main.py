'''
Created on 5 apr. 2020

@author: Alexandraah
'''
from GA import GA
from ReadData import ReadData
from utils import *
import matplotlib.pyplot as plt


data = ReadData("C:\\@Alexandra\\anul2\\semestrul2\\ai\\lab\\laborator4\\berlin.txt")
params = {'popSize': 5, 'noGen': 1000}
ga = GA(params, data.problParams)
ga.initialisation()
ga.evaluation()

res=[]
for i in range(params['noGen']):
    ga.oneGeneration()
    #ga.oneGenerationElitism()
    #ga.oneGenerationSteadyState()
    best = ga.bestChromosome()
    fitnesses = [c.fitness for c in ga.population]
    avgFitness = sum(fitnesses) / len(fitnesses)
    res.append(avgFitness)
    print('Generation: ' + str(i) + '\nBest chromosome: ' + str(best.repres) + '\nLocal best fitness: ' + str(best.fitness)
         +'\nAverage fitness: '+ str(avgFitness)+'\n')
    
plt.plot(res)
plt.ylabel('Best Fit/Generation')
plt.xlabel('Generation')
plt.show()
