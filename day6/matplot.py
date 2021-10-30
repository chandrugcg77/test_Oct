import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,24,9,6])
plt.show()

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,24,9,6])
plt.xlabel("Date")
plt.ylabel("publications")
plt.title("Date vs publications plot")
plt.show()

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,24,9,6])
plt.xlabel("Date")
plt.ylabel("publications")
plt.title("Date vs publications plot")

# import os
# os.chdir("C:\ReadMyCourse")
plt.savefig("Date Vs Publication plot.png")
plt.savefig("Date Vs Publication plot.svg")
plt.savefig("Date Vs Publication plot.tiff")

plt.show()
plt.axis([1,10,1,30])