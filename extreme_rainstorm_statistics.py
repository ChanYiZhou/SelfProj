
# -*- coding: utf-8 -*-
# -*- version: python2.7

# =========== purpose ============= #
# 1. 统计极端暴雨日数逐年时间序列
# 2. 计算极端暴雨日数的年际和年代际变化
# 3. 根据天气分析对极端暴雨日数分类
# 4. 建立预报模式、确定指标
# 5. 诊断指标与预报模式之间的相关性
# 6. 选取合适的指标使用
# ================================= #


# ==== 导入模块
import os
import glob
import numpy as np
import pandas as pd


# ==== 定义全局变量
dataPath = os.path.join(r'E:\CodesWorks', 'github', 'test',
	'FengWX', 'Data', 'HeNan_Rainfall') # 输入数据路径
file_prefix = range(1960,2011,10)  # 文件名前缀
NeedId = [53995] # 指定站点
ColNames = ['std','datestr','Rain']


def main():
	# 0. 抽取指定站点的数据
	Data = []
	for ipre in file_prefix:
		flsEFlag = False
		fls = glob.glob(os.path.join(dataPath,str(ipre)+'*'))
		print fls
		if len(fls): flsEFlag = True
		if flsEFlag:
			for ifl in fls:
				flAdata = pd.read_csv(ifl,names=ColNames,delim_whitespace=True,
					index_col=0,skiprows=1, engine='python')
				# print flAdata

				for _ in NeedId:
					if _ in flAdata.index:
						istdData = flAdata[flAdata.index == _]
						Data.append(istdData)
						# print istdData
					

	NeedData = pd.concat(Data)
	# NeedData.to_csv(os.path.join(dataPath,'NeedRain.csv'))

	# 1. 统计逐年暴雨日数(50~100mm)
	# 设置缺失值，逐日重采样，暴雨区间设置为1，其余为0，然后逐年求和，并输出
	NeedData.reindex = ['datestr','std','Rain']
	print NeedData.head(5)



		


if __name__ == '__main__':
	main()