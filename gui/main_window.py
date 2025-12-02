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
        self.setFixedSize(70, 35)
        self.setCursor(Qt.PointingHandCursor)
        
    def paintEvent(self, event):
        from PyQt5.QtGui import QPainter, QBrush, QPen
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        if self.is_on:
            brush = QBrush(QColor(39, 174, 96))
        else:
            brush = QBrush(QColor(192, 57, 43))
        
        painter.setBrush(brush)
        painter.setPen(QPen(Qt.NoPen))
        painter.drawRoundedRect(0, 0, 70, 35, 17, 17)
        
        circle_x = 40 if self.is_on else 5
        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(circle_x, 5, 25, 25)
    
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
        self.setFixedHeight(100)
        self.setStyleSheet("""
            QFrame {
                background-color: #2d3e50;
                border: 1px solid #34495e;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)
        
        text_layout = QVBoxLayout()
        text_layout.setSpacing(5)
        
        title_label = QLabel(title)
        title_font = QFont()
        title_font.setPointSize(13)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #ecf0f1;")
        
        desc_label = QLabel(description)
        desc_font = QFont()
        desc_font.setPointSize(8)
        desc_label.setFont(desc_font)
        desc_label.setStyleSheet("color: #95a5a6;")
        desc_label.setWordWrap(True)
        
        text_layout.addWidget(title_label)
        text_layout.addWidget(desc_label)
        
        layout.addLayout(text_layout, 1)
        
        self.toggle = ToggleSwitch(category_name, self)
        layout.addWidget(self.toggle, 0, Qt.AlignRight | Qt.AlignVCenter)
        
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Windows Optimizer")
        self.setGeometry(100, 100, 1000, 750)
        self.setStyleSheet("background-color: #1c2833;")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 20, 30, 20)
        main_layout.setSpacing(20)
        
        header = QLabel("Select Optimization Options")
        header_font = QFont()
        header_font.setPointSize(16)
        header_font.setBold(True)
        header.setFont(header_font)
        header.setStyleSheet("color: #ecf0f1; padding: 10px;")
        header.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(header)
        
        self.apply_all_btn = QPushButton("✓ Apply All Optimizations")
        self.apply_all_btn.setFixedHeight(50)
        self.apply_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #2980b9;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 15px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3498db;
            }
            QPushButton:pressed {
                background-color: #2471a3;
            }
        """)
        self.apply_all_btn.clicked.connect(self.apply_all)
        main_layout.addWidget(self.apply_all_btn)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                background: #34495e;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #7f8c8d;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical:hover {
                background: #95a5a6;
            }
        """)
        
        scroll_content = QWidget()
        scroll_content.setStyleSheet("background-color: transparent;")
        scroll_layout = QVBoxLayout()
        scroll_layout.setSpacing(12)
        
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
            try:
                worker = OptimizationWorker(module, category_name, is_enable)
                worker.finished.connect(lambda success: self.on_optimization_finished(success, category_name))
                self.workers.append(worker)
                worker.start()
            except:
                pass
    
    def on_optimization_finished(self, success, category_name):
        if self.workers:
            try:
                self.workers = [w for w in self.workers if w.isRunning()]
            except:
                pass
    
    def apply_all(self):
        for title, desc, cat_name, module in self.categories:
            try:
                if not manager.has_backup(cat_name):
                    backup_data = module.get_backup_data()
                    manager.save_backup(cat_name, backup_data)
                    worker = OptimizationWorker(module, cat_name, True)
                    worker.start()
                    self.workers.append(worker)
            except:
                pass

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
