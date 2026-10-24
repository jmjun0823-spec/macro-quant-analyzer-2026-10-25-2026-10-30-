import pandas as pd
import yfinance as yf


def fetch_all_market_data():
  print("\n[1] 매크로 및 4대 지표 실시간 데이터 수집 중...")
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
    df = yf.download(ticker, period="3mo", progress=False)
    if not df.empty:
      close = (
          df[("Close", ticker)]
          if isinstance(df.columns, pd.MultiIndex)
          else df["Close"]
      )
      data[name] = close

  df_all = pd.DataFrame(data)
  print(df_all.tail(3))
  return df_all
