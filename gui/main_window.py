import sys
import ctypes
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QScrollArea, QFrame)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QPalette
from optimizations import network, graphics, power, privacy, services, storage, updates
from backup_manager import manager

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class OptimizationWorker(QThread):
    finished = pyqtSignal(bool)
    
    def __init__(self, optimization_module, category_name, is_enable):
        super().__init__()
        self.optimization_module = optimization_module
        self.category_name = category_name
        self.is_enable = is_enable
    
    def run(self):
        try:
            if self.is_enable:
                backup_data = self.optimization_module.get_backup_data()
                manager.save_backup(self.category_name, backup_data)
                self.optimization_module.apply()
            else:
                backup_data = manager.load_backup(self.category_name)
                if backup_data:
                    self.optimization_module.restore(backup_data)
                    manager.delete_backup(self.category_name)
            self.finished.emit(True)
        except:
            self.finished.emit(False)

class ToggleSwitch(QWidget):
    def __init__(self, category_name, parent=None):
        super().__init__(parent)
        self.category_name = category_name
        self.is_on = manager.has_backup(category_name)
        self.setFixedSize(60, 30)
        self.setCursor(Qt.PointingHandCursor)
        
    def paintEvent(self, event):
        from PyQt5.QtGui import QPainter, QBrush, QPen
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        if self.is_on:
            brush = QBrush(QColor(0, 200, 0))
        else:
            brush = QBrush(QColor(200, 0, 0))
        
        painter.setBrush(brush)
        painter.setPen(QPen(Qt.NoPen))
        painter.drawRoundedRect(0, 0, 60, 30, 15, 15)
        
        circle_x = 35 if self.is_on else 5
        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(circle_x, 5, 20, 20)
    
    def mousePressEvent(self, event):
        self.is_on = not self.is_on
        self.update()
        self.parent().parent().parent().toggle_optimization(self.category_name, self.is_on)

class OptimizationCard(QFrame):
    def __init__(self, title, description, category_name, parent=None):
        super().__init__(parent)
        self.category_name = category_name
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.setLineWidth(2)
        self.setStyleSheet("""
            QFrame {
                background-color: #2b2b2b;
                border: 2px solid #3a3a3a;
                border-radius: 10px;
                padding: 15px;
            }
        """)
        
        layout = QHBoxLayout()
        
        text_layout = QVBoxLayout()
        
        title_label = QLabel(title)
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: white;")
        
        desc_label = QLabel(description)
        desc_font = QFont()
        desc_font.setPointSize(9)
        desc_label.setFont(desc_font)
        desc_label.setStyleSheet("color: #aaaaaa;")
        desc_label.setWordWrap(True)
        
        text_layout.addWidget(title_label)
        text_layout.addWidget(desc_label)
        text_layout.addStretch()
        
        layout.addLayout(text_layout, 1)
        
        self.toggle = ToggleSwitch(category_name, self)
        layout.addWidget(self.toggle, 0, Qt.AlignRight | Qt.AlignVCenter)
        
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Windows Optimizer")
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet("background-color: #1e1e1e;")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        header = QLabel("Windows System Optimizer")
        header_font = QFont()
        header_font.setPointSize(18)
        header_font.setBold(True)
        header.setFont(header_font)
        header.setStyleSheet("color: white; padding: 20px;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        self.apply_all_btn = QPushButton("Apply All Optimizations")
        self.apply_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 15px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1084d8;
            }
            QPushButton:pressed {
                background-color: #006cbd;
            }
        """)
        self.apply_all_btn.clicked.connect(self.apply_all)
        main_layout.addWidget(self.apply_all_btn)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")
        
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_layout.setSpacing(15)
        
        self.categories = [
            ("Network Optimizations", "Optimize TCP/IP settings, DNS cache, and network adapter configurations", "network", network),
            ("Graphics & GPU", "Optimize GPU driver settings, disable GPU throttling, improve frame latency", "graphics", graphics),
            ("Power Management", "Maximize performance, disable CPU throttling, optimize power settings", "power", power),
            ("Privacy & Telemetry", "Disable telemetry, tracking, and data collection services", "privacy", privacy),
            ("System Services", "Disable unnecessary Windows services and scheduled tasks", "services", services),
            ("Storage & File System", "Optimize disk performance, disable indexing and compression", "storage", storage),
            ("Windows Updates", "Disable automatic updates and related services", "updates", updates),
        ]
        
        for title, desc, cat_name, module in self.categories:
            card = OptimizationCard(title, desc, cat_name, self)
            scroll_layout.addWidget(card)
        
        scroll_layout.addStretch()
        scroll_content.setLayout(scroll_layout)
        scroll.setWidget(scroll_content)
        
        main_layout.addWidget(scroll)
        central_widget.setLayout(main_layout)
        
        self.workers = []
    
    def toggle_optimization(self, category_name, is_enable):
        module = None
        for title, desc, cat_name, mod in self.categories:
            if cat_name == category_name:
                module = mod
                break
        
        if module:
            worker = OptimizationWorker(module, category_name, is_enable)
            worker.finished.connect(lambda success: self.on_optimization_finished(success, category_name))
            self.workers.append(worker)
            worker.start()
    
    def on_optimization_finished(self, success, category_name):
        pass
    
    def apply_all(self):
        for title, desc, cat_name, module in self.categories:
            if not manager.has_backup(cat_name):
                backup_data = module.get_backup_data()
                manager.save_backup(cat_name, backup_data)
                worker = OptimizationWorker(module, cat_name, True)
                worker.start()
                self.workers.append(worker)

def run():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
