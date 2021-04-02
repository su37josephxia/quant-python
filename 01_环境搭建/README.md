# Python环境安装
- anaconda 
> Anaconda介绍、安装及使用教程 https://www.jianshu.com/p/62f155eb6ac5
- python


## anaconda安装

Anaconda是专注于数据分析的Python发行版本，包含了conda、Python等190多个科学包及其依赖项。conda 是开源包（packages）和虚拟环境（environment）的管理系统。

- packages 管理：可以使用 conda 来安装、更新 、卸载工具包 ，并且它更关注于数据科学相关的工具包。在安装 anaconda 时就预先集成了像 Numpy、Scipy、 pandas、Scikit-learn 这些在数据分析中常用的包。
- 虚拟环境管理： 在conda中可以建立多个虚拟环境，用于隔离不同项目所需的不同版本的工具包，以防止版本上的冲突。对纠结于 Python 版本的同学们，我们也可以建立 Python2 和 Python3 两个环境，来分别运行不同版本的 Python 代码。


anaconda 水蚺(南美洲蟒蛇);
[https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)


安装清华源

```bash
# 删除之前的镜像源，恢复默认状态
conda config --remove-key channels

#添加镜像源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2

#显示检索路径
conda config --set show_channel_urls yes

#显示镜像通道
conda config --show channels

```



## Jupyter Notebook 交互笔记本

Jupyter Notebook（此前被称为 IPython notebook）是一个交互式笔记本，支持运行 40 多种编程语言。
 Jupyter Notebook 的本质是一个 Web 应用程序，便于创建和共享文学化程序文档，支持实时代码，数学方程，可视化和 [markdown](https://baike.baidu.com/item/markdown)。 用途包括：数据清理和转换，数值模拟，统计建模，机器学习等等 。





```bash
conda install jupyter notebook

pip install jupyter
```

配置环境变量

```bash
sudo vi ~/.bash_profile
 
export PATH="/Users/anaconda3/bin:$PATH"
 
# 测试环境变量是否生效
source ~/.bash_profile

# 测试
conda list

```


> mac 安装anacoda [https://blog.csdn.net/lq_547762983/article/details/81003528](https://blog.csdn.net/lq_547762983/article/details/81003528)

启动

```
jupyter notebook

# 指定文件夹


# 指定端口
jupyter notebook --port 9999

```



使用

> jupyter使用 https://www.jianshu.com/p/91365f343585/

