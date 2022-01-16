import pandas as pd
import json
#read JSON data
in_json = [{"Gender":"Male","HeightCm":171,"WeightKg":96},
           {"Gender":"Male","HeightCm":161,"WeightKg":85},
           {"Gender":"Male","HeightCm":180,"WeightKg":77},
           {"Gender":"Female","HeightCm":166,"WeightKg":62},
           {"Gender":"Female","HeightCm":150,"WeightKg":70},
           {"Gender":"Female","HeightCm":167,"WeightKg":82}]
in_data = json.dumps(in_json)
in_list = json.loads(in_data)

# read reference BMI data
BMI_DF = pd.read_csv("vamstar_challange.csv")

out_data=[]
count = 0
for i in range(len(in_list)):
    out_list = in_list[i]
    h = pow(in_list[i]['HeightCm'] / 100,2) # convert to m2
    m = in_list[i]['WeightKg']
    bmi = m / h # calculate BMI
    bmi_ref_data = (BMI_DF.loc[(BMI_DF['lower_range'] < bmi) & (BMI_DF['upper_range'] > bmi),:]).reset_index(drop=True)
    out_list['catagory'] = bmi_ref_data['catagory'].to_string(index=False)
    out_list['health_risk'] = bmi_ref_data['health_risk'].to_string(index=False)
    out_list['BMI'] = bmi
    out_data.append(out_list)
    if out_list['catagory'] == 'overweight':
        count = count + 1

print("output data with 3 columns added:",out_data)
print("count of overweight people:",count)

