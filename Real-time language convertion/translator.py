from transformers import pipeline
# I am using hugging face pipeline to save time
# It will download both model, one 280MB each.
translator_en = pipeline("translation_en_to_de", model= "Helsinki-NLP/opus-mt-en-de")  
translator_de = pipeline("translation_de_to_en", model= "Helsinki-NLP/opus-mt-de-en")

# Function for Eng-German conversion
def translate_en_de(text):
  output = translator_en(text, clean_up_tokenization_spaces=True)
  return output[0]['translation_text']

#test function
if __name__ == "__main__":
  text_en = "I am just a mortal"
  print(translate_en_de(text_en))
 
# Function for German to Eng
def translate_de_en(text):
  output = translator_de(text, clean_up_tokenization_spaces=True)
  return output[0]['translation_text']

#test function
if __name__ == "__main__":
  text_de = "Ich bin nur ein Sterblicher"
  print(translate_de_en(text_de))
