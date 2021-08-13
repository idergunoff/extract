import subprocess
import traceback

import pandas as pd
import os, sys
import re

from PyQt5.QtWidgets import QApplication, QFileDialog, QCheckBox, QTableWidgetItem

from extract_dialog import *
from dialog_instruction import *
from dialog_formulas import *
from functions import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.tableWidget.resizeColumnsToContents()


def open_dir():
    ui.listWidget.clear()  # очищаем таблицу и список ошибок
    row_count = ui.tableWidget.rowCount()
    for i in range(row_count + 1):
        ui.tableWidget.removeRow(row_count - i)

    dir_name = QFileDialog.getExistingDirectory()
    tab_error = pd.DataFrame(columns=['n_obr', 'n_pr', 'error'])
    for_round = ui.spinBox_round.text()
    for direct in os.walk(dir_name):
        for file_journal in direct[-1]:
            if file_journal.endswith(('.xls', '.xlsx')) and file_journal.startswith(('Журнал', 'журнал')):
                if ui.radioButton_extr.isChecked():
                    tabl_coef_extr = pd.read_excel(dir_name + '/' + file_journal, header=5)
                    tabl_coef_extr['pentane'] = 0
                    for n, i in enumerate(
                            tabl_coef_extr['Объем экстрагента (пентана/хлористого метилена), мл']):  # выбираем объем пентана
                        tabl_coef_extr['pentane'][n] = float(str(i).split('/')[0])
                    tabl_coef_extr['c_extr'] = tabl_coef_extr['pentane'] / tabl_coef_extr['Масса навески обр. на экстракцию, г']
                    tabl_coef_extr['c_extr'] = tabl_coef_extr['c_extr'] / tabl_coef_extr['c_extr'][0]  # нормируем коэфициент ???
                    tabl_coef_extr['V_zak'] = tabl_coef_extr['Объем закола экстракта в хромато-масспектрометр, мкл']
                    tab_coef = pd.DataFrame(tabl_coef_extr[['№ образца', 'c_extr', 'V_zak']])
                    del tabl_coef_extr
                    tab_coef = tab_coef.dropna(how='all').reset_index()
                    for n, i in enumerate(tab_coef['№ образца']):
                        tab_coef['№ образца'][n] = str(i)

                elif ui.radioButton_kern.isChecked():
                    tabl_ves_kern = pd.read_excel(dir_name + '/' + file_journal, header=1)
                    tabl_ves_kern = tabl_ves_kern.dropna(how='all').reset_index()
                    for n, i in enumerate(tabl_ves_kern['№ образца']):
                        if tabl_ves_kern['№ образца'][n] == 'замена лайнера':
                            tabl_ves_kern = tabl_ves_kern.drop(index=n)
                        tabl_ves_kern['№ образца'][n] = str(i)
                    tabl_ves_kern = tabl_ves_kern.reset_index()
                    del tabl_ves_kern['level_0']
                    del tabl_ves_kern['index']
                    print(tabl_ves_kern)

    list_row = 0

    for direct in os.walk(dir_name):
        for filename in direct[-1]:  # создаем таблицу со всеми названиями компонентов из первого файла
            if filename.endswith(('.xls', '.xlsx')) and re.search(r'^\d+\w+_\d', filename):
                tab = pd.read_excel(direct[0] + '/' + filename, header=None)
                list_comp = tab[0].tolist()
                column_comp = ['obr', 'pr']
                for i in list_comp:
                    column_comp.append(i + '_t')  # время выхода компонента
                    column_comp.append(i + '_c')  # концентрация компонента
                list_param = ['otnpri_fi', 'otnpri_17', 'otnfi_18', 'ki', 'otn27_17', 'cpi19_23', 'cpi17_21',
                              'cpi19_25', 'cpi23_29', 'cpi23_33', 'oepc19', 'oepc21', 'oepc23', 'oepc25', 'oepc27',
                              'oepc29', 'cpi_2', 'otn17_25', 'otn16_29', 'otn35_34', 'c15_c20', 'c21_c30', 'otn15_30',
                              'c16_c22', 'c23_c29', 'otn15_24', 'otn25_34', 'c11_c18', 'otn15_29']
                tab_comp = pd.DataFrame(columns=column_comp + list_param, index=range(len(direct[-1])))
                print(tab_comp)
                break

        n = 0
        ui.progressBar.reset()
        ui.progressBar.setMaximum(len(direct[-1]))
        ui.label.setText('Считываем данные по пробам')
        ui.label.setStyleSheet('color: blue')
        for filename in direct[-1]:
            if filename.endswith(('.xls', '.xlsx')) and re.search(r'^\d+\w+_\d', filename):
                data_name = filename.split('.')[0].split('_')
                obr, pr = data_name[0], data_name[1]
                if obr.startswith('0'):
                    obr = obr[1:]
                tab = pd.read_excel(direct[0] + '/' + filename, header=None)
                tab_comp['obr'][n] = obr
                tab_comp['pr'][n] = pr
                # print(obr, pr, obr[:-1], pr[-1])
                for i in list_comp:
                    tab_comp[i + '_t'][n] = tab[2].loc[tab[0] == i].tolist()[0]
                    # умножаем на коэф экстракции этого образца и делим на объем пробы
                    if isinstance(tab[1].loc[tab[0] == i].tolist()[0], str):
                        tab_comp[i + '_c'][n] = 0
                    else:
                        if ui.radioButton_extr.isChecked():
                            tab_comp[i + '_c'][n] = tab[1].loc[tab[0] == i].tolist()[0] * \
                                                    float(tab_coef['c_extr'].loc[
                                                              tab_coef['№ образца'] == obr[:-1]].tolist()[0]) / \
                                                    float(tab_coef['V_zak'].loc[
                                                              tab_coef['№ образца'] == obr[:-1]].tolist()[0])
                        elif ui.radioButton_kern.isChecked():
                            ves = tabl_ves_kern['Проба ' + pr[-1]].loc[tabl_ves_kern['№ образца'] == obr[:-1]].tolist()[0]
                            tab_comp[i + '_c'][n] = tab[1].loc[tab[0] == i].tolist()[0] / ves / 1000
                n += 1
                ui.progressBar.setValue(n + 1)
        ui.label.setText('Готово!')
        ui.label.setStyleSheet('color: green')
    tab_comp = tab_comp.dropna(how='all').reset_index()

    """ Считаем параметры """

    ui.progressBar.reset()
    ui.progressBar.setMaximum(len(tab_comp.index))
    ui.label.setText('Рассчитываем геохимические параметры по пробам')
    ui.label.setStyleSheet('color: blue')
    for n, i in enumerate(tab_comp.index):
        c7 = tab_comp['Heptane_c'][i]
        c8 = tab_comp['Octane_c'][i]
        c9 = tab_comp['Nonane_c'][i]
        c10 = tab_comp['Decane_c'][i]
        c11 = tab_comp['Undecane_c'][i]
        c12 = tab_comp['Dodecane_c'][i]
        c13 = tab_comp['Tridecane_c'][i]
        c14 = tab_comp['Tetradecane_c'][i]
        c15 = tab_comp['Pentadecane_c'][i]
        c16 = tab_comp['Hexadecane_c'][i]
        c17 = tab_comp['Heptadecane_c'][i]
        Pristane = tab_comp['Pristane_c'][i]
        c18 = tab_comp['Octadecane_c'][i]
        Phytane = tab_comp['Phytane_c'][i]
        c19 = tab_comp['Nonadecane_c'][i]
        c20 = tab_comp['Eicosane_c'][i]
        c21 = tab_comp['Heneicosane_c'][i]
        c22 = tab_comp['Docosane_c'][i]
        c23 = tab_comp['Tricosane_c'][i]
        c24 = tab_comp['Tetracosane_c'][i]
        c25 = tab_comp['Pentacosane_c'][i]
        c26 = tab_comp['Hexacosane_c'][i]
        c27 = tab_comp['Heptacosane_c'][i]
        c28 = tab_comp['Octacosane_c'][i]
        c29 = tab_comp['Nonacosane_c'][i]
        c30 = tab_comp['Triacontane_c'][i]
        c31 = tab_comp['Hentriacontane_c'][i]
        c32 = tab_comp['Dotriacontane_c'][i]
        c33 = tab_comp['Tritriacontane_c'][i]
        c34 = tab_comp['Tetratriacontane_c'][i]
        c35 = tab_comp['Pentatriacontane_c'][i]
        c36 = tab_comp['Hexatriacontane_c'][i]
        c37 = tab_comp['Heptatriacontane_c'][i]
        c38 = tab_comp['Octatriacontane_c'][i]
        c39 = tab_comp['Nonatriacontane_c'][i]
        c40 = tab_comp['Tetracontane_c'][i]

        tab_comp['otnpri_fi'][i] = Pristane / Phytane
        tab_comp['otnpri_17'][i] = Pristane / c17
        tab_comp['otnfi_18'][i] = Phytane / c18
        tab_comp['ki'][i] = (Pristane + Phytane) / (c17 + c18)
        tab_comp['otn27_17'][i] = c27 / c17
        tab_comp['cpi19_23'][i] = ((c19 + c21 + c23) + (c21 + c23 + c25)) / (2 * (c20 + c22 + c24))
        tab_comp['cpi17_21'][i] = ((c17 + c19 + c21) + (c19 + c21 + c23)) / (2 * (c18 + c20 + c22))
        tab_comp['cpi19_25'][i] = ((c19 + c21 + c23 + c25) + (c21 + c23 + c25 + c27)) / (2 * (c20 + c22 + c24 + c26))
        tab_comp['cpi23_29'][i] = ((c23 + c25 + c27 + c29) + (c25 + c27 + c29 + c31)) / (2 * (c24 + c26 + c28 + c30))
        tab_comp['cpi23_33'][i] = ((c23 + c25 + c27 + c29 + c31 + c33) + (c25 + c27 + c29 + c31 + c33 + c35)) / (
                2 * (c24 + c26 + c28 + c30 + c32 + c34))
        tab_comp['oepc19'][i] = (c17 + 6 * c19 + c21) / (4 * c18 + 4 * c20)
        tab_comp['oepc21'][i] = (c19 + 6 * c21 + c23) / (4 * c20 + 4 * c22)
        tab_comp['oepc23'][i] = (c21 + 6 * c23 + c25) / (4 * c22 + 4 * c24)
        tab_comp['oepc25'][i] = (c23 + 6 * c25 + c27) / (4 * c24 + 4 * c26)
        tab_comp['oepc27'][i] = (c25 + 6 * c27 + c29) / (4 * c26 + 4 * c28)
        tab_comp['oepc29'][i] = (c27 + 6 * c29 + c31) / (4 * c28 + 4 * c30)
        tab_comp['cpi_2'][i] = ((c25 + c27 + c29 + c31 + c33) / (c26 + c28 + c30 + c32 + c34) + (
                c25 + c27 + c29 + c31 + c33) / (c26 + c28 + c30 + c32 + c24)) / 2
        tab_comp['otn17_25'][i] = c17 / c25
        tab_comp['otn16_29'][i] = (c16 + c17 + c18 + c19 + c20 + c21 + c22) / (c23 + c24 + c25 + c26 + c27 + c28 + c29)
        tab_comp['otn35_34'][i] = c35 / c34
        tab_comp['c15_c20'][i] = c15 + c16 + c17 + c18 + c19 + c20
        tab_comp['c21_c30'][i] = c21 + c22 + c23 + c24 + c25 + c26 + c27 + c28 + c29 + c30
        tab_comp['otn15_30'][i] = (c15 + c16 + c17 + c18 + c19 + c20) / (
                c21 + c22 + c23 + c24 + c25 + c26 + c27 + c28 + c29 + c30)
        tab_comp['c16_c22'][i] = c16 + c17 + c18 + c19 + c20 + c21 + c22
        tab_comp['c23_c29'][i] = c23 + c24 + c25 + c26 + c27 + c28 + c29
        tab_comp['otn15_24'][i] = (c15 + c17) / (c22 + c24)
        tab_comp['otn25_34'][i] = (c25 + c26 + c27 + c28 + c29 + c30 + c31 + c32 + c33) / (
                c26 + c27 + c28 + c29 + c30 + c31 + c32 + c33 + c34)
        tab_comp['c11_c18'][i] = c11 + c12 + c13 + c14 + c15 + c16 + c17 + c18
        tab_comp['otn15_29'][i] = (c15 + c17 + c19) / (c25 + c27 + c29)
        ui.progressBar.setValue(n + 1)

    ui.label.setText('Готово!')
    ui.label.setStyleSheet('color: green')
    print(tab_comp)
    if not os.path.isdir(dir_name + '/результат'):
        os.mkdir(dir_name + '/результат')
    tab_UV = pd.DataFrame(
        tab_comp[['obr', 'pr', 'Heptane_c', 'Octane_c', 'Nonane_c', 'Decane_c', 'Undecane_c', 'Dodecane_c',
                  'Tridecane_c', 'Tetradecane_c', 'Pentadecane_c', 'Hexadecane_c', 'Heptadecane_c', 'Pristane_c',
                  'Octadecane_c', 'Phytane_c', 'Nonadecane_c', 'Eicosane_c', 'Heneicosane_c', 'Docosane_c',
                  'Tricosane_c', 'Tetracosane_c', 'Pentacosane_c', 'Hexacosane_c', 'Heptacosane_c', 'Octacosane_c',
                  'Nonacosane_c', 'Triacontane_c', 'Hentriacontane_c', 'Dotriacontane_c', 'Tritriacontane_c',
                  'Tetratriacontane_c', 'Pentatriacontane_c', 'Hexatriacontane_c', 'Heptatriacontane_c',
                  'Octatriacontane_c', 'Nonatriacontane_c', 'Tetracontane_c']])
    tab_UV = tab_UV.rename(
        columns={'obr': 'Образец', 'pr': 'Проба', 'Heptane_c': 'Heptane (C7)', 'Octane_c': 'Octane (C8)', 'Nonane_c':
            'Nonane (C9)', 'Decane_c': 'Decane (C10)', 'Undecane_c': 'Undecane (C11)', 'Dodecane_c':
                     'Dodecane (C12)', 'Tridecane_c': 'Tridecane (C13)', 'Tetradecane_c': 'Tetradecane (C14)',
                 'Pentadecane_c': 'Pentadecane (C15)', 'Hexadecane_c': 'Hexadecane (C16)', 'Heptadecane_c':
                     'Heptadecane (C17)', 'Pristane_c': 'Pristane', 'Octadecane_c': 'Octadecane_c (C18)', 'Phytane_c':
                     'Phytane', 'Nonadecane_c': 'Nonadecane (C19)', 'Eicosane_c': 'Eicosane (C20)', 'Heneicosane_c':
                     'Heneicosane (C21)', 'Docosane_c': 'Docosane (C22)', 'Tricosane_c': 'Tricosane (C23)',
                 'Tetracosane_c':
                     'Tetracosane (C24)', 'Pentacosane_c': 'Pentacosane (C25)', 'Hexacosane_c': 'Hexacosane (C26)',
                 'Heptacosane_c': 'Heptacosane (C27)', 'Octacosane_c': 'Octacosane (C28)', 'Nonacosane_c':
                     'Nonacosane (C29)', 'Triacontane_c': 'Triacontane (C30)',
                 'Hentriacontane_c': 'Hentriacontane (C31)',
                 'Dotriacontane_c': 'Dotriacontane (C32)', 'Tritriacontane_c': 'Tritriacontane (C33)',
                 'Tetratriacontane_c': 'Tetratriacontane (C34)', 'Pentatriacontane_c': 'Pentatriacontane (C35)',
                 'Hexatriacontane_c': 'Hexatriacontane (C36)', 'Heptatriacontane_c': 'Heptatriacontane (C37)',
                 'Octatriacontane_c': 'Octatriacontane (C38)', 'Nonatriacontane_c': 'Nonatriacontane (C39)',
                 'Tetracontane_c': 'Tetracontane (C40)'})
    tab_UV.to_excel(dir_name + '/результат/_сводная по компонентам.xlsx', float_format="%." + for_round + "f")
    tab_param = pd.DataFrame(
        tab_comp[['obr', 'pr', 'otnpri_fi', 'otnpri_17', 'otnfi_18', 'ki', 'otn27_17', 'cpi19_23', 'cpi17_21',
                  'cpi19_25', 'cpi23_29', 'cpi23_33', 'oepc19', 'oepc21', 'oepc23', 'oepc25', 'oepc27', 'oepc29',
                  'cpi_2', 'otn17_25', 'otn16_29', 'otn35_34', 'c15_c20', 'c21_c30', 'otn15_30', 'c16_c22', 'c23_c29',
                  'otn15_24', 'otn25_34', 'c11_c18', 'otn15_29']])
    tab_param = tab_param.rename(
        columns={'obr': 'Образец', 'pr': 'Проба', 'otnpri_fi': 'Pr/Ph', 'otnpri_17': 'Pr/n-C17', 'otnfi_18': 'Ph/n-C18',
                 'ki': 'Ki', 'otn27_17': 'C27/C17', 'cpi19_23': 'CPI nC19-nC23', 'cpi17_21': 'CPI  nC17-nC21',
                 'cpi19_25': 'CPI  nC19-nC25', 'cpi23_29': 'CPI nC23-nC29', 'cpi23_33': 'CPI nC23-nC33', 'oepc19':
                     'OEP при nС19', 'oepc21': 'OEP при nС21', 'oepc23': 'OEP при nС23', 'oepc25': 'OEP при nС25',
                 'oepc27':
                     'OEP при nС27', 'oepc29': 'OEP при nС29', 'cpi_2': 'CPI nC25-nC33', 'otn17_25': 'nC17/nC25 ',
                 'otn16_29': 'nC16- nC22/nC23- nC29', 'otn35_34': 'nC35/nC34', 'c15_c20': 'nC15-nC20', 'c21_c30':
                     'nC21-nC30', 'otn15_30': 'nC15- nC20/nC21- nC30', 'c16_c22': 'nC16-nC22', 'c23_c29': 'nC23-nC29',
                 'otn15_24': 'nC15- nC17/nC22- nC24', 'otn25_34': 'nC25- nC33/nC26- nC34', 'c11_c18': 'nC11-nC18',
                 'otn15_29': 'nC15- nC19/nC25- nC29'})
    tab_param.to_excel(dir_name + '/результат/_сводная по параметрам.xlsx', float_format="%." + for_round + "f")
    if ui.radioButton_extr.isChecked():
        tab_var = pd.DataFrame(columns=list_comp + list_param, index=tab_coef['№ образца'])
        tab_mean = pd.DataFrame(columns=list_comp + list_param, index=tab_coef['№ образца'])
    elif ui.radioButton_kern.isChecked():
        tab_var = pd.DataFrame(columns=list_comp + list_param, index=tabl_ves_kern['№ образца'])
        tab_mean = pd.DataFrame(columns=list_comp + list_param, index=tabl_ves_kern['№ образца'])
    obr = tab_comp['obr'][0]
    pp = 0
    n_row = 0

    ui.progressBar.reset()
    ui.progressBar.setMaximum(len(tab_comp['obr']))
    ui.label.setText('Рассчитываем коэффициенты вариации для концентраций и геохимических параметров')
    ui.label.setStyleSheet('color: blue')
    for n_pp, n_obr in enumerate(tab_comp['obr']):
        if n_obr != obr:
            #   считаем среднее
            ui.tableWidget.insertRow(n_row)
            ui.tableWidget.setItem(n_row, 0, QTableWidgetItem(obr))
            ui.tableWidget.item(n_row, 0).setBackground(QtGui.QColor(176, 224, 230))
            ui.tableWidget.setVerticalHeaderItem(n_row, QTableWidgetItem(obr))
            ui.tableWidget.setItem(n_row, 1, QTableWidgetItem('среднее'))
            ui.tableWidget.item(n_row, 1).setBackground(QtGui.QColor(176, 224, 230))
            n_col = 2
            for n, comp in enumerate(list_comp + list_param):
                if n < len(list_comp):
                    mean_val = tab_comp[comp + '_c'].iloc[pp: n_pp].mean()
                else:
                    mean_val = tab_comp[comp].iloc[pp: n_pp].mean()
                tab_mean[comp][obr[:-1]] = mean_val
                ui.tableWidget.setItem(n_row, n_col, QTableWidgetItem(str(round(mean_val, int(for_round)))))
                ui.tableWidget.item(n_row, n_col).setBackground(QtGui.QColor(176, 224, 230))
                n_col += 1
            n_row += 1
            #   считаем коэффициент вариации
            ui.tableWidget.insertRow(n_row)
            ui.tableWidget.setItem(n_row, 0, QTableWidgetItem(obr))
            ui.tableWidget.item(n_row, 0).setBackground(QtGui.QColor(152, 251, 152))
            ui.tableWidget.setVerticalHeaderItem(n_row, QTableWidgetItem(obr))
            ui.tableWidget.setItem(n_row, 1, QTableWidgetItem('k_вариации'))
            ui.tableWidget.item(n_row, 1).setBackground(QtGui.QColor(152, 251, 152))
            n_col = 2
            for n, comp in enumerate(list_comp + list_param):
                if n < len(list_comp):
                    k_var = tab_comp[comp + '_c'].iloc[pp: n_pp].std() / tab_comp[comp + '_c'].iloc[pp: n_pp].mean() * \
                            100
                else:
                    k_var = tab_comp[comp].iloc[pp: n_pp].std() / tab_comp[comp].iloc[pp: n_pp].mean() * 100
                tab_var[comp][obr[:-1]] = k_var
                ui.tableWidget.setItem(n_row, n_col, QTableWidgetItem(str(round(k_var, int(for_round)))))
                ui.tableWidget.item(n_row, n_col).setBackground(QtGui.QColor(152, 251, 152))
                if k_var > 33:
                    if n < len(list_comp):
                        cri_val = found_critical_value(tab_comp[comp + '_c'].iloc[pp: n_pp].to_list())
                        if cri_val != 'limbo':
                            cri_pr = tab_comp['pr'].iloc[pp: n_pp].loc[tab_comp[comp + '_c'] == cri_val].tolist()[0]
                        else:
                            cri_pr = 'не определён'
                            cri_val = 0
                    else:
                        cri_val = found_critical_value(tab_comp[comp].iloc[pp: n_pp].to_list())
                        if cri_val != 'limbo':
                            cri_pr = tab_comp['pr'].iloc[pp: n_pp].loc[tab_comp[comp] == cri_val].tolist()[0]
                        else:
                            cri_pr = 'не определён'
                            cri_val = 0
                    err = {'n_obr': obr, 'n_pr': comp, 'error': 'k_var = {}, выброс: {}, в пробе: {}'.format(
                        str(round(k_var, int(for_round))), str(round(cri_val, int(for_round))), str(cri_pr))}
                    tab_error = tab_error.append(err, ignore_index=True)
                    ui.listWidget.insertItem(list_row, '{}. {} - {} k_var = {}, выброс: {}, в пробе: {}__{}_{}'.format(
                        str(list_row + 1), obr, comp, str(round(k_var, int(for_round))),
                        str(round(cri_val, int(for_round))), str(cri_pr), str(n_row), str(n_col)))
                    ui.listWidget.item(list_row).setBackground(QtGui.QColor(255, 160, 122))
                    ui.tableWidget.item(n_row, 0).setBackground(QtGui.QColor(255, 160, 122))
                    ui.tableWidget.item(n_row, 1).setBackground(QtGui.QColor(255, 160, 122))
                    ui.tableWidget.item(n_row, n_col).setBackground(QtGui.QColor(255, 160, 122))
                    list_row += 1
                n_col += 1
            obr, pp = n_obr, n_pp
            n_row += 1
        #   заносим в таблицу концентрации и расчетные параметры
        ui.tableWidget.insertRow(n_row)
        ui.tableWidget.setItem(n_row, 0, QTableWidgetItem(obr))
        ui.tableWidget.setVerticalHeaderItem(n_row, QTableWidgetItem(obr))
        ui.tableWidget.setItem(n_row, 1, QTableWidgetItem(tab_comp['pr'][n_pp]))
        n_col = 2
        for n, comp in enumerate(list_comp + list_param):
            if n < len(list_comp):
                ui.tableWidget.setItem(n_row, n_col,
                                       QTableWidgetItem(str(round(tab_comp[comp + '_c'][n_pp], int(for_round)))))
                if tab_comp[comp + '_c'][n_pp] == 0:
                    print(obr + '-' + tab_comp['pr'][n_pp] + ' - ' + comp + '. концетрация = 0')
                    err = {'n_obr': obr, 'n_pr': tab_comp['pr'][n_pp],
                           'error': 'концетрация = 0'}
                    tab_error = tab_error.append(err, ignore_index=True)
                    ui.listWidget.insertItem(list_row, str(list_row + 1) + '. ' + obr + '-' + tab_comp['pr'][n_pp] +
                                             ' - ' + comp + '. концетрация = 0' + '_' + str(n_row) + '_' + str(n_col))
                    ui.listWidget.item(list_row).setBackground(QtGui.QColor(255, 69, 0))
                    ui.tableWidget.item(n_row, 0).setBackground(QtGui.QColor(255, 69, 0))
                    ui.tableWidget.item(n_row, 1).setBackground(QtGui.QColor(255, 69, 0))
                    ui.tableWidget.item(n_row, n_col).setBackground(QtGui.QColor(255, 69, 0))
                    list_row += 1
                ui.tableWidget.item(n_row, n_col).setToolTip('Время выхода - ' + str(round(tab_comp[comp + '_t'][n_pp],
                                                                                           int(for_round))))
            else:
                ui.tableWidget.setItem(n_row, n_col, QTableWidgetItem(str(round(tab_comp[comp][n_pp], int(for_round)))))
            n_col += 1
        """ проверяем время выхода компонентов """
        for j in range(len(list_comp)):
            if j + 1 != len(list_comp):
                dt = tab_comp[list_comp[j + 1] + '_t'][n_pp] - tab_comp[list_comp[j] + '_t'][n_pp]
                if dt <= 0:
                    for i in range(len(list_comp) + 2):
                        ui.tableWidget.item(n_row, i).setBackground(QtGui.QColor(240, 230, 140))
                    err = {'n_obr': obr, 'n_pr': tab_comp['pr'][n_pp], 'error': 'Время выхода: ' + list_comp[j] + ' - '
                                                                                + str(
                        round(tab_comp[list_comp[j] + '_t'][n_pp], int(for_round))) + ', ' + list_comp[j + 1] + ' - ' +
                                                                                str(round(
                                                                                    tab_comp[list_comp[j + 1] + '_t'][
                                                                                        n_pp], int(for_round)))}
                    tab_error = tab_error.append(err, ignore_index=True)
                    print(tab_comp['obr'][n_pp] + ' - ' + tab_comp['pr'][n_pp] + ' - ' + str(j) + '. ' + list_comp[
                        j] + '-' + list_comp[j + 1] + ' - ' + str(dt))
                    ui.listWidget.insertItem(list_row, str(list_row + 1) + '. ' +
                                             tab_comp['obr'][n_pp] + ' проба - ' + tab_comp['pr'][n_pp] +
                                             '. Время выхода: ' + list_comp[j] + ' - ' +
                                             str(round(tab_comp[list_comp[j] + '_t'][n_pp], int(for_round))) + ', ' +
                                             list_comp[j + 1] + ' - ' +
                                             str(round(tab_comp[list_comp[j + 1] + '_t'][n_pp],
                                                       int(for_round))) + '_' + str(n_row) +
                                             '_' + str(j + 2))
                    ui.listWidget.item(list_row).setBackground(QtGui.QColor(240, 230, 140))
                    list_row += 1
        n_row += 1
        ui.progressBar.setValue(n_pp + 1)

    ui.tableWidget.insertRow(n_row)
    ui.tableWidget.setItem(n_row, 0, QTableWidgetItem(obr))
    ui.tableWidget.item(n_row, 0).setBackground(QtGui.QColor(176, 224, 230))
    ui.tableWidget.setVerticalHeaderItem(n_row, QTableWidgetItem(obr))
    ui.tableWidget.setItem(n_row, 1, QTableWidgetItem('среднее'))
    ui.tableWidget.item(n_row, 1).setBackground(QtGui.QColor(176, 224, 230))
    n_col = 2
    for n, comp in enumerate(list_comp + list_param):
        if n < len(list_comp):
            mean_val = tab_comp[comp + '_c'].iloc[pp: n_pp + 1].mean()
        else:
            mean_val = tab_comp[comp].iloc[pp: n_pp + 1].mean()
        tab_mean[comp][obr[:-1]] = mean_val
        ui.tableWidget.setItem(n_row, n_col, QTableWidgetItem(str(round(mean_val, int(for_round)))))
        ui.tableWidget.item(n_row, n_col).setBackground(QtGui.QColor(176, 224, 230))
        n_col += 1
    n_row += 1
    ui.tableWidget.insertRow(n_row)
    ui.tableWidget.setItem(n_row, 0, QTableWidgetItem(obr))
    ui.tableWidget.item(n_row, 0).setBackground(QtGui.QColor(152, 251, 152))
    ui.tableWidget.setVerticalHeaderItem(n_row, QTableWidgetItem(obr))
    ui.tableWidget.setItem(n_row, 1, QTableWidgetItem('k_вариации'))
    ui.tableWidget.item(n_row, 1).setBackground(QtGui.QColor(152, 251, 152))
    n_col = 2
    for n, comp in enumerate(list_comp + list_param):
        if n < len(list_comp):
            k_var = tab_comp[comp + '_c'].iloc[pp: n_pp + 1].std() / tab_comp[comp + '_c'].iloc[
                                                                     pp: n_pp + 1].mean() * 100
        else:
            k_var = tab_comp[comp].iloc[pp: n_pp + 1].std() / tab_comp[comp].iloc[pp: n_pp + 1].mean() * 100
        tab_var[comp][obr[:-1]] = k_var
        ui.tableWidget.setItem(n_row, n_col, QTableWidgetItem(str(round(k_var, int(for_round)))))
        ui.tableWidget.item(n_row, n_col).setBackground(QtGui.QColor(152, 251, 152))
        if k_var > 33:
            if n < len(list_comp):
                cri_val = found_critical_value(tab_comp[comp + '_c'].iloc[pp: n_pp].to_list())
                if cri_val != 'limbo':
                    cri_pr = tab_comp['pr'].iloc[pp: n_pp].loc[tab_comp[comp + '_c'] == cri_val].tolist()[0]
                else:
                    cri_pr = 'не определён'
                    cri_val = 0
            else:
                cri_val = found_critical_value(tab_comp[comp].iloc[pp: n_pp].to_list())
                if cri_val != 'limbo':
                    cri_pr = tab_comp['pr'].iloc[pp: n_pp].loc[tab_comp[comp] == cri_val].tolist()[0]
                else:
                    cri_pr = 'не определён'
                    cri_val = 0
            err = {'n_obr': obr, 'n_pr': comp, 'error': 'k_var = {}, выброс: {}, в пробе: {}'.format(
                str(round(k_var, int(for_round))), str(round(cri_val, int(for_round))), str(cri_pr))}
            tab_error = tab_error.append(err, ignore_index=True)
            ui.listWidget.insertItem(list_row, '{}. {} - {} k_var = {}, выброс: {}, в пробе: {}__{}_{}'.format(
                str(list_row + 1), obr, comp, str(round(k_var, int(for_round))),
                str(round(cri_val, int(for_round))), str(cri_pr), str(n_row), str(n_col)))
            ui.listWidget.item(list_row).setBackground(QtGui.QColor(255, 160, 122))
            ui.tableWidget.item(n_row, 0).setBackground(QtGui.QColor(255, 160, 122))
            ui.tableWidget.item(n_row, 1).setBackground(QtGui.QColor(255, 160, 122))
            ui.tableWidget.item(n_row, n_col).setBackground(QtGui.QColor(255, 160, 122))
            list_row += 1
        n_col += 1
    tab_UV_var = pd.DataFrame(
        tab_var[['Heptane', 'Octane', 'Nonane', 'Decane', 'Undecane', 'Dodecane', 'Tridecane', 'Tetradecane',
                 'Pentadecane', 'Hexadecane', 'Heptadecane', 'Pristane', 'Octadecane', 'Phytane', 'Nonadecane',
                 'Eicosane', 'Heneicosane', 'Docosane', 'Tricosane', 'Tetracosane', 'Pentacosane', 'Hexacosane',
                 'Heptacosane', 'Octacosane', 'Nonacosane', 'Triacontane', 'Hentriacontane', 'Dotriacontane',
                 'Tritriacontane', 'Tetratriacontane', 'Pentatriacontane', 'Hexatriacontane', 'Heptatriacontane',
                 'Octatriacontane', 'Nonatriacontane', 'Tetracontane']])
    tab_UV_var = tab_UV_var.rename(
        columns={'Heptane': 'Heptane (C7)', 'Octane': 'Octane (C8)', 'Nonane': 'Nonane (C9)', 'Decane': 'Decane (C10)',
                 'Undecane': 'Undecane (C11)', 'Dodecane': 'Dodecane (C12)', 'Tridecane': 'Tridecane (C13)',
                 'Tetradecane': 'Tetradecane (C14)', 'Pentadecane': 'Pentadecane (C15)', 'Hexadecane':
                     'Hexadecane (C16)', 'Heptadecane': 'Heptadecane (C17)', 'Pristane': 'Pristane', 'Octadecane':
                     'Octadecane (C18)', 'Phytane': 'Phytane', 'Nonadecane': 'Nonadecane (C19)', 'Eicosane':
                     'Eicosane (C20)', 'Heneicosane': 'Heneicosane (C21)', 'Docosane': 'Docosane (C22)', 'Tricosane':
                     'Tricosane (C23)', 'Tetracosane': 'Tetracosane (C24)', 'Pentacosane': 'Pentacosane (C25)',
                 'Hexacosane': 'Hexacosane (C26)', 'Heptacosane': 'Heptacosane (C27)', 'Octacosane': 'Octacosane (C28)',
                 'Nonacosane': 'Nonacosane (C29)', 'Triacontane': 'Triacontane (C30)', 'Hentriacontane':
                     'Hentriacontane (C31)', 'Dotriacontane': 'Dotriacontane (C32)', 'Tritriacontane':
                     'Tritriacontane (C33)', 'Tetratriacontane': 'Tetratriacontane (C34)', 'Pentatriacontane':
                     'Pentatriacontane (C35)', 'Hexatriacontane': 'Hexatriacontane (C36)', 'Heptatriacontane':
                     'Heptatriacontane (C37)', 'Octatriacontane': 'Octatriacontane (C38)', 'Nonatriacontane':
                     'Nonatriacontane (C39)', 'Tetracontane': 'Tetracontane (C40)'})
    tab_UV_var.to_excel(dir_name + '/результат/К_вар по компонентам.xlsx', float_format="%." + for_round + "f")
    tab_param_var = pd.DataFrame(
        tab_var[['otnpri_fi', 'otnpri_17', 'otnfi_18', 'ki', 'otn27_17', 'cpi19_23', 'cpi17_21', 'cpi19_25',
                 'cpi23_29', 'cpi23_33', 'oepc19', 'oepc21', 'oepc23', 'oepc25', 'oepc27', 'oepc29', 'cpi_2',
                 'otn17_25', 'otn16_29', 'otn35_34', 'c15_c20', 'c21_c30', 'otn15_30', 'c16_c22', 'c23_c29',
                 'otn15_24', 'otn25_34', 'c11_c18', 'otn15_29']])
    tab_param_var = tab_param_var.rename(
        columns={'otnpri_fi': 'Pr/Ph', 'otnpri_17': 'Pr/n-C17', 'otnfi_18': 'Ph/n-C18', 'ki': 'Ki', 'otn27_17':
            'C27/C17', 'cpi19_23': 'CPI nC19-nC23', 'cpi17_21': 'CPI  nC17-nC21', 'cpi19_25': 'CPI  nC19-nC25',
                 'cpi23_29': 'CPI nC23-nC29', 'cpi23_33': 'CPI nC23-nC33', 'oepc19': 'OEP при nС19', 'oepc21':
                     'OEP при nС21', 'oepc23': 'OEP при nС23', 'oepc25': 'OEP при nС25', 'oepc27': 'OEP при nС27',
                 'oepc29': 'OEP при nС29', 'cpi_2': 'CPI nC25-nC33', 'otn17_25': 'nC17/nC25 ', 'otn16_29':
                     'nC16- nC22/nC23- nC29', 'otn35_34': 'nC35/nC34', 'c15_c20': 'nC15-nC20', 'c21_c30': 'nC21-nC30',
                 'otn15_30': 'nC15- nC20/nC21- nC30', 'c16_c22': 'nC16-nC22', 'c23_c29': 'nC23-nC29', 'otn15_24':
                     'nC15- nC17/nC22- nC24', 'otn25_34': 'nC25- nC33/nC26- nC34', 'c11_c18': 'nC11-nC18', 'otn15_29':
                     'nC15- nC19/nC25- nC29'})
    tab_param_var.to_excel(dir_name + '/результат/К_вар по параметрам.xlsx', float_format="%." + for_round + "f")
    tab_UV_mean = pd.DataFrame(
        tab_mean[['Heptane', 'Octane', 'Nonane', 'Decane', 'Undecane', 'Dodecane', 'Tridecane', 'Tetradecane',
                  'Pentadecane', 'Hexadecane', 'Heptadecane', 'Pristane', 'Octadecane', 'Phytane', 'Nonadecane',
                  'Eicosane', 'Heneicosane', 'Docosane', 'Tricosane', 'Tetracosane', 'Pentacosane', 'Hexacosane',
                  'Heptacosane', 'Octacosane', 'Nonacosane', 'Triacontane', 'Hentriacontane', 'Dotriacontane',
                  'Tritriacontane', 'Tetratriacontane', 'Pentatriacontane', 'Hexatriacontane', 'Heptatriacontane',
                  'Octatriacontane', 'Nonatriacontane', 'Tetracontane']])
    tab_UV_mean = tab_UV_mean.rename(
        columns={'Heptane': 'Heptane (C7)', 'Octane': 'Octane (C8)', 'Nonane': 'Nonane (C9)', 'Decane': 'Decane (C10)',
                 'Undecane': 'Undecane (C11)', 'Dodecane': 'Dodecane (C12)', 'Tridecane': 'Tridecane (C13)',
                 'Tetradecane': 'Tetradecane (C14)', 'Pentadecane': 'Pentadecane (C15)', 'Hexadecane':
                     'Hexadecane (C16)', 'Heptadecane': 'Heptadecane (C17)', 'Pristane': 'Pristane', 'Octadecane':
                     'Octadecane (C18)', 'Phytane': 'Phytane', 'Nonadecane': 'Nonadecane (C19)', 'Eicosane':
                     'Eicosane (C20)', 'Heneicosane': 'Heneicosane (C21)', 'Docosane': 'Docosane (C22)', 'Tricosane':
                     'Tricosane (C23)', 'Tetracosane': 'Tetracosane (C24)', 'Pentacosane': 'Pentacosane (C25)',
                 'Hexacosane': 'Hexacosane (C26)', 'Heptacosane': 'Heptacosane (C27)', 'Octacosane': 'Octacosane (C28)',
                 'Nonacosane': 'Nonacosane (C29)', 'Triacontane': 'Triacontane (C30)', 'Hentriacontane':
                     'Hentriacontane (C31)', 'Dotriacontane': 'Dotriacontane (C32)', 'Tritriacontane':
                     'Tritriacontane (C33)', 'Tetratriacontane': 'Tetratriacontane (C34)', 'Pentatriacontane':
                     'Pentatriacontane (C35)', 'Hexatriacontane': 'Hexatriacontane (C36)', 'Heptatriacontane':
                     'Heptatriacontane (C37)', 'Octatriacontane': 'Octatriacontane (C38)', 'Nonatriacontane':
                     'Nonatriacontane (C39)', 'Tetracontane': 'Tetracontane (C40)'})
    tab_UV_mean.to_excel(dir_name + '/результат/средние по компонентам.xlsx', float_format="%." + for_round + "f")
    tab_param_mean = pd.DataFrame(
        tab_mean[['otnpri_fi', 'otnpri_17', 'otnfi_18', 'ki', 'otn27_17', 'cpi19_23', 'cpi17_21', 'cpi19_25',
                  'cpi23_29', 'cpi23_33', 'oepc19', 'oepc21', 'oepc23', 'oepc25', 'oepc27', 'oepc29', 'cpi_2',
                  'otn17_25', 'otn16_29', 'otn35_34', 'c15_c20', 'c21_c30', 'otn15_30', 'c16_c22', 'c23_c29',
                  'otn15_24', 'otn25_34', 'c11_c18', 'otn15_29']])
    tab_param_mean = tab_param_mean.rename(
        columns={'otnpri_fi': 'Pr/Ph', 'otnpri_17': 'Pr/n-C17', 'otnfi_18': 'Ph/n-C18', 'ki': 'Ki', 'otn27_17':
            'C27/C17', 'cpi19_23': 'CPI nC19-nC23', 'cpi17_21': 'CPI  nC17-nC21', 'cpi19_25': 'CPI  nC19-nC25',
                 'cpi23_29': 'CPI nC23-nC29', 'cpi23_33': 'CPI nC23-nC33', 'oepc19': 'OEP при nС19', 'oepc21':
                     'OEP при nС21', 'oepc23': 'OEP при nС23', 'oepc25': 'OEP при nС25', 'oepc27': 'OEP при nС27',
                 'oepc29': 'OEP при nС29', 'cpi_2': 'CPI nC25-nC33', 'otn17_25': 'nC17/nC25 ', 'otn16_29':
                     'nC16- nC22/nC23- nC29', 'otn35_34': 'nC35/nC34', 'c15_c20': 'nC15-nC20', 'c21_c30': 'nC21-nC30',
                 'otn15_30': 'nC15- nC20/nC21- nC30', 'c16_c22': 'nC16-nC22', 'c23_c29': 'nC23-nC29', 'otn15_24':
                     'nC15- nC17/nC22- nC24', 'otn25_34': 'nC25- nC33/nC26- nC34', 'c11_c18': 'nC11-nC18', 'otn15_29':
                     'nC15- nC19/nC25- nC29'})
    tab_param_mean.to_excel(dir_name + '/результат/средние по параметрам.xlsx', float_format="%." + for_round + "f")
    ui.tableWidget.resizeColumnsToContents()
    ui.label.setText('Готово!')
    ui.label.setStyleSheet('color: green')
    print(tab_error)
    tab_error.to_excel(dir_name + '/результат/ошибки.xlsx')


def scroll_to_error():
    row = int(ui.listWidget.item(ui.listWidget.currentRow()).text().split('_')[-2])
    col = int(ui.listWidget.item(ui.listWidget.currentRow()).text().split('_')[-1])
    ui.tableWidget.setCurrentCell(row, col)


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)
    sys.exit()


def open_instruction():
    Manual = QtWidgets.QDialog()
    ui_m = Ui_Manual()
    ui_m.setupUi(Manual)
    Manual.show()

    def open_template_extr():
        subprocess.call('шаблоны/Журнал экстракция шаблон.xlsx', shell=True)

    def open_template_kern():
        subprocess.call('шаблоны/Журнал керн шаблон.xlsx', shell=True)

    def open_template_obr():
        subprocess.call('шаблоны/Проба шаблон.xlsx', shell=True)

    ui_m.pushButton_templ_extr.clicked.connect(open_template_extr)
    ui_m.pushButton_templ_kern.clicked.connect(open_template_kern)
    ui_m.pushButton_templ_obr.clicked.connect(open_template_obr)
    Manual.exec_()


def open_formulas():
    Formulas = QtWidgets.QDialog()
    ui_f = Ui_Formulas()
    ui_f.setupUi(Formulas)
    Formulas.show()

    Formulas.exec_()


sys.excepthook = log_uncaught_exceptions

ui.pushButton_dir.clicked.connect(open_dir)
ui.pushButton_instr.clicked.connect(open_instruction)
ui.pushButton_fm.clicked.connect(open_formulas)
ui.listWidget.itemClicked.connect(scroll_to_error)

sys.exit(app.exec_())
