import json
import os
import math
mileage_delta_errors=[]
bayesian_delta_errors=[]
time_delta_errors=[]

geo_dir = os.path.dirname('D:\Tesi\prediction_var\  ')
with open(geo_dir+'\crescini_mile-offline__prediction_var.json') as json_file:
    mileage=json.load(json_file)

with open(geo_dir+'\crescini_mile-offline__prediction_var_test.json') as json_file2:
    mileageGPS=json.load(json_file2)

with open(geo_dir+'\crescini_bayesian__prediction_var.json') as json_file3:
    bayesian=json.load(json_file3)

with open(geo_dir+'\crescini_bayesian__prediction_var_test.json') as json_file4:
    bayesianGPS=json.load(json_file4)

with open(geo_dir+'\crescini_time-offline__prediction_var.json') as json_file5:
    time=json.load(json_file5)

with open(geo_dir+'\crescini_time-offline__prediction_var_test.json') as json_file6:
    timeGPS=json.load(json_file6)


for i,m in enumerate(mileage):
    target_deltadate = mileage[i]['values'][0]['target']['target_deltamileage']
    mileage_delta_errors.append(math.fabs(mileage[i]['values'][0]['prediction']['prediction']['deltamileage']-target_deltadate)-math.fabs(mileageGPS[i]['values'][0]['prediction']['prediction']['deltamileage']-target_deltadate))

for i,m in enumerate(bayesian):
    target_deltadate = bayesian[i]['values'][0]['target']['target_deltamileage']
    bayesian_delta_errors.append(math.fabs(bayesian[i]['values'][0]['prediction']['prediction']['deltamileage']-target_deltadate)-math.fabs(bayesianGPS[i]['values'][0]['prediction']['prediction']['deltamileage']-target_deltadate))

for i,m in enumerate(time):
    target_deltadate = time[i]['values'][0]['target']['target_deltadate']
    time_delta_errors.append(math.fabs(time[i]['values'][0]['prediction']['prediction']['deltadate']-target_deltadate)-math.fabs(timeGPS[i]['values'][0]['prediction']['prediction']['deltadate']-target_deltadate))



print 'mileage',mileage_delta_errors
print 'bayesian',bayesian_delta_errors
print 'time',time_delta_errors
print 'miglioramenti mileage',sum(x>0 for x in mileage_delta_errors)
print 'peggioramenti mileage',sum(x<0 for x in mileage_delta_errors)
print 'miglioramenti bayesian',sum(x>0 for x in bayesian_delta_errors)
print 'peggioramenti bayesian',sum(x<0 for x in bayesian_delta_errors)
print 'miglioramenti time',sum(x>0 for x in time_delta_errors)
print 'peggioramenti time',sum(x<0 for x in time_delta_errors)