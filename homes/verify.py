import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('./yotearriendo.json')
default_app = firebase_admin.initialize_app(cred)

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjE1ZjUyYTRhNGE5Y2MzNmZjOGEyNWZmMmQ0NzY4NmE0OGM2YjcxZWQifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20veW90ZWFycmllbmRvLWQ1MzJmIiwibmFtZSI6IkplcnNvbiBMb3BleiBDYXN0YcOxbyIsInBpY3R1cmUiOiJodHRwczovL2xoNS5nb29nbGV1c2VyY29udGVudC5jb20vLVMteVJQY0p4UGxJL0FBQUFBQUFBQUFJL0FBQUFBQUFBUW9RL3pRRy1sRElkbVhZL3Bob3RvLmpwZyIsImF1ZCI6InlvdGVhcnJpZW5kby1kNTMyZiIsImF1dGhfdGltZSI6MTUyODI5MDU5MywidXNlcl9pZCI6InViT0VxZnA5WkhQMGdMNGxrb1licm5hb3R3RzMiLCJzdWIiOiJ1Yk9FcWZwOVpIUDBnTDRsa29ZYnJuYW90d0czIiwiaWF0IjoxNTI4MjkwNTkzLCJleHAiOjE1MjgyOTQxOTMsImVtYWlsIjoiamVyc29ubG9wZXouMTIwNEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExNTY3NTQ2NzUxOTA3NTA3NTEyNCJdLCJlbWFpbCI6WyJqZXJzb25sb3Blei4xMjA0QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.fGU-1ox_wJdC7IAj1fryAbhsfTQtJ2uUpAWE0qeUCD2MMTXOFrJ9F7pwAweNx4gK2yzJnCfyHzkWux7XnyXglXl2qPbrXUw97WVdfjWIySKjk2HmCoeFG0rO2DSrxsitl5e7kCRlxflGTMdp6JZclurYSIhu0kGaEPRpCfE6Hi1MG5loQi5_Srl4XCK10-R61pONlKprd8PMGt2ubrxQuz8BNoFLGtX5awzU0D70N6tuhSBU_x3rzV-RJa4aPRc106mW8dYvo8eZzoa4rpAuBQMj-T46d843oL3MYYyZ7ODquWBLZ0MeFQI4HULlot4CQEGqI6WM9NU28oB-V4x4sw"

def verificar(id_token):
    response = ""
    try:
        decoded_token = auth.verify_id_token(id_token)
        response = decoded_token['uid']        
    except ValueError as err:
        print("\nHubo un error decodificando el Token: \n\n",err)
        response = "Error"
    #print(response)
    return response

#verificar(token)

