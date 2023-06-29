import numpy

np = numpy

ASSIGNMENTS = ('__name__', '__doc__', '__package__', '__loader__', '__spec__',
               '__annotations__', '__builtins__', '__file__', '__cached__',
               'np', 'ASSIGNMENTS', 'init_namespace')


def init_namespace(space_name, ignore_name=ASSIGNMENTS):
    keys = list(space_name.keys())
    for key in keys:
        if key not in ignore_name:
            del space_name[key]


"""
<h3>dtype</h3>
<h3>数据类型</h3>
    b	布尔型
    i	(有符号) 整型
    u	无符号整型 integer
    f	浮点型
    c	复数浮点型
    m	timedelta（时间间隔）
    M	datetime（日期时间）
    O	(Python) 对象
    S, a	(byte-)字符串, 后面加数字指定位数
    U	Unicode
    V	原始数据 (void)

<h3>数组属性</h3>
    ndarray.ndim，秩，即轴的数量或维度的数量
    ndarray.shape，数组的维度
    ndarray.size，数组元素的总个数
    ndarray.dtype，ndarray 对象的元素类型
    ndarray.itemsize，ndarray 对象中每个元素的字节大小
    ndarray.flags，ndarray 对象的内存信息
    ndarray.real，ndarray元素的实部
    ndarray.imag，ndarray 元素的虚部
    ndarray.data，包含实际数组元素的缓冲区，但一般通过数组的索引获取元素
    
<h3>创建数组</h3>
<h3>narray</h3>
    numpy.array， 创建一个ndarray
    numpy.dtype，创建一个数据类型
    numpy.array().astype，转换ndarray的数据类型
    numpy.empty，创建一个指定形状(shape)、数据类型(dtype)且未初始化的数组
    numpy.empty_like，创建形状和类型与原型相同的未初始化（任意）数据数组
    numpy.zeros， 创建指定大小的数组，数组元素以 0 来填充
    numpy.zeros_like，创建具有相同形状和类型的零的阵列
    numpy.ones，创建指定形状的数组，数组元素以 1 来填充
    numpy.ones_like，创建形状与类型与给定数组相同的数组
    numpy.arange，创建均匀间隔的值的数组
    numpy.linspace，创建一个一维等差数列的数组
    numpy.asarray，将Python 的基础数据类型（如列表、元组等）转换成ndarray
    numpy.frombuffer，以流的形式读入转化成 ndarray 对象，用于实现动态数组
    numpy.fromiter，从可迭代对象中建立一维ndarray对象

    numpy.eye，生成单位矩阵
    numpy.diag，生成对角矩阵
    
<h3>random</h3>
    np.random.random，生成0到1之间的随机数
    np.random.uniform，生成均勻分布的随机数
    np.random.randn，生成标准正态的随机数
    np.random.randint	生成随机的整数
    np.random.normal	生成正态分布
    np.random.shuffle	随机打乱顺序
    np.random.seed	设置随机数种子
    np.random.random_sample	生成随机的浮点数

<h3>数组索引</h3>
<h3>array index</h3>
    arr[0]，访问数组第一个元素
    arr[0, 1]，访问第一维中的第二个元素
    arr[0, 1, 2]，访问第一个维度，第二个维度，第三个维度中第一，第二，第三的元素
    arr[-1]，访问数组最后一个元素
    
<h3>数组切片</h3>
<h3>array slice</h3>
    arr[start：end：step]，切片，start是小于end的正整数， 不管是多少维的切片，都是最后一个start：end：step中的end不包括
    arr[-start：-end:step]，负向切片，一般需要start大于end来保证arr[-start]在arr[-end]的左边，否则切片出来为空数组
    arr[start：end：step, start：end：step]，对二维数组的切片
    
    布尔索引是利用布尔数组进行索引
    arr > 5，获取大于5的布尔索引，（目测NaN会被忽略掉），返回的布尔索引是可以多维的
    np.isnan(arr)，获取是NaN的布尔索引，返回的布尔索引是可以多维的
    np.iscomplex(a)，获取是NaN的布尔索引，返回的布尔索引是可以多维的
    ~np.isnan(arr)，获取不是NaN的布尔索引， 返回的布尔索引是可以多维的
    arr[~np.isnan(arr)]，通过布尔索引获取的值是一维的
    
    arr[[0,1,2], [0,1,0]]，使用整数数组索引获取元素
    arr[1:3,[1,2]]，使用切片和整数索引获取元素
    花式索引本质上与整数索引相同，数组与花式索引的维度相同获取数组的值，维度不同则是对数组的切片和排序
    arr[[4,2,1,7]]，正序的花式索引数组
    arr[[-4,-2,-1,-7]])，倒序的花式索引数组
    np.ix_([1,5,7,2],[0,3,1,2])，二维的花式索引数组
    
<h3>副本与视图</h3>
    副本与原数据的物理内存不在同一位置
    视图与原数据的物理内存在同一位置
    副本发生在：Python 序列的切片操作，copy.deepCopy()，numpy.copy()。副本与原始数据互不影响，物理内存不在同一位置
    视图发生在：numpy的切片操作返回原数据的视图，arr.view()。 后者类似于浅拷贝，而且外壳的变化并不会造成原数据的变化。虽然视图指向原数据，但是id不一样，即视图在操作上与赋值引用是由区别的
<h3>数组迭代</h3>
    numpy.nditer(arr)：是可迭代对象，迭代按照储存方式进行，不同储存方式C（行序优先）, F（列序优先），其遍历出的结果是不一样的。打印出来是一样的
    默认情况下是只读模式，需要添加op_flags=['readwrite']模式， flags有四个参数。广播迭代 for arr in np.nditer([arr1,arr2])

<h3>ufunc</h3>
<h3>通用函数</h3>
    通用函数在 NumPy 中实现矢量化，这比迭代元素要快
    sqrt()、sin()、cos()、abs()、log()、logl()、log2()、sum()、mean()、median()
    dot()，矩阵运算(点积，内积)
    exp()，指数函数
    cumsum()、cumproduct()，累计求和、求积
    std()、var()，标准差、方差
    corrcoef()，计算相关系数
    outer(), 外积
    kron(),张量积
    向量化，就是迭代语句转换为基于向量的操作。比如对两个列表按照相同索引求和，可以用zip,也可以通过ufunc:add来完成 

<h3>reshape</h3>
<h3>数组形状修改</h3>
    创建数组时可以传递ndmin，即指定秩。通过arr.shape可以获取秩，arr.reshape可以改变秩。
    arr.reshape(-1)，展平数组
    arr.reshape(2, 2, -1), 第三维是未知的维，但是元素的个数需要能整除（2*2），否则会报错
    arr.reshape(4,1) 等效于arr[:, np.newaxis]
    
<h3>位运算</h3>
<h3>广播</h3>
    两个数组具有相同的形状：两个数组相乘，则直接是位运算
    两个数组具有不相同的形状：较小的数组将在较大的数组上进行广播
    <b>广播规则</b>：NumPy会逐元素地比较它们的形状。它从尾随尺寸开始，并向前发展。两个尺寸兼容的条件：相同或者其中一个是1。长度为1的轴在广播期间会被扩展为更大的大小
    
<h3>数组翻转</h3>
    numpy.transpose，对换数组的维度
    arr.T，对换数组的维度
    numpy.rollaxis，向后滚动指定的轴
    numpy.swapaxes，对换数组的两个轴
    
<h3>数组连接</h3>
    numpy.concatenate，连接沿现有轴的数组序列
    numpy.stack，沿着新的轴加入一系列数组。
    numpy.hstack，水平堆叠序列中的数组（列方向）
    numpy.vstack，竖直堆叠序列中的数组（行方向）
    numpy.dstack，沿高度堆叠，该高度与深度相同,对于n个完全匹配的2维数组的output[:, :, n]与第n个输入数组相同； 如果是3维的，
    x = numpy.zeros([2, 2, 3])， y = numpy.ones([2, 2, 4])，那么z[:, :, :3]将与x相同，而z[:, :, 3:7]将与y相同
    
<h3>数组分割</h3>
    numpy.split，将一个数组分割为多个子数组
    numpy.array_split，将一个数组分割为多个子数组
    numpy.hsplit，将一个数组水平分割为多个子数组（按列）
    numpy.vsplit，将一个数组垂直分割为多个子数组（按行）
    
<h3>数组添加和删除</h3>       
    numpy.resize，返回指定形状的新数组
    numpy.append，将值添加到数组末尾
    numpy.insert，沿指定轴将值插入到指定下标之前
    numpy.delete，删掉某个轴的子数组，并返回删除后的新数组
    numpy.unique，查找数组内的唯一元素, 也可获取索引，计数

    
<h3>数组排序</h3>
    numpy.sort，对每个元素进行排序, 定义了dtype，order可以指定dtype中的key或dtype
    numpy.lexsort，多级排序，通过该函数获取所有要排序的列排序后的列索引
    arr.argsort， 数组中的元素进行从小到大排序，返回相应序列元素的数组下
    numpy.searchsorted，在一维数组（被排序后的）中找出插入的位置索引

    
<h3>数组筛选</h3>
    使用布尔索引进行筛选，创建过滤器数组或者是直接从数组创建过滤器，进行过滤
    
numpy.in1d中前者中每一个元素是否在后者中，返回布尔值组成的数组
numpy.count_nonzero计算每一列或行的非0元素
np.argmax()，返回最大值的下标
np.argmin()，返回最小值的下标
np.where()，用法参数位置与三元运算符类似

<h3>numpy随机数</h3>
    numpy.random.randint()，生成随机数
    numpy.random.rand()，生成浮点数
    numpy.random.randint(100, size=(5))，生成随机数组
    numpy.random.randint(100, size=(3, 5))，生成随机数组
    numpy.random.choice([1,3,5,7])，基于数组中的值生成随机值
    
<h3>NumPy 字符串函数</h3>
    numpy.char.add()，函数依次对两个数组的元素进行字符串连接
    numpy.char.multiply("AD",3)，函数执行多重连接
    numpy.char.center()，函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充。
    numpy.char.capitalize()，函数将字符串的第一个字母转换为大写
    numpy.char.title()，函数将字符串的每个单词的第一个字母转换为大写
    numpy.char.lower()，函数对数组的每个元素转换为小写
    numpy.char.upper()，函数对数组的每个元素转换为大写
    numpy.char.split()，通过指定分隔符对字符串进行分割，并返回数组
    numpy.char.splitlines()，函数以换行符作为分隔符来分割字符串，并返回数组。
    numpy.char.strip()，函数用于移除开头或结尾处的特定字符
    numpy.char.join()，函数通过指定分隔符来连接数组中的元素或字符串
    numpy.char.replace()，函数使用新字符串替换字符串中的所有子字符串。
    numpy.char.encode()，函数对数组中的每个元素调用 str.encode 函数。 默认编码是 utf-8，可以使用标准 Python 库中的编解码器。
    numpy.char.decode()，函数对编码的元素进行 str.decode() 解码。
    
<h3>NumPy 数学函数</h3>
    正函数获取值，反函数获取弧度，角度弧度转换获得角度
    np.sin()、np.cos()、np.tan()、arcsin、arccos、arctan三角函数
    np.degrees(弧度值))，角度与弧度转换，1 = np.pi / 180
    numpy.around()，函数返回指定数字的四舍五入值。
    numpy.floor()，向下取整
    numpy.ceil()，向上取整
    
<h3>NumPy 统计函数</h3>
    numpy.amin()，计算数组中的元素沿指定轴的最小值
    numpy.amax()，计算数组中的元素沿指定轴的最大值
    numpy.ptp()，函数计算数组中元素最大值与最小值的差（最大值 - 最小值）
    numpy.percentile()，百分位数是统计中使用的度量，表示小于这个值的观察值的百分比
    numpy.median()，函数用于计算数组 a 中元素的中位数（中值）
    numpy.mean()，函数返回数组中元素的算术平均值
    numpy.average()，函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
    numpy.std()，std = sqrt(mean((x - x.mean())**2))，标准差是一组数据平均值分散程度的一种度量
    numpy.var()，mean((x - x.mean())** 2)，统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数
    
<h3>NumPy 字节交换</h3>
    大端模式：指数据的高字节保存在内存的低地址中，而数据的低字节保存在内存的高地址中
    小端模式：指数据的高字节保存在内存的高地址中，而数据的低字节保存在内存的低地址中
    numpy.ndarray.byteswap()，函数将 ndarray 中每个元素中的字节进行大小端转换。
    
<h3>NumPy 矩阵库(Matrix)</h3>
矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的。
    import numpy.matlib
    import numpy as np
    numpy.matlib.empty，函数返回一个新的矩阵
    numpy.matlib.zeros，创建一个以 0 填充的矩阵
    numpy.matlib.ones，创建一个以 1 填充的矩阵
    numpy.matlib.eye，返回一个矩阵，对角线元素为 1，其他位置为零
    numpy.matlib.identity，函数返回给定大小的单位矩阵
    numpy.matlib.rand，创建一个给定大小的矩阵，数据是随机填充的
    
    np.matrix('1,2;3,4')，字符串转矩阵
    np.asarray()，matrix转ndarray
    np.asmatrix，ndarray转matrix
<h3>NumPy 线性代数</h3>
    numpy.dot，两个数组的点积，即元素对应相乘。
    numpy.vdot，两个向量的点积
    numpy.inner，两个数组的内积
    numpy.matmul，两个数组的矩阵积
    numpy.linalg.det，数组的行列式(determinant)
    numpy.linalg.solve，求解线性矩阵方程
    numpy.linalg.inv，计算矩阵的乘法逆矩阵
<h3>NumPy IO</h3>
    numpy.save，将数组保存到以 .npy 为扩展名的文件
    numpy.savez，将多个数组保存到以 npz 为扩展名的文件中
    numpy.savetxt，以简单的文本文件格式存储数据，并使用loadtxt() 函数来获取数据
<h3>NumPy Matplotlib</h3>
"""
data = [
    ('小明', ['A', 'B', 'A'], 17),
    ('小红', ['B', 'A', 'C'], 18),
    ('小王', ['C', 'A', 'A'], 19)
]
from numpy import dtype

t = dtype({'names': ['name', 'age', 'height'], 'formats': ['U8', 'U3', 'int32']})

a = np.array(data, dtype='U8, 3U3, int32')
