import matplotlib.pyplot as plt
import read_csv as read

def generate_bar_chart(labels,values):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.show()

def generate_pie_chart(labels,values): 
  fig, ax = plt.subplots()
  ax.pie(values,labels=labels)
  ax.axis('equal')
  plt.show()


  

if __name__ == '__main__':
  generate_pie_chart()

  