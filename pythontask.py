# # def calculate(a,b):
# #     c = a+b
# #     sub = c - 2
# #     multi = sub * 3
# #     if multi >20:
# #         return True
# #     elif multi >10 and multi <=20:
# #         return "Ok"
# #     else:
# #         return False
    
# # def main(a,b):
# #     output = calculate(a,b)
# #     return output


# # final = main(10,3)
# # print(final)
# # # for i in final:
# # #     print(i)

# def get_largest_number(a,b,c):
#     """ this function returns the largest number from the given inputs"""
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     else:
#         if b>c:
#             return b
#         else:
#             return c
        
# x = get_largest_number(100,50,70)   
# print(x)   

# sentence = "  I am a data analyst  "
# print(len(sentence))
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.capitalize())
# print(sentence.count(" "))

# print(len(sentence))

# list_of_num = [1,22,"bhavana",4,[5,9],6,7,8]
# print(len(list_of_num))
    
# dict_of_profile = {"name":"bhavana", "age":23, "role":"data analyst"}
# print(len(dict_of_profile))      
# print(dict_of_profile["name"])

# list_num = [1,2,3,4,5,6,7,8,"asd"]
# print(sum(list_num))


# def get_name():
#     return 'bhavana'

# import pandas as pd 

# def read_df(n):
#     df = None
#     try:
#         df = pd.read_csv(r"C:\Users\Acer\Documents\Supermart_dataset.csv")
#     except Exception as e:
#         print("Exception in read_df():   ", e)
#     finally:
#         return df, n

# # read_df()

# def main(n):
#     df, mul = read_df(n)
#     name = "bhavana "
#     # n_names = name * mul
#     # print(df)
#     return name, df, mul
    
# name = main(3)
# print(name)

def input_name(sent):
    sent = sent.lower()
    if 'a' in sent or 'e' in sent or 'i' in sent or 'o' in sent or 'u' in sent:
        return True, sent
    else:
        return False
print(input_name("I AM A DATA ANALYST"))



        