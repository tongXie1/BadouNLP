#week3作业

#词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改
Dict = {"经常":0.1,
        "经":0.05,
        "有":0.1,
        "常":0.001,
        "有意见":0.1,
        "歧":0.001,
        "意见":0.2,
        "分歧":0.2,
        "见":0.05,
        "意":0.05,
        "见分歧":0.05,
        "分":0.1}

#待切分文本
sentence = "经常有意见分歧"

#实现全切分函数，输出根据字典能够切分出的所有的切分方式
#动态规划
def all_cut(sentence, Dict):
    #TODO
    n = len(sentence)
    if not n:
        return []
    
    DP = {i: [] for i in range(n + 1)} #初始化DP[k]表示包含前k个字的切分方式
    DP[0] = [[]] 
    for i in range(1, n+1):
        #状态转移方程
        #在第i个字进行逆向匹配，假设有j个字组成了词，那就在i-j的所有切分中加上这个词
        for j in range(1, i+1):
            if sentence[i-j:i] in Dict:
                for prev in DP[i-j]:
                    DP[i].append(prev + [sentence[i-j:i]])
        
    return DP[n] #DP[n]就是sentence的所有切分方式

#目标输出;顺序不重要
target = [
    ['经常', '有意见', '分歧'],
    ['经常', '有意见', '分', '歧'],
    ['经常', '有', '意见', '分歧'],
    ['经常', '有', '意见', '分', '歧'],
    ['经常', '有', '意', '见分歧'],
    ['经常', '有', '意', '见', '分歧'],
    ['经常', '有', '意', '见', '分', '歧'],
    ['经', '常', '有意见', '分歧'],
    ['经', '常', '有意见', '分', '歧'],
    ['经', '常', '有', '意见', '分歧'],
    ['经', '常', '有', '意见', '分', '歧'],
    ['经', '常', '有', '意', '见分歧'],
    ['经', '常', '有', '意', '见', '分歧'],
    ['经', '常', '有', '意', '见', '分', '歧']
]

#print(all_cut(sentence, Dict))
