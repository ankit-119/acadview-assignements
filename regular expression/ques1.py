import re
string="asdfgdhefjmdsdfvg ankitkaushik066@gmail.com asdfgfhndbgvcxhj ankitkaushik067@gmail.com"
res=re.findall(r'[A-Za-z]\w*@\w+[.]com',string)
print(res)
