from account import Account

def account_tester():
    tester = Account("Tester", 500000)
    
    tester.display_info()
    for i in range(10):
        tester.deposit(50000)
    tester.deposit(-1000)
    tester.withdraw(99999999)
    tester.withdraw(15000)
    tester.deposit_history()
    print("-" * 50)
    tester.withdraw_history()
    return tester

if __name__ == "__main__":
    first_account = Account("James", 10000000)
    second_account = Account("Amy", 1000000)
    third_account = Account("Tom", 100000)

    # TEST CASE 1
    print("TEST CASE 1\nAccount 클래스로부터 생성된 계좌의 개수 출력 및 잔고 100만원 이상 고객 정보만 출력")
    print("-" * 50)
    third_account.get_account_num()
    for account in [first_account, second_account, third_account]:
        if account.balance >= 1000000:
            account.display_info()
    print("-" * 50)

    # TEST CASE 2
    print("TEST CASE 2\n입금 메서드, 출금 메서드, 이자 지급 기능 / 입금과 출금 내역 출력")
    print("-" * 50)
    test_account = account_tester()