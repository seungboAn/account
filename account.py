import random
from datetime import datetime

"""
Q1. Account 클래스 : 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자(hint: 매직매서드..!!)를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다. (은행이름: SC은행, 계좌번호: 111-11-111111)
Q2. account_count는 클래스로 부터 생성된 계좌의 갯수를 말한다.
Q3. get_account_num()함수는 account_count를 출력한다.
Q4. deposit 함수는 입금. 최소 1원부터 가능
Q5. withdraw 함수는 출금. 출금은 계좌의 잔고 이상으로 출금할 수 없다.
Q6. display_info 인스턴수 변수 출력. 잔고는 세자리마다 쉼표를 붙여야한다.
Q7. 이자 지급하기 : 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.
Q8. 여러 객체 생성 : Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.
Q9. 객체 순회 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.
Q10. 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 
(입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.)


은행 계좌 만들기: 3점
Account 클래스로부터 생성된 계좌의 개수 출력, 잔고 100만원 이상 고객 정보만 출력 - 1점
입금 메서드, 출금 메서드, 이자 지급 기능 완성 - 1점
입금과 출금 내역 출력에 성공 - 1점
"""

class Account():
    account_count = 0

    def __init__(self, depositor, balance):
        self.bank_name = "SC은행"
        self.depositor = depositor
        self.balance = balance
        self.account_number = self.create_account_number()
        self.deposit_count = 0
        self.history = {"deposit": [], "withdraw": []}
        self.history_count = 0
        Account.account_count += 1

    def create_account_number(self) -> str:
        res = []
        for i in range(13):
            if i == 3 or i == 6:
                res.append('-')
            else:
                res.append(str(random.randint(0, 9)))
        return "".join(res)

    def display_info(self):
        print(f'은행이름: {self.bank_name}, 예금주: {self.depositor}, 계좌번호: {self.account_number}, 잔고: {self.balance:,}원')

    def get_account_num(self):
        print(f'생성된 계좌의 총 개수: {self.account_count}개')

    def deposit(self, deposit_amount):
        if deposit_amount >= 1:
            self.balance += deposit_amount
            self.deposit_count += 1
            print(f'{deposit_amount}원이 입금되었습니다.')
            self.history_count += 1
            now = datetime.now()
            self.history["deposit"].append(f'{now.month}/{now.day} {self.history_count}회: 입금 금액: {deposit_amount}원 잔액: {self.balance}원')
            if self.deposit_count == 5:
                self.apply_interest()
        else:
            print("입금은 최소 1원 이상만 가능합니다.")

    def withdraw(self, withdraw_amount):
        tmp = self.balance - withdraw_amount
        if tmp >= 0:
            self.balance -= withdraw_amount
            print(f'출금 후 잔액: {self.balance}')
            self.history_count += 1
            now = datetime.now()
            self.history["withdraw"].append(f'{now.month}/{now.day} {self.history_count}회: 출금 금액: {withdraw_amount}원 잔액: {self.balance}원')
        else:
            print("출금은 계좌 잔고 이상으로 출금할 수 없습니다.")

    def apply_interest(self):
        interest = int(self.balance * 0.01)
        self.balance += interest
        self.history_count += 1
        now = datetime.now()
        self.history["deposit"].append(f'{now.month}/{now.day} {self.history_count}회: 이자지급 금액: {interest}원 잔액: {self.balance}원')
        print(f'{interest}원의 이자가 입금되었습니다.')
        self.deposit_count = 0

    def deposit_history(self):
        for history in self.history["deposit"]:
            print(history)
    def withdraw_history(self):
        for history in self.history["withdraw"]:
            print(history)