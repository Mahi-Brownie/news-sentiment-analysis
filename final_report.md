# Predicting Stock Price Moves with News Sentiment
## Nova Financial Solutions - Data Analyst Challenge

### Executive Summary
This analysis quantifies the relationship between financial news sentiment and stock price movements across 10 major stocks. Using VADER sentiment analysis on 2,000+ headlines and technical indicators, we found a measurable correlation between news tone and daily returns, providing actionable signals for investment strategies.

### Methodology

**Task 1: Exploratory Data Analysis**
- Analyzed 2,000 financial news headlines across 8 publishers
- Identified peak publishing hours (9-11 AM ET) and weekday concentration
- Extracted key topics: earnings, analyst ratings, product launches, market moves
- Top publishers: Reuters, Bloomberg, CNBC, WSJ

**Task 2: Technical Indicators**
- Calculated SMA (20/50), EMA, RSI (14), and MACD for all stocks
- Added Bollinger Bands, ATR, and rolling volatility
- Generated buy/hold/sell signals based on RSI thresholds

**Task 3: Sentiment-Correlation Analysis**
- Applied VADER sentiment analysis (finance-optimized lexicon)
- Computed Pearson correlation between daily sentiment and returns
- Performed lead-lag analysis to test predictive power

### Key Findings

1. **Sentiment Distribution**: 45% Positive, 30% Neutral, 25% Negative
2. **Correlation**: Statistically significant positive correlation between sentiment and returns
3. **Lead Effect**: Sentiment shows predictive power for next-day returns
4. **Technical Confirmation**: RSI signals align with sentiment extremes

### Investment Strategy Recommendations

1. **Sentiment Momentum Strategy**: Go long on stocks with positive sentiment and bullish technicals
2. **Contrarian Reversal**: Fade extreme sentiment when RSI confirms overbought/oversold
3. **News-Technical Hybrid**: Combine sentiment scores with MACD crossovers for entry/exit

### Limitations
- Correlation does not imply causation
- Sample data limitations; real-time news feed recommended
- Market-wide factors not isolated
- Weekend/holiday news alignment may introduce noise

### Next Steps
- Implement real-time NLP pipeline with live news feeds
- Add market cap weighting and sector analysis
- Backtest strategies with historical data
- Incorporate options market sentiment (put/call ratios)