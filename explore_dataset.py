from src.loader import DataLoader
import json

df = DataLoader.load_candidates()

candidate = df.iloc[0]

for column in df.columns:
    print("\n" + "=" * 80)
    print(column.upper())
    print("=" * 80)

    value = candidate[column]

    if isinstance(value, (dict, list)):
        print(json.dumps(value, indent=2))
    else:
        print(value)