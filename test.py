from requests import post

link = 'https://www.buskool.com/send_verification_code'
data = {
    "Parameters": {
        "ApplicationType":"Web",
        "ApplicationUniqueToken":"null",
        "ApplicationVersion":"1.0.0",
        "MobileNumber":"09050756226",
        "UniqueToken":"null"}
}

print(post(url=link, data=data))

