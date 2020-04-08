
# Vendor机器人播放Bad apple

## 效果

[BV1vK411L78c](https://www.bilibili.com/video/BV1vK411L78c/)



## 如何实现

实际原理是通过Vector Robot SDK逐步显示图片

### 前置条件

- 可通过 [Vector SDK](https://developer.anki.com/vector/docs/index.html) 连接Vendor
- [ffmpeg](http://ffmpeg.org/) 命令行工具，用来处理视频



### 步骤

1. 下载Bad apple视频。我是从[BV1Ds411r7Pg](https://www.bilibili.com/video/BV1Ds411r7Pg)下载的视频文件。
2. 将视频缩放至机器人屏幕大小，机器人支持接收`184*96`的图片
```bash
ffmpeg -y -i 9431310-1-208.mp4  -s 184*96 9431310-1-208-2.mp4 
```
3. 生成图片，我这里按每秒生成10张图片
```bash
ffmpeg -i 9431310-1-208-2.mp4 -r 10 images10/image-%05d.jpeg
```
4. 执行脚本
```bash
python3 play.py
```

