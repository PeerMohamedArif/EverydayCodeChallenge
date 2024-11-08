# # # file not found exception
# # try:
# #     file =open("a_file.txt")
# #     a_dictionary={
# #         "key": "value"
# #     }
# #     #print(a_dictionary["keywefkjns"])
# #     print(a_dictionary["key"])
# # except FileNotFoundError:
# #     file=open("a_file.txt","w")
# #     file.write("something")
# # except KeyError as error_message :
# #     print(f"the key {error_message} does not exist")
# # else:
# #     content=file.read()
# #     print(content)
# # finally:
# #     # file.close()
# #     # print("file was closed")
# #     #raise KeyError
# #     raise TypeError("This is an error i made up")
# #
#
#
# height= float(input("height"))
# weight= int(input("weight"))
#
# if height>3:
#     raise ValueError("Human height cannot be more than 3 meters.")
#
# bmi=weight/ height**2
# print(bmi)
