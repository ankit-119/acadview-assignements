import re
num="123456789 23456789 +918968774768 +916785432191 919674399503 912345678901"
res=re.findall(r'[+]91[6-9]{1}\d{9}',num)
print(res)
