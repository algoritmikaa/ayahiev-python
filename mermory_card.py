from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                              QVBoxLayout, QMessageBox, QRadioButton,
                                  QHBoxLayout, QGroupBox, QButtonGroup)


from random import shuffle


def show_results():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')





def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    GroupBox.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    GroupBox.setExclusive(True)





def ask(question1, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    card.setText(question1)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_corret.setText(right_answer)
    show_question()


def show_correct(res):
    lb_result.setText(res)
    show_results()



def check_answer():
    if answers[0].isChecked():
        show_correct('Правда')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправда')





app = QApplication([])
main_win = QWidget()
main_win.resize(500, 300)
main_win.setWindowTitle('Mermory card')


card = QLabel('Вопрос')
button = QPushButton('Ответить')
rbt1 = QRadioButton('Ответ1')
rbt2 = QRadioButton('Ответ2')
rbt3 = QRadioButton('Ответ3')
rbt4 = QRadioButton('Ответ4')

answers = [rbt1, rbt2, rbt3, rbt4]


GroupBox = QButtonGroup()
GroupBox.addButton(rbt1)
GroupBox.addButton(rbt2)
GroupBox.addButton(rbt3)
GroupBox.addButton(rbt4)




RadioGroupBox = QGroupBox('Варианты ответов')



main_group_line = QVBoxLayout()
main1 = QHBoxLayout()
main2 = QHBoxLayout()



main1.addWidget(rbt1)
main1.addWidget(rbt2)
main2.addWidget(rbt3)
main2.addWidget(rbt4)


main_group_line.addLayout(main1)
main_group_line.addLayout(main2)

RadioGroupBox.setLayout(main_group_line)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel("Правда/неправда")
lb_corret = QLabel('Сам верный ответ')



ans_group_line = QVBoxLayout()
ans_group_line.addWidget(lb_result, alignment=(Qt.AlignTop | Qt.AlignLeft))
ans_group_line.addWidget(lb_corret, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(ans_group_line)



main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()



line1.addWidget(card, alignment=Qt.AlignCenter)
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3.addStretch(2)
line3.addWidget(button, stretch=2)
line3.addStretch(2)
AnsGroupBox.hide()



main_line.addLayout(line1, stretch=2)
main_line.addLayout(line2, stretch=8)
main_line.addStretch(1)
main_line.addLayout(line3, stretch=2)
main_line.addStretch(1)
main_line.addSpacing(5)





main_line.addLayout(line1)
main_line.addLayout(line2)
main_line.addLayout(line3)

main_win.setLayout(main_line)


ask('кто съел весь королевский торт, о крошка осталась от него пожалуй съем', 'я съел когда спал', 'убайд', 'мой кот', 'продал')
button.clicked.connect(check_answer)

main_win.show()
app.exec()


