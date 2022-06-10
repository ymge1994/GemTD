import pyautogui
import time 


def operate_gamestart(pre_sleep):
    """
    pre_sleep 为初始等待时间
    code = 0 -> 初始
    code = 1 -> 成功
    code = -1 -> 大厅没找到
    code = -2 -> 开始按钮没找到
    code = -3 -> 接受按钮没找到
    """
    print('Initializing gamestart')
    time.sleep(pre_sleep)
    operate_code = 0
    
    seeker_lb = pyautogui.locateOnScreen('.//pics//lobby.png', grayscale=True)

    if seeker_lb:
        print('In the lobby!') 
        # 此时已经在大厅, 应当点击开始游戏
        
        seeker_start = pyautogui.locateCenterOnScreen('.//pics//start.png', grayscale=True)
        if seeker_start:
            print('Start button found!')
            pyautogui.click(seeker_start, clicks=3, interval=0.5) # 连续点击 “开始”
            
            # 点完开始, 等待接受按钮出现, 这里至少搜索30秒
            seeker_accept = pyautogui.locateCenterOnScreen('.//pics//accept.png', grayscale=True, minSearchTime=30)
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





if __name__ == '__main__':
    """
    执行基本操作
    """
    
    #%%
    # Step1. 找到游戏是否在主界面
    code_start = operate_gamestart(3)
    
        
    #%% Step2. 找到游戏是否在选人界面