import csv
import numpy as np
import math
def naive_bayes_classifier(dataset_filepath, patient_measurements):
  
  data = mean_and_stand(dataset_filepath)
  temperature = patient_measurements[0]
  heart_rate = patient_measurements[1]
  temp_density_healthy = prob_den_func(temperature, data['healthy_temp_mean'], data['healthy_temp_std'])
  heart_density_healthy = prob_den_func(heart_rate, data['healthy_heart_mean'], data['healthy_heart_std'])
  temp_density_disease = prob_den_func(temperature, data['diseased_temp_mean'], data['diseased_temp_std'])
  heart_density_disease = prob_den_func(heart_rate, data['diseased_heart_mean'], data['diseased_heart_std'])
    
  health =  temp_density_healthy * heart_density_healthy
  disease = temp_density_disease * heart_density_disease
  total = health + disease
  normal_health = health / total
  normal_disease =  disease / total
    
  if normal_health > normal_disease:
        most_likely_class = 'healthy'
  else:
        most_likely_class = 'diseased'
    
  class_probabilities = [normal_health, normal_disease]
  return most_likely_class, class_probabilities



def csv_format(filename):
    grid = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
           grid.append(row)
    return grid


def prob_den_func(x, mean, std):
    
    #expo = math.exp(-((x - mean) ** 2) / (2 * std ** 2))

    exponent_value = -0.5 * (( (x- mean) / std )) **2
    bottom_value = (1 / (std * math.sqrt(2 * math.pi))) * math.e
    result = bottom_value * math.e * math.exp(exponent_value)

    return result
  
def mean_and_stand(grid):
  grid = csv_format(grid)
  healthy_temp_list = []
  healthy_heart_list = []
  diseased_temp_list = []
  diseased_heart_list = []


  for i in range(len(grid)):
    
      if 'healthy' in grid[i]:
            healthy_temp_list.append(float(grid[i][1]))
            healthy_heart_list.append(float(grid[i][2]))
      else:
            diseased_temp_list.append(float(grid[i][1]))
            diseased_heart_list.append(float(grid[i][2]))
  
  
   
  healthy_temp_array = np.array(healthy_temp_list)
  healthy_heart_array = np.array(healthy_heart_list)
  diseased_temp_array = np.array(diseased_temp_list)
  diseased_heart_array = np.array(diseased_heart_list)

  
  healthy_temp_mean = np.mean(healthy_temp_array)
  healthy_heart_mean = np.mean(healthy_heart_array)
  healthy_temp_std = np.std(healthy_temp_array, ddof=0)  
  healthy_heart_std = np.std(healthy_heart_array, ddof=0)

  diseased_temp_mean = np.mean(diseased_temp_array)
  diseased_heart_mean = np.mean(diseased_heart_array)
  diseased_temp_std = np.std(diseased_temp_array, ddof=0)
  diseased_heart_std = np.std(diseased_heart_array, ddof=0)

  data = {
        "healthy_temp_mean": healthy_temp_mean,
        "healthy_heart_mean": healthy_heart_mean,
        "healthy_temp_std": healthy_temp_std,
        "healthy_heart_std": healthy_heart_std,
        "diseased_temp_mean": diseased_temp_mean,
        "diseased_heart_mean": diseased_heart_mean,
        "diseased_temp_std": diseased_temp_std,
        "diseased_heart_std": diseased_heart_std
    }
  return data



  
  
        
         
         

def main():
  dataset_filepath = r'C:\Users\haroo\Desktop\AIA2\Examples\Example1\dataset.csv'
  patient_measurements = [37.6, 80]  
  print(naive_bayes_classifier(dataset_filepath, patient_measurements))
 
main()
