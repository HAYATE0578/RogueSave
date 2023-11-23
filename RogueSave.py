# _*_ coding: utf-8 _*_
# @Time : 2023/11/14 12:40
# @Author : _TOSHIYUKI
# @ File : __init__.py
# @ Project : myPython

# 1. Import package. 注入界面操作包。
import PySimpleGUI as sg
import datetime
import os
import pickle
import shutil
import threading
import time

# 2. Set the main theme and layout. 设置主题和主界面。
sg.theme('SystemDefaultForReal')

# 3. Initialize some methods and variables. 初始化一些方法和变量。

# The path of WarmSnow save path. 暖雪的默认保存路径。
default_Path = r'C:\Users\user\AppData\LocalLow\BadMudStudio'
# Set a path of temp save path. 设置一个暂时的保存路径。
tmp_Save_Path = r'D:\TmpSave_WarmSnow'
# Set user language. 设置用户界面语言。
lan = 'CHINESE'
# The situation of activating . 当前软件运行状态。
isSaving = False
# Font in the soft. 本软件的通用字体。
font = ('Consolas', 20)


# This method is used to set and save settings. 这个方法用于保存设定。
def set_settings():
    local_Settings = {0: default_Path, 1: tmp_Save_Path, 2: lan}
    with open('tmpSavePath.pkl', 'wb') as tmp:
        pickle.dump(local_Settings, tmp)

（我才意识到立案十分重要。到快写完了我想加个语言转换功能却写成了屎山。应该直接声明个语言列表...）

# This method is used to set and save the path. 这个方法用于设定，保存路径。
def set_lan_window(lan_Parameter, window, start_Situation):
    if lan_Parameter == 'CHINESE':
        lan = 'CHINESE'
        set_settings()
        window['-TITLE-'].update('请确认您的存档路径和目标路径。设置您偏好的本软件语言：')
        window['-SAVE_PATH-'].update('存档路径')
        window['-TEMP_PATH-'].update('目标路径')
        window['-CHINESE-'].update('中文')
        window['-ENGLISH-'].update('英文')
        window['-JAPANESE-'].update('日文')
        window['-Set_Path1-'].update('保存文档路径')
        window['-Set_Path2-'].update('保存目标路径')
        window['-SAVESTART-'].update('开始保存')
        window['-LOAD-'].update('载入存档')
        if start_Situation == False:
            window['-SITUATION-'].update('...停止中...')
        elif start_Situation == True:
            window['-SITUATION-'].update('...运行中...')

    if lan_Parameter == 'ENGLISH':
        lan = 'ENGLISH'
        set_settings()
        window['-TITLE-'].update('Set the save path and the target path. Set language: ')
        window['-SAVE_PATH-'].update('SAVE_PATH')
        window['-TEMP_PATH-'].update('TEMP_PATH')
        window['-CHINESE-'].update('CN')
        window['-ENGLISH-'].update('US')
        window['-JAPANESE-'].update('JP')
        window['-Set_Path1-'].update('Set path1')
        window['-Set_Path2-'].update('Set path2')
        window['-SAVESTART-'].update('Start Saving')
        window['-SITUATION-'].update('...End...')
        window['-LOAD-'].update('Load Archive')
        if start_Situation == False:
            window['-SITUATION-'].update('...End...')
        elif start_Situation == True:
            window['-SITUATION-'].update('...Executing...')

    if lan_Parameter == 'JAPANESE':
        lan = 'JAPANESE'
        set_settings()
        window['-TITLE-'].update('保存パスと目標パスをご確認ください。本ソフトの言語：')
        window['-SAVE_PATH-'].update('保存パス')
        window['-TEMP_PATH-'].update('目標パス')
        window['-CHINESE-'].update('中国語')
        window['-ENGLISH-'].update('英語')
        window['-JAPANESE-'].update('日本語')
        window['-Set_Path1-'].update('保存パスを設定')
        window['-Set_Path2-'].update('目標パスを設定')
        window['-SAVESTART-'].update('保存開始')
        window['-SITUATION-'].update('...停止状態...')
        window['-LOAD-'].update('元にロード')
        if start_Situation == False:
            window['-SITUATION-'].update('...停止状態...')
        elif start_Situation == True:
            window['-SITUATION-'].update('...稼働中...')


# Copy and paste path. 强制覆盖路径的文件。
def copy_directory(src, dest):
    try:
        # 复制整个目录及其内容
        shutil.rmtree(dest, ignore_errors=True)
        shutil.copytree(src, dest, dirs_exist_ok=True)
    except Exception as e:
        window['-SITUATION-'].update(e)


# Copy path paste frequently. 频繁的覆盖路径的文件。
def copy_directory_frequently():
    # Counter. 计数器。
    times = 0
    try:
        while True:
            # Interval of saving. 保存所需的时间间隔。
            time.sleep(300)
            # Count times. 计数。
            times += 1
            # Write the newest path. 设定最新的路径。
            datetime_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            target_Path = tmp_Save_Path + '\\' + datetime_str
            # Make the path. 强力制作路径。
            os.makedirs(target_Path, exist_ok=True)

            # Archives maximum is 50. 设定最大保存50个存档。
            if count_directories(tmp_Save_Path) == 50:
                shutil.rmtree(find_latest_directory(tmp_Save_Path, 'min'))

            # Excute saving. 执行保存。
            copy_directory(default_Path, target_Path)
            window['-SITUATION-'].update(target_Path)

    except Exception as e:
        window['-SITUATION-'].update(os.access(tmp_Save_Path, os.W_OK))


# Open the path. 打开路径。
def open_path(path):
    try:
        # 使用默认程序打开路径
        os.startfile(path)
        print(f"Opened '{path}' successfully.")
    except Exception as e:
        print(f"Error opening '{path}': {e}")


# Copy path paste frequently. 频繁的覆盖路径的文件。
def find_latest_directory(base_Path, isLatest):
    try:
        # Get all items. 获取目录中的所有项。
        all_items = os.listdir(base_Path)

        # Get all dirs which are dir. 筛选出是目录的项。
        directories = [item for item in all_items if os.path.isdir(os.path.join(base_Path, item))]

        latest_directory = ''
        if isLatest == 'max':
            # Sort by last create time. 使用最后创造时间排序目录。
            latest_directory = max(directories, key=lambda d: os.path.getctime(os.path.join(base_Path, d)))
        elif isLatest == 'min':
            # Sort by first create time. 使用最早创造时间排序目录。
            latest_directory = min(directories, key=lambda d: os.path.getctime(os.path.join(base_Path, d)))

        return os.path.join(base_Path, latest_directory)
    except Exception as e:
        print()


# Count folders. 统计当前目录的目录数。
def count_directories(base_path):
    try:
        # Get all items. 获取目录中的所有项。
        all_items = os.listdir(base_path)

        # Get all dirs which are dir. 筛选出是目录的项。
        directories = [item for item in all_items if os.path.isdir(os.path.join(base_path, item))]

        return len(directories)
    except OSError as e:
        print()


# Initialization. 初始化。
try:
    with open('tmpSavePath.pkl', 'rb') as sp:
        load_Settings = pickle.load(sp)
        default_Path = load_Settings[0]
        tmp_Save_Path = load_Settings[1]
        lan = load_Settings[2]

except FileNotFoundError:
    set_settings()

except MemoryError:
    set_settings()

layout = []
if lan == 'CHINESE':
    layout = [
        # Set language. 设置语言。
        [sg.Text('请确认您的存档路径和目标路径。设置您偏好的本软件语言：', key='-TITLE-', font=font),
         sg.Button('英文', key='-ENGLISH-', font=font), sg.Button('中文', key='-CHINESE-', font=font),
         sg.Button('日文', key='-JAPANESE-', font=font)],
        # Set paths. 设置路径。
        [sg.Text('存档路径', font=font, key='-SAVE_PATH-', enable_events=True),
         sg.InputText(default_Path, key='-path1-', font=font),
         sg.Button('保存文档路径', key='-Set_Path1-', font=font)],
        [sg.Text('目标路径', font=font, key='-TEMP_PATH-', enable_events=True),
         sg.InputText(tmp_Save_Path, key='-path2-', font=font),
         sg.Button('保存目标路径', key='-Set_Path2-', font=font)],
        # Set tool buttons. 设置功能按钮。
        [sg.Button('载入存档', key='-LOAD-', font=font),
         sg.Button('开始保存', key='-SAVESTART-', font=font),
         sg.Text('...停止中...', key='-SITUATION-', font=font), ],
    ]

if lan == 'ENGLISH':
    layout = [
        # Set language. 设置语言。
        [sg.Text('Set the save path and the target path. Set language: ', key='-TITLE-', font=font),
         sg.Button('US', key='-ENGLISH-', font=font), sg.Button('CN', key='-CHINESE-', font=font),
         sg.Button('JP', key='-JAPANESE-', font=font)],
        # Set paths. 设置路径。
        [sg.Text('SAVE_PATH', font=font, key='-SAVE_PATH-', enable_events=True),
         sg.InputText(default_Path, key='-path1-', font=font),
         sg.Button('set path1', key='-Set_Path1-', font=font)],
        [sg.Text('TEMP_PATH', font=font, key='-TEMP_PATH-', enable_events=True),
         sg.InputText(tmp_Save_Path, key='-path2-', font=font),
         sg.Button('set path2', key='-Set_Path2-', font=font)],
        # Set tool buttons. 设置功能按钮。
        [sg.Button('Load Archive', key='-LOAD-', font=font),
         sg.Button('Start Saving', key='-SAVESTART-', font=font),
         sg.Text('...End...', key='-SITUATION-', font=font), ],
    ]

if lan == 'JAPANESE':
    layout = [
        # Set language. 设置语言。
        [sg.Text('保存パスと目標パスをご確認ください。本ソフトの言語：', key='-TITLE-', font=font),
         sg.Button('英語', key='-ENGLISH-', font=font), sg.Button('中国語', key='-CHINESE-', font=font),
         sg.Button('日本語', key='-JAPANESE-', font=font)],
        # Set paths. 设置路径。
        [sg.Text('保存パス', font=font, key='-SAVE_PATH-', enable_events=True),
         sg.InputText(default_Path, key='-path1-', font=font),
         sg.Button('保存パスを設定', key='-Set_Path1-', font=font)],
        [sg.Text('目標パス', font=font, key='-TEMP_PATH-', enable_events=True),
         sg.InputText(tmp_Save_Path, key='-path2-', font=font),
         sg.Button('目標パスを設定', key='-Set_Path2-', font=font)],
        # Set tool buttons. 设置功能按钮。
        [sg.Button('元にロード', key='-LOAD-', font=font),
         sg.Button('保存開始', key='-SAVESTART-', font=font),
         sg.Text('...停止状態...', key='-SITUATION-', font=font), ],
    ]

# 4. Window Starts。 界面开始初始化。
window = sg.Window('saveRouge', layout)

# 5. Read the layout and events. 读取界面和事件。
thread = threading.Thread(target=copy_directory_frequently)

while True:
    event, values = window.read()

    # ① Event of closing the soft. 关闭此软件的事件。
    if event is None:
        break

    # ② Event of setting user's own path. 设定用户自己设定路径的事件。
    if event == '-Set_Path1-':
        default_Path = values['-path1-']
        sg.popup('Success. ', font=font)
        set_settings()

    # ③ Event of setting temp path. 设定用户暂定的存档路径的事件。
    if event == '-Set_Path2-':
        tmp_Save_Path = values['-path2-']
        sg.popup('Success. ', font=font)
        set_settings()

    # ④ Event of setting languages. 设定页面语言的事件。
    if event == '-ENGLISH-':
        lan = 'ENGLISH'
        set_lan_window(lan, window, isSaving)
        set_settings()

    if event == '-CHINESE-':
        lan = 'CHINESE'
        set_lan_window(lan, window, isSaving)
        set_settings()

    if event == '-JAPANESE-':
        lan = 'JAPANESE'
        set_lan_window(lan, window, isSaving)
        set_settings()

    # ⑤ Check to start and end saving. 设置用于开始和结束保存。
    if event == '-SAVESTART-':
        if isSaving == True:
            continue
        isSaving = True
        thread.start()

        if lan == 'ENGLISH':
            window['-SITUATION-'].update('...Executing...')
        if lan == 'CHINESE':
            window['-SITUATION-'].update('...运行中...')
        if lan == 'JAPANESE':
            window['-SITUATION-'].update('...稼働中...')

    # ⑥ Load archives to default path. 把保存过的存档放回原位。
    if event == '-LOAD-':
        try:
            # Create a yes or no window. 创建 Yes/No 窗口。
            response = ''
            if lan == 'CHINESE':
                response = sg.popup_yes_no('您是否确定要载入已保存的存档？', title='确认操作', font=font)
            elif lan == 'ENGLISH':
                response = sg.popup_yes_no('Are you sure to retrieve the archive? ', title='CONFIRM', font=font)
            elif lan == 'JAPANESE':
                response = sg.popup_yes_no('セーブをロードしますか？', title='操作確認', font=font)

            if response == 'Yes':
                copy_directory(find_latest_directory(tmp_Save_Path, 'max'), default_Path)
                sg.popup('Success.', font=font)
            else:
                sg.popup('Canceled.', font=font)
        except Exception as e:
            sg.popup('Fail.', font=font)

    # ⑦ Open the path of saving and temp location. 打开保存的路径。
    if event == '-SAVE_PATH-':
        open_path(default_Path)

    if event == '-TEMP_PATH-':
        open_path(tmp_Save_Path)

window.close()
