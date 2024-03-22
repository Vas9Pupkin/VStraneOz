from PyQt5 import QtCore, QtWidgets
# Для cv2: Не использовать русские названия файлов
def Opening():
    '''
    Открыть
    '''
    try:
        app = QtWidgets.QApplication([])
        wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
        return wb_patch
    except Exception as e:
        print('Ошибка')
        print(e)
        # Наиболее вероятно - недостаточно прав для доступа к файлу
def Soxrani():
    '''
    Сохранить
    '''
    app = QtWidgets.QApplication([])
    return QtWidgets.QFileDialog.getSaveFileName(directory="img.jpg",filter="Image (*.png *.jpg)")[0]