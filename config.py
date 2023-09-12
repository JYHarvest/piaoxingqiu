# 输入自己的token
token = 'eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkMFOwzAQRP9lzznYjuPGPRaBQGqFVNEDJ-Q4azVSbFeOg4Cq_84GI-gJ5JNXM2925wzRzPn4EFyEdZjHsYJ5wlT-Z-iGj5vYI6zh7n77soMKprnb_AyVUCvTMsRe8LaRYtUqx6WWpCPnPo6LaHN4vt3TxGd7WND9YpSuF42rG3RWccYYV4TpTDH-J7NwqQDfTkPCp8FTBldaS91oUZPmC_F4wmRy_BPTUZpNaPIvRcqaC3pM0aXvU0ZfLi3NeEz2aEK-bovWuM6v4BXTNMRAw1JlMP4bcPkEAAD__w.LDebDi7BsxvZ_W4AU14wKY7vSbwPQWCionFUHkUN23aabQNClObVITaJqUEqhq-dvcJ6bVEZc7iEuq21bJ4ys8rYfVKiCKWqxumF2NZqzJEIBfsZPG5JiZt7VuSdNkw1MO_ykmztPlbEVLk9pRW9OU71LflA_dNshlP8Xz36mWk'
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