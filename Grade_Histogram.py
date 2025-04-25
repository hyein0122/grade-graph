import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.rcParams['font.family'] = 'Malgun Gothic'

#엑셀 파일 읽기
file_path = file_path = 'C:/Users/LG/Desktop/Parkhyein/5. Python/grade.xlsx'
df = pd.read_excel(file_path)

#데이터 출력
print(df)

# #학생 ID를 인덱스로 설정
# df.set_index('Student Num', inplace=True)

# 학생 이름 기준으로 데이터프레임 정렬
df.sort_values(by='Student Name', inplace=True)

# 컬러맵 생성
colors = cm.get_cmap('tab20', len(df))

#그래프 그리기
plt.figure(figsize=(14,7))

#각 학생의 월별 성적을 선 그래프로 그리기 
for i, student_num in enumerate(df.index):
    student_name = df.loc[student_num, 'Student Name']  # 학생 이름 가져오기
    plt.plot(df.columns[2:], df.loc[student_num][2:], marker='o', label=student_name, color=colors(i)) #, color='k'

# 그래프 설정
plt.title('30명 학생 성적')
plt.xlabel('월')
plt.ylabel('성적')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)
plt.grid(True)
plt.tight_layout()


# y축 눈금을 5 단위로 설정 (0에서 100 사이로 가정)
plt.yticks(range(0, 101, 5))

# 그래프 보여주기
plt.show()