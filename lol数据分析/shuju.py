import requests
import json


# url = 'https://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_TEAMRANK_LIST_148_1_5.js'
# 爬取数据
def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.77 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)

    return response.text


# 获取战队数据
def team_data():
    team_api = 'https://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_TEAMRANK_LIST_148_1_5.js'
    info = get_data(team_api)
    info = json.loads(info)  # 转化为字典
    info_msg = info['msg']  # 获取键msg对应的值

    teamname = [i['sTeamName'] for i in info_msg]  # 战队名
    out_sum = [i['iAppearancesFrequency'] for i in info_msg]  # 出场次数
    win = [i['iWin'] for i in info_msg]  # 胜场
    loss = [i['iLoss'] for i in info_msg]  # 败场
    kill = [i['iKill'] for i in info_msg]  # 总击杀
    death = [i['iDeath'] for i in info_msg]  # 总死亡
    placed_eye = [int(float(i['sAveragingWardPlaced'])) for i in info_msg]  # 场均插眼
    kill_eye = [int(float(i['sAveragingWardKilled'])) for i in info_msg]  # 场均排眼
    wins = [str((int(i['iWin']) / (int(i['iWin']) + int(i['iLoss'])) * 100))[:2] for i in info_msg]  # 胜率
    # for i in info_msg:
    #     i = i['sTeamName']
    #     print(i)
    info_list = [
        ('战队名', teamname), ('出场次数', out_sum), ('胜场', win), ('败场', loss), ('总击杀', kill), ('总死亡', death),
        ('场均插眼', placed_eye), ('场均排眼', kill_eye), ('胜率', wins)
    ]
    info_dict = {key: valus for key, valus in info_list}
    return info_dict


# 获取队员个人数据
def pers_data():
    pers_api = 'https://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_PERSONALRANK_LIST_148_1_5.js'
    info_pers = get_data(pers_api)
    info_pers = json.loads(info_pers)
    info_pers = info_pers['msg']
    # name = [j['sMemberName'] for j in info_pers]  # 队员名字
    # position = [j['iPosition'] for j in info_pers]  # 位置
    # games_sum = [j['iAppearancesFrequency'] for j in info_pers]  # 出场次数
    # kill_sum = [j['iKill'] for j in info_pers]  # 总击杀
    # kill_avg = [str((int(j['iKill']) / int(j['iAppearancesFrequency'])))[:3] for j in info_pers]  # 场均击杀
    # assists = [j['iAssists'] for j in info_pers]  # 助攻
    # death = [j['iDeath'] for j in info_pers]  # 死亡
    # death_avg = [(j['sAveragingDeath'])[:3] for j in info_pers]  # 场均死亡
    # kda = [(j['iKDA'])[:3] for j in info_pers]
    # gold = [(j['sAveragingGold'])[:4] for j in info_pers]  # 场均金钱
    # lasthit = [int(float(j['sAveragingLastLasthit'])) for j in info_pers]  # 场均补刀
    # placed_eyes = [int(float(j['sAveragingWardPlaced'])) for j in info_pers]  # 场均插眼
    # kill_eyes = [int(float(j['sAveragingWardKilled'])) for j in info_pers]  # 场均排眼
    # rate = [str(float(j['sAveragingOfferedRate']) * 100)[:4] for j in info_pers]  # 参团率
    # mvp = [j['iMVPFrequency'] for j in info_pers]  # mvp次数
    # # print(rate)
    # infos_list = [
    #     ('队员', name), ('位置', position), ('出场次数', games_sum), ('总击杀', kill_sum), ('场均击杀', kill_avg),
    #     ('助攻', assists), ('死亡', death), ('场均死亡', death_avg), ('kda', kda), ('场均金钱', gold), ('场均补刀', lasthit),
    #     ('场均插眼', placed_eyes), ('场均排眼', kill_eyes), ('参团率', rate), ('mvp次数', mvp)
    # ]
    # infos_dict = {key: value for key, value in infos_list}
    # 创建一个字典
    key_list = ['sMemberName', 'iPosition', 'iAppearancesFrequency', 'iKill', 'iAssists', 'iDeath', 'sAveragingDeath',
                'iKDA', 'sAveragingGold', 'sAveragingLastLasthit', 'sAveragingWardPlaced', 'sAveragingWardKilled',
                'sAveragingOfferedRate', 'iMVPFrequency']
    info_list = list(map(lambda key: [j[f'{key}'] for j in info_pers], key_list))
    infos_list = [
        ('队员', info_list[0]), ('位置', info_list[1]), ('出场次数', info_list[2]), ('总击杀', info_list[3]),
        ('助攻', info_list[4]), ('死亡', info_list[5]), ('场均死亡', info_list[6]),
        ('kda', info_list[7]), ('场均金钱', info_list[8]), ('场均补刀', info_list[9]), ('场均插眼', info_list[10]),
        ('场均排眼', info_list[11]), ('参团率', info_list[12]), ('mvp次数', info_list[13])
    ]
    info_dict = {key: value for key, value in infos_list}
    return info_dict


# 获取英雄id对应的英雄名,英雄比赛中的数据
def hero_name():
    hero_name_api = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    hero = get_data(hero_name_api)
    hero = json.loads(hero)
    hero_value = hero['hero']

    key_list = ['heroId', 'name']
    hero_list = list(map(lambda key: [j[f'{key}'] for j in hero_value], key_list))
    name_list = [('ID', hero_list[0]), ('名字', hero_list[1])]
    name_dict = {key: value for key, value in name_list}
    return name_dict

# 获取英雄数据
def hero_data():
    hero_data_api = 'https://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_HERORANK_LIST_148_1_5.js'
    data = get_data(hero_data_api)
    data = json.loads(data)
    hero_data_msg = data['msg']
    key2_list = ['iChampionId', 'iAppearancesFrequency', 'sAveragingPick', 'sAveragingBan', 'sAveragingWin']
    hero_data_list = list(map(lambda key: [j[f'{key}'] for j in hero_data_msg], key2_list))
    data_list = [('ID', hero_data_list[0]), ('出场次数', hero_data_list[1]), ('pick比率', hero_data_list[2]),
                 ('ban比率', hero_data_list[3]), ('胜率', hero_data_list[4])]
    data_dict_list = {key: value for key, value in data_list}
    return data_dict_list
    # ID = []
    # for i in data_list[0]:
    #     for j in hero_name_id_list:
    #         if i == j:
    #             ID.append(hero_name_list[hero_name_id_list.index(j)])
    #
    # return ID


# print(team_data())
if __name__ == '__main__':
    team_data()
    pers_data()
    hero_name()
    hero_data()
