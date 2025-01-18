import re 

phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumregex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
print(phonenumregex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

