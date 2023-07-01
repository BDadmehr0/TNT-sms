#!/bin/bash
sudo apt install -y python3
pip install -r ./requirements.txt

script_path=$(pwd)
tntsms_content="#!/bin/bash\n\ncd $script_path\npython3 main.py"

echo -e $tntsms_content > /usr/local/bin/tntsms.sh
chmod +x /usr/local/bin/tntsms.sh
