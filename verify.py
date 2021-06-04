# import base64
# import json
#
# import muggle_ocr
#
# import conf
# import util
#
#
# def get_code():
#     r = util.fast_post(str(conf.graphql['get_code']).encode('utf-8'))
#     if 'error' in r.text:
#         raise Exception(r.text)
#     captcha_obj = json.loads(r.text)['data']['prereserve']['captcha']
#     code_id = str(captcha_obj['code'])
#     code_img = str(captcha_obj['data'])
#     print(r.text)
#     return code_id, code_img
#
#
# def identify_code(img_str):
#     sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
#     base64_str = img_str.removeprefix("data:image/jpg;base64,")
#     pic = base64.b64decode(base64_str)
#     text = sdk.predict(pic)
#     print(text)
#     return text
#
#
# def submit_code(code, res):
#     r = util.fast_post(str(conf.graphql['submit_code']) % (res, code))
#     print(r.text)
