


print()
print()
print()
print()

groups=['','結構','',	'',	'',	'',	'',	'',
	'','壓射系統',	'澆注系統',	'油壓系統',	'',	'',	'',
	'','潤滑系統',	'氮氣',	'電路控制',	'自動噴霧',	'自動取出',	'模具'
	]
items=['格林柱','機架底座',	'模板(定)',	'模板(動)',	'合模',	'曲軸',	'鋼帶',
	'膜厚調節','',	'',	'油管',	'過濾網',	'油箱',	'馬達',
	'電磁閥','',	'',	'',	'',	'',	''
	]
	
id=0	
for item in items:
    id+=1
    # print ({:0>2d}.format(id)+item)
    if (id<10):
        s='0'+str(id)
    else:
        s=''+str(id)
    core='data'+s    
    data='<td>'+groups[id]+'</td>'
    dataa='<td>{{item001.'+core+'a'+'}}</td>'
    datab='<td>{{item001.'+core+'b'+'}}</td>'
    datac='<td>{{item001.'+core+'c'+'}}</td>'
    datad='<td>{{item001.'+core+'d'+'}}</td>'
    datae='<td colspan="2">{{item001.'+core+'e'+'}}</td>'
    
    
    print ('<tr>'+data+'<td>'+item+'</td>'+dataa+datab+datac+datad+datae+'</tr>')
    
    
