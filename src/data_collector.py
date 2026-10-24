import pandas as pd
import yfinance as yf


def fetch_all_market_data():
  print("\n[1] 매크로 및 4대 지표 기간별 데이터 수집 중 (2026-10-18 ~ 2026-10-24)...")
  tickers = {
      "US 10Y Yield": "^TNX",
      "VIX": "^VIX",
      "Crude Oil": "CL=F",
      "S&P 500": "^GSPC",
      "NASDAQ": "^IXIC",
      "SOXX": "SOXX",
      "KOSPI": "^KS11",
      "KOSDAQ": "^KQ11",
  }

  data = {}
  for name, ticker in tickers.items():
    # start와 end 날짜를 지정하여 데이터 수집 (end 날짜는 포함되지 않으므로 25일로 지정)
    df = yf.download(
        ticker, start="2026-10-18", end="2026-10-25", progress=False
    )
    if not df.empty:
      close = (
          df[("Close", ticker)]
          if isinstance(df.columns, pd.MultiIndex)
          else df["Close"]
      )
      data[name] = close

  df_all = pd.DataFrame(data)
  print(df_all)
  return df_all
