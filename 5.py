import numpy as np
fuel_efficiency = np.array([35, 38, 45, 48, 32, 31, 44, 45])
average_fuel_efficiency = np.mean(fuel_efficiency)
modelA_index = 1  
modelB_index = 3  
modelA_efficiency = fuel_efficiency[modelA_index]
modelB_efficiency = fuel_efficiency[modelB_index]
percentage_improvement = ((modelB_efficiency - modelA_efficiency) / modelA_efficiency) * 100
print("Average fuel efficiency:", average_fuel_efficiency, "miles per gallon")
print("Percentage improvement in fuel efficiency between Model A and Model B:", percentage_improvement, "%")

