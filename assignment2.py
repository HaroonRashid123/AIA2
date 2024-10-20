import csv
import numpy as np
import math
def naive_bayes_classifier(dataset_filepath, patient_measurements):
  # dataset_filepath is the full file path to a CSV file containing the dataset
  # patient_measurements is a list of [temperature, heart rate] measurements for a patient

  # most_likely_class is a string indicating the most likely class, either "healthy", "diseased"
  # class_probabilities is a two element list indicating the probability of each class in the order [healthy probability, diseased probability]
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

    bottom_value = (1 / math.sqrt(2 * math.pi * std ** 2)) * math.e

    result = bottom_value ** (exponent_value)

    return result
  
def mean_and_stand():

  grid = csv_format(r'C:\Users\haroo\Desktop\AIA2\Examples\Example0\dataset.csv')
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



  print()
  
        
         
         
   


def main():
  #  print(csv_format(r'C:\Users\haroo\Desktop\AIA2\Examples\Example0\dataset.csv'))
   print(mean_and_stand())
main()
