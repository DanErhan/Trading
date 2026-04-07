[index.html](https://github.com/user-attachments/files/26551357/index.html)
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>TradingView Charts</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      background: #0f0f0f;
      color: #e0e0e0;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      background: #161616;
      border-bottom: 1px solid #2a2a2a;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }

    header h1 {
      font-size: 15px;
      font-weight: 600;
      color: #fff;
      letter-spacing: 0.3px;
    }

    .symbol-bar {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      flex: 1;
    }

    .symbol-btn {
      background: #222;
      border: 1px solid #333;
      color: #aaa;
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 12px;
      cursor: pointer;
      transition: all 0.15s;
      font-weight: 500;
    }

    .symbol-btn:hover { background: #2a2a2a; color: #fff; border-color: #444; }
    .symbol-btn.active { background: #1a3a5c; color: #5ba4f5; border-color: #2a5a8a; }

    .interval-bar {
      display: flex;
      gap: 4px;
    }

    .interval-btn {
      background: transparent;
      border: 1px solid #2a2a2a;
      color: #888;
      padding: 4px 9px;
      border-radius: 5px;
      font-size: 11px;
      cursor: pointer;
      transition: all 0.15s;
    }

    .interval-btn:hover { color: #ccc; border-color: #444; }
    .interval-btn.active { background: #252525; color: #fff; border-color: #555; }

    #chart-container {
      flex: 1;
      width: 100%;
      min-height: calc(100vh - 60px);
    }

    #chart-container iframe,
    #chart-container .tradingview-widget-container,
    #chart-container .tradingview-widget-container__widget {
      width: 100% !important;
      height: 100% !important;
      min-height: calc(100vh - 60px);
    }
  </style>
</head>
<body>

<header>
  <h1>📈 Charts</h1>

  <div class="symbol-bar">
    <span style="font-size:11px;color:#555;align-self:center;margin-right:4px;">CRYPTO</span>
    <button class="symbol-btn active" data-symbol="BINANCE:BTCUSDT">BTC</button>
    <button class="symbol-btn" data-symbol="BINANCE:ETHUSDT">ETH</button>
    <button class="symbol-btn" data-symbol="BINANCE:SOLUSDT">SOL</button>

    <span style="font-size:11px;color:#555;align-self:center;margin-left:8px;margin-right:4px;">STOCKS</span>
    <button class="symbol-btn" data-symbol="NASDAQ:AAPL">AAPL</button>
    <button class="symbol-btn" data-symbol="NASDAQ:TSLA">TSLA</button>
    <button class="symbol-btn" data-symbol="NASDAQ:NVDA">NVDA</button>
    <button class="symbol-btn" data-symbol="NASDAQ:SPY">SPY</button>

    <span style="font-size:11px;color:#555;align-self:center;margin-left:8px;margin-right:4px;">FOREX</span>
    <button class="symbol-btn" data-symbol="FX:EURUSD">EUR/USD</button>
    <button class="symbol-btn" data-symbol="FX:GBPUSD">GBP/USD</button>
    <button class="symbol-btn" data-symbol="FX:USDJPY">USD/JPY</button>

    <span style="font-size:11px;color:#555;align-self:center;margin-left:8px;margin-right:4px;">COMMODITIES</span>
    <button class="symbol-btn" data-symbol="CAPITALCOM:GOLD">GOLD</button>
    <button class="symbol-btn" data-symbol="NYMEX:CL1!">OIL</button>
  </div>

  <div class="interval-bar">
    <button class="interval-btn" data-interval="1">1m</button>
    <button class="interval-btn" data-interval="5">5m</button>
    <button class="interval-btn" data-interval="15">15m</button>
    <button class="interval-btn" data-interval="60">1h</button>
    <button class="interval-btn" data-interval="240">4h</button>
    <button class="interval-btn active" data-interval="D">1D</button>
    <button class="interval-btn" data-interval="W">1W</button>
  </div>
</header>

<div id="chart-container"></div>

<script>
  let currentSymbol = 'BINANCE:BTCUSDT';
  let currentInterval = 'D';

  function loadChart(symbol, interval) {
    const container = document.getElementById('chart-container');
    container.innerHTML = '';

    const wrapper = document.createElement('div');
    wrapper.className = 'tradingview-widget-container';
    wrapper.style.height = '100%';
    wrapper.style.width = '100%';

    const widget = document.createElement('div');
    widget.className = 'tradingview-widget-container__widget';
    widget.style.height = '100%';
    widget.style.width = '100%';
    wrapper.appendChild(widget);

    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js';
    script.async = true;
    script.innerHTML = JSON.stringify({
      autosize: true,
      symbol: symbol,
      interval: interval,
      timezone: "Etc/UTC",
      theme: "dark",
      style: "1",
      locale: "en",
      allow_symbol_change: true,
      calendar: false,
      support_host: "https://www.tradingview.com",
      backgroundColor: "rgba(15, 15, 15, 1)",
      gridColor: "rgba(42, 42, 42, 0.4)",
      studies: ["STD;MACD", "STD;RSI"]
    });

    wrapper.appendChild(script);
    container.appendChild(wrapper);
  }

  document.querySelectorAll('.symbol-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.symbol-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentSymbol = btn.dataset.symbol;
      loadChart(currentSymbol, currentInterval);
    });
  });

  document.querySelectorAll('.interval-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.interval-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentInterval = btn.dataset.interval;
      loadChart(currentSymbol, currentInterval);
    });
  });

  loadChart(currentSymbol, currentInterval);
</script>

</body>
</html>
