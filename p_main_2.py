import sys
import time
import os
import xlwt
import xlrd
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from p2_file import *
from p2_login import *
from p2_function import *
from p2_parameter import *
import tui


class MyMainWindow(QMainWindow, Ui_login):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.account_path = r"D:\luopengcheng\TXT\python\UI"
        self.account_file = "account.xls"
        self.account = os.environ.get("USERNAME")  # 从系统账户里获取用户名

        self.lineEdit_account.setText(self.account)
        self.date_now = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.bc = Background(self)
        self.btn()

    def use_palette(self):  # 设置背景图
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(),
                             QtGui.QBrush(QtGui.QPixmap(r"D:\luopengcheng\TXT\python\UI\bc2.png")))
        self.setPalette(window_pale)

    def btn(self):
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_register.clicked.connect(self.reg)
        self.pushButton_forgot.clicked.connect(self.print_info)

    def login(self):
        if os.path.exists(self.account_path) & os.path.exists(self.account_file):
            os.chdir(self.account_path)
            password = self.lineEdit_password.text()  # 从输入框提取信息
            workbook1 = xlrd.open_workbook(self.account_file, formatting_info=True)  # 获取文件
            sheet1 = workbook1.sheet_by_name('account_info')
            info = dict(zip(sheet1.col_values(0), sheet1.col_values(1)))
            # print(self.account)
            if self.account in sheet1.col_values(0):
                if password == info[self.account]:
                    # if self.account == "HZ4EYB":
                    #     QMessageBox.about(self, "欢迎大佬", "一日不见，如隔三秋哇 ｡◕ᴗ◕｡")
                    # else:
                    #     QMessageBox.about(self, "欢迎%s ｡◕ᴗ◕｡" % self.account)
                    self.file_ui = File()
                    self.file_ui.show()
                    self.close()
                else:
                    QMessageBox.about(self, "提示", "密码错了！找管理员去！")
            else:
                QMessageBox.about(self, "提示", "嘿，哥们儿，你还没注册啦！！(❐_❐✧ ")
        else:
            QMessageBox.about(self, "提示", "账户不存在，先注册一个吧 ｡◕ᴗ◕｡")

    def print_info(self):
        QMessageBox.about(self, "哦噢！！！", "真搞忘啦，好遗憾！！！\n去找管理员吧 ಠ╭╮ಠ")

    def reg(self):
        if not os.path.exists(self.account_path):
            os.makedirs(self.account_path)
        os.chdir(self.account_path)
        password = self.lineEdit_password.text()  # 从输入框提取信息
        if len(password) < 4:
            QMessageBox.about(self, "提示", "嘿，哥们儿，密码不能小于4位数啦 ｡◕ᴗ◕｡")

        elif os.path.exists(self.account_file) & (len(password) >= 4):
            from xlutils.copy import copy
            workbook1 = xlrd.open_workbook(self.account_file, formatting_info=True)  # xlrd形式获取文件
            sheet1 = workbook1.sheet_by_name('account_info')
            rows = sheet1.nrows  # 获取总行数
            if self.account in sheet1.col_values(0):
                QMessageBox.about(self, "提示", "嘿，哥们儿，你已经注册过啦 ｡◕ᴗ◕｡")
            else:
                workbook = copy(workbook1)  # copy形式可将xlrd转换到xlwt，用于在现有的xls里追加数据
                sheet = workbook.get_sheet('account_info')
                self.wt(workbook, sheet, rows, password)
        else:
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet("account_info", cell_overwrite_ok=True)
            tall_style = xlwt.easyxf('font:height 400;')  # 20pt,类型小初的字号
            sheet.write(0, 0, "Account")
            sheet.write(0, 1, "Password")
            sheet.write(0, 2, "register_date")
            first_row = sheet.row(0)
            first_row.set_style(tall_style)
            rows = 1
            sheet.col(0).width = 256 * 15  # A列宽度，256为衡量单位，15为字符数
            sheet.col(1).width = 256 * 15
            sheet.col(2).width = 256 * 20
            self.wt(workbook, sheet, rows, password)

    def wt(self, workbook, sheet, rows, password):
        sheet.write(rows, 0, self.account)
        sheet.write(rows, 1, password)
        sheet.write(rows, 2, self.date_now)
        workbook.save("account.xls")
        replay = QMessageBox.information(self, "菜鸟%s" % self.account, "恭喜恭喜，注册成功！\n要直接登录吗？ (◕ω◕)",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if replay == QMessageBox.Yes:
            self.file_ui.show()
            self.close()


class File(QMainWindow, Ui_file):
    def __init__(self, parent=None):
        super(File, self).__init__(parent)
        self.setupUi(self)
        self.validator()
        self.file_btn()
        self.bc = Background(self)

    def file_btn(self):
        self.toolButton_open.clicked.connect(self.open_file)
        self.pushButton_next.clicked.connect(self.next_btn)

    def validator(self):  # 输入信息过滤器
        my_regex = QtCore.QRegExp("^[a-zA-Z0-9_]{10}$")
        my_validator = QtGui.QRegExpValidator(my_regex, self.lineEdit_project)
        self.lineEdit_project.setValidator(my_validator)
        my_regex2 = QtCore.QRegExp("^V[0-9|.]{10}$")
        my_validator2 = QtGui.QRegExpValidator(my_regex2, self.lineEdit_version)
        self.lineEdit_version.setValidator(my_validator2)
        # QMessageBox.about(self, "注意", "此处仅支持字母、数字、下划线三种形式！")

    def open_file(self):
        file = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', 'CAD files (*.x_t)')
        path = file[0]
        self.lineEdit_file.setText(path)

    def next_btn(self):  # TODO global参数
        global cad_file, file_path, file_name, date_now, scdoc_file, mesh_file, new_solve_jou, new_mesh_jou  # 全局参数声明
        cad_path = self.lineEdit_file.text()
        project = self.lineEdit_project.text()
        version = self.lineEdit_version.text()
        line = "_"
        date_now = time.strftime('%y%m%d', time.localtime(time.time()))
        file_name = project + line + version + line + date_now
        mesh_file = file_name + ".msh"
        new_mesh_jou = file_name + "_mesh.jou"
        scdoc_file = file_name + ".scdoc"
        new_solve_jou = file_name + "_solve.jou"
        # file_path = ""
        # cad_file = ""

        if (len(project) == 0) | (len(version) == 0) | (len(cad_path) == 0):
            QMessageBox.about(self, "提示", "嘿，哥们儿，你的信息还没填完哟 ｡◕ᴗ◕｡")

        elif " " in cad_path:
            QMessageBox.about(self, "警告！！！", "文件名和路径信息不能有空格，请修正！！！ ｡◕ᴗ◕｡")

        elif self.check(cad_path) is True:
            file_path, cad_file = os.path.split(cad_path)
            print(file_path, cad_file)
            self.hide()
            self.func = Function()
            self.func.show()

    def check(self, cad_path):
        for ch in cad_path:
            if u'\u4e00' <= ch <= u'\u9fff':
                QMessageBox.about(self, "警告！！！", "文件名和路径信息不能有中文字符，请修正！！！ ｡◕ᴗ◕｡")
        else:
            return True


class Function(QMainWindow, Ui_function):
    def __init__(self, parent=None):
        super(Function, self).__init__(parent)
        self.setupUi(self)
        self.bc = Background(self)
        self.func_btn()

    def func_btn(self):
        self.pushButton_back.clicked.connect(self.back_btn)
        self.pushButton_next.clicked.connect(self.next_btn)

    def func_default(self):
        self.pushButton_CG.setChecked(True)
        self.checkBox_sphere.setChecked(True)
        self.checkBox_evap.setChecked(True)
        self.checkBox_distributor.setChecked(True)

    def back_btn(self):
        replay = QMessageBox.question(self, "Remind", "Data will lost for the current page！",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if replay == QMessageBox.Yes:
            self.hide()
            self.file_ui = File()
            self.file_ui.show()

    def next_btn(self):
        # TODO 测试用
        # file_path = r"C:\Users\hz4eyb\Desktop\pas"
        # file_name = "t1_V1_190912"
        # cad_file = "1test_p.x_t"
        # scdoc_file = file_name + ".scdoc"
        replay = QMessageBox.information(self, "Remind", "Make sure the required parts are selected",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if replay == QMessageBox.Yes:
            os.chdir(file_path)
            self.ex_facename()
            tui.write_mesh_jou(file_path, file_name)
            self.CAD_thread = SCDM()
            if os.path.exists(scdoc_file):
                replay = QMessageBox.information(self, "Warning", "SCDOC file already exist\nPlease 'confirm' "
                                                                  "if the current file needs to be replaced｡◕ᴗ◕｡",
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if replay == QMessageBox.Yes:
                    self.CAD_thread.start()
            else:
                self.CAD_thread.start()
            print("4")
            self.hide()
            self.para = Parameter()
            self.para.show()
            self.check_part()  # 传递已选项到参数页

    def ex_facename(self):  # 输出所选几何的面和体
        self.face_name = "facename.py"
        message1, message2 = self.message_fv()
        message = "face_list = %s\nbody_list = %s\n" % (message1, message2)  # TODO
        # message = """
        # , cad_file, scdoc_file
# print('start script')
# # Open File
# DocumentOpen.Execute(r"%s", FileSettings1, GetMaps("220e223d"))
# body_list = %s
# body_number = len(body_list)
#
# i = 0
# for i in range(body_number):
#     selection = Selection.Create(Parti)
#     result = ComponentHelper.CreateNewComponent(selection, Info2)
#     # Rename 'Component1' to 'eva'
#     # selection = Selection.Create(Part3)
#     result = RenameObject.Execute(selection,body_list[i])
#     i += 1
#
# # face rename
# face_list = %s
# for i in range(len(face_list)):
#     # Create Named Selection Group
#     primarySelection = Selection.Create(Facei)
#     secondarySelection = Selection()
#     result = NamedSelection.Create(primarySelection, secondarySelection)
#     # Rename Named Selection
#     result = NamedSelection.Rename("Groupi", face_list[i])
#
# # save file
# options = ExportOptions.Create()
# DocumentSave.Execute(r"%s", options)
# print('script finished')
# """ % (cad_file, message2, message1, scdoc_file)

        fp = open(self.face_name, 'w')
        fp.write(message)
        fp.close()
        print("%s 写入成功" % self.face_name)
        # os.system(self.face_name)

    def message_fv(self):
        ef = hf = ev = hv = sf = df = t1f = t2f = sv = dv = t1v = t2v = []
        if self.checkBox_evap.isChecked() is True:
            ef = ["evap_in", "evap_out"]
            ev = ["v_evap"]
        if self.checkBox_heater.isChecked() is True:
            hf = ["heater_in", "heater_out"]
            hv = ["v_heater"]
        if self.checkBox_sphere.isChecked() is True:
            sf = ["inlet"]
            sv = ["v_sphere"]
        if self.checkBox_distributor.isChecked() is True:
            df = ["outlet"]  # TODO 出口数需要变更
            dv = ["v_distributor"]
        if self.checkBox_tempdoor1.isChecked() is True:
            t1f = ["tempdoor1_wall"]
            t1v = ["v_tempdoor1"]
        if self.checkBox_tempdoor2.isChecked() is True:
            t2f = ["tempdoor2_wall"]
            t2v = ["v_tempdoor2"]

        message_f = str(ef + hf + sf + df + t1f + t2f)
        message_v = str(ev + hv + sv + dv + t1v + t2v)
        print(message_f, message_v)
        return message_f, message_v

    def check_part(self):
        if self.checkBox_evap.isChecked() is True:
            self.para.radioButton_evap.show()
        if self.checkBox_heater.isChecked() is True:
            self.para.radioButton_heater.show()
        if self.checkBox_tempdoor1.isChecked() is True:
            self.para.radioButton_tempdoor1.show()
        if self.checkBox_tempdoor2.isChecked() is True:
            self.para.radioButton_tempdoor2.show()


class Background(QMainWindow):
    def __init__(self, ui):
        super(Background, self).__init__()
        self.use_palette(ui)

    def use_palette(self, ui):  # 设置背景图
        png_file = r"D:\luopengcheng\TXT\python\UI\es.png"
        window_pale = QtGui.QPalette()
        window_pale.setBrush(ui.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(png_file)))
        ui.setPalette(window_pale)


class SCDM(QThread):
    finishCAD = pyqtSignal(str)

    def __init__(self, parent=None):
        super(SCDM, self).__init__(parent)

    def run(self):
        import subprocess  # TODO 导入模型，设置边界名称、关键体名称，share，保存并退出
        subprocess.Popen(r'C:\Program Files\ANSYS Inc\v191\scdm\SpaceClaim.exe', shell=True)
        # os.chdir(r"C:\Program Files\ANSYS Inc\v191\SCDM")
        # os.system("SpaceClaim.exe")
        self.finishCAD.emit('CAD软件已关闭')


class Parameter(QMainWindow, Ui_parameter):

    def __init__(self):
        super(Parameter, self).__init__()
        self.setupUi(self)
        self.bc = Background(self)
        self.file_path = r"D:\luopengcheng\TXT\python\UI"
        self.file_name = 'test'
        self.default_state2()
        self.default_state()
        self.mesh = Meshing()
        self.para_btn()
        self.scdoc_file = self.file_name + ".scdoc"
        self.mesh_file = self.file_name + ".msh"
        self.meshing_jou = self.file_name + "_mesh.jou"
        self.solve_jou = self.file_name + "_solve.jou"
        # self.OpenDialog()

    def open_dialog(self):  # TODO 槽函数未测试完成
        pass
        # dialog = Function(self)
        # '''连接子窗口的内置信号与主窗口的槽函数'''

        # dialog.checkBox_evap.connectNotify.connect(self.radioButton_evap.show)
        # dialog.checkBox_evap.isSignalConnected.connect(self.radioButton_evap.show)
        # dialog.checkBox_evap.clicked.connect(self.RadioButton_evap.show)
        # '''连接子窗口的自定义信号与主窗口的槽函数'''
        # dialog.Signal_OneParameter.connect(self.deal_emit_slot)
        # dialog.show()

    def check_data(self):
        b = 0
        if self.radioButton_base.isHidden() is False:
            if (len(self.lineEdit_massflow.text()) == 0) | \
                    (len(self.lineEdit_num.text()) == 0) | \
                    (len(self.lineEdit_inloos.text()) == 0):
                b += 1
                QMessageBox.about(self, "提示", "嘿，哥们儿，base模块还没填完哟 ｡◕ᴗ◕｡")

        if self.radioButton_evap.isHidden() is False:
            if (len(self.lineEdit_ec1.text()) == 0) | (len(self.lineEdit_ec2.text()) == 0) | \
                    (len(self.lineEdit_ex1.text()) == 0) | (len(self.lineEdit_ex2.text()) == 0) | \
                    (len(self.lineEdit_ey1.text()) == 0) | (len(self.lineEdit_ey2.text()) == 0) | \
                    (len(self.lineEdit_ez1.text()) == 0) | (len(self.lineEdit_ez2.text()) == 0):
                b += 1
                QMessageBox.about(self, "提示", "嘿，哥们儿，evap模块还没填完哟 ｡◕ᴗ◕｡")

        if self.radioButton_heater.isHidden() is False:
            if (len(self.lineEdit_hc1.text()) == 0) | (len(self.lineEdit_hc2.text()) == 0) | \
                    (len(self.lineEdit_hx1.text()) == 0) | (len(self.lineEdit_hx2.text()) == 0) | \
                    (len(self.lineEdit_hy1.text()) == 0) | (len(self.lineEdit_hy2.text()) == 0) | \
                    (len(self.lineEdit_hz1.text()) == 0) | (len(self.lineEdit_hz2.text()) == 0):
                b += 1
                QMessageBox.about(self, "提示", "嘿，哥们儿，heater模块还没填完哟 ｡◕ᴗ◕｡")

        if b == 0:
            return True
        else:
            # print(a)
            return False

    def default_state(self):
        self.radioButton_heater.hide()
        self.radioButton_evap.hide()
        self.radioButton_tempdoor1.hide()
        self.radioButton_tempdoor2.hide()
        self.pushButton_solve.setEnabled(False)
        self.base.show()

    def default_state2(self):
        self.evap.hide()
        self.heater.hide()
        self.base.hide()

    def para_btn(self):
        self.radioButton_base.clicked.connect(lambda: self.only_show(self.base))
        self.radioButton_evap.clicked.connect(lambda: self.only_show(self.evap))
        self.radioButton_heater.clicked.connect(lambda: self.only_show(self.heater))
        self.pushButton_import.clicked.connect(self.import_btn)
        self.pushButton_export.clicked.connect(self.export_btn)
        self.pushButton_mesh.clicked.connect(self.mesh_btn)
        self.pushButton_solve.clicked.connect(self.solve_btn)
        self.pushButton_back.clicked.connect(self.back_btn)

    def back_btn(self):
        replay = QMessageBox.warning(self, "注意", "返回后当前页面的数据会丢失！！！\n返回之前或许需要export暂存数据 ｡◕ᴗ◕｡",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if replay == QMessageBox.Yes:
            self.hide()
            self.func_ui = Function()
            self.func_ui.show()

    def keyPressEvent(self, e):  # 设置快捷键(单键）
        if e.key() == Qt.Key_F4:
            self.lineEdit_massflow.setText('1')
            self.lineEdit_num.setText('1')
            self.lineEdit_inloos.setText('1')
            # self.mesh_btn()

    def key(self, e):  # 设置快捷键(组合键）TODO 未完成
        if e.key() == Qt.Key_1:
            if QApplication.keyboardModifiers() == Qt.ControlModifier:
                self.mesh_btn()

    def import_btn(self):
        # file_name = "test"
        excel_file = QFileDialog.getOpenFileName(self, "Open file", "./", "Excel Files (*.xls *.xlsm *,xlsx)")
        worksheet = xlrd.open_workbook(excel_file[0])
        table = worksheet.sheet_by_name(file_name + "_info")
        info = dict(zip(table.col_values(0), table.col_values(1)))  # 把Excel表中的第一列和第二列转换为字典形式
        # print(info["massflow"])
        self.lineEdit_massflow.setText(info["massflow"]),
        self.lineEdit_inloos.setText(info["inlet_loos_coef"]),
        self.lineEdit_num.setText(info["iterate_num"]),
        self.lineEdit_ec1.setText(info["evap_C1"]),
        self.lineEdit_ec2.setText(info["evap_C2"]),
        self.lineEdit_ex1.setText(info["evap_dx1"]),
        self.lineEdit_ex2.setText(info["evap_dx2"]),
        self.lineEdit_ey1.setText(info["evap_dy1"]),
        self.lineEdit_ey2.setText(info["evap_dy2"]),
        self.lineEdit_ez1.setText(info["evap_dz1"]),
        self.lineEdit_ez2.setText(info["evap_dz2"]),
        self.lineEdit_hc1.setText(info["heater_C1"]),
        self.lineEdit_hc2.setText(info["heater_C2"]),
        self.lineEdit_hx1.setText(info["heater_dx1"]),
        self.lineEdit_hx2.setText(info["heater_dx2"]),
        self.lineEdit_hy1.setText(info["heater_dy1"]),
        self.lineEdit_hy2.setText(info["heater_dy2"]),
        self.lineEdit_hz1.setText(info["heater_dz1"]),
        self.lineEdit_hz2.setText(info["heater_dz2"]),
        self.lineEdit_htemp.setText(info["heater_temp"])

    def export_btn(self):  # TODO 微测试完成
        check = self.check_data()
        # dict_ex = self.dict_exim()
        if check is True:  # 参数值有空需要提醒
            replay = QMessageBox.warning(self, "警告", "嘿，哥们儿，本次仅导出本页面填写的参数哟\n"
                                                     "另外，本次导出会删除历史数据后重新导出!!!\n"
                                                     "请'确认'是否需要导出当前数据｡◕ᴗ◕｡",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if replay == QMessageBox.Yes:
                os.chdir(file_path)
                workbook = xlwt.Workbook()
                sheet = workbook.add_sheet(file_name + "_info", cell_overwrite_ok=True)
                tall_style = xlwt.easyxf('font:height 400;')  # 20pt,类型小初的字号
                first_row = sheet.row(0)
                first_row.set_style(tall_style)
                row = 1
                sheet.col(0).width = 256 * 20  # A列宽度，256为衡量单位，22为字符数
                sheet.write(row - 1, 0, "type")
                sheet.write(row - 1, 1, "parameter")
                row += 1

                dict_ex = {
                    "massflow": self.lineEdit_massflow.text(),
                    "inlet_loos_coef": self.lineEdit_inloos.text(),
                    "iterate_num": self.lineEdit_num.text(),
                    "evap_C1": self.lineEdit_ec1.text(),
                    "evap_C2": self.lineEdit_ec2.text(),
                    "evap_dx1": self.lineEdit_ex1.text(),
                    "evap_dx2": self.lineEdit_ex2.text(),
                    "evap_dy1": self.lineEdit_ey1.text(),
                    "evap_dy2": self.lineEdit_ey2.text(),
                    "evap_dz1": self.lineEdit_ez1.text(),
                    "evap_dz2": self.lineEdit_ez2.text(),
                    "heater_C1": self.lineEdit_hc1.text(),
                    "heater_C2": self.lineEdit_hc2.text(),
                    "heater_dx1": self.lineEdit_hx1.text(),
                    "heater_dx2": self.lineEdit_hx2.text(),
                    "heater_dy1": self.lineEdit_hy1.text(),
                    "heater_dy2": self.lineEdit_hy2.text(),
                    "heater_dz1": self.lineEdit_hz1.text(),
                    "heater_dz2": self.lineEdit_hz2.text(),
                    "heater_temp": self.lineEdit_htemp.text()
                }
                for a in dict_ex:
                    sheet.write(row - 1, 0, a)
                    sheet.write(row - 1, 1, dict_ex[a])
                    row += 1  # 行加一
                    # print(a)
                workbook.save(file_path + '\\' + file_name + '.xls')
                QMessageBox.about(self, "提示", "参数导出成功｡◕ᴗ◕｡")

    def mesh_btn(self):
        # file_path = r"D:\share\1test"
        os.chdir(file_path)
        check = self.check_data()
        evap_C1 = self.lineEdit_ec1.text()
        evap_C2 = self.lineEdit_ec2.text()
        evap_dx1 = self.lineEdit_ex1.text()
        evap_dx2 = self.lineEdit_ex2.text()
        evap_dy1 = self.lineEdit_ey1.text()
        evap_dy2 = self.lineEdit_ey2.text()
        evap_dz1 = self.lineEdit_ez1.text()
        evap_dz2 = self.lineEdit_ez2.text()
        heater_C1 = self.lineEdit_hc1.text()
        heater_C2 = self.lineEdit_hc2.text()
        heater_dx1 = self.lineEdit_hx1.text()
        heater_dx2 = self.lineEdit_hx2.text()
        heater_dy1 = self.lineEdit_hy1.text()
        heater_dy2 = self.lineEdit_hy2.text()
        heater_dz1 = self.lineEdit_hz1.text()
        heater_dz2 = self.lineEdit_hz2.text()
        heater_temp = self.lineEdit_htemp.text()
        massflowin = self.massflow.text()
        outlet_loos_coef = self.lineEdit_inloos.text()  # TODO 跟UI里的inloos关系异常
        iterate_num = self.lineEdit_num.text()
        # test test test

        if (check is True) and os.path.exists(new_mesh_jou) and os.path.exists(scdoc_file):

            tui.write_solve_jou(file_path, file_name, outlet_loos_coef, massflowin, heater_temp, iterate_num,
                                evap_C1, evap_C2, evap_dx1, evap_dx2, evap_dy1, evap_dy2, evap_dz1, evap_dz2,
                                heater_C1, heater_C2, heater_dx1, heater_dx2, heater_dy1, heater_dy2, heater_dz1, heater_dz2)
            self.mesh.start()  # TODO start 可启动多线程
            self.pushButton_mesh.setDisabled(True)
            self.mesh.finishmesh.connect(self.mesh_back)

        else:
            self.textNote.append("数据不完整或scdoc文件不存在，请核查！")

    def mesh_back(self, msg):
        self.textNote.append(msg)  # mesh结果反馈到交互窗口
        self.pushButton_solve.setEnabled(True)

    def solve_btn(self):
        # file_path = r"D:\luopengcheng\works\MQB_A1\foot_V3_0827"
        # new_solve_jou = file_path + "MQBA1_foot_V3_0903_solve.jou"
        os.chdir(file_path)
        if os.path.exists(new_solve_jou) & os.path.exists(mesh_file):
            import subprocess
            myWin.hide()
            subprocess.Popen(r"C:\Program Files\ANSYS Inc\v191\fluent\ntbin\win64\fluent 3d -t4 -gu -i %s\%s"
                             % (file_path, new_solve_jou), shell=True, stdout=subprocess.PIPE)
            myWin.show()
        else:
            print("%s或%s文件缺失，去查看下吧！" % (new_solve_jou, mesh_file))

    def only_show(self, part):  # parameter页选部件用
        self.default_state2()
        part.show()


class Meshing(QThread):
    finishmesh = pyqtSignal(str)

    def __init__(self):
        super(Meshing, self).__init__()

    def run(self):
        import subprocess
        print("run")
        # new_meshing_jou = file_name + "_mesh.jou"
        os.chdir(r'C:\Program Files\ANSYS Inc\v191\fluent\ntbin\win64')
        # p = subprocess.Popen(r"fluent -gu 3d -t24", shell=True, stdout=subprocess.PIPE)
        p = subprocess.Popen(r"fluent 3d -t12 -meshing -i %s\%s" % (file_path, new_mesh_jou),
                             shell=True, stdout=subprocess.PIPE)
        nl = 0
        while p.poll() is None:
            nl += 1
            line = p.stdout.readline()
            msg = line.decode()
            print(nl, msg)
            if "Unexpected license problem" in msg:
                p.terminate()   # 结束当前进程
                print("抱歉，来晚了，license被抢完了，晚点儿在来看看吧！")
                break
            if "error Object:" in msg:
                p.terminate()
                print("老铁，几何导入出错了，回去检查下几何再试试呗！")
                break

        self.finishmesh.emit('Mesh已完成!')


class time_count():
    def __init__(self):
        super(time_count, self).__init__()
        self.star_time = time.strftime('%H:%M:%S', time.localtime(time.time()))  # TODO 计时器，可能会用到多线程
        self.time_c()

    def time_c(self):
        print("计时开始……")
        print("当前时间：%s" % self.star_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # myWin = MyMainWindow()
    myWin = File()
    # myWin = Function()
    # myWin = Parameter()
    myWin.show()
    sys.exit(app.exec_())
