#!/bin/bash
script_path=$(pwd)
tntsms_content="#!/bin/bash\n\ncd $script_path\npython3 main.py"

echo -e $tntsms_content > /usr/local/bin/tntsms.sh
