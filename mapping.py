import pyautogui
import time 
import pydirectinput

max_rows = 37
max_cols = 37
corner_cols = 29


def get_map_basics():
    """
    得到地图基本参数
    """
    n_count = 0

    while n_count < 10:
        seeker_corner = pyautogui.locateOnScreen('.//pics//loc_tag_corner.png', grayscale=True, confidence=0.8)
        n_count += 1
        time.sleep(1)
        if seeker_corner:
            break
    
    # seeker_corner 位于 0行, 29 列    
    grid_size = (seeker_corner[2] + seeker_corner[3]) / 2 / 8
    zero_coor = (seeker_corner[0] - grid_size * corner_cols, seeker_corner[1])
    
    print('Map basic parameters, generated!')
    
    return zero_coor, grid_size


def from_number_to_coordinate(i_row, i_col, zero_coor, grid_size):
    """
    (i_row, i_col) int
    (x, y) 分辨率坐标
    zero_coor 左上角边界的分辨率坐标
    grid_size 格子大小
    """
    x = zero_coor[0] + (i_col + 0.5) * grid_size
    y = zero_coor[1] + (i_row + 0.5) * grid_size
    
    return (x, y)


# def from 


if __name__ == '__main__':
    """
    定义地图映射
    宝石TD 地图 n_rows = 37, n_cols = 37
    """
    time.sleep(3)
    
    zero_coor, grid_size = get_map_basics()
    print('123')
    pyautogui.moveTo(from_number_to_coordinate(18, 18, zero_coor, grid_size))
    