info={"id1":{"Name":"Sashuel","Age":"13","City":"Chennai"},
      "id2":{"Name":"Villain","Age":"12","City":"Mumbai"},
      "id3":{"Name":"Sashuel","Age":"13","City":"Chennai"}}

result={}
for key,value in info.items():
    if value not in result.values():
        result[key]=value

print(result)