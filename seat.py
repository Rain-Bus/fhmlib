import json

import conf
import util


def often_seats():
    r = util.fast_post(str(conf.graphql['home']).encode('utf-8'))
    r.encoding = 'utf-8'
    json_obj = json.loads(r.text)
    often_seat_obj = json_obj['data']['userAuth']['oftenseat']['list']
    seats = {}
    for seat in often_seat_obj:
        seats[seat['id']] = {'lib_id': seat['lib_id'], 'seat_key': seat['seat_key']}
    return seats


def scan_seats():
    data = str(conf.graphql['list_seats']).encode("utf-8") % conf.lib_id
    r = util.fast_post(data)
    # 获取座位映射关系以及状态
    seats_info = json.loads(r.text)['data']['userAuth']['reserve']['libs'][0]['lib_layout']['seats']
    seats = {}
    for seat in seats_info:
        if seat['name'] is not None and str.isnumeric(seat['name']):
            seats[int(seat['name'])] = {'key': seat['key'], 'status': seat['status']}
    return seats


def scan_unused_seat():
    all_seat = scan_seats()
    for seat in all_seat:
        if not all_seat[seat]['status']:
            return seat, all_seat[seat]
    return None
