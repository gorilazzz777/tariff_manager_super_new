# from datetime import datetime
#
# import requests
#
# max_time = 0
# for n, _ in enumerate(range(40)):
#     s = datetime.now()
#     ss = requests.get('https://notifications.boxberry.ru/api/notification?message=Посылка 0000470881969 выдана. Получатель: Андрусенко Дмитрий Сергеевич&clientId=79257860365&order_list=P&number=0000989898561&order_id=23082023%D1%82%D0%B5%D1%81%D1%827',
#                       headers={'Notify-Access-Token': 'xtiparJ3iYwMd0T9LlDCILBOROpDjZVBUJCw9aKZRUbLRr32C5fI8yW9'})
#     sss = datetime.now()
#     print(f'{n} - {(sss - s).total_seconds()}')
#     if (sss - s).total_seconds() > max_time:
#         max_time = (sss - s).total_seconds()
# # print(f'начало: {s}, финиш - {sss}, time = {(sss - s).total_seconds()}')
# # print(ss.text)
# print(max_time)


s = {'a': 1}
if list(s.values())[0] == 1:
    print(True)