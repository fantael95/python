dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}
if "나이" not in dict_variable:
    dict_variable["나이"] = "24세"

print("나이 : "+dict_variable["나이"])