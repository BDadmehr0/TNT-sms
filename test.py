from requests import post

link = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
data = {
    "Parameters":{
        "ApplicationType":"Web",
        "ApplicationUniqueToken":"null",
        "ApplicationVersion":"1.0.0",
        "MobileNumber":"09050756226",
        "UniqueToken":"null"
    }
}


print(post(url=link, data=data).text)
