import requests
import json

response= requests.get('https://api.lorem.space/image/fashion?w=640&h=480&r=9350')
print(response.content)


# response= requests.get("https://api.escuelajs.co/api/v1/products/?categoryId=1")
# data= json.loads(response.content)
# product_list= [value for value in data[:4]]
# productlst= []
# print(data[0])

# for product in json.loads(response.content)[:4]:
#     productlst.append({
#                 "thumbnail":{
#                     "image": product['images'][0]
#                     },
#                     "title": product['title'],
#                     "price": product['price'],
#                     "description":"",
#                     "actionables":[
#                         {
#                             "actionable_text":"View Scorecard",
#                             "location_required": False,
#                             "is_default":0,
#                             "uri":"CAROUSEL_DETAIL",
#                             "type":"APP_ACTION",
#                             "payload":{
#                                 "title": product['title'],
#                                 "price": product['price'],
#                                 "description": product['description'],
#                                 "images":[
#                                     "http://haptikappimg.s3.amazonaws.com/Cricket_Images/Match_Scorecard/Innings_Score_Batting_1_186013_1_1523189431.png",
#                                     "http://haptikappimg.s3.amazonaws.com/Cricket_Images/Match_Scorecard/Innings_Score_Batting_2_186013_1_1523189432.png",
#                                     "http://haptikappimg.s3.amazonaws.com/Cricket_Images/Match_Scorecard/Innings_Score_Bowling_186013_1_1523189431.png"
#                                     ],
#                                     "gogo_message":"",
#                                     "link":""
#                                     },
#                                     "emoji":""
#                                     }
#                                 ]
#             })

# print(productlst[0])

