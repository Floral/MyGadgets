# My Gadgets

Here are some gadgets I wrote myself while working on other projects

## Video2Binary

这是一个将视频转成二进制文件的python小脚本（目前只支持转化为二值（其实自己修改一下也很简单））

### 运行环境

> python
>
> 需求额外安装库：
>
> - opencv-python (cv2)
> - pillow (PIL)
> - numpy

### 使用方法

把该脚本放在你所需要转化的视频所在的同一个目录下，在命令行中进入该目录，并使用python命令运行脚本，具体格式如下：

`$ python video2binary.py "Your Video Name" "Your target binary file's name" [target img's width [target img's height] `

后面两个参数为可选项，且为数字，前面两个文件名应放在英文的双引号中（包括后缀名）。

最后生成的二进制文件与视频在同一个目录下，同时会在该目录下创建一个imgs文件夹，视频转化为的图片都放在其中。