import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

plt.rcParams['font.family'] = 'Malgun Gothic'

# 엑셀 파일 읽기
file_path = 'C:/Users/LG/Desktop/박혜인/5. Python/grade.xlsx'
df = pd.read_excel(file_path)

# 데이터 출력
print(df)

# 학생 이름 기준으로 데이터프레임 정렬
df.sort_values(by='Student Name', inplace=True)

# 컬러맵 생성
colors = cm.get_cmap('tab20', len(df))

# 그래프 그리기
plt.figure(figsize=(14,7))

# 월별 데이터를 위한 막대 너비 설정
bar_width = 0.8 / len(df.columns[2:])

# 각 월별로 막대 그래프 그리기
months = df.columns[2:]
indices = np.arange(len(df))

for i, month in enumerate(months):
    plt.bar(indices + i * bar_width, df[month], bar_width, label=month)

# x축 설정
plt.xticks(indices + bar_width * (len(months) / 2), df['Student Name'], rotation=90)

# 그래프 설정
plt.title('30명 학생 성적')
plt.xlabel('학생 이름')
plt.ylabel('성적')

# y축 눈금을 5 단위로 설정 (0에서 100 사이로 가정)
plt.yticks(range(0, 101, 5))

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)
plt.grid(True)
plt.tight_layout()

# 그래프 보여주기
plt.show()
