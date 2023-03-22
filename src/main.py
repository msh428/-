import os
import sys
import random
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox

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
        jjigae = ['청국장찌개', '순두부찌개', '고추장찌개', '부대찌개', '김치찌개', '된장찌개', '비지찌개', '전찌개', '동태찌개']
        special = ['갈비찜', '닭볶음탕', '스테이크', '아귀찜', '삼계탕', '수육', '월남쌈', '불고기', '찜닭']
        rice = ['제육덮밥', '비빔밥', '오므라이스', '카레덮밥', '김치볶음밥', '오징어덮밥', '짜장밥', '야채볶음밥', '간장밥']
        snack = ['토스트', '또띠아피자', '떡꼬치', '쿠키/과자', '떡볶이', '호떡', '샌드위치', '시리얼', '팝시클']
        guk = ['육개장', '떡국', '미역국', '콩나물국', '북엇국', '소고기무국', '시래깃국', '된장국', '감잣국']
        noodle = ['라면', '토마토 스파게티', '크림 스파게티', '잔치국수', '비빔국수', '칼국수', '우동', '볶음 우동', '콩국수']
        menu_comprehensive = jjigae + special + rice + snack + guk + noodle

        customer = ['깐풍만두', '닭가슴살 냉채', '잡채', '찜닭', '갈비찜', '월날쌈', '칠리새우', '투움바 파스타', '라자냐']
        after_drink = ['대파라면', '콩나물 해장국', '홍합탕', '굴국밥', '김치 콩나물죽', '토마토 주스', '북엇국', '오징어 무국', '순두부 찌개']
        lunch_box = ['각종김밥', '유부초밥', '밥버거', '바게트', '버거', '볶음밥', '캘리포니아롤', '스팸 무스비', '각종 샌드위치', '오니기리']
        nutrition = ['전복죽', '추어탕', '장어구이', '낙지 연포탕', '더덕구이 삼계탕', '훈제오리 부추무침', '닭죽', '갈비탕']
        diet = ['토마토 달걀볶음', '바나나쉐이크', '두부스테이크', '곤약국수', '해독주스', '단호박스프', '닭가슴살샐러드', '리코타치즈', '양배추스프']
        speedy = ['오믈렛', '연어덮밥', '치킨마요덮밥', '김치볶음밥', '계란찜', '떡국', '만둣국', '오차즈케', '누룽지죽']
        brunch = ['팬케이크', '프리타타', '몬테크리스토', '샐러드파스타', '크로크무슈/마담', '불고기부리또', '에그베네딕트', '조개스프', '프렌치토스트']
        menu_by_condition = customer + after_drink + lunch_box + nutrition + diet + speedy + brunch


        potato_onion = ['감자채볶음', '감자고추장찌개', '감자조림', '야채죽', '감잣국', '포테이토피자', '감자스프', '으깬감자샐러드', '감자/양파튀김']
        tuna = ['참치비빔밥', '참치김치볶음밥', '참치김밥 참치쌈짱', '야채참치죽', '참치김치전', '참치마요덮밥', '밥버거', '고추장참치찌개']
        pork = ['수육', '갈비찜 동파육', '김치찜 제육볶음 두루치기', '탕수육', '목살스테이크', '불고기']
        lamen = ['토마토냉라면', '대파라면', '김치버터라면', '짜파구리', '냉채라면', '골뱅이비빔면', '라볶이', '백종원볶음라면', '크림치즈라면']
        chick = ['닭죽', '닭볶음탕', '찜닭', '치킨까스', '닭강정', '삼계탕', '닭갈비', '치킨마요덮밥', '깐풍기']
        cold_rice = ['누룽지', '볶음밥', '주먹밥', '김치밥 말아먹기', '밥전', '각종죽', '리소토', '크로켓', '주먹밥']
        vegetable = ['볶음밥', '프리타타', '비빔밥', '채소전', '야채볶음', '잡채', '소시지야채볶음', '그라탕', '볶음우동']
        egg = ['계란찜', '계란말이', '오믈렛', '감동란', '계란빵', '계란장조림', '스카치에그', '계란푸딩', '스티프드에그']
        menu_by_ingredient = potato_onion + tuna + pork + lamen + chick + cold_rice + vegetable + egg

        japan = ['규동', '우동', '미소시루', '찜닭', '감츠동', '오니기리', '하이 라이스', '라멘', '오코노미야끼']
        china = ['깐풍기', '볶음면', '동파육', '짜장면', '짬뽕', '마파두부', '탕수육', '토마토 달걀볶음', '고추잡채']
        korea = ['해물파전', '김치', '쌈밥', '된장찌개', '비빔밥', '칼국수', '불고기', '떡볶이', '제육볶음']
        italy = ['라자냐', '그라탕', '나폴리 피자', '각종 스파게티', '노끼', '페투치니 알프레도', '리소토', '프리타타', '파니니']
        east_south_asia = ['팟타이', '카오팟', '나시고랭', '파인애플 볶음밥', '쌀국수', '반미(바게트샌드위치)', '연유라떼', '짜조', '분짜']
        france = ['부야베스', '라타투이', '뵈프 부르기뇽', '끼슈', '마카롱', '코코뱅', '프렌치 토스트', '크로크 무슈/마담', '뱅쇼']
        america = ['각종 햄버거', '각종 핫도그', '바비큐', '후라이드 치킨', '클램 차우더', '잠발라야', '미트로프', '맥앤치즈', '에그 베네딕트']
        middle_east_asia = ['케밥', '삭슈카(에그인쉘)', '허머스(후무스)', '팔라펠', '페투쉬', '필라프', '무사카', '피타', '쿠스쿠스(중동식파스타)']
        menu_by_country = japan + china + korea + italy + east_south_asia + france + america + middle_east_asia


        menu_by_category = []


        menu = menu_comprehensive + menu_by_condition + menu_by_ingredient + menu_by_country + menu_by_category

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