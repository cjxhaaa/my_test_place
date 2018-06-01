
_credit = {"security_code":"123|3456"}
codes = [x for x in _credit["security_code"].split('|') if x.strip()]
assert len(codes) == 2
codes.sort(key=lambda x:len(x))
_credit["security_code"],_credit["other_security_code"] = codes
print(_credit["security_code"])
print(_credit["other_security_code"])