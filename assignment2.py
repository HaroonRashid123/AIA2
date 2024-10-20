import csv
import numpy as np
import math

def naive_bayes_classifier(dataset_filepath, patient_measurements):
  data = mean_and_stand(dataset_filepath)
  #Using PDF function to calculate prob density
  temp_density_healthy = prob_den_func(patient_measurements[0], data['healthy_temp_mean'], data['healthy_temp_std'])
  heart_density_healthy = prob_den_func(patient_measurements[1], data['healthy_heart_mean'], data['healthy_heart_std'])
  temp_density_disease = prob_den_func(patient_measurements[0], data['diseased_temp_mean'], data['diseased_temp_std'])
  heart_density_disease = prob_den_func(patient_measurements[1], data['diseased_heart_mean'], data['diseased_heart_std'])

  health =  temp_density_healthy * heart_density_healthy * data['prior_health'] 
  disease = temp_density_disease * heart_density_disease * data['prior_disease']
  total = health + disease

  #Normalize the probability
  normal_health = health / total
  normal_disease =  disease / total
  # Calculate which normal is greater and return the value of which is    
  if normal_health > normal_disease:
        most_likely_class = 'healthy'
  else:
        most_likely_class = 'diseased'
        
  return most_likely_class, [normal_health, normal_disease]


def csv_format(filename):
    #csv format to get a 2d list from the csv file
    grid = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
           grid.append(row)
    return grid


def prob_den_func(x, mean, std):
    
    # Probability densisty function functions for temperature and heart rate for healthy
    # patients and diseased patients from an existing dataset of patients

    exponent_value = -0.5 * (( (x- mean) / std )) **2
    bottom_value = (1 / (std * math.sqrt(2 * math.pi))) 
    result = bottom_value *  math.exp(exponent_value)

    return result 
  
def mean_and_stand(grid):
  grid = csv_format(grid)
  healthy_temp_list = []
  healthy_heart_list = []
  diseased_temp_list = []
  diseased_heart_list = []
  num_of_healthy = 0
  num_of_disease = 0
  data = {}
  #Loop through the 2d array to add the healthy and disease columns while also incrementing the number of patients for each
  for i in range(len(grid)):
      
      if 'healthy' in grid[i]:
            healthy_temp_list.append(float(grid[i][1]))
            healthy_heart_list.append(float(grid[i][2]))
            num_of_healthy +=1
      else:
            diseased_temp_list.append(float(grid[i][1]))
            diseased_heart_list.append(float(grid[i][2]))
            num_of_disease += 1
  # Get average of total patients divided by number of pateince between health and disease
  prior_health = num_of_healthy / (i +1)
  print(prior_health)
  prior_disease = num_of_disease / (i + 1)
   
  healthy_temp_array = np.array(healthy_temp_list)
  healthy_heart_array = np.array(healthy_heart_list)
  diseased_temp_array = np.array(diseased_temp_list)
  diseased_heart_array = np.array(diseased_heart_list)

  #Calculate mean and standard deviation of tempature and heartrate
  healthy_temp_mean = np.mean(healthy_temp_array)
  healthy_heart_mean = np.mean(healthy_heart_array)
  healthy_temp_std = np.std(healthy_temp_array, ddof=1)  
  healthy_heart_std = np.std(healthy_heart_array, ddof=1)

  diseased_temp_mean = np.mean(diseased_temp_array)
  diseased_heart_mean = np.mean(diseased_heart_array)
  diseased_temp_std = np.std(diseased_temp_array, ddof=1)
  diseased_heart_std = np.std(diseased_heart_array, ddof=1)
  #Put all this data into a dictionary so i can use it in the bayes classifier function
  data = {
        "healthy_temp_mean": healthy_temp_mean,
        "healthy_heart_mean": healthy_heart_mean,
        "healthy_temp_std": healthy_temp_std,
        "healthy_heart_std": healthy_heart_std,
        "diseased_temp_mean": diseased_temp_mean,
        "diseased_heart_mean": diseased_heart_mean,
        "diseased_temp_std": diseased_temp_std,
        "diseased_heart_std": diseased_heart_std,
        "prior_health": prior_health,
        "prior_disease": prior_disease
    }
  return data

def main():
  dataset_filepath = r'C:\Users\haroo\Desktop\AIA2\Examples\Example0\dataset.csv'
  patient_measurements = [37.6, 80]  
  print(naive_bayes_classifier(dataset_filepath, patient_measurements))
 
main()
