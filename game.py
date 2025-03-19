import tkinter as tk
from tkinter import scrolledtext

class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Пригодницька гра: Тіні Темного Лісу")
        self.root.configure(bg='black')  # Чорний фон
        self.root.geometry("600x400")  # Початковий розмір
        self.root.resizable(True, True)  # Дозволяємо зміну розміру
        
        # Налаштування адаптивного розміщення
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=3)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        
        # Вікно подій
        self.event_window = scrolledtext.ScrolledText(root, state='disabled', bg='black', fg='white', wrap=tk.WORD)
        self.event_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
        
        # Інвентар
        self.inventory_label = tk.Label(root, text="Інвентар:", bg='black', fg='white')
        self.inventory_label.grid(row=1, column=0, sticky='w', padx=10)
        
        self.inventory_list = tk.Listbox(root, bg='black', fg='white')
        self.inventory_list.grid(row=2, column=0, padx=10, pady=5, sticky='nsew')
        
        # Статуси гравця
        self.status_label = tk.Label(root, text="Статуси гравця:", bg='black', fg='white')
        self.status_label.grid(row=1, column=1, sticky='w', padx=10)
        
        self.hp_label = tk.Label(root, text="HP: 100", bg='black', fg='white')
        self.hp_label.grid(row=2, column=1, sticky='w', padx=10)
        
        self.stamina_label = tk.Label(root, text="Витривалість: 100", bg='black', fg='white')
        self.stamina_label.grid(row=3, column=1, sticky='w', padx=10)
        
        # Панель вибору дій
        self.action_frame = tk.Frame(root, bg='black')
        self.action_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
        
        self.action_buttons = []
        
        # Кнопка для переходу до наступної події
        self.event_button = tk.Button(root, text="Наступна подія", command=self.next_event, bg='gray', fg='white')
        self.event_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Список подій
        self.events = [
            {"text": "Ви опинилися у темному лісі. Ліс виглядає непривітно і загадково. Ви чуєте звуки природи, але з кожним кроком починаєте відчувати, що за вами спостерігають.", "choices": ["Йти вперед по дивній дорозі", "Оглянутися"]},
            {"text": "Перед вами розвилка. Лівий шлях веде до ферми, а правий – до міста, що знаходиться в 65 км.", "choices": ["Ферма (тропа на ліво)", "Місто 65 кілометрів (тропа на право)"]},
            {"text": "Ви йдете до ферми. Тут тихо і спокійно, але щось у повітрі здається дивним.", "choices": ["Зайти в будинок", "Оглянути територію"]},
            {"text": "Ви натрапили на старий міст, що веде до міста. Дорога небезпечна, але ви повинні продовжити.", "choices": ["Продовжити йти", "Зупинитися і відпочити"]},
            {"text": "Ви продовжили свій шлях і знайшли селище, але будинки здаються покинутими. Це виглядає як пастка.", "choices": ["Попробувати покликати когось", "Оглянути будинки", "Пройти повз"]},
            {"text": "У будинку ви знаходите ключ до невідомого механізму. Це може бути важливим для вашої місії.", "choices": []},
            {"text": "Прихід до храму, де зберігається артефакт темряви. Але тут ви зустрічаєте Темного Лорда.", "choices": ["Битися з Темним Лордом", "Спробувати використовувати артефакт для знищення Лорда"]},
            {"text": "Ви успішно перемогли Темного Лорда і забрали артефакт. Світ врятовано, але що буде далі?", "choices": []},
            # Додаткові події
            {"text": "Перед вами на землі лежить таємничий предмет, він світиться. Що це?", "choices": ["Забрати предмет", "Пройти повз"]},
            {"text": "Ви знайшли стару карту на землі. Вона веде до незнайомого місця.", "choices": ["Слідувати карті", "Залишити карту"]},
            {"text": "Після кількох годин подорожі ви знаходите річку. Перейти через неї чи залишитись на березі?", "choices": ["Перейти річку", "Залишитись на березі"]},
            {"text": "Ви зупиняєтесь на відпочинок. Чи не заблукали ви насправді?", "choices": ["Продовжити йти", "Оглянути місце на предмет можливих небезпек"]},
            {"text": "Ви натрапляєте на стару хатину. Ви бачите вікно, яке світиться всередині.", "choices": ["Зайти в хатину", "Обійти хатину"]},
            {"text": "Ви чуєте вдалині звуки битви. Що робити?", "choices": ["Підійти до битви", "Залишитись осторонь"]},
            {"text": "На вашому шляху з'являється величезний лісовий звір. Що робити?", "choices": ["Битися з ним", "Втікти"]},
            {"text": "Ви знайшли цілу групу мандрівників, які проходять цей ліс. Вони пропонують допомогу.", "choices": ["Прийняти допомогу", "Відмовитися від допомоги"]},
            {"text": "Ви доходите до старої руїни. Тут ви знайшли таємничі документи, які пояснюють походження цього лісу.", "choices": ["Забрати документи", "Залишити документи"]},
            {"text": "На горизонті з'являється чорний хмара. Це знак, що щось велике йде.", "choices": ["Шукати укриття", "Продовжити подорож"]},
            {"text": "Ви натрапляєте на ворогів, які намагаються вас обкрасти. Що робити?", "choices": ["Битися з ними", "Сховатися і уникнути бою"]},
            {"text": "Ви стоїте перед величезними воротами. Вони ведуть до таємного місця. Як поступити?", "choices": ["Відкрити ворота", "Піти іншою дорогою"]},
            {"text": "Ви натрапляєте на пастку, але за допомогою ключа, знайденого раніше, вдається відкрити її.", "choices": []},
            {"text": "Ви віднайшли артефакт, здатний відкрити двері до іншого світу.", "choices": []},
            {"text": "Ви зустрічаєте старця, який просить допомоги. Ви готові йому допомогти?", "choices": ["Допомогти старцю", "Відмовитися від допомоги"]},
            {"text": "Ви підійшли до джерела і знайшли магічне зілля, що може відновити ваші сили.", "choices": ["Випити зілля", "Не пити зілля"]},
        ]
        self.current_event = 0
        
        # Запуск першої події
        self.next_event()
    
    def next_event(self):
        if self.current_event < len(self.events):
            event = self.events[self.current_event]
            self.display_event(event["text"])
            self.display_choices(event["choices"])
            
            # Блокуємо кнопку, якщо є вибори
            if event["choices"]:
                self.event_button.config(state=tk.DISABLED)
            else:
                self.event_button.config(state=tk.NORMAL)
            
            self.current_event += 1
        else:
            self.display_event("Пригода завершена!")
    
    def display_event(self, text):
        self.event_window.config(state='normal')
        self.event_window.insert(tk.END, text + "\n")
        self.event_window.config(state='disabled')
        self.event_window.yview(tk.END)
    
    def display_choices(self, choices):
        # Видаляємо старі кнопки
        for button in self.action_buttons:
            button.destroy()
        self.action_buttons.clear()
        
        # Додаємо нові кнопки вибору
        for choice in choices:
            button = tk.Button(self.action_frame, text=choice, command=lambda c=choice: self.process_choice(c), bg='gray', fg='white')
            button.pack(side=tk.LEFT, padx=5)
            self.action_buttons.append(button)
    
    def process_choice(self, choice):
        self.display_event(f"[Вибір гравця]: {choice}")
        
        # Видаляємо кнопки вибору
        for button in self.action_buttons:
            button.destroy()
        self.action_buttons.clear()
        
        # Логіка для розгалуження сюжету
        if choice == "Ферма (тропа на ліво)":
            self.events.insert(self.current_event, {"text": "Ви прийшли до ферми. Тут тихо і спокійно.", "choices": ["Зайти в будинок", "Оглянути територію"]})
        elif choice == "Місто 65 кілометрів (тропа на право)":
            self.events.insert(self.current_event, {"text": "Ви вирушили до міста. Дорога довга і небезпечна.", "choices": ["Продовжити йти", "Зупинитися і відпочити"]})
        elif choice == "Зупинитися і відпочити":
            self.events.insert(self.current_event, {"text": "Ви відпочили та знайшли ключ, який приведе вас до важливого місця.", "choices": ["Взяти ключ", "Нічого не робити"]})
        elif choice == "Продовжити йти":
            self.events.insert(self.current_event, {"text": "Ви продовжили йти і після довгого шляху ви побачили місто. Ви вирушили до селища.", "choices": ["Зайти в селище", "Пройти повз"]})
        elif choice == "Зайти в селище":
            self.events.insert(self.current_event, {"text": "Ви зайшли в селище і побачили багато будинків. Вони здаються давно покинутими.", "choices": ["Попробувати покликати когось", "Пройти повз", "Оглянути будинки"]})
        # Розблоковуємо кнопку наступної події
        self.event_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()
