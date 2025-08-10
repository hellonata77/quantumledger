import argparse
from quantumledger.analyzer import QuantumLedgerAnalyzer

def main():
    parser = argparse.ArgumentParser(description="QuantumLedger — крипто-анализатор аномалий транзакций")
    parser.add_argument("address", help="Кошелёк для анализа")
    parser.add_argument("--network", choices=["btc", "eth"], default="btc", help="Сеть (btc или eth)")
    args = parser.parse_args()

    analyzer = QuantumLedgerAnalyzer(args.address, args.network)
    result = analyzer.analyze()

    if "error" in result:
        print(f"[!] {result['error']}")
    else:
        print("\n📊 Результаты анализа:")
        for key, value in result.items():
            print(f"{key}: {value}")
        if result["quantum_anomaly_score"] > 0.5:
            print("\n⚠️ Обнаружены признаки аномальной активности!")
        else:
            print("\n✅ Активность выглядит нормальной.")

if __name__ == "__main__":
    main()
