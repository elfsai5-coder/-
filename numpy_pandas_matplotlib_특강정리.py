"""
========================================================================================
 🐟 [금붕어도 이해하는 데이터 분석 3대장] Numpy, Pandas, Matplotlib 완벽 실습 가이드
========================================================================================
 - Numpy     : 파이썬 기본 리스트보다 100배 빠른 '초고속 숫자 계산기'
 - Pandas    : 2D 리스트에 이름표(행/열) 붙여서 엑셀처럼 쓰는 '초능력 장부'
 - Matplotlib: 숫자로 된 데이터를 막대/꺾은선 그림으로 그려주는 '도화지와 크레파스'
========================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 70)
print(" 1. Numpy (넘파이) 실습 : 초고속 숫자 계산기")
print("=" * 70)

# 1.1 명시적 타입 지정과 다차원 슬라이싱 [행 범위, 열 범위]
# int64 등으로 타입을 딱 정해주면 컴퓨터 메모리를 아낄 수 있어요!
matrix = np.array([[10, 20, 30], 
                   [40, 50, 60], 
                   [70, 80, 90]], dtype=np.int64)

print("\n[원래 3x3 행렬]:\n", matrix)
print("-> 0행 2열 값 콕 집기 (matrix[0, 2]):", matrix[0, 2])
print("-> 0~1행, 1~2열 네모나게 도려내기 (matrix[0:2, 1:3]):\n", matrix[0:2, 1:3])
print("-> 모든 행(:)의 0번 열만 몽땅 가져오기 (matrix[:, 0]):", matrix[:, 0])

# 1.2 차원 변경 (reshape, flatten)과 축 (Axis)
# 1차원 12개 숫자를 3줄짜리 바둑판으로 변신! (-1을 쓰면 칸 수는 알아서 자동 계산)
arr = np.arange(1, 13) # 1부터 12까지
mat_3x4 = arr.reshape(3, -1) # 3행 4열로 변환
flat_arr = mat_3x4.flatten()  # 다시 1줄짜리로 쫙 펴기(평탄화)

print("\n[reshape(3, -1) 형상 변환]:\n", mat_3x4)
print("[flatten() 1차원 평탄화]:", flat_arr)

# 축(Axis) 연산 방향 (★가장 중요★)
# axis=0 : 위에서 아래로 쿵 찍어서 계산 (세로 방향 / 열별 합) -> 각 과목별 평균
# axis=1 : 왼쪽에서 오른쪽으로 쓱 밀어서 계산 (가로 방향 / 행별 합) -> 각 학생별 총점
mat_2x3 = np.arange(1, 7).reshape(2, 3)
print("\n[2x3 행렬]:\n", mat_2x3)
print("-> axis=0 (세로 방향 합계):", mat_2x3.sum(axis=0)) # [1+4, 2+5, 3+6]
print("-> axis=1 (가로 방향 합계):", mat_2x3.sum(axis=1)) # [1+2+3, 4+5+6]

# 1.3 브로드캐스팅 (크기가 다른 배열끼리 알아서 크기 맞춰서 일괄 연산)
# 파이썬 기본 리스트는 [1, 2, 3] + 5 하면 에러 나지만, 넘파이는 전부 5씩 알아서 더해줌!
print("\n[스칼라 덧셈 (+5 브로드캐스팅)]:\n", mat_2x3 + 5)

# 1.4 행렬 전치 (.T)와 행렬곱 (@)
# 전치(.T): 가로와 세로를 휙 뒤집음 (2x3 -> 3x2)
# 행렬곱(@): AI/머신러닝에서 가중치 곱할 때 쓰는 기호 (2x3 @ 3x2 -> 2x2)
print("\n[전치 행렬 (.T)]:\n", mat_2x3.T)
print("[행렬곱 (@ 결과)]:\n", mat_2x3 @ mat_2x3.T)


print("\n" + "=" * 70)
print(" 2. Pandas (판다스) 기초 : 이름표 달린 2D 초능력 엑셀")
print("=" * 70)

# 2.1 Series (1차원 한 줄) vs DataFrame (2차원 전체 표)
# Series는 엑셀에서 세로 1줄 떼온 것, DataFrame은 엑셀 시트 전체!
data = {
    '이름': ['김철수', '이영희', '박지민'],
    '부서': ['개발', '기획', '개발'],
    '급여': [4500, 5200, 4800]
}
df = pd.DataFrame(data)
print("\n[기본 DataFrame]:\n", df)

# 2.2 데이터 상태 진단 (건강검진)
print(f"\n[크기(shape)]: {df.shape} (3행 3열)")
print("[컬럼 목록]:", df.columns.tolist())
print("[describe() 기초 통계 요약]:\n", df.describe())

# 2.3 열 추가 및 인덱스 제어 (set_index, reset_index)
df['보너스'] = df['급여'] * 0.1 # 새 열 추가
df_indexed = df.set_index('이름') # '이름' 열을 맨 왼쪽 고유 번호표(Index)로 승격!
print("\n['이름'을 인덱스로 지정한 후]:\n", df_indexed)
df_restored = df_indexed.reset_index() # 다시 일반 컬럼으로 원상 복구

# 2.4 판다스 브로드캐스팅 (과목별 평균 편차 구하기)
score_df = pd.DataFrame({
    '중간고사': [80, 95, 70],
    '기말고사': [85, 90, 75],
}, index=['김철수', '이영희', '박지민'])

col_mean = score_df.mean(axis=0) # 각 시험(열)별 평균 계산
deviation_df = score_df.sub(col_mean, axis=1) # 학생 점수에서 시험별 평균을 한 방에 감산!
print("\n[학생 점수 표]:\n", score_df)
print("[시험별 평균]:\n", col_mean)
print("[과목별 평균과의 편차 (내점수 - 평균)]:\n", deviation_df.round(2))


print("\n" + "=" * 70)
print(" 3. Pandas 정밀 조회 및 결측치(빵꾸) 정제 7대 비법")
print("=" * 70)

df_sample = pd.DataFrame({
    '나이': [25, 30, 35, 40],
    '점수': [80, 95, 70, 85],
    '등급': ['B', 'A', 'C', 'B'],
}, index=['user1', 'user2', 'user3', 'user4'])

# 3.1 loc (이름/라벨로 찾기) vs iloc (숫자 순서로 찾기)
print("\n[loc: 'user2' 행의 '나이'와 '등급']:\n", df_sample.loc['user2', ['나이', '등급']])
print("[iloc: 0~1번째 행, 0~1번째 열 (컴퓨터 순서)]:\n", df_sample.iloc[0:2, 0:2])

# 3.2 조건 검색 (불리언 인덱싱 vs query)
target_score = 80
# 방법 1: 불리언 인덱싱
filtered_bool = df_sample[(df_sample['나이'] >= 30) & (df_sample['점수'] >= target_score)]
# 방법 2: query() 메서드 (@변수명 으로 외부 변수 사용 가능!)
filtered_query = df_sample.query('나이 >= 30 and 점수 >= @target_score')
print("\n[query() 필터링 결과 (나이 30 이상 & 점수 80 이상)]:\n", filtered_query)

# 3.3 결측치(Missing Data / NaN) 7대 처리 기법
print("\n--- [결측치 7대 정제 기법] ---")
# 1) 탐지 (isna().sum()): 빈칸 개수 세기
raw_df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [pd.NA, 5, 6], 'C': [7, 8, 9]})
print("1. 결측치 개수 집계:\n", raw_df.isna().sum())

# 2) 삭제 (dropna()): 빵꾸 난 줄 그냥 버리기
df_drop = pd.DataFrame({'A': [1, None, 3], 'B': [4, None, None]})
print("\n2. 결측 행 삭제 (dropna):\n", df_drop.dropna())

# 3) 대푯값 대치 (fillna(median)): 이상치에 강한 '중앙값'으로 채우기
df_age = pd.DataFrame({'나이': [20, 25, None, 30, 95]}) # 95살 이상치 포함
median_val = df_age['나이'].median() # 중앙값 계산 (27.5)
print("\n3. 중앙값으로 빈칸 채우기 (fillna):\n", df_age.fillna(median_val))

# 4) 시계열 직전/직후 값 대치 (ffill / bfill): 주가, 기온처럼 연속된 데이터
ts_df = pd.DataFrame({'온도': [18.2, None, None, 21.0]})
print("\n4. 직전 값으로 채우기 (ffill):\n", ts_df.ffill())

# 5) 선형 보간법 (interpolate): 앞뒤 숫자의 흐름을 보고 비례해서 채우기 (10과 40 사이 -> 20, 30)
speed_df = pd.DataFrame({'속도': [10.0, None, None, 40.0]})
print("\n5. 선형 보간 (interpolate):\n", speed_df.interpolate(method='linear'))

# 6) 이상 기호 치환 & 강제 수치형 변환 (errors='coerce')
# '?'나 '-999' 같은 이상한 글자 때문에 object 타입으로 꼬였을 때 숫자로 강제 변환!
survey_df = pd.DataFrame({'점수': [85, -999, '?', 95]})
clean_series = survey_df['점수'].replace([-999, '?'], pd.NA)
survey_df['점수'] = pd.to_numeric(clean_series, errors='coerce') # 숫자로 못 바꾸는 글자는 NaN으로 강제 변경
print("\n6. 이상 기호 정제 후 숫자 변환 (평균 계산 가능):\n", survey_df)
print("-> 점수 평균:", survey_df['점수'].mean())

# 7) 결측 여부 지표 변수 생성 (소득 미응답 자체가 중요한 정보일 때)
user_df = pd.DataFrame({'소득': [300, None, 450, None]})
user_df['소득_미응답여부'] = user_df['소득'].isna() # True/False 열 생성
print("\n7. 결측 지표 변수 생성:\n", user_df)

# 3.4 그룹화 집계 (groupby)와 머신러닝 연계 (.to_numpy())
sales_df = pd.DataFrame({'지점': ['서울', '서울', '부산', '부산'], '매출': [100, 150, 80, 120]})
summary = sales_df.groupby('지점').mean(numeric_only=True)
matrix_features = sales_df[['매출']].to_numpy(dtype=np.float64) # 판다스 -> 넘파이 변환
print("\n[지점별 평균 매출 (groupby)]:\n", summary)
print("[머신러닝용 넘파이 행렬 변환 (.to_numpy())]:\n", matrix_features)


print("\n" + "=" * 70)
print(" 4. Matplotlib (맷플롯립) : 데이터를 그림으로 그리는 도화지")
print("=" * 70)
print("-> 2x2 분할 대시보드 그래프 창을 띄웁니다. (창을 닫으면 프로그램이 종료됩니다)")

# fig = 전체 도화지, axes = 4개의 개별 차트 영역 (2행 2열)
fig, axes = plt.subplots(2, 2, figsize=(10, 7))

# [0, 0] 파란색 꺾은선 그래프 (Line Plot) - 추세 확인용
x_line = [1, 2, 3]
y_line = [10, 20, 15]
axes[0, 0].plot(x_line, y_line, color='blue', linestyle='-', marker='o')
axes[0, 0].set_title('1. Line Plot (Trend)')
axes[0, 0].grid(True)

# [0, 1] 빨간색 사인 곡선 (Curve)
x_curve = np.linspace(0, 3, 50)
y_curve = np.sin(x_curve)
axes[0, 1].plot(x_curve, y_curve, color='red', linestyle='-')
axes[0, 1].set_title('2. Curve (Function)')
axes[0, 1].grid(True)

# [1, 0] 초록색 산점도 (Scatter) - 두 변수 간의 상관관계 확인용
height = [160, 165, 170, 175, 180, 185]
weight = [55, 62, 65, 74, 78, 85]
axes[1, 0].scatter(height, weight, color='green', s=60, alpha=0.8)
axes[1, 0].set_title('3. Scatter (Height vs Weight)')
axes[1, 0].set_xlabel('Height (cm)')
axes[1, 0].set_ylabel('Weight (kg)')
axes[1, 0].grid(True)

# [1, 1] 주황색 막대 그래프 (Bar) & 박스플롯 이상치 검출 예시
categories = ['Group A', 'Group B', 'Group C']
counts = [24, 38, 19]
axes[1, 1].bar(categories, counts, color='orange', alpha=0.85)
axes[1, 1].set_title('4. Bar Chart (Category Comparison)')

plt.tight_layout() # 그래프끼리 글자 안 겹치게 자동 정리
plt.show() # 화면에 그래프 띄우기

print("\n🎉 모든 실습 예제 실행이 완료되었습니다!")
