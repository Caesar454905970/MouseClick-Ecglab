import pyautogui
import time

# 1920x1080初始坐标：
x_beginning=350
y_beginning=186

# 每次选中的病例数：z_select
z_select=eval(input('请输入每次批量选中的病例数：'))
print("每次选中{}".format(z_select))


# 输入病例的总数
sum_case=eval(input('请输入删除的病例总数：'))
# 一次删除42个病例数，执行的批量数：z
# 向下取整+1
z_batch=(sum_case//z_select)+1
print("删除的批量：{}".format(z_batch))



# a+打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
f = open('log.txt','a+',encoding="utf-8")



for j in range(0,z_batch):
    x_beginning = 350
    y_beginning = 186
    for i in range(0, z_select):
        pyautogui.click(x=x_beginning, y=y_beginning, clicks=1, interval=0.0, button='left', duration=0.0,tween=pyautogui.linear)
        y_beginning += 17

    # 删除病例
    pyautogui.click(x=1774, y=991, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)
    # 确定删除病例
    pyautogui.click(x=931, y=575, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)
    # 删除病例坐标
    # 1774, 991
    # 确定删除病例坐标
    # 执行批量的时间写入日志
    # z_batch_localtime= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(z_batch_localtime)
    # f.writelines(z_batch_localtime+"\n")
print("执行删除病例结束")
z_batch_localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(z_batch_localtime)
f.writelines(z_batch_localtime+"："+"执行删除病例结束"+"\n")
f.close()

# 打包文件，pyinstaller -F xxx.py（xxx.py，打包的文件）
