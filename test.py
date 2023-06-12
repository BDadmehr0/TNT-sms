from requests import post

link = 'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=09050756226'
data = {
}

print(post(url=link, data=data))