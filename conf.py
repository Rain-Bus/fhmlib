import json

url = "https://wechat.v2.traceint.com/index.php/graphql/"

cookies = {}

header = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 "
                  "Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI "
                  "MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200) "
}

seat_key = 0
lib_id = 0
interval = 0
retry_times = 0

graphql = {
    "home": "{\"operationName\":\"index\",\"query\":\"query index($pos: String!, $param: [hash]) {\\n userAuth {\\n "
            "oftenseat {\\n list {\\n id\\n info\\n lib_id\\n seat_key\\n status\\n }\\n }\\n message {\\n new(from: "
            "\\\"system\\\") {\\n has\\n from_user\\n title\\n num\\n }\\n }\\n reserve {\\n reserve {\\n token\\n "
            "status\\n user_id\\n user_nick\\n sch_name\\n lib_id\\n lib_name\\n lib_floor\\n seat_key\\n "
            "seat_name\\n date\\n exp_date\\n exp_date_str\\n validate_date\\n hold_date\\n diff\\n diff_str\\n "
            "mark_source\\n isRecordUser\\n isChooseSeat\\n isRecord\\n mistakeNum\\n openTime\\n threshold\\n "
            "daynum\\n mistakeNum\\n closeTime\\n timerange\\n forbidQrValid\\n renewTimeNext\\n forbidRenewTime\\n "
            "forbidWechatCancle\\n }\\n getSToken\\n }\\n currentUser {\\n user_id\\n user_nick\\n user_mobile\\n "
            "user_sex\\n user_sch_id\\n user_sch\\n user_last_login\\n user_avatar(size: MIDDLE)\\n user_adate\\n "
            "user_student_no\\n user_student_name\\n area_name\\n user_deny {\\n deny_deadline\\n }\\n sch {\\n "
            "sch_id\\n sch_name\\n activityUrl\\n isShowCommon\\n isBusy\\n }\\n }\\n prereserve {\\n "
            "prereserveCheckMsg\\n }\\n }\\n ad(pos: $pos, param: $param) {\\n name\\n pic\\n url\\n }\\n}\","
            "\"variables\":{\"pos\":\"App-首页\"}}",
    "list_seats": "{\"operationName\":\"libLayout\",\"query\":\"query libLayout($libId: Int, $libType: Int) {\\n "
                  "userAuth {\\n reserve {\\n libs(libType: $libType, libId: $libId) {\\n lib_id\\n is_open\\n "
                  "lib_floor\\n lib_name\\n lib_type\\n lib_layout {\\n seats_total\\n seats_booking\\n seats_used\\n "
                  "max_x\\n max_y\\n seats {\\n x\\n y\\n key\\n type\\n name\\n seat_status\\n status\\n }\\n }\\n "
                  "}\\n }\\n }\\n}\",\"variables\":{\"libId\":%d}}",
    "reserve": "{\"operationName\":\"reserveSeat\",\"query\":\"mutation reserveSeat($libId: Int!, $seatKey: String!, "
               "$captchaCode: String, $captcha: String!) {\\n userAuth {\\n reserve {\\n reserveSeat(\\n libId: "
               "$libId\\n seatKey: $seatKey\\n captchaCode: $captchaCode\\n captcha: $captcha\\n )\\n }\\n }\\n}\","
               "\"variables\":{\"seatKey\":\"%s\",\"libId\":%d,\"captchaCode\":\"\",\"captcha\":\"\"}}",
    "pre_reserve": "{\"operationName\":\"save\",\"query\":\"mutation save($key: String!, $libid: Int!, $captchaCode: "
                   "String, $captcha: String) {\\n userAuth {\\n prereserve {\\n save(key: $key, libId: $libid, "
                   "captcha: $captcha, captchaCode: $captchaCode)\\n }\\n }\\n}\",\"variables\":{\"key\":\"13,60\","
                   "\"libid\":114118,\"captchaCode\":\"\",\"captcha\":\"\"}}",
    "get_code": "{\"operationName\":\"getStep0\",\"query\":\"query getStep0 {\\n userAuth {\\n prereserve {\\n "
                "getNum\\n captcha {\\n code\\n data\\n }\\n }\\n }\\n}\"}",
    "submit_code": "{\"operationName\":\"setStep1\",\"query\":\"mutation setStep1($captcha: String!, $captchaCode: "
                   "String!) {\\n userAuth {\\n prereserve {\\n verifyCaptcha(captcha: $captcha, "
                   "code: $captchaCode)\\n setStep1\\n }\\n }\\n}\",\"variables\":{\"captcha\":\"%s\","
                   "\"captchaCode\":\"%s\"}} "
}


def get_info():
    with open("./conf.json", "r") as f:
        global cookies, lib_id, seat_key, retry_times, interval
        json_obj = dict(json.load(f))
        cookies = json_obj['cookies'] \
            if json_obj.__contains__('cookies') and json_obj['cookies'] != '' else None
        seat_key = int(json_obj['seat_key']) \
            if json_obj.__contains__('seat_key') and json_obj['seat_key'] != '' else None
        lib_id = int(json_obj['lib_id']) \
            if json_obj.__contains__('lib_id') and json_obj['lib_id'] != '' else None
        retry_times = int(json_obj['retry_times']) \
            if json_obj.__contains__('retry_times') and json_obj['retry_times'] != '' else 30
        interval = int(json_obj['interval']) \
            if json_obj.__contains__('interval') and json_obj['interval'] != '' else 60
