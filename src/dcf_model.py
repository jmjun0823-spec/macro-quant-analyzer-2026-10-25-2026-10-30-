def run_dcf_sensitivity_analysis():
  print(
      "\n[2] 통화정책 Pivot 및 할인율(Discount Rate) 변화에 따른 DCF 민감도"
      " 분석"
  )

  # 가정: 향후 5년간 추정 FCF (예: 100, 110, 121, 133, 146)
  fcf_projections = [100, 110, 121, 133, 146]

  # 할인율(r) 시나리오별 현재가치(PV) 계산 (현재 4.30% vs 인하 시나리오 등)
  discount_rates = [0.035, 0.040, 0.043, 0.050, 0.060]

  results = {}
  for r in discount_rates:
    pv = sum(
        fcf / ((1 + r) ** (i + 1)) for i, fcf in enumerate(fcf_projections)
    )
    results[f"{r*100:.2f}%"] = round(pv, 2)

  print(f"- 할인율 변동별 내재가치(PV) 시뮬레이션 결과:")
  for rate, pv_val in results.items():
    print(f"  * 할인율 {rate}: 이론적 내재가치 PV = {pv_val}억 원")
