# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

#定义x和y为角色，分别为小明和小红
define x = Character("小明")
define y = Character("小红")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene black with None #开头的黑屏

    play music "music.MP3"fadein 2.0 #music.MP3为音乐文件名将其替换本地音乐即可
    
    "这是开头的话"

    #结束黑屏一下展示图片
    scene picture with Dissolve(2.0) #picture为图片文件名将其替换本地图片即可

    #一下是对话
    y "。。。。。"
    y "这游戏怎么更新那么慢啊"
    x "小红，没事吧"

    #这个是选择分支，展示玩家可以选择的选项，选项下是玩家选择后跳转的标签
    menu:
        "有事":
            jump xx11

        "没事":
            jump text_2


define x = Character("小明")
define y = Character("小红")

label xx11:
    y "什么事"
    x "游戏更新好慢"
    y "受着"
    return #结束
    

define x = Character("小明")
define y = Character("小红")


label text_2: 
    y "没事"
    y "就是游戏更新有点慢"
    x "你把手机给我"
    "小明把手机给了小红"
    "。。。。。。。。。。"
    x "好了，小红还你手机"
    y "你咋把我游戏删了？"
    x "嘿嘿"
    return #结束


    
