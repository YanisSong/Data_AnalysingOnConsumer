import re
import matplotlib.pyplot as plt

# x = [0, 1]
# y = [0, 1]
# plt.figure()
# plt.plot(x, y)
# plt.show()


f = "123safsfasfasf"
price = re.findall(r"\d{2,3}", f)
print(int(price[0]))