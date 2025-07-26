### QPushButton

---

在Qt6中，按钮(QPushButton)的QSS样式可以使用以下属性进行定制：

- background-color：设置按钮的背景颜色。
- color：设置按钮文本的颜色。
- border：设置按钮的边框样式，如边框宽度、边框颜色等。
- padding：设置按钮的内边距，即按钮内容与边框之间的距离。
- font-size：设置按钮文本的字体大小。
- font-family：设置按钮文本的字体系列。
- font-weight：设置按钮文本的字体粗细。
- border-radius：设置按钮的圆角半径，使按钮的边角变为圆角。
- text-align：设置按钮文本的对齐方式，如居中、左对齐、右对齐等。
- text-decoration：设置按钮文本的装饰效果，如下划线、删除线等。
- hover：设置按钮在鼠标悬停时的样式。
- pressed：设置按钮在按下时的样式。
- disabled：设置按钮在禁用状态下的样式。

- background-repeat: 设置背景图像是否重复显示;
  - `no-repeat` 表示背景图像不会重复，只有一次。如果背景图像尺寸大于按钮，这部分背景将不显示。

```css
QPushButton {
	background-image: url(:/background/文档.png);
	background-position: center;
    background-repeat: no-repeat;
	border: none;
	border-left: solid transparent;
	background-color: rgb(37, 41, 48);
	text-align: left;
	padding: 144px;
	color: rgb(113, 126, 149);
}
```



### QPropertyAnimation 设置动画





##### setEasingCurve

用于设置动画的缓动曲线（即动画的变化速度）

**`QEasingCurve.Type.InOutQuart`** 是一种缓动曲线类型

~~~python
    # 使用 QPropertyAnimation 设置动画
    self.animation = QPropertyAnimation(left_menu, b"minimumWidth")
    self.animation.setDuration(Settings.TIME_ANIMATION)
    self.animation.setStartValue(current_width)
    self.animation.setEndValue(target_width)
    self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
    self.animation.start()
~~~





上边框

leftMenuFrame{\n"

"    border-top: 3px solid rgb(44, 49, 58);\





![image-20250720152413297](C:\Users\ZZQ\AppData\Roaming\Typora\typora-user-images\image-20250720152413297.png)
