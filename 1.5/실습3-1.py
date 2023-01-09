dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

import datetime
this_year=datetime.date.today()

print(f"""나이" : {this_year.year - int(dict_variable["생년"])+1} "세""")
