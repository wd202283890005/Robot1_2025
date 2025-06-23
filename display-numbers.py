from microbit import *

# 1. 定义数字显示函数（后续可被其他模块调用）
def show_number(num, duration=1000):
    """在LED屏幕上显示数字，并持续指定时间（默认1秒）"""
    if 0 <= num <= 9:  # 确保数字合法
        display.show(str(num))  # 直接显示字符（兼容性更好）
        sleep(duration)
    else:
        display.scroll("ERR")  # 错误提示

# 2. 数字与人脸的映射关系（预留接口）
# 后续可替换为人脸识别结果的映射（如 { "Alice": 1, "Bob": 2 }）
face_to_number = {
    1: 1,  # 假设人脸ID 1 对应数字1
    2: 2,
    3: 3
}

# 3. 模拟人脸识别触发（测试阶段用按钮代替）
# 实际使用时替换为人脸识别模块的返回结果
def mock_face_detection():
    """模拟人脸识别：按A/B按钮切换不同'人脸'"""
    if button_a.was_pressed():
        return 1  # 模拟识别到人脸1
    elif button_b.was_pressed():
        return 2  # 模拟识别到人脸2
    return None

# 4. 主循环（兼容当前测试和未来扩展）
while True:
    # 模拟人脸识别（后续替换为实际识别代码）
    detected_face = mock_face_detection()
    
    if detected_face is not None:
        # 从映射表中获取对应数字并显示
        target_num = face_to_number.get(detected_face, 0)  # 0表示未知人脸
        show_number(target_num)
    
    sleep(100)  # 降低CPU占用
