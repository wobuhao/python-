import pandas as pd
import numpy as np
from uiautomation import WindowControl

# 绑定微信主窗口
wx = WindowControl(Name='微信')

print(wx)

# 切换窗口
wx.SwitchToThisWindow()
# 寻找会话控件绑定
hw = wx.ListControl(Name='会话')
print('寻找会话控件绑定', hw)
# 通过pd读取数据
df = pd.read_csv('新建文本文档1.csv', encoding='gb18030')

while True:
    we = hw.TextControl(searchDepth=4)

    while not we.Exists(0):
        pass
    print('未读消息哦', we)
    # 存在未读消息
    if we.Name:
        # 点击未读消息
        we.Click(simulateMove=False)
        # 读取最后一条未读消息
        last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name
        print('读取最后一条消息', last_msg)
        # 判断关键字
        msg = df.apply(lambda x: x['回复内容'] if x['关键词'] in last_msg else None, axis=1)
        msg.dropna(axis=0, how='any', inplace=True)

        ar = np.array(msg).tolist()

        if ar:
            wx.SendKeys(ar[0].replace('{br}', '{Shift}{Enter}'), waitTime=0)
            # 发送消息
            wx.SendKeys('{Enter}', waitTime=0)
            # 通过消息匹配检索会话栏的联系人
            wx.TextControl(SubName=ar[0][:5]).RightClick()
        else:
            wx.SendKeys('我没有理解您的意思', waitTime=0)
            wx.SendKeys('{Enter}', waitTime=0)
            wx.TextControl(SubName=last_msg[:5]).RightClick()