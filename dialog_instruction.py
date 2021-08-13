# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\extract\dialog_instruction.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Manual(object):
    def setupUi(self, Manual):
        Manual.setObjectName("Manual")
        Manual.resize(815, 889)
        self.textBrowser = QtWidgets.QTextBrowser(Manual)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 781, 811))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Manual)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 840, 781, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_templ_extr = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_templ_extr.setFont(font)
        self.pushButton_templ_extr.setObjectName("pushButton_templ_extr")
        self.horizontalLayout.addWidget(self.pushButton_templ_extr)
        self.pushButton_templ_kern = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_templ_kern.setFont(font)
        self.pushButton_templ_kern.setObjectName("pushButton_templ_kern")
        self.horizontalLayout.addWidget(self.pushButton_templ_kern)
        self.pushButton_templ_obr = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_templ_obr.setFont(font)
        self.pushButton_templ_obr.setObjectName("pushButton_templ_obr")
        self.horizontalLayout.addWidget(self.pushButton_templ_obr)

        self.retranslateUi(Manual)
        QtCore.QMetaObject.connectSlotsByName(Manual)

    def retranslateUi(self, Manual):
        _translate = QtCore.QCoreApplication.translate
        Manual.setWindowTitle(_translate("Manual", "Manual"))
        self.textBrowser.setHtml(_translate("Manual", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Инструкция к программе </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:16pt; font-weight:600; text-decoration: underline;\">«</span><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">EXTRACT</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:16pt; font-weight:600; text-decoration: underline;\">»</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600; text-decoration: underline;\">по формированию таблиц хроматографического анализа образцов чистого и экстрагированного керна</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">В программе предусмотрена обработка хроматограмм чистого и экстрагированного керна по опциям «</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">экстракция</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">» или «</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">керн</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">» с выбором соответствующего каталога. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">    </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Каталоги экстракции и керна должны быть разными.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">    </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">В каталоге одновременно с файлами хроматограмм (проб), обработанными и выгруженными в </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600; font-style:italic;\">.xls</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> или </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600; font-style:italic;\">.xlsx</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">, должен находиться лабораторный журнал с историей проведенного анализа.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">3.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">    </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Необходимо проверить соответствие заполнения (структуру) журнала с шаблонами, ознакомится с которыми можно нажав на соответствующие кнопки в нижней части окна инструкции. Имя журнала </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; text-decoration: underline;\">обязательно</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> должно начинаться со слова «</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">журнал</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">». Выделенные зеленым цветом столбцы и строки обязательны для заполнения. Выделенные красным цветом ячейки должны </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; text-decoration: underline;\">полностью</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> соответствовать шаблону. Все текстовые строки должны располагаться только в столбце «Примечание».</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">4.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">    </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Проверить также структуру имени файла хроматограмм. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Имя файла для экстракции –    </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; color:#ff0000;\">aa</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">E_</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; color:#ff0000;\">bb</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">.xlsx</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Имя файла для керна –               </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; color:#ff0000;\">aa</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">К_</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; color:#ff0000;\">bb</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">.xlsx</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">где     </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; color:#ff0000;\">aa</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> – номер образца (например </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">17</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> или </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">17b</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">), </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; color:#ff0000;\">bb</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> – номер пробы (например </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">02</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">)</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">5.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">    </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Выходные таблицы формируются в окне программы и выгружаются в формате .xlsx в отдельный каталог «</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">результат</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">»:</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">- Сводная таблица по пробам по компонентам: </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#1f497d;\">«_сводная по компонентам.xlsx»</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">- Таблица средних значений по компонентам: </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#1f497d;\">«средние по компонентам.xlsx» </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Средние значения также отображаются в окне программы</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">- Таблица коэффициентов вариации по компонентам для проверки допустимого разброса значений между пробами в образце (критическое значение – 33): </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#1f497d;\">«К_вар по компонентам.xlsx» </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Также отображаются в окне программы, в случае превышения критического значения закрашиваются красным и заносятся в список ошибок</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">- Сводная таблица по пробам по параметрам: </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#1f497d;\">«_сводная по параметрам.xlsx»</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">- Таблица  средних значений по параметрам: </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#1f497d;\">«средние по параметрам.xlsx»</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">- Таблица коэффициентов вариации по параметрам: </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#1f497d;\">«К_вар по параметрам.xlsx»</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">- Таблица ошибок: </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#1f497d;\">«ошибки.xlsx»</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">, таблицу необходимо проанализировать. В таблицу заносятся ошибки: 1) совпадение времени выхода разных компонентов, 2) нулевые значения концентрации, 3) превышение критического значения коэффициента вариации. Данные ошибки также отображаются в списке ошибок в окне программы и выделяются цветом в результирующей таблице программы.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">6.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">    </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Передать выходные таблицы в работу для проведения статистического анализа только при пустой таблице ошибок вместе с лабораторным журналом, содержащем важные сведения для статистической оценки.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; text-decoration: underline; color:#ff0000;\">Внимание!!!</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> При запуске обработки в программе выходные файлы .xlsx должны быть закрыты.</span><span style=\" font-size:12pt;\"> </span></p></body></html>"))
        self.pushButton_templ_extr.setText(_translate("Manual", "Журнал экстракции шаблон.xlsx"))
        self.pushButton_templ_kern.setText(_translate("Manual", "Журнал керн шаблон.xlsx"))
        self.pushButton_templ_obr.setText(_translate("Manual", "Проба шаблон.xlsx"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Manual = QtWidgets.QDialog()
    ui = Ui_Manual()
    ui.setupUi(Manual)
    Manual.show()
    sys.exit(app.exec_())
