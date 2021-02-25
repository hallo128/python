#天天向上的力量
'''
dayfactors = [0.005, 0.01]
for dayfactor in dayfactors:
	dayup = pow(1 + dayfactor, 365)
	daydown = pow(1 - dayfactor, 365)
	print("每天改变:{:.2f}%, 向上:{:.2f}, 向下:{:.2f}".format(dayfactor*100, dayup, daydown))
'''

#一年，工作日进行1%，休息日退步0.5%
dayup = 1
factor = [0.01, 0.005]
for n in range(365):
	if n % 7 in [6,0]:
		dayup *= (1 - factor[1])
	else:
		dayup *= (1 + factor[0])
print("最终改变改变:{:.2f}%".format(dayup))


#def dayUp(up):
	



