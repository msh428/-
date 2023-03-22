import os
import sys
import random
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class LunchRecommendation(QWidget):
    def __init__(self):
        super().__init__()
        self.update_from_github()
        self.initUI()

    def initUI(self):
        # 윈도우 크기와 제목 설정
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('점심 추천 프로그램')

        # 레이블 생성
        self.label = QLabel('오늘 점심은 뭘 먹을까요?', self)
        self.label.move(50, 30)
        self.label.resize(200, 30)

        # 버튼 생성
        self.button = QPushButton('추천 받기', self)
        self.button.move(100, 100)
        self.button.resize(100, 30)
        self.button.clicked.connect(self.show_recommendation)

    def show_recommendation(self):
        # 추천할 음식 리스트
        menu = ['피자', '치킨', '햄버거', '짜장면', '떡볶이', '초밥', '샐러드', '샌드위치']

        # 랜덤하게 추천
        recommendation = random.choice(menu)

        # 추천 결과를 레이블에 출력
        self.label.setText(f'오늘 점심은 "{recommendation}" 어떠세요?')

    def update_from_github(self):
        try:
            if not os.path.exists('lunch-recommendation'):
                subprocess.run(['git', 'clone', 'https://github.com/username/lunch-recommendation.git'])
            else:
                os.chdir('lunch-recommendation')
                subprocess.run(['git', 'pull'])
        except Exception as e:
            print(f'GitHub 업데이트 실패: {e}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LunchRecommendation()
    ex.show()
    sys.exit(app.exec_())