# About


       _____ _  _ _____            
       
     |_   _| \| |_   _|___ __  ___
   
       | | | .` | | |(_-< '  \(_-<
   
       |_| |_|\_| |_|/__/_|_|_/__/
          
TNT sms |  Call &amp; SMS Bomber for Iranain Number

TNT sms is a program for Linux that will be transferred to Termux in the future
We want to extract many APIs from Iranian sites and use them to send SMS. Also, the important part of this issue is that the sites do not limit us, for which I have made other plans, such as changing the IP address or user agents.

**Not Support Windows OS**

## Installation

```bash
chmod +x ./install.sh
sudo ./install.sh # install to /usr/local/bin/
sudo tntsms.sh
```

## Usage

```python
from lib.sms import send

num = '09*********'
send(range_n=15, phone_number=num)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
