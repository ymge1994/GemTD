import pyautogui
import time 
import pydirectinput
from operations import operate_gamestart, operate_ingame, get_heros, operate_camera, operate_ag
from mapping import get_map_basics, from_number_to_coordinate





if __name__ == '__main__':
    """
    模拟操作
    """
    code_start = 0
    code_ingame = 0
    game_mode = '1p'
    
    screen_name = 5
    
    
    width, height = pyautogui.size()
    code_start = operate_gamestart(3, game_mode=game_mode) # Step1. 找到游戏是否在主界面
    
    if code_start == 1:
        code_ingame = operate_ingame(10) #%% Step2. 找到游戏是否在选人界面
    
    if code_ingame == 1:
        time.sleep(10) # 等待 10 秒游戏完成加载
        pyautogui.click(x=width/2, y=height/2, clicks=2, duration=1) # 点击一下中心点进入游戏界面
        heros_list = get_heros(game_mode=game_mode) # 选定英雄, 编队
        operate_camera(screen_name = screen_name) # 调节视野大小, 编队
        time.sleep(3)
        zero_coor, grid_size = get_map_basics()
        
        heros_list[0].h_choose()
        for i_col in range(14, 19, 1):
            heros_list[0].h_build(from_number_to_coordinate(18, i_col, zero_coor, grid_size))
            time.sleep(0.5)
    #
    code_ag = operate_ag(3)       
        
