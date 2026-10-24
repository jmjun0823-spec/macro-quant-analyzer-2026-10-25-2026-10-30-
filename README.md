# macro-quant-analyzer

거시경제(Macro) 지표 수집 및 퀀트 자산배분·음의 복리 마모(Volatility Drag) 시뮬레이션 자동화 검증 엔진

## 📁 프로젝트 구조

```text
macro-quant-analyzer/
├── src/
│   ├── __init__.py
│   ├── data_collector.py       # 매크로 및 4대 지표 수집 (yfinance 등)
│   ├── dcf_model.py            # DCF 밸류에이션 및 할인율(10년물 금리) 민감도 분석
│   ├── volatility_drag.py      # 레버리지 ETF 음의 복리 마모(Volatility Drag) 검증
│   └── market_pressure.py      # 중동 지정학적 리스크 및 수급 쏠림 분석
├── .github/
│   └── workflows/
│       └── run_analysis.yml    # 전체 파이프라인 자동화 워크플로우
├── requirements.txt
└── main.py                     # 전체 분석 실행 진입점
