from src.loader import DataLoader
from src.features.jd_features import JDFeatureExtractor

jd = DataLoader.load_job_description()

features = JDFeatureExtractor.extract(jd)

print(features)