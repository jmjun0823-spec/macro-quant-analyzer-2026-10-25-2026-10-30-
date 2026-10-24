import numpy as np


def simulate_volatility_drag():
  print("\n[3] 실적 시즌 횡보장 & 음의 복리 마모(Volatility Drag) 정밀 검증")

  # 횡보장 시뮬레이션 (상승과 하락이 반복될 때 2배 레버리지의 자산 갉아먹기 현상 검증)
  np.random.seed(42)
  days = 60
  daily_returns = np.random.normal(loc=0.0005, scale=0.02, size=days)

  underlying_prices = 100 * np.cumprod(1 + daily_returns)
  leverage_prices = 100 * np.cumprod(
      1 + (2 * daily_returns - 0.0002)
  )  # 운용 보수 및 마모 감안

  underlying_return = (underlying_prices[-1] - 100) / 100 * 100
  leverage_ideal = 100 * (1 + 2 * (underlying_prices[-1] - 100) / 100)
  leverage_actual = leverage_prices[-1]
  drag_loss = leverage_ideal - leverage_actual

  print(f"- 기초자산 누적 변동률: {underlying_return:+.2f}%")
  print(f"- 2배 레버리지 이론적 기대치: {leverage_ideal:,.2f}원")
  print(f"- 실제 레버리지 시뮬레이션 결과: {leverage_actual:,.2f}원")
  print(
      f"- 횡보장 누적 복리 마모 손실(Volatility Drag): -{drag_loss:,.2f}원"
      " (장기 보유 리스크 입증)"
  )
