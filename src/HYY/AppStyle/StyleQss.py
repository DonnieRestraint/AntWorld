"""
QMainWindow#MainFrame{
    border-image: url(:/images/bg001.png) no-repeat 0px 0px;
}

MenuPage{}
QWidget#title_widget {
    background: rgba(255,255,255,0);
}
QPushButton#minimize_btn {
    border-image: url(:/images/minimize.png) no-repeat 0px 0px;
}
QPushButton#settingWidget {
    border-image: url(:/images/setting.png) no-repeat 0px 0px;
}
QPushButton#close_btn {
    border-image: url(:/images/close.png) no-repeat 0px 0px;
}
QLabel#title_text {
    padding:0px;
    margin:0px;
    color:rgba(63,63,63,255);
    font-size:%(nav_font)spx;
    font-weight: %(font_bold)s;
    font-family:%(font_family)s;
}


navPage{}
QScrollArea#nav_bar{
    border-radius: 0px;
    border: 0px solid ;
    border-color: rgba(255,255,255,255);
    background-color:rgba%(nav_color)s;
}
QPushButton#NavPushButton{
    background-color: rgba%(nav_color)s;
    border-radius:0px;
    padding:0px;
    margin:0px;
    border:%(nav_border)spx solid rgba(150,120,100, %(opacity)s);
    color:rgba%(nav_font_color)s;
    font-size:%(nav_font)spx;
    font-weight: %(font_bold)s;
    font-family:%(font_family)s;
}
QPushButton#NavPushButton:hover {
    background: rgba(240, 255, 250, %(opacity)s);
    color:rgba%(nav_font_color)s;
    font-size:%(nav_font)spx;
    font-weight: %(font_bold)s;
    font-family:%(font_family)s;
}
QPushButton#NavPushButton:pressed {
    background: rgba(255, 255, 255, %(opacity)s);
    color:rgba%(nav_font_color)s;
    font-size:%(nav_font)spx;
    font-weight: %(font_bold)s;
}
QPushButton#NavPushButton:focus {
    background: rgba(255, 255, 255, %(opacity)s);
    color:rgba%(nav_font_color)s;
}


NavSubPage{}
QPushButton#NavSubPushButton{
    padding:0px;
    margin:0px;
    background-color: rgba%(white)s;
    color:rgba(143,143,143,%(opacity)s);

    border: 0px solid white;
    border-radius:0px;

    font-size: 14px;
    font-weight: %(font_bold)s;
    font-family:%(font_family)s;
}
QPushButton#NavSubPushButton:focus {
    border-bottom: 2px solid rgba(0,255,255,%(opacity)s);
}


TaskPage{}
QStackedWidget#TaskStackedWidget{
    margin:0px;
    padding:0px;
    background: rgba(215,200,200,0);
}
QTableWidget#TaskTableWidget{
    border:0px;
    margin:0px;
    padding:0px;
    background:rgba(255, 255, 255, %(opacity)s);
}
QLineEdit#TaskLineEdit {
    padding:0px;
    margin:5px 5px 5px 5px;

    background-color: rgba%(white)s;
    color:rgba(143,143,143,%(opacity)s);

    border: 1px solid grey;
    border-radius:0px;

    font-size: 14px;
    font-weight: %(font_bold)s;
    font-family:%(font_family)s;
}
QPushButton#TaskPushButton {
    padding:0px;
    margin:5px 5px 5px 5px;
    background-color: rgba%(white)s;
    color:rgba(143,143,143,%(opacity)s);

    border: 1px solid grey;
    border-radius:0px;

    font-size: 14px;
    font-weight: %(font_bold)s;
    font-family:%(font_family)s;
}

QLineEdit#filePath {
    padding:0px;
    margin:5px 5px 5px 5px;

    background-color: rgba%(white)s;
    color:rgba(143,143,143,%(opacity)s);

    border: 0px solid grey;
    border-radius:0px;

    font-size: 14px;
    font-weight: %(font_bold)s;
    font-family:%(font_family)s;
}
QLineEdit#saltInput {
    padding:0px;
    margin:5px 5px 5px 5px;

    background-color: rgba%(white)s;
    color:rgba(143,143,143,%(opacity)s);

    border: 0px solid grey;
    border-radius:0px;
    font-size: 14px;
    font-weight: %(font_bold)s;
    font-family:%(font_family)s;
}
QPushButton#runButton{
    padding:0px;
    margin:5px 5px 5px 5px;
    background-color: rgba%(white)s;
    color:rgba(143,143,143,%(opacity)s);

    border: 0px solid grey;
    border-radius:5px;

    font-size: 14px;
    font-weight: %(font_bold)s;
    font-family:%(font_family)s;
}
QWidget#tipLabel{
    font-size: 20px;
    font-weight: 400;
    font-family: monospace;
}
"""
from PyQt5.QtGui import QFont

nav_font = 18

white = (255, 255, 255)
font_normal = 400  # 正常字体
font_bold = 700  # 加粗字体
moon_light_color = (255, 255, 204, 200)
nav_color = (57, 55, 57, 255)
nav_font_color = (118, 101, 91, 255)
opacity = 1
nav_border = 0
font_family = "monospace "


QSS = __doc__ % {
    "nav_color": nav_color,
    "nav_border": nav_border,
    "nav_font_color": nav_font_color,
    "opacity": int(opacity * 255),
    "font_normal": font_normal,
    "moon_light_color": moon_light_color,
    "font_bold": font_bold,
    "nav_font": nav_font,
    "white": white,
    "font_family": font_family,
}


class StyleQss(object):
    @staticmethod
    def get_qss(nav_color=nav_color,
                nav_border=nav_border,
                nav_font_color=nav_font_color,
                opacity=int(opacity*255),
                font_normal=font_normal,
                moon_light_color=moon_light_color,
                font_bold=font_bold,
                white=white,
                font_family=font_family,
                qss=__doc__
                ):

        param = {}
        param.update(nav_color=nav_color,
                     nav_border=nav_border,
                     nav_font_color=nav_font_color,
                     opacity=opacity,
                     font_normal=font_normal,
                     moon_light_color=moon_light_color,
                     font_bold=font_bold,
                     nav_font=nav_font,
                     white=white,
                     font_family=font_family,
                     )
        return qss % param

    white = white
    nav_color = nav_color
    moon_light_color = moon_light_color


if __name__ == '__main__':
    """
    QLabel#LogoLabel{
        background:QLinearGradient(
            spread:pad,
            x1:0,
            y1:1,
            x2:0,
            y2:0,
            stop:0 rgba(200, 200, 200, %(opacity)s),
            stop:0.5 rgba(150, 150, 200,%(opacity)s),
            stop:1 rgba(150, 200, 200, %(opacity)s)
        );
        border-radius:0px;color:white;
        border:%(nav_border)spx solid rgba(66, 66, 66, %(opacity)s);"""
    StyleQss().get_qss()
    f = QFont()
    f.setFamily()

