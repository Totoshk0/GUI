import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 400))
        
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Создаем различные виджеты
        self.create_widgets()
        
        # Настраиваем обработчики событий
        self.bind_events()
        
        self.panel.SetSizer(self.sizer)
        self.Centre()
        self.Show()
    
    def create_widgets(self):
        """Создание и размещение виджетов на панели"""
        
        # Статический текст
        self.title = wx.StaticText(self.panel, label="Демонстрация wxPython виджетов")
        self.title.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.sizer.Add(self.title, 0, wx.ALL | wx.CENTER, 10)
        
        # Поле ввода текста
        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE, size=(400, 100))
        self.sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 10)
        
        # Кнопки
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn_ok = wx.Button(self.panel, label="OK")
        self.btn_cancel = wx.Button(self.panel, label="Cancel")
        self.btn_clear = wx.Button(self.panel, label="Clear")
        
        button_sizer.Add(self.btn_ok, 0, wx.ALL, 5)
        button_sizer.Add(self.btn_cancel, 0, wx.ALL, 5)
        button_sizer.Add(self.btn_clear, 0, wx.ALL, 5)
        
        self.sizer.Add(button_sizer, 0, wx.CENTER)
        
        # Чекбокс
        self.checkbox = wx.CheckBox(self.panel, label="Включить опцию")
        self.sizer.Add(self.checkbox, 0, wx.ALL, 10)
        
        # Радио-кнопки
        radio_box = wx.RadioBox(self.panel, 
                               label="Выберите вариант",
                               choices=["Вариант 1", "Вариант 2", "Вариант 3"],
                               majorDimension=1,
                               style=wx.RA_SPECIFY_COLS)
        self.sizer.Add(radio_box, 0, wx.ALL | wx.EXPAND, 10)
        
        # Выпадающий список
        choices = ["Элемент 1", "Элемент 2", "Элемент 3"]
        self.combo = wx.ComboBox(self.panel, choices=choices, style=wx.CB_READONLY)
        self.sizer.Add(self.combo, 0, wx.ALL | wx.EXPAND, 10)
        
        # Ползунок
        self.slider = wx.Slider(self.panel, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.sizer.Add(self.slider, 0, wx.ALL | wx.EXPAND, 10)
    
    def bind_events(self):
        """Привязка обработчиков событий"""
        self.btn_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.btn_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.btn_clear.Bind(wx.EVT_BUTTON, self.on_clear)
        self.checkbox.Bind(wx.EVT_CHECKBOX, self.on_check)
        self.combo.Bind(wx.EVT_COMBOBOX, self.on_combo)
        self.slider.Bind(wx.EVT_SLIDER, self.on_slide)
    
    def on_ok(self, event):
        """Обработчик нажатия кнопки OK"""
        wx.MessageBox("Вы нажали OK!", "Информация", wx.OK | wx.ICON_INFORMATION)
    
    def on_cancel(self, event):
        """Обработчик нажатия кнопки Cancel"""
        self.Close()
    
    def on_clear(self, event):
        """Обработчик нажатия кнопки Clear"""
        self.text_ctrl.Clear()
    
    def on_check(self, event):
        """Обработчик изменения состояния чекбокса"""
        state = "включена" if self.checkbox.GetValue() else "выключена"
        self.text_ctrl.AppendText(f"Опция {state}\n")
    
    def on_combo(self, event):
        """Обработчик выбора в комбобоксе"""
        selection = self.combo.GetStringSelection()
        self.text_ctrl.AppendText(f"Выбран: {selection}\n")
    
    def on_slide(self, event):
        """Обработчик перемещения ползунка"""
        value = self.slider.GetValue()
        self.text_ctrl.AppendText(f"Значение ползунка: {value}\n")

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, "wxPython Demo")
    app.MainLoop()