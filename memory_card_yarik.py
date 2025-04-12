from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("Государственный язык Бразилии", "Португальский", "Бразильский", "Испанский", "Итальянский"))
question_list.append(Question("Какого нету цвета на флаге РФ", "Зелёный", "белый", "синий", "красный"))
question_list.append(Question("Национальная хижина якутов", "ураса", "Юрта", "Иглу", "Хата"))
question_list.append(Question("Сколько стран есть в мире в 2024 году", "206", "197", "52", "273"))
question_list.append(Question("Сколько мне лет", "10", "15", "18", "7"))
question_list.append(Question("Как меня зовут", "Ярослав", "Влад", "Илья", "Михаил"))
question_list.append(Question("Сколько звёзд в Млечном пути", "> 100 млрд", "< 10 млн", "> 1 трл", "< 100 млн"))
question_list.append(Question("Какая страна первая побывала на луне", "Америка", "Россия", "Китай", "Япония"))
question_list.append(Question("В каком году умер М.Ю.Лермонтов", "1841", "1913", "1895", "1794"))
question_list.append(Question("В каком году родился и умер А.С.Пушкин", "1799 - 1837", "1835 - 1873", "1814 - 1841", "1754 - 1812"))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory card')

btn_ok = QPushButton("Ответить")
lb_quest = QLabel('Какой то вопрос?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Вариант 1')
rbtn2 = QRadioButton('Вариант 2')
rbtn3 = QRadioButton('Вариант 3')
rbtn4 = QRadioButton('Вариант 4')

layaout_ans1 = QHBoxLayout()
layaout_ans2 = QVBoxLayout()
layaout_ans3 = QVBoxLayout()

layaout_ans2.addWidget(rbtn1)
layaout_ans2.addWidget(rbtn2)
layaout_ans3.addWidget(rbtn3)
layaout_ans3.addWidget(rbtn4)

layaout_ans1.addLayout(layaout_ans2)
layaout_ans1.addLayout(layaout_ans3)
RadioGroupBox.setLayout(layaout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_result = QLabel("прав ты или нет")
lb_correct = QLabel("ответ будет тут")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_l1= QHBoxLayout()
layout_l2 = QHBoxLayout()
layout_l3 = QHBoxLayout()


layout_l1.addWidget(lb_quest, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_l2.addWidget(RadioGroupBox)
layout_l2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_l3.addStretch(1)
layout_l3.addWidget(btn_ok, stretch=2)
layout_l3.addStretch(1)
layout_card = QVBoxLayout()

layout_card.addLayout(layout_l1, stretch=2)
layout_card.addLayout(layout_l2, stretch=8)
layout_card.addStretch(1)

layout_card.addLayout(layout_l3, stretch=1)
layout_card.addStretch(1)

layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Следующий вопрос")

def show_ques():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Ответить")
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_quest.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_ques()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно! ^_^")
        window.score += 1
        print('Статистика \n-Всего вопросов: ', window.total, '\n-Правильно ответов', window.score)
        print('Рейтинг:', (window.score/window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("НЕПРАВИЛЬНО! :-(")
            print('Рейтинг:', (window.score/window.total * 100), '%')

def next_ques():
    window.total += 1
    print('Статистика \n-Всего вопросов: ', window.total, '\n-Правильно ответов', window.score)
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)

def click_ok():
    if btn_ok.text() == "Ответить":
        check_answer()
    else:
        next_ques()

window.cur_question = -1

btn_ok.clicked.connect(click_ok)

window.score = 0
window.total = 0

next_ques()

window.setLayout(layout_card)
window.resize(400, 300)
window.show()
app.exec()
