# https://docs.python.org/2/tutorial/datastructures.html
cola=['外部主件','','','','','','','','控制系统','','','压射系统','澆注系統','油壓系統','潤滑系統','氮氣','锁模系统','自動噴霧','自動取出','模具',]
colb=['格林柱','機架底座','模板(定)','模板(動)','合模','曲軸','鋼帶','保温炉','膜厚調節','主电箱','操作面板','','','','','','','','','',]
colc=['格林柱','機架底座','模板(定)','模板(動)','油路板|合模油缸油路板|合模油缸','曲轴销|衬套曲轴销|衬套','鋼帶','炉盖|加热管|电线|感温棒','开关','电路板|保险丝|保温炉控制器电路板|保险丝|保温炉控制器','控制面板','行程开关|射杆 连接板|料管|射杆接头','链条齿轮|链条|铜套|编码器|接触开关',',油管|過濾網|油箱|馬達|電磁閥','油嘴|分油器|油管|油泵','氮气钢瓶|氮气瓶油封 轴承带','电子尺','雾化器|喷雾机板|铜管|电磁阀|缓冲器','取件机手臂|缓冲器|夹手|轴承|马达','模芯|顶针|滑块|定模仁|动模仁|油缸',]

rem=['磨損|無法修復','磨損|裂縫|漏油','平面變型|無法修復','平面變型|無法修復','合模缸漏油|合模缸螺旋斷裂|合模活塞磨損|無法修 復','磨損|無法修復','磨損|斷裂|無法修復','磨損|斷裂|無法修復|炉盖损坏|加热管断|电路断|温度不准','開關損壞|線路不通|短路|無法修復','保险丝烧坏|線路不通|無法修復','按键损坏|系统坏|無法修復','無壓力|線路不通|壓射缸漏油|射杆彎曲|连接板断裂|开关无信号|料管磨损|接头断','链条断|齿轮滑牙斷|編碼器異常|銅套磨損','破損|斷裂|接頭滑絲|堵塞|油品變質|磨損|軸心斷裂|線路不通|閥心斷裂','管道不通|管 道斷裂|泵心磨損','鋼瓶裂縫|壓力過高|壓力過低|磨损','读数不准','霧化器損壞|線路不通|緩衝彈簧斷裂|喷头螺丝滑牙|断裂|漏水',
'手臂断裂|夹手磨损|缓冲器坏|手臂轴承坏|内部烧坏','尺寸NG|模崩|模芯斷|顶针斷|重覆修模|待修模',]

# for i in range (1, 20):
#     print (cola[i])
v=0
for  v1,v2,v3,v4 in zip(cola,colb,colc, rem):
    # print ("    <tr><th>{0:s}</th><th>{1:s}</th><td>{2:s}</td><td></td><td></td><td></td><td colspan='2'>{3:s}</td></tr>".format(v1,v2, v3,v4))
    v += 1
    a='    data{0:02d}a = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 零件")'.format(v, v1, v2)
    b='    data{0:02d}b = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度一")'.format(v, v1, v2)
    c='    data{0:02d}c = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度二")'.format(v, v1, v2)
    d='    data{0:02d}d = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度三")'.format(v, v1, v2)
    e='    data{0:02d}e_00 = models.NullBooleanField(verbose_name="{1:s} {2:s} 備註說明  正常")'.format(v,v1, v2)

    print("###")
    # print(a)
    
    # data01e_00 = models.NullBooleanField(verbose_name="格林柱-備註說明-正常")
    # data01e_01 = models.NullBooleanField(verbose_name="格林柱-備註說明-磨損")
    
    if (len(v3)>0):
        parts = v3.split("|")
        i=1
        for part in parts:
            # print (part)    
            axx='    data{0:02d}a_{1:02d} = models.NullBooleanField(verbose_name="{2:s} {3:s} 零件  {4:s}")'.format(v,i,v1, v2, part)
            print (axx)    
            i += 1
            
    print(b)
    
    print(c)
    print(d)
    print(e)
    
    
    if (len(v4)>0):
        rems = v4.split("|")
        i=1
        for rem in rems:
            # print (rem)    
            exx='    data{0:02d}e_{1:02d} = models.NullBooleanField(verbose_name="{2:s} {3:s} 備註說明  {4:s}")'.format(v, i, v1,v2,rem)
            print (exx)    
            i += 1
            
            
            
    
    # data01a = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    # data01b = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    # data01c = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    # data01d = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    # data01e = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明", choices=CHOICE01)
    
    # data01e_00 = models.NullBooleanField(verbose_name="格林柱-備註說明-正常")
    # data01e_01 = models.NullBooleanField(verbose_name="格林柱-備註說明-磨損")
    # data01e_02 = models.NullBooleanField(verbose_name="格林柱-備註說明-無法修復")
 