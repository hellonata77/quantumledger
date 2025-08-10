# QuantumLedger

QuantumLedger — это утилита на Python для анализа криптовалютных кошельков (BTC и ETH) и вычисления **Quantum Anomaly Score** — индекса, показывающего, насколько транзакции адреса отличаются от нормального поведения.

## Возможности
- Поддержка Bitcoin и Ethereum (через BlockCypher API)
- Вычисление статистики транзакций: средние суммы, стандартное отклонение, интервалы
- Определение аномальной активности
- CLI-интерфейс для быстрого запуска

## Установка
```bash
git clone https://github.com/yourname/quantumledger.git
cd quantumledger
pip install -r requirements.txt
