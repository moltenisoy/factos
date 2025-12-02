import sys
import ctypes
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QScrollArea, QFrame)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QColor
import opt_full
import opt_network
import opt_graphics
import opt_power
import opt_privacy
import opt_services
import opt_storage
import backup_mgr

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

class OptimizationWorker(QThread):
    finished = pyqtSignal(bool)
    
    def __init__(self, apply_func, backup_file, is_enable):
        super().__init__()
        self.apply_func = apply_func
        self.backup_file = backup_file
        self.is_enable = is_enable
    
    def run(self):
        try:
            if self.is_enable:
                backup_data = {'backup_created': True}
                backup_mgr.save_backup(self.backup_file, backup_data)
                self.apply_func()
            else:
                backup_data = backup_mgr.load_backup(self.backup_file)
                if backup_data:
                    backup_mgr.delete_backup(self.backup_file)
            self.finished.emit(True)
        except Exception:
            self.finished.emit(False)

class ToggleSwitch(QWidget):
    def __init__(self, backup_file, parent=None):
        super().__init__(parent)
        self.backup_file = backup_file
        self.is_on = backup_mgr.has_backup(backup_file)
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
        self.parent().parent().parent().toggle_optimization(self.backup_file, self.is_on)

class OptimizationCard(QFrame):
    def __init__(self, title, description, backup_file, parent=None):
        super().__init__(parent)
        self.backup_file = backup_file
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.setLineWidth(2)
        self.setMinimumHeight(110)
        self.setMaximumHeight(130)
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
        
        self.toggle = ToggleSwitch(backup_file, self)
        layout.addWidget(self.toggle, 0, Qt.AlignRight | Qt.AlignVCenter)
        
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Optimizador de Windows")
        
        # Center window on screen
        self.setFixedSize(1000, 750)
        self.center_on_screen()
        self.setStyleSheet("background-color: #1c2833;")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 20, 30, 20)
        main_layout.setSpacing(20)
        
        header = QLabel("Seleccione las Opciones de Optimización")
        header_font = QFont()
        header_font.setPointSize(16)
        header_font.setBold(True)
        header.setFont(header_font)
        header.setStyleSheet("color: #ecf0f1; padding: 10px;")
        header.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(header)
        
        self.apply_all_btn = QPushButton("✓ Aplicar Todas las Optimizaciones")
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
            ("Red y Conectividad", "Optimiza TCP/IP, DNS, firewall y configuraciones de red para\nmejorar velocidad y reducir latencia de conexión", "backup_opt_network.json", opt_network.apply_network),
            ("Gráficos y Rendimiento Visual", "Mejora GPU, pantalla, DWM y efectos visuales para\nmaximizar FPS y respuesta en juegos y aplicaciones gráficas", "backup_opt_graphics.json", opt_graphics.apply_all),
            ("Energía y CPU", "Configura gestión de energía y CPU para máximo rendimiento,\ndesactiva ahorro de energía y optimiza procesador", "backup_opt_power.json", opt_power.apply_power),
            ("Privacidad y Seguridad", "Desactiva telemetría, diagnósticos y seguimiento de Windows,\nprotege tu privacidad deshabilitando recopilación de datos", "backup_opt_privacy.json", opt_privacy.apply_privacy),
            ("Servicios de Windows", "Deshabilita servicios innecesarios de Windows para\nliberar recursos del sistema y mejorar velocidad general", "backup_opt_services.json", opt_services.apply_services),
            ("Almacenamiento y Disco", "Optimiza SSD, disco, indexación y compresión para\nmejorar tiempos de lectura/escritura y vida útil del disco", "backup_opt_storage.json", opt_storage.apply_storage),
        ]
        
        for title, desc, backup_file, apply_func in self.categories:
            card = OptimizationCard(title, desc, backup_file, self)
            card.apply_func = apply_func
            scroll_layout.addWidget(card)
        
        scroll_layout.addStretch()
        scroll_content.setLayout(scroll_layout)
        scroll.setWidget(scroll_content)
        
        main_layout.addWidget(scroll)
        central_widget.setLayout(main_layout)
        
        self.workers = []
    
    def center_on_screen(self):
        """Center the window on the screen"""
        screen = QApplication.desktop().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def toggle_optimization(self, backup_file, is_enable):
        apply_func = None
        for title, desc, bf, func in self.categories:
            if bf == backup_file:
                apply_func = func
                break
        
        if apply_func:
            try:
                worker = OptimizationWorker(apply_func, backup_file, is_enable)
                worker.finished.connect(lambda success: self.on_optimization_finished(success, backup_file))
                self.workers.append(worker)
                worker.start()
            except Exception:
                pass
    
    def on_optimization_finished(self, success, backup_file):
        if self.workers:
            try:
                self.workers = [w for w in self.workers if w.isRunning()]
            except Exception:
                pass
    
    def apply_all(self):
        self.apply_all_btn.setEnabled(False)
        self.apply_all_btn.setText("Aplicando...")
        
        for title, desc, backup_file, apply_func in self.categories:
            try:
                if not backup_mgr.has_backup(backup_file):
                    backup_data = {'backup_created': True}
                    backup_mgr.save_backup(backup_file, backup_data)
                    worker = OptimizationWorker(apply_func, backup_file, True)
                    worker.finished.connect(lambda: self.on_apply_all_finished())
                    self.workers.append(worker)
                    worker.start()
            except Exception:
                pass
    
    def on_apply_all_finished(self):
        self.apply_all_btn.setEnabled(True)
        self.apply_all_btn.setText("✓ Aplicar Todas las Optimizaciones")

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
