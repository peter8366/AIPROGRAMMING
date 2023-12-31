# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o9vWemtSlvjX9iqORqGEhrh2mN8QyygH
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# 수정된 데이터 설정
x_values = np.array([2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032])
y_ticks = np.array([0, 23, 46, 69, 92, 115, 138, 161, 184, 207, 230])
y_values = np.array([16.86, 21.87, 28.37, 36.8, 47.74, 61.93, 80.34, 104.21, 135.18, 175.36, 227.48])
color_map = LinearSegmentedColormap.from_list('custom_cmap', [(0.8, 0.8, 0.8), (0, 0, 0.5)], N=250)

# 그래프 그리기
plt.figure(figsize=(10, 6))
bars = plt.bar(x_values, y_values, color=color_map(y_ticks), width=0.8)

# 막대 위에 y값 표시
for x, y in zip(x_values, y_values):
    plt.text(x, y, f'${y:.2f}', ha='center', va='bottom', color='black', fontsize=10)

# 그래프 제목 설정
plt.title('ARTIFICIAL INTELLIGENCE [AI] CHIP MARKET SIZE, 2023 TO 2032 [USD BILLION]', color='navy', fontsize=16)

# x와 y 축 레이블 설정
plt.xlabel('Year', color='navy', fontsize=12)
plt.ylabel('Market Size [USD Billion]', color='navy', fontsize=12)

# 오른쪽 아래의 Source 정보 추가 (왼쪽 아래로 이동)
plt.text(2030, -24, 'Source: www.precedencresearch.com', fontsize=8, color='navy')

# x 축 눈금 라벨 설정 (똑바로 나오게 함)
plt.xticks(x_values, x_values, rotation=0)

# y 축 범위 및 눈금 설정
plt.yticks(y_ticks)

# 그래프 표시
plt.show()