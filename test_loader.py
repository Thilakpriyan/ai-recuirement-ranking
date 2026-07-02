from src.loader import DataLoader

df = DataLoader.load_candidates()

print(df.head())

print()

print(df.columns)

print()

print(len(df))

print()

jd = DataLoader.load_job_description()

print(jd[:1000])