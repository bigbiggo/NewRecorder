# 环境配置



## pyenv

```
pip install pyenv-win --target C:/z_file/pyenv/.pyenv
```

把PYENV添加到系统变量。注意不是用户变量

```
PYENV
C:\z_file\pyenv\.pyenv\pyenv-win
```

把下面的两个路径，添加到PATH变量里面即可。可以添加到用户变量的PATH。

```
%PYENV%\bin
%PYENV%\shims
```

测试

```
pyenv --version
```

使用

pass





## cudn pytorch Anaconda

Anaconda

先卸载安装的python

![](D:\Recorder\搜图环境搭建\pics\z_98.png)

conda 历史版本

https://repo.anaconda.com/archive/



![](D:\Recorder\搜图环境搭建\pics\z_97.png)



配置环境变量

![](D:\Recorder\搜图环境搭建\pics\z_96.png)

```
conda --version
```



 ![](D:\Recorder\搜图环境搭建\pics\z_95.png)



https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html

```
NVIDIA-SMI 497.29       Driver Version: 497.29       CUDA Version: 11.5
```





显卡驱动

```
nvidia-smi
```

![](D:\Recorder\搜图环境搭建\pics\z_100.png)





cuda 11.5

https://developer.nvidia.com/cuda-11-5-0-download-archive





```
pip install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio===0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
```



### pytorch



https://pytorch.org/get-started/locally/





解决cuda11.5//torch.cuda.is_available()输出False解决办法

https://blog.csdn.net/weixin_43806237/article/details/122158823



pytorch+CUDA+CUDNN配置教程

https://blog.csdn.net/wangpeideeeee/article/details/105981610



win10安装Anaconda、Cuda、Cudnn和Pytorch(gpu版)

https://blog.csdn.net/u012369535/article/details/106950286/



win10 pytorch安装（cuda + cudnn、anaconda、pytorch ）

https://blog.csdn.net/weixin_40333653/article/details/105150357



conda下安装pytorch最详细教程 // 安装pytorch踩坑记录 // cuda11.5下pytorch安装 // torch.cuda.is_available()输出False解决办法

https://blog.csdn.net/qq_45281807/article/details/121294644

## 正確的安裝方法

參考文章

显卡，显卡驱动,nvcc, cuda driver,cudatoolkit,cudnn到底是什么

https://www.cnblogs.com/marsggbo/p/11838823.html

cuda和cudatoolkit   +++++++++++++

https://blog.csdn.net/xiqi4145/article/details/110254093  



可能使用到的安裝資源

---

conda 历史版本

https://repo.anaconda.com/archive/

---



### cuda

可以不必使用 anaconda，測試使用 pip 安裝不會出現問題

雖然按照教程上説的要安裝 cuda對應的版本，但是測試發現依然可用

```
nvidia-smi

顯示的結果如下

 NVIDIA-SMI 511.79       Driver Version: 511.79       CUDA Version: 11.6
```

安裝之前

cuda



```
CUDA（Compute Unified Device Architecture），是显卡厂商NVIDIA推出的运算平台。 CUDA™是一种由NVIDIA推出的通用并行计算架构，该架构使GPU能够解决复杂的计算问题。 它包含了CUDA指令集架构（ISA）以及GPU内部的并行计算引擎。 开发人员可以使用C语言来为CUDA™架构编写程序，所编写出的程序可以在支持CUDA™的处理器上以超高性能运行。CUDA3.0已经开始支持C++和FORTRAN
```

更多關於cuda的介紹

认识cuda

https://zhuanlan.zhihu.com/p/146431357



下載驅動，殺毒軟件或者驅動管家也提供顯卡驅動的安裝，不過也可以考慮下載官方驅動

選擇好自己的顯卡版本，即可下載

![](D:\Recorder\搜图环境搭建\pics\x_100.png)

### CUDA Toolkit 



![](D:\Recorder\搜图环境搭建\pics\x_99.png)





### pytorch

https://pytorch.org/get-started/locally/

一次使用 conda 安裝 失敗

第二次使用 pip 安裝成功

```
pip3 install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio===0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
```

![](D:\Recorder\搜图环境搭建\pics\x_98.png)



測試安裝是否成功

```
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
print(torch.version.cuda)

返回實例：
cuda
11.3
```



yolo

https://github.com/BruceDone/darknet_demo





使用深度学习破解点击验证码   +++++++

https://zhuanlan.zhihu.com/p/34186397

https://github.com/cos120/captcha_crack?hmsr=joyk.com&utm_source=joyk.com&utm_medium=referral



https://cos120.github.io/crack/





