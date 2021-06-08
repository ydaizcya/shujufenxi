import pandas as pd
import shuju
import xlwt
# 数据转换
team_data = shuju.team_data()
team_data = pd.DataFrame(team_data)
pers_data = shuju.pers_data()
pers_data = pd.DataFrame(pers_data)
hero_name = shuju.hero_name()
hero_name = pd.DataFrame(hero_name)
hero_data = shuju.hero_data()
hero_data = pd.DataFrame(hero_data)
# 数据存入excel
with pd.ExcelWriter(r'C:\Users\Administrator\Desktop/lol数据分析2.xlsx') as write:
    team_data.to_excel(write, sheet_name='战队数据', index=False)
    pers_data.to_excel(write, sheet_name='队员数据', index=False)
    hero_name.to_excel(write, sheet_name='英雄名称', index=False)
    hero_data.to_excel(write, sheet_name='英雄数据', index=False)
    write.save()
write.close()
# def save_data():
#     pf = shuju.team_data()
#     pf = pd.DataFrame(pf)
#     pf.fillna()
#     pf.to_excel('file/lol数据分析.xlsx', sheet_name='战队数据', index=False)
# #     return pf
# # print(save_data())
#     # order = ['战队名', '出场次数', '胜率', '胜场', '总击杀', '总死亡', '场均插眼', '场均排眼']
#     # pf = pf[order]
#     # pf.rename(columns=order, inplace=True)
# #     file_path = pd.ExcelWriter('file/lol数据分析.xlsx')
# #     pf.to_excel(file_path, encoding = 'utf-8', index= False)
# #     file_path.save()
# if __name__ == '__main__':
#     save_data()