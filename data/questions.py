QUESTIONS = [
    # ===================== Python Basics =====================
    {
        "id": "py1",
        "topic": "python_basics",
        "difficulty": "easy",
        "type": "multiple_choice",
        "question": {
            "en": "What is the output of `type(42)`?",
            "ru": "Что вернёт `type(42)`?",
            "ua": "Що поверне `type(42)`?",
        },
        "options": {
            "en": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'number'>"],
            "ru": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'number'>"],
            "ua": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'number'>"],
        },
        "correct": 0,
        "explanation": {
            "en": "42 is an integer, so type() returns <class 'int'>.",
            "ru": "42 — целое число, поэтому type() возвращает <class 'int'>.",
            "ua": "42 — ціле число, тому type() повертає <class 'int'>.",
        },
    },
    {
        "id": "py2",
        "topic": "python_basics",
        "difficulty": "easy",
        "type": "open_ended",
        "question": {
            "en": "What keyword is used to define a function in Python?",
            "ru": "Какое ключевое слово используется для определения функции в Python?",
            "ua": "Яке ключове слово використовується для визначення функції в Python?",
        },
        "correct": "def",
        "accept": ["def"],
        "explanation": {
            "en": "The 'def' keyword is used to define functions.",
            "ru": "Ключевое слово 'def' используется для определения функций.",
            "ua": "Ключове слово 'def' використовується для визначення функцій.",
        },
    },
    {
        "id": "py3",
        "topic": "python_basics",
        "difficulty": "medium",
        "type": "multiple_choice",
        "question": {
            "en": "What is the result of `[1, 2, 3] + [4, 5]`?",
            "ru": "Каков результат `[1, 2, 3] + [4, 5]`?",
            "ua": "Який результат `[1, 2, 3] + [4, 5]`?",
        },
        "options": {
            "en": ["[1, 2, 3, 4, 5]", "[5, 7]", "Error", "[[1,2,3],[4,5]]"],
            "ru": ["[1, 2, 3, 4, 5]", "[5, 7]", "Ошибка", "[[1,2,3],[4,5]]"],
            "ua": ["[1, 2, 3, 4, 5]", "[5, 7]", "Помилка", "[[1,2,3],[4,5]]"],
        },
        "correct": 0,
        "explanation": {
            "en": "The + operator concatenates lists.",
            "ru": "Оператор + объединяет списки.",
            "ua": "Оператор + об'єднує списки.",
        },
    },
    {
        "id": "py4",
        "topic": "python_basics",
        "difficulty": "hard",
        "type": "multiple_choice",
        "question": {
            "en": "What does `bool([])` return?",
            "ru": "Что возвращает `bool([])`?",
            "ua": "Що повертає `bool([])`?",
        },
        "options": {
            "en": ["False", "True", "None", "Error"],
            "ru": ["False", "True", "None", "Ошибка"],
            "ua": ["False", "True", "None", "Помилка"],
        },
        "correct": 0,
        "explanation": {
            "en": "An empty list is falsy in Python, so bool([]) returns False.",
            "ru": "Пустой список — ложное значение в Python, поэтому bool([]) возвращает False.",
            "ua": "Порожній список — хибне значення в Python, тому bool([]) повертає False.",
        },
    },

    # ===================== OOP =====================
    {
        "id": "oop1",
        "topic": "oop",
        "difficulty": "easy",
        "type": "multiple_choice",
        "question": {
            "en": "Which keyword is used to create a class in Python?",
            "ru": "Какое ключевое слово создаёт класс в Python?",
            "ua": "Яке ключове слово створює клас у Python?",
        },
        "options": {
            "en": ["class", "def", "struct", "object"],
            "ru": ["class", "def", "struct", "object"],
            "ua": ["class", "def", "struct", "object"],
        },
        "correct": 0,
        "explanation": {
            "en": "The 'class' keyword defines a new class.",
            "ru": "Ключевое слово 'class' определяет новый класс.",
            "ua": "Ключове слово 'class' визначає новий клас.",
        },
    },
    {
        "id": "oop2",
        "topic": "oop",
        "difficulty": "medium",
        "type": "open_ended",
        "question": {
            "en": "What is the name of the method that initializes a new object in Python? (e.g. __xxx__)",
            "ru": "Как называется метод инициализации нового объекта в Python? (напр. __xxx__)",
            "ua": "Як називається метод ініціалізації нового об'єкта в Python? (напр. __xxx__)",
        },
        "correct": "__init__",
        "accept": ["__init__", "init", "__init__()", "__init__(self)"],
        "explanation": {
            "en": "__init__ is the constructor method called when creating a new instance.",
            "ru": "__init__ — метод-конструктор, вызываемый при создании нового экземпляра.",
            "ua": "__init__ — метод-конструктор, що викликається при створенні нового екземпляра.",
        },
    },
    {
        "id": "oop3",
        "topic": "oop",
        "difficulty": "medium",
        "type": "multiple_choice",
        "question": {
            "en": "What OOP principle allows a child class to use methods of a parent class?",
            "ru": "Какой принцип ООП позволяет дочернему классу использовать методы родительского?",
            "ua": "Який принцип ООП дозволяє дочірньому класу використовувати методи батьківського?",
        },
        "options": {
            "en": ["Inheritance", "Encapsulation", "Polymorphism", "Abstraction"],
            "ru": ["Наследование", "Инкапсуляция", "Полиморфизм", "Абстракция"],
            "ua": ["Наслідування", "Інкапсуляція", "Поліморфізм", "Абстракція"],
        },
        "correct": 0,
        "explanation": {
            "en": "Inheritance lets a child class reuse parent class functionality.",
            "ru": "Наследование позволяет дочернему классу использовать функциональность родительского.",
            "ua": "Наслідування дозволяє дочірньому класу використовувати функціональність батьківського.",
        },
    },

    # ===================== Testing =====================
    {
        "id": "test1",
        "topic": "testing",
        "difficulty": "easy",
        "type": "multiple_choice",
        "question": {
            "en": "What type of testing checks individual functions or methods?",
            "ru": "Какой тип тестирования проверяет отдельные функции или методы?",
            "ua": "Який тип тестування перевіряє окремі функції або методи?",
        },
        "options": {
            "en": ["Unit testing", "Integration testing", "E2E testing", "Load testing"],
            "ru": ["Модульное тестирование", "Интеграционное тестирование", "E2E тестирование", "Нагрузочное тестирование"],
            "ua": ["Модульне тестування", "Інтеграційне тестування", "E2E тестування", "Навантажувальне тестування"],
        },
        "correct": 0,
        "explanation": {
            "en": "Unit testing focuses on testing individual units of code in isolation.",
            "ru": "Модульное тестирование проверяет отдельные единицы кода изолированно.",
            "ua": "Модульне тестування перевіряє окремі одиниці коду ізольовано.",
        },
    },
    {
        "id": "test2",
        "topic": "testing",
        "difficulty": "easy",
        "type": "open_ended",
        "question": {
            "en": "What Python framework is most commonly used for unit testing? (one word)",
            "ru": "Какой Python-фреймворк чаще всего используют для модульного тестирования? (одно слово)",
            "ua": "Який Python-фреймворк найчастіше використовують для модульного тестування? (одне слово)",
        },
        "correct": "pytest",
        "accept": ["pytest", "unittest", "py.test"],
        "explanation": {
            "en": "pytest is the most popular Python testing framework.",
            "ru": "pytest — самый популярный фреймворк для тестирования в Python.",
            "ua": "pytest — найпопулярніший фреймворк для тестування в Python.",
        },
    },
    {
        "id": "test3",
        "topic": "testing",
        "difficulty": "hard",
        "type": "multiple_choice",
        "question": {
            "en": "What is the purpose of a test fixture?",
            "ru": "Для чего нужна тестовая фикстура (fixture)?",
            "ua": "Для чого потрібна тестова фікстура (fixture)?",
        },
        "options": {
            "en": [
                "Set up preconditions for tests",
                "Generate random test data",
                "Measure test performance",
                "Deploy code to production",
            ],
            "ru": [
                "Настроить предусловия для тестов",
                "Генерировать случайные тестовые данные",
                "Измерять производительность тестов",
                "Развернуть код в продакшен",
            ],
            "ua": [
                "Налаштувати передумови для тестів",
                "Генерувати випадкові тестові дані",
                "Вимірювати продуктивність тестів",
                "Розгорнути код у продакшен",
            ],
        },
        "correct": 0,
        "explanation": {
            "en": "Fixtures set up the necessary preconditions and state for tests.",
            "ru": "Фикстуры настраивают необходимые предусловия и состояние для тестов.",
            "ua": "Фікстури налаштовують необхідні передумови та стан для тестів.",
        },
    },

    # ===================== Selenium =====================
    {
        "id": "sel1",
        "topic": "selenium",
        "difficulty": "easy",
        "type": "multiple_choice",
        "question": {
            "en": "What does Selenium WebDriver do?",
            "ru": "Что делает Selenium WebDriver?",
            "ua": "Що робить Selenium WebDriver?",
        },
        "options": {
            "en": [
                "Automates web browser interaction",
                "Manages databases",
                "Runs API tests",
                "Compiles Python code",
            ],
            "ru": [
                "Автоматизирует взаимодействие с браузером",
                "Управляет базами данных",
                "Запускает API-тесты",
                "Компилирует код Python",
            ],
            "ua": [
                "Автоматизує взаємодію з браузером",
                "Керує базами даних",
                "Запускає API-тести",
                "Компілює код Python",
            ],
        },
        "correct": 0,
        "explanation": {
            "en": "Selenium WebDriver automates browser actions for testing web apps.",
            "ru": "Selenium WebDriver автоматизирует действия в браузере для тестирования веб-приложений.",
            "ua": "Selenium WebDriver автоматизує дії в браузері для тестування веб-додатків.",
        },
    },
    {
        "id": "sel2",
        "topic": "selenium",
        "difficulty": "medium",
        "type": "open_ended",
        "question": {
            "en": "What method finds an element by its CSS selector in Selenium? (e.g. driver.xxx)",
            "ru": "Какой метод находит элемент по CSS-селектору в Selenium? (напр. driver.xxx)",
            "ua": "Який метод знаходить елемент за CSS-селектором у Selenium? (напр. driver.xxx)",
        },
        "correct": "find_element",
        "accept": [
            "find_element",
            "find_element_by_css_selector",
            "driver.find_element",
            "find_element(by.css_selector)",
        ],
        "explanation": {
            "en": "driver.find_element(By.CSS_SELECTOR, '...') locates elements by CSS selector.",
            "ru": "driver.find_element(By.CSS_SELECTOR, '...') находит элементы по CSS-селектору.",
            "ua": "driver.find_element(By.CSS_SELECTOR, '...') знаходить елементи за CSS-селектором.",
        },
    },
    {
        "id": "sel3",
        "topic": "selenium",
        "difficulty": "hard",
        "type": "multiple_choice",
        "question": {
            "en": "What is an explicit wait in Selenium?",
            "ru": "Что такое явное ожидание (explicit wait) в Selenium?",
            "ua": "Що таке явне очікування (explicit wait) у Selenium?",
        },
        "options": {
            "en": [
                "Wait for a specific condition before proceeding",
                "Always wait a fixed number of seconds",
                "Wait for page to fully load",
                "Pause the entire test suite",
            ],
            "ru": [
                "Ждать выполнения определённого условия",
                "Всегда ждать фиксированное число секунд",
                "Ждать полной загрузки страницы",
                "Приостановить весь набор тестов",
            ],
            "ua": [
                "Чекати виконання певної умови",
                "Завжди чекати фіксовану кількість секунд",
                "Чекати повного завантаження сторінки",
                "Призупинити весь набір тестів",
            ],
        },
        "correct": 0,
        "explanation": {
            "en": "Explicit waits pause execution until a specified condition is met.",
            "ru": "Явное ожидание приостанавливает выполнение до выполнения указанного условия.",
            "ua": "Явне очікування призупиняє виконання до виконання вказаної умови.",
        },
    },

    # ===================== API Testing =====================
    {
        "id": "api1",
        "topic": "api_testing",
        "difficulty": "easy",
        "type": "multiple_choice",
        "question": {
            "en": "Which HTTP method is used to retrieve data from a server?",
            "ru": "Какой HTTP-метод используется для получения данных с сервера?",
            "ua": "Який HTTP-метод використовується для отримання даних з сервера?",
        },
        "options": {
            "en": ["GET", "POST", "DELETE", "PATCH"],
            "ru": ["GET", "POST", "DELETE", "PATCH"],
            "ua": ["GET", "POST", "DELETE", "PATCH"],
        },
        "correct": 0,
        "explanation": {
            "en": "GET requests retrieve data without modifying server state.",
            "ru": "GET-запросы получают данные, не изменяя состояние сервера.",
            "ua": "GET-запити отримують дані, не змінюючи стан сервера.",
        },
    },
    {
        "id": "api2",
        "topic": "api_testing",
        "difficulty": "medium",
        "type": "multiple_choice",
        "question": {
            "en": "What HTTP status code means 'Not Found'?",
            "ru": "Какой HTTP-код означает 'Не найдено'?",
            "ua": "Який HTTP-код означає 'Не знайдено'?",
        },
        "options": {
            "en": ["404", "200", "500", "301"],
            "ru": ["404", "200", "500", "301"],
            "ua": ["404", "200", "500", "301"],
        },
        "correct": 0,
        "explanation": {
            "en": "404 indicates the requested resource was not found.",
            "ru": "404 означает, что запрашиваемый ресурс не найден.",
            "ua": "404 означає, що запитуваний ресурс не знайдено.",
        },
    },
    {
        "id": "api3",
        "topic": "api_testing",
        "difficulty": "hard",
        "type": "open_ended",
        "question": {
            "en": "What Python library is most commonly used for making HTTP requests? (one word)",
            "ru": "Какая Python-библиотека чаще всего используется для HTTP-запросов? (одно слово)",
            "ua": "Яка Python-бібліотека найчастіше використовується для HTTP-запитів? (одне слово)",
        },
        "correct": "requests",
        "accept": ["requests", "httpx", "aiohttp", "urllib"],
        "explanation": {
            "en": "The 'requests' library is the most popular HTTP client for Python.",
            "ru": "Библиотека 'requests' — самый популярный HTTP-клиент для Python.",
            "ua": "Бібліотека 'requests' — найпопулярніший HTTP-клієнт для Python.",
        },
    },

    # ===================== SQL =====================
    {
        "id": "sql1",
        "topic": "sql",
        "difficulty": "easy",
        "type": "multiple_choice",
        "question": {
            "en": "Which SQL statement is used to retrieve data from a database?",
            "ru": "Какой SQL-оператор используется для извлечения данных из базы?",
            "ua": "Який SQL-оператор використовується для отримання даних з бази?",
        },
        "options": {
            "en": ["SELECT", "INSERT", "UPDATE", "DROP"],
            "ru": ["SELECT", "INSERT", "UPDATE", "DROP"],
            "ua": ["SELECT", "INSERT", "UPDATE", "DROP"],
        },
        "correct": 0,
        "explanation": {
            "en": "SELECT retrieves rows from one or more tables.",
            "ru": "SELECT извлекает строки из одной или нескольких таблиц.",
            "ua": "SELECT отримує рядки з однієї або кількох таблиць.",
        },
    },
    {
        "id": "sql2",
        "topic": "sql",
        "difficulty": "medium",
        "type": "open_ended",
        "question": {
            "en": "What SQL clause is used to filter rows? (one word)",
            "ru": "Какое SQL-выражение используется для фильтрации строк? (одно слово)",
            "ua": "Який SQL-вираз використовується для фільтрації рядків? (одне слово)",
        },
        "correct": "WHERE",
        "accept": ["where", "WHERE"],
        "explanation": {
            "en": "The WHERE clause filters rows based on specified conditions.",
            "ru": "Выражение WHERE фильтрует строки по указанным условиям.",
            "ua": "Вираз WHERE фільтрує рядки за вказаними умовами.",
        },
    },
    {
        "id": "sql3",
        "topic": "sql",
        "difficulty": "hard",
        "type": "multiple_choice",
        "question": {
            "en": "What type of JOIN returns all rows from the left table and matched rows from the right?",
            "ru": "Какой тип JOIN возвращает все строки из левой таблицы и совпавшие из правой?",
            "ua": "Який тип JOIN повертає всі рядки з лівої таблиці та збіги з правої?",
        },
        "options": {
            "en": ["LEFT JOIN", "INNER JOIN", "CROSS JOIN", "RIGHT JOIN"],
            "ru": ["LEFT JOIN", "INNER JOIN", "CROSS JOIN", "RIGHT JOIN"],
            "ua": ["LEFT JOIN", "INNER JOIN", "CROSS JOIN", "RIGHT JOIN"],
        },
        "correct": 0,
        "explanation": {
            "en": "LEFT JOIN returns all rows from the left table, with NULLs for non-matching right rows.",
            "ru": "LEFT JOIN возвращает все строки из левой таблицы, NULL для несовпавших правых.",
            "ua": "LEFT JOIN повертає всі рядки з лівої таблиці, NULL для незбіжних правих.",
        },
    },
]
