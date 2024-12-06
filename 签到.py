import json
import requests

def aes_decrypt(response: bytes) -> str:
    # 设置密钥
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    key = b'e82ckenh8dichen8'  # 在ECB模式下，加密和解密时都使用相同的密钥

    # 初始化AES解密器
    decipher = AES.new(key, AES.MODE_ECB)

    # 解密数据
    plain_text = unpad(decipher.decrypt(response), AES.block_size)

    return plain_text.decode('utf-8')
def sign_data(cookies,headers):
    import requests
    data = {
        'params': 'F7134374847BA31B43090F226D58DEC1590A150550241E497A98FB1E7A8C95A8C3AA94370FB43643B6D6086E47BDA11A9D7CA4F6749261A0393179CB405BB1B9F825BD1E4A1B628C251A3C215C33D9F12AA9D5892580D1355629EF705C0DA88E729E0C319304F10C51A3B01590C01C4B279FB03A74D1C73C863D67754B20664FC591886DA40D50AC0D668B96529A30003DF3B7A7C72D0DCBF455B99FAF2BB5EA8C3D1C416130513D78114FB5B7BBEF2C4F36480D80EA7E52424386F5C7AAC016C9EB3741FE0A41A7FA6C7D1703D534A4EBDBBDE07B650FFA912E68B1C34C81949546ED358463A9EBF6A27AFD2F53BE25572D4E93E9EC473ED9B769CD2A01C661B880C696DEC532D9351BB17E5ECA4563A0986B162BDF7EA9CE9CCA08C7E4D17D8D304C8E4BF061FA48D5CB3180981B6B5719C00E5A9B71712AE8C7AC4A2E57872C834703E335B7D5F7EF30CB0B9227AC11112BF801A4479AACAC8C9DCE253F57375E39069D593AF19F4039D303C10B8E5063C631113EE4E80C1EB7BDBD161422826080A7FDB4925E045C654D46B39DC312FB2128F5EEEF7A2EFB8AD7E5E16865285E3F8E3D05F67DFC390DF927E55082337D3419CD3847E1AA13E9652D6512A8E2DB05CC258A728BC29DA096D076B603716339E57363B991FB43BA9B9F49C04E2AF472BFAB543598065E22173835AE98',
    }
    response = requests.post(
        'https://interface.music.163.com/eapi/pointmall/sign/calendar',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    count = 0
    print(response.text)
    data = aes_decrypt(response.content)
    print(data)
    a = json.loads(data)['data']['signStr']
    for i in a:
        # 计算a中有多少个1
        if i == '1':
            count += 1
    return count
headers = {
    "Host": "interface.music.163.com",
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded",
    "mconfig-info": "{\"IuRPVVmc3WWul9fT\":{\"version\":727040,\"appver\":\"3.0.19.203184\"}}",
    "origin": "orpheus://orpheus",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Chrome/91.0.4472.164 NeteaseMusicDesktop/3.0.19.203184",
    "sec-ch-ua": "\"Chromium\";v=\"91\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-language": "en-US,en;q=0.9"
}



def main(headers,cookies):
    url = "https://interface.music.163.com/eapi/pointmall/user/sign/config"
    data = {
        "params": "6E0B1C712DCB3648589D7C950C2962047DBCDFC62BE06D88339A32CA6644156A83B31EBCEA2406A063CEA88FC25A3AF34BA7D00D569EE24FF6D65FBBDFE1EE111A507ACDCB61A2F6A1C1D943BA4AD956781DB7A399C3CC3C530E9D58E362A8F29D49F93A8158563E7A6C6F00C510752D3164E3B4938B25F1CB2FC3700F7CCDCE24F4B8D85348766392A14A95D492B30E0E278B8AFCD79A8D2E4858B7EB287F825C85B16F8E02556B0D240F2F75FFC5E57FAB77AA8C9567B44062BAF28748CF508BB499CC50AEDD3E563D9DE393C219FA388FD6842F32DFBAD1EBBC2951BB26CA816BEFBA40C9518E788E973BAD20A83EF36A27F128F70CB3987E082812B46772F01B5514AF1EB08AB7D298DB4D651878505F481B4BD40B87792CAF552BB3E51B05CA3D80687C1D3C2AF35549632EF0B8AD24EE6784866633C9A3971447E6D05D3D5685A72136665253913E3AC6F6ACD92E727BD3B4E471290E89296495CAA41BE9D4AC595A19E151D21568F41F0F4CEF1B71C4D935BDF95D0BFC7E4CCE0FBB3D6DDBE0ECC150ADB9B79337E5BA02A6B7BB30337CF94FB914B01DC0279B6C3BD18A56ADC281A3BC7F2C8E59AA11C967FC518FB954745135FD00B07E5470F59ABF3C575E26D00803A4DF00E5EB63D60A6FF7E0FB25EA2A4934588AE67A8AB9A23500EDC4DF09EEE21F68B83FADF7E1EA826AA3B102FBE7296AB0DB9EA5C46AD12B"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    print(aes_decrypt(response.content))
    # input('adsfasdf')

    url = 'https://wxpusher.zjiecode.com/api/send/message'
    headers_wx = {
        'Content-Type': 'application/json'
    }
    data = {
        "appToken": "AT_RnS6I8R8Zx8wRNjqs7fw7XHIEZ2OBi6R",
        "content": "<h1>H1标题</h1><br/><p style=\"color:red;\">欢迎你使用WxPusher，推荐使用HTML发送</p>",
        "summary": f"第{sign_data(cookies, headers)}天签到成功",
        "contentType": 2,
        "topicIds": [
            123
        ],
        "uids": [
            "UID_XHNfkTMaoZ9QWKQhhrRG8iHBKSJu"
        ],
        "url": "https://wxpusher.zjiecode.com",
        "verifyPay": 'false',
        "verifyPayType": 0,
    }
    data = json.dumps(data, separators=(",", ":"))
    res = requests.post(url, data=data, headers=headers_wx).json()
    print(res)


if __name__ == '__main__':
    cookies_150 = {
        "os": "pc",
        "deviceId": "5153BC83D4BD25F7EB89768640DF09370BDCD53350EBF6C3BB1F",
        "osver": "Microsoft-Windows-10-Home-China-build-22631-64bit",
        "WEVNSM": "1.0.0",
        "ntes_kaola_ad": "1",
        "_ntes_nuid": "f79fd25dc539466a795b73b708e9451e",
        "_ntes_nnid": "f79fd25dc539466a795b73b708e9451e,1704246135708",
        "_iuqxldmzr_": "33",
        "channel": "netease",
        "NMTID": "00OTebWX4KtZO8F-EFrnUAbAFnxhIkAAAGEGL8wvg",
        "mode": "ASUS TUF Gaming F15 FX507ZC_FX507ZC",
        "appver": "3.0.19.203184",
        "clientSign": "50:EB:F6:C3:BB:1F@@@303030305F303030305F303030305F303030305F413432385F423730325F363241335F303043332@@@@@@65c4e9b662c3503ef4141b671eae7112ac6c4760c1f57ed03e95fdaf6a36c231",
        "__csrf": "8045d7b4a64ce5bd73c0509f826d9669",
        "WNMCID": "zmorrj.1733310688792.01.0",
        "__remember_me": "true",
        "MUSIC_U": "00D14E593EA724655601A62AF210B3F9E8496440B8BF9CDDE5433E23E9D514E3021481F7CE974971452FE9010F483190CF08797951CF67CAF974FAE47C6396CD7A74AEA0B33827793B8E028F673D09D1501D2BE0A152037CF4089EEB7F8B42982E453AD07E9E52B252670892152D888A648A025AF4EF5390E15C9A5C69857541B495F93F098AD278015EE4D8C9AF42DD191CB04617ED3B521A1B1682CAF15C7B7E6DCB25D5F327F63E5CF6A3EEB7FC6CFD5A3C0F1C6B48034411CA50ECD2930B40F273E2F356FCADBC83EF54DAEE8DB1CBDC66FDDFADA6E3E4850BDE5543782451B3C4E18AA2FDD61D2D2B9284F919B16D44A6FA1E2BDE8D3D4B373FC43305B3F5D8EAE32F1596E12B5B827CBCD015D60408BFE0AFA32DA15409E910972D5C291DC46C3E7C989845AEAD31B4FDFAA7413548A44C3A17D4C28811BB6281C6B8D0D902089E248A05E00FF737CD03AADF552E746CDA33370A3A89EF6F02A6678E9ADB1B041B2BA7DC35F08CBA98B224A40C5488659B726FD3EEAA2B9553654A924BF55F3D8D3DBB17D4ED6F29F94146F187B4B67AC4CD4438A9D9B2FC4EFC1CD0E48CACFDD22D57526A24FA8F4E11F692F87660EF84938C2865382ADFEADF9A5692F3",
        "JSESSIONID-WYYY": "AwHjOzmUbPpGEdTgEUDxk2%2FPdeoE9o2vKjdP4hjBZreyemui%2FO%2B5gpCcd6YHB6VQBG2BjfuUOThDzuG7ulg1rQdjem2JzVhnY3bU29bP56uP5Z9eXBjErZxW%2Fpg2IHR51Et9OeOPFSF8HVhkJNQPYc%5C%2B6NSia4l0l3hWE5ioMaKsqMnh%3A1733312854328"
    }
    main(headers, cookies_150)
