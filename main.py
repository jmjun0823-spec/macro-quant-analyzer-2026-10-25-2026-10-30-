import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_collector import fetch_all_market_data
from src.dcf_model import run_dcf_sensitivity_analysis
from src.volatility_drag import simulate_volatility_drag
from src.market_pressure import analyze_market_pressure


def main():
  print("=" * 60)
  print("[주간 증시 전망] 블로그 데이터 및 모델 검증 파이프라인 가동")
  print("=" * 60)

  # 1. 데이터 수집
  df_market = fetch_all_market_data()

  # 2. DCF 및 할인율 변수 검증
  run_dcf_sensitivity_analysis()

  # 3. 레버리지 ETF 음의 복리 마모 검증
  simulate_volatility_drag()

  # 4. 지정학적 리스크 및 수급 쏠림 분석
  analyze_market_pressure()

  print("\n[INFO] 모든 검증 시뮬레이션이 성공적으로 완료되었습니다.")


if __name__ == "__main__":
  main()
