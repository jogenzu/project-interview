import gi
import pdfkit
try:
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
    print("GTK3 安装成功! 版本:", Gtk.get_major_version(), Gtk.get_minor_version())
except Exception as e:
    print(f"无法加载 GTK3: {str(e)}")
    print("请确保 GTK3 正确安装并配置了环境变量")