- M1：

  ```python
  # 在此定义下，
  plt.xlim(x_range)
  plt.ylim(y_range)
  ax.yaxis.set_major_locator(MultipleLocator(y_step))
  ax.xaxis.set_major_locator(MultipleLocator(x_step))
  plt.xticks()  # 重定义x轴刻度的显示label与索引
  # 处理到的一个需求：锚点(x_point, y_point)在一个rect左上顶点，在rect中间显示一个text
  plt.subplot(ax0)  #选定一个ax0
  ax = gca()	# 提取到当前的ax
  
  from matplotlib.patches import Rectangle
  ax.add_patch(Rectangle((x_point, y_point - height_rect), width_rect, height_rect, fc='red', ec='g', lw=1, alpha=0.2))
  ax.text(x_point + width_rect/2, y_point - height_rect/2, label, fontsize=12, color='black', horizontalalignment='center', verticalalignment='center')
  
  # Rectangle从xy（x_point, y_point - height_rect）从左下点(锚点可以在边框任意点)向右上画出的区域
  # text会参照一个点,使用ha，va进行left,right,center设置
  # text也有外框，但是是基于text定位过后的，也可单独设置pad（貌似是像素），但是与boxstyle中的pad（貌似是文字的比例）不同。bbox = dict(fc='green', alpha=0.3, ec='none', boxstyle="square, pad=0.3")
  
  # 用此达到固定锚点，但也因此产生了一个问题，设定文字尺寸，或者说是像素，如何精确控制？
  
  ```

  
