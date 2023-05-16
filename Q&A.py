import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Tải dữ liệu và thiết lập nltk
nltk.download('punkt')
nltk.download('wordnet')

# Đọc dữ liệu đầu vào
with open('C:/Users/Admin/anaconda3/datatest.txt', 'r', encoding='utf-8') as file:
    raw_data = file.read().lower()

# Chuẩn bị dữ liệu
sent_tokens = nltk.sent_tokenize(raw_data)
word_tokens = nltk.word_tokenize(raw_data)
lemmer = nltk.stem.WordNetLemmatizer()

# Hàm chuyển đổi từ vựng thành dạng chuẩn
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

# Hàm loại bỏ dấu câu
def RemovePunctuations(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Hàm tiền xử lý câu đầu vào
def Preprocess(text):
    return LemTokens(nltk.word_tokenize(RemovePunctuations(text.lower())))

# Hàm tìm câu trả lời phù hợp
def Response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=Preprocess, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response = robo_response + "Xin lỗi, tôi không hiểu ý của bạn."
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response

# Giao diện chatbot
print("Bot: Chào bạn! Hãy hỏi tôi điều gì bạn muốn.")
while True:
    user_input = input("You: ")
    user_input = user_input.lower()
    if user_input != 'bye':
        if user_input == 'thanks' or user_input == 'thank you':
            print("Bot: Rất vui được giúp bạn!")
            
        else:
            print("Bot: ", end="")
            print(Response(user_input))
            sent_tokens.remove(user_input)
    else:
        print("Bot: Chúc bạn một ngày tốt lành!")
        
