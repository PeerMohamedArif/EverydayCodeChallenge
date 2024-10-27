# # with open ("weather_data.csv") as data_file:
# #     data=data_file.readlines()
# #     print(data)
#
# # import csv
# # with open ("weather_data.csv") as data_file:
# #     data=csv.reader(data_file)
# #     temperature=[]
# #     for row in data:
# #         if row[1]!= 'temp':
# #             temperature.append(row[1])
# #     print(temperature)
# #
# #     for i in range(0,len(temperature)-1):
# #         print(temperature[i])
#
# import pandas as pd
# #data=pd.read_csv("weather_data.csv")
# #print(data)
# #print(type(data["temp"]))
# #print(type(data))
# #
# # # print(data.to_dict())
# # temp_list=data["temp"].tolist()
# # # print(temp_list)
# # print((data['temp']).mean())
# # print((data['temp']).max())
# #
# # print(data.condition)
#
# # print(data.iloc[0])
# # print("\n\n\n")
# # print(data[data['day']=='Monday'])
#
# # print(data[data['temp']==data['temp'].max()])
# # print (data[data['day']== 'Monday'])
# # print(data[data.temp == data.temp.max()])
# # monday=data[data['day']== 'Monday']
# # monday['temp']=monday['temp']*1.8 +32
# # print(monday)
#
# # create a dataframe from scratch
# # data1={
# #     "students":["Amy","James","Arif"],
# #     "scores":[76,56,100]
# # }
# # data2=pd.DataFrame(data1)
# # print(data2)
# # data2.to_csv("new.csv")
#
# # CENTRAL PARK SQUIRREL DATASET BELOW
# import pandas as pd
#
# data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrel_count=len(data[data['Primary Fur Color']=="Gray"])
# red_squirrel_count=len(data[data['Primary Fur Color']=="Cinnamon"])
# black_squirrel_count=len(data[data['Primary Fur Color']=="Black"])
# print(grey_squirrel_count)
# print(red_squirrel_count)
# print(black_squirrel_count)
#
# data_dict={
#     "fur_color":["grey","cinnamon","black"],
#     "Count":[grey_squirrel_count,red_squirrel_count,black_squirrel_count]
# }
#
# print(data_dict)
# df=pd.DataFrame(data_dict)
# print(df)
# df.to_csv("squirrel_count")
# 
#
#
