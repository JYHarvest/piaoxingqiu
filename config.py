# 输入自己的token
token = ''
# 项目id，必填
show_id = ''
# 指定场次id，不指定则默认从第一场开始遍历
session_id = ''
# 场次序号，从0开始;-1表示按session_id来
session_id_index = 0
# 购票数量，一定要看购票须知，不要超过上限
buy_count = 2
# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0,1]
# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
# 薛之谦EXPRESS；周董ID_CARD
deliver_method = ''
# 票价序号，从0开始;-1表示按顺序遍历所有票
seat_plan_id_index = -1