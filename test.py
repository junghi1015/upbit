import pyupbit

access = "mlrAgmaGSqymflKXnfUiOWz1h6lx9fCBBz9sl3a6"          # 본인 값으로 변경
secret = "m70FyXrXmtFDrUxAnYasZaqm5KEuo0vM43YugDDT"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-OMG"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
