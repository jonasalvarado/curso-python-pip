import matplotlib.pyplot as plt
import read_csv as read




def generate_bar_chart(name,labels,values):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig(f'img/{name}_bar.png')
  plt.close()

def generate_pie_chart(labels,values): 
  fig, ax = plt.subplots()
  ax.pie(values,labels=labels)
  ax.axis('equal')
  plt.savefig('img/world_pie.png')
  plt.close()


  

if __name__ == '__main__':
  generate_pie_chart(100,100)

  