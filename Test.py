import json
import os
import math
mileage_delta_errors=[]
bayesian_delta_errors=[]

geo_dir = os.path.dirname('D:\Tesi\prediction_var\  ')
with open(geo_dir+'\crescini_mile-offline__prediction_var.json') as json_file:
    mileage=json.load(json_file)

with open(geo_dir+'\crescini_mile-offline__prediction_var_test.json') as json_file2:
    mileageGPS=json.load(json_file2)

with open(geo_dir+'\crescini_bayesian__prediction_var.json') as json_file:
    bayesian=json.load(json_file)

with open(geo_dir+'\crescini_bayesian__prediction_var_test.json') as json_file2:
    bayesianGPS=json.load(json_file2)

for i,m in enumerate(mileage):
    target_deltadate = mileage[i]['values'][0]['target']['target_deltamileage']
    mileage_delta_errors.append(math.fabs(mileage[i]['values'][0]['prediction']['prediction']['deltamileage']-target_deltadate)-math.fabs(mileageGPS[i]['values'][0]['prediction']['prediction']['deltamileage']-target_deltadate))
print 'bayesian'
for i,m in enumerate(bayesian):
    target_deltadate = bayesian[i]['values'][0]['target']['target_deltamileage']
    bayesian_delta_errors.append(math.fabs(bayesian[i]['values'][0]['prediction']['prediction']['deltamileage']-target_deltadate)-math.fabs(bayesianGPS[i]['values'][0]['prediction']['prediction']['deltamileage']-target_deltadate))
print 'mileage',mileage_delta_errors
print 'bayesian',bayesian_delta_errors
print 'miglioramenti mileage',sum(x>0 for x in mileage_delta_errors)
print 'peggioramenti mileage',sum(x<0 for x in bayesian_delta_errors)
print 'miglioramenti bayesian',sum(x>0 for x in mileage_delta_errors)
print 'peggioramenti bayesian',sum(x<0 for x in bayesian_delta_errors)