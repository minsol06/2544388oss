import matplotlib.pyplot as plt

# DORA 4대 지표 데이터 설정 (원하는 값으로 수정 가능)
metrics = {
    'Deployment Frequency': 5,
    'Lead Time (min)': 12.5,
    'MTTR (min)': 15.0,
    'Change Failure Rate (%)': 0
}

# 그래프 색상 지정 (보내주신 사진과 동일한 색상)
colors = ['#72B762', '#5D9CEC', '#EAA145', '#E9573F']

# 2x2 서브플롯 생성
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
fig.suptitle('DORA Metrics Dashboard', fontsize=16, fontweight='bold')

# 각 지표별 막대 그래프 그리기
for ax, (title, value), color in zip(axes.flatten(), metrics.items(), colors):
    bars = ax.bar([title], [value], color=color)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # Y축 범위 설정 및 값 표시
    if value > 0:
        ax.set_ylim(0, value * 1.5)
        # 막대 위에 수치 텍스트 표시
        ax.text(0, value / 2, f'{value}', ha='center', va='center', 
                color='white', fontweight='bold', fontsize=12)
    else:
        ax.set_ylim(0, 10)

plt.tight_layout()

# 이미지 파일로 저장
plt.savefig('dora_dashboard.png', dpi=300)
print("✅ dora_dashboard.png 파일이 성공적으로 생성되었습니다!")