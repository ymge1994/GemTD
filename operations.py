import pyautogui
import time 
import pydirectinput


class Hero(object):
    def __init__(self, name, skills, press_key = ['z', 'x', 'c', 'v', 'b', 'n']):
        """
        name -> int 编队数字
        skills -> list 技能名字
        press_key -> list 键位
        """
        self.name = name
        self.skills = skills
        self.press_key = press_key
        self.dict_key = dict(zip(skills, press_key))
        
    def h_choose(self): # 选中英雄
        pydirectinput.press('5') # 视角居中
        pydirectinput.press(str(self.name)) 
        
        
    def h_move(self, coor): # 移动
        x = coor[0]
        y = coor[1]
        pyautogui.moveTo(x, y)
        time.sleep(0.5)
        pyautogui.click(button='right') 
        
    
    def h_build(self, coor): # 建造 
        
        x = coor[0]
        y = coor[1]
        button = self.dict_key['build']
        pyautogui.moveTo(x, y)
        time.sleep(0.5)
        pydirectinput.press(button)
        time.sleep(0.5)
        pyautogui.click()   
        
    def h_destroy(self):
        button = self.dict_key['destroy']
        pass # 摧毁
        
    def h_skill(self):
        pass # 特殊技能
    
    
def operate_gamestart(pre_sleep, game_mode='1p'):
    """
    pre_sleep 为初始等待时间
    code = 0 -> 初始
    code = 1 -> 成功
    code = -1 -> 大厅没找到
    code = -2 -> 开始按钮没找到
    code = -3 -> 接受按钮没找到
    game_mode = '1p' or 'co'
    """
    print('Initializing: gamestart...')
    time.sleep(pre_sleep)
    operate_code = 0
    
    seeker_lb = pyautogui.locateOnScreen('.//pics//lobby.png', grayscale=True, confidence=0.8)

    if seeker_lb:
        print('In the lobby!') 
        # 此时已经在大厅, 应当点击开始游戏
        pyautogui.click(seeker_lb, clicks=2, interval=0.5)
        # time.sleep(1)
        seeker_gv = pyautogui.locateOnScreen('.//pics//game_inventory.png', grayscale=True, confidence=0.8)
        pyautogui.click(seeker_gv, clicks=2, interval=1)
        # time.sleep(1)
        seeker_gem = pyautogui.locateOnScreen('.//pics//gem_icon.png', grayscale=True, confidence=0.8)
        pyautogui.click(seeker_gem, clicks=2, interval=1)
        
        
        for pic_name in ['race', '1p', 'co']:
            seeker_menu = pyautogui.locateCenterOnScreen('.//pics//menu_%s.png'%(pic_name), grayscale=True, confidence=0.8)
            if seeker_menu:
                break
            
        if pic_name != game_mode:
            pyautogui.click(seeker_menu, clicks=2, duration=1, interval=1)
            seeker_sub = pyautogui.locateCenterOnScreen('.//pics//sub_%s.png'%(game_mode), grayscale=True, confidence=0.8)
            pyautogui.click(seeker_sub, clicks=1, duration=1)
          
        seeker_start = pyautogui.locateCenterOnScreen('.//pics//start.png', grayscale=True, confidence=0.8)
        if seeker_start:
            print('Start button found!')
            pyautogui.click(seeker_start, clicks=2, interval=1) # 连续点击 “开始”
            
            # 点完开始, 等待接受按钮出现, 这里至少搜索10次
            
            n_count = 0
            while n_count < 10:
                seeker_accept = pyautogui.locateCenterOnScreen('.//pics//accept.png', grayscale=True, confidence=0.8)
                n_count += 1
                time.sleep(1)
                if seeker_accept:
                    break
                
            if seeker_accept:
                print('Game accepted!')
                pyautogui.click(seeker_accept, clicks=3, interval=0.5)
                operate_code = 1
            else:
                print('Not accepted!')
                operate_code = -3
        else:
            print('Start button not found!')
            operate_code = -2      
    else:
        print('Lobby not found!')
        operate_code = -1
    
    if operate_code == 1:
        print('Game start: success!')
    else:
        print('Game start: failed!')
    
    return operate_code


def operate_ingame(pre_sleep):
    print('Initializing: ingame...')
    time.sleep(pre_sleep)
    operate_code = 0
    
    n_count = 0
    while n_count < 100:
        seeker_ig = pyautogui.locateCenterOnScreen('.//pics//start_ingame.png', grayscale=True, confidence=0.8)
        n_count += 1
        time.sleep(2)
        if seeker_ig:
            break
        
    if seeker_ig:
        print('Ingame start!')
        pyautogui.click(seeker_ig, clicks=1, duration=1)
        operate_code = 1
    else:
        print('Ingame error!')
        operate_code = -1
    
    if operate_code == 1:
        print('Ingame start: success!')
    else:
        print('Ingame start: failed!')
    
    return operate_code
    

def operate_ag(pre_sleep):
    """
    自动打 -wtf, 并退出
    """
    
    print('AG-ing...')
    time.sleep(pre_sleep)
    operate_code = 0
    
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.write('-wtf')
    time.sleep(1)
    pydirectinput.press('enter', presses=2, interval=0.5)
    
    # 然后等待退出按钮
    time.sleep(8)
    n_count = 0
    
    while n_count < 10:
        seeker_exit = pyautogui.locateCenterOnScreen('.//pics//exit_ingame.png', grayscale=True, confidence=0.8)
        n_count += 1
        time.sleep(1)
        if seeker_exit:
            break
        
    if seeker_exit:
        print('Exit success!')
        pyautogui.click(seeker_exit, clicks=1, duration=1)
        operate_code = 1
    else:
        print('Exit failed')
        operate_code = -1
        
    return operate_code


def operate_camera(screen_name=5):
    """
    拉动视窗, 调节至合适;
    给视野编队为 screnn
    """
    # Step1. 使用键盘方向键调节
    time.sleep(2)    
    pydirectinput.press('right')
    time.sleep(0.5)
    pydirectinput.press('down')
    time.sleep(1)
    
    # Step2. 一直 scoll down
    time.sleep(1)
    print('...')
    i = 0
    while i < 10:
        i += 1
        pyautogui.scroll(-1000)  # scroll down 10 "clicks"
        
    print('Camera in right location!')
    
    pydirectinput.keyDown('ctrl')  # hold down the ctrl key
    pydirectinput.press(str(screen_name)) # 编队
    pydirectinput.keyUp('ctrl')    # release the ctrl key

    

def get_heros(game_mode):
    """
    实现对英雄的编队
    （TBD）. 1p的编队
    （TBD）. 英雄技能的识别
    """
    hero_list = []
    if game_mode == '1p':
        
        pydirectinput.press('f1') # 选取英雄
        pydirectinput.keyDown('ctrl')  # hold down the ctrl key
        pydirectinput.press('1') # 编队
        pydirectinput.keyUp('ctrl')    # release the ctrl key
            
        hero1 = Hero(1, ['build', 'destroy', 'none3', 'none4', 'none5', 'none6'])
        hero_list.append(hero1)
        
    elif game_mode == 'co':
        pass
    else:
        raise(ValueError)

    return hero_list


#%
if __name__ == '__main__':
    """
    执行基本操作
    """
    
    #
    code_start = 0
    code_ingame = 0
    game_mode = '1p'
    
    
    width, height = pyautogui.size()
    code_start = operate_gamestart(3, game_mode=game_mode) # Step1. 找到游戏是否在主界面
    
    if code_start == 1:
        code_ingame = operate_ingame(10) #%% Step2. 找到游戏是否在选人界面
    
    if code_ingame == 1:
        time.sleep(10) # 等待 10 秒游戏完成加载
        pyautogui.click(x=width/2, y=height/2, clicks=2, duration=2) # 点击一下中心点进入游戏界面
        heros_list = get_heros(game_mode=game_mode) # 选定英雄, 编队
        operate_camera() # 调节视野大小
    
    # time.sleep(20) # pretend I am playing  
    
    #%%
    code_ag = operate_ag(3)
    
    
    
    #%% (Temp use)
    while True:
        time.sleep(3)
        print('Move')
        pyautogui.moveTo(x=seeker_recorder[0], y=seeker_recorder[1])
                    
        
    
        
        
        
        
        
        
    
        