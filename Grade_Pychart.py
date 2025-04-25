import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.rcParams['font.family'] = 'Malgun Gothic'

# 엑셀 파일 읽기
file_path = 'C:/Users/LG/Desktop/박혜인/5. Python/grade.xlsx'
df = pd.read_excel(file_path)

# 데이터 출력
print(df)

# 각 학생의 6개월 평균 성적 계산
df['Average Score'] = df.iloc[:, 2:].mean(axis=1)

# 성적 평균순으로 데이터프레임 정렬
df.sort_values(by='Average Score', ascending=False, inplace=True)

# 상위 10명의 학생 선택
top_10_students = df.nlargest(10, 'Average Score')
top_10_indices = top_10_students.index

# 파이차트 그리기
plt.figure(figsize=(10, 10))

# 레이블에 학생 이름을 표시
labels = df['Student Name']

# explode 배열 생성 (상위 10명의 조각을 튀어나오게 하기 위해)
explode = [0.1 if i in top_10_indices else 0 for i in df.index]

# 파이차트 그리기
plt.pie(df['Average Score'], labels=labels, autopct='%1.1f%%', startangle=140, explode=explode)

# 그래프 설정
plt.title('학생별 6개월 평균 성적', pad=20)  # 제목과 그래프 사이의 간격 설정
plt.axis('equal')  # 파이차트를 원형으로 유지

# 그래프 보여주기
plt.show()
