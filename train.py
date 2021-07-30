import nltk, os, mastermind, shutil

nltk.download('punkt')
nltk.download('wordnet')

train_path = os.path.join("data", "models", "general_model")
dataset = os.path.join("data", "general_dataset.json")
if(os.path.exists(train_path)):
  shutil.rmtree(train_path)
mastermind.generate_model(dataset, train_path, "Hi")