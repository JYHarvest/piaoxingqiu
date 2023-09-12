import request
import config
import time
import sys

show_id = config.show_id
session_id = config.session_id
session_id_index = config.session_id_index
buy_count = config.buy_count
audience_idx = config.audience_idx
deliver_method = config.deliver_method
seat_plan_id_index = config.seat_plan_id_index
seat_plan_id = ''
session_id_exclude = []
price = 0
failCount = 0

# 入参从1开始，会做减一处理
if len(sys.argv) > 1:
    if sys.argv[1] == 'zjl':
        show_id = '64f4310635699900017da27a'
        deliver_method = 'ID_CARD'
    elif sys.argv[1] == 'xzq':
        show_id = '64f1c6294f487d00016ab476'
        deliver_method = 'EXPRESS'
    session_id_index = int(sys.argv[2]) - 1
    seat_plan_id_index = int(sys.argv[3]) - 1

print("场次序号:" + str(session_id_index + 1))
print("票价序号:" + str(seat_plan_id_index + 1))
print("交付方式:" + deliver_method)

print("----------------------------------------------------------------")

while True:
    if failCount > 1000:
        print('异常多次，break')
        break
    try:
        milliseconds = int(round(time.time() * 1000))
        # 指定了场次
        if session_id_index >= 0:
            sessions = request.get_sessions(show_id)
            if sessions and sessions[session_id_index]:
                session = sessions[session_id_index]
                print('场次状态:' + session["sessionStatus"])
                if (session["sessionStatus"] == 'PRE_SALE' or session["sessionStatus"] == 'ON_SALE') and session["bizShowSessionId"] not in session_id_exclude:
                    session_id = session["bizShowSessionId"]
                    print("场次Id:" + session_id)
                else:
                    session_id = ''
                    session_id_exclude = []
        else:
         # 未指定场次
         if not session_id:
            while True:
                sessions = request.get_sessions(show_id)
                if sessions:
                    for i in sessions:
                        if (i["sessionStatus"] == 'PRE_SALE' or i["sessionStatus"] == 'ON_SALE') and i["bizShowSessionId"] not in session_id_exclude:
                            session_id = i["bizShowSessionId"]
                            print("场次Id:" + session_id)
                            break
                    if session_id:
                        break
                    else:
                        print("未获取到在售状态且符合购票数量需求的场次id")
                        session_id_exclude = []
        # print("获取场次耗时：" + str(int(round(time.time() * 1000)) - milliseconds) + 'ms')

        if not session_id:
            print("场次Id是空的，继续抢")
            print("----------------------------------------------------------------")
            continue

        seat_plans = request.get_seat_plans(show_id, session_id)
        seat_count = request.get_seat_count(show_id, session_id)

        print("所有票价信息：")
        print(seat_count)

        # 指定了票价
        if seat_plan_id_index >= 0:
            seat = seat_count[seat_plan_id_index]
            print("已选票价信息：")
            print(seat)
            if seat["canBuyCount"] > 0 and seat["canBuyCount"] >= buy_count:
                seat_plan_id = seat["seatPlanId"]
                for j in seat_plans:
                    if j["seatPlanId"] == seat_plan_id:
                        price = j["originalPrice"]  # 门票单价
                        break
        else:
            # 未指定票价
            for i in seat_count:
                if i["canBuyCount"] > 0 and i["canBuyCount"] >= buy_count:
                    seat_plan_id = i["seatPlanId"]
                    for j in seat_plans:
                        if j["seatPlanId"] == seat_plan_id:
                            price = j["originalPrice"]  # 门票单价
                            break
                    break

        print("票价ID:" + str(seat_plan_id))
        print(price)

        if not seat_plan_id:
            print("该场次" + session_id + "没有符合条件的座位，将为你继续搜寻其他在售场次")
            session_id_exclude.append(session_id)
            session_id = ''
            continue

        if not deliver_method:
            deliver_method = request.get_deliver_method(show_id, session_id, seat_plan_id, price, buy_count)

        print("交付方式:" + deliver_method)

        if deliver_method == "VENUE_E":
            request.create_order(show_id, session_id, seat_plan_id, price, buy_count, deliver_method, 0, None,
                                 None, None, None, None, [])
        else:
            audiences = request.get_audiences()
            if len(audience_idx) == 0:
                audience_idx = range(buy_count)
            audience_ids = [audiences[i]["id"] for i in audience_idx]

            if deliver_method == "EXPRESS":
                address = request.get_address()
                address_id = address["addressId"]
                location_city_id = address["locationId"]  # 460102
                receiver = address["username"]
                cellphone = address["cellphone"]
                detail_address = address["detailAddress"]

                express_fee = request.get_express_fee(show_id, session_id, seat_plan_id, price, buy_count,
                                                      location_city_id)

                request.create_order(show_id, session_id, seat_plan_id, price, buy_count, deliver_method,
                                     express_fee["priceItemVal"], receiver,
                                     cellphone, address_id, detail_address, location_city_id, audience_ids)
            elif deliver_method == "VENUE" or deliver_method == "E_TICKET" or deliver_method == 'ID_CARD':
                request.create_order(show_id, session_id, seat_plan_id, price, buy_count, deliver_method, 0, None,
                                     None, None, None, None, audience_ids)
            else:
                print("不支持的deliver_method:" + deliver_method)
        break
    except Exception as e:
        print(e)
        session_id_exclude.append(session_id)
        session_id = ''
        failCount = failCount + 1

