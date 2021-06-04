import json

import conf
import seat
import util


def reserve_seat(seat_key, lib_id):
    r = util.fast_post(conf.graphql['reserve'] % (seat_key, lib_id))
    r_json = json.loads(r.text)
    if 'errors' not in str(r_json):
        print("预定成功")
        return True
    # print(r_json['errors'][0]['msg'])
    return False


def reserve_conf_seat():
    seats = seat.scan_seats()
    seat_key = seats[conf.seat_key]['key']
    lib_id = conf.lib_id
    return reserve_seat(seat_key, lib_id)


def reserve_often_seat():
    often_seats = seat.often_seats()
    for often_seat in often_seats.values():
        if reserve_seat(often_seat['seat_key'], often_seat['lib_id']):
            return True
    return False


def reserve_random_seat():
    first_unused_seat = seat.scan_unused_seat()
    if first_unused_seat is None:
        return False
    seat_id, seat_info = first_unused_seat
    return reserve_seat(seat_info['key'], conf.lib_id)


def reserve():
    if conf.lib_id is None:
        print("常用位置预定")
        return reserve_often_seat()
    elif conf.seat_key is None:
        print("随机预定")
        return reserve_random_seat()
    else:
        print("指定座位预定")
        return reserve_conf_seat()
