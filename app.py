def demonstrate_python_features(items=None, **options):
    """
    Демонстрационная функция, показывающая возможности Python:
    - Работа со списками
    - Обработка ошибок
    - Генераторы
    - Лямбда-функции
    """
    
    # Обработка входных данных
    if items is None:
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    operation = options.get('operation', 'filter')
    threshold = options.get('threshold', 5)
    verbose = options.get('verbose', True)
    
    if verbose:
        print(f"📊 Исходные данные: {items}")
        print(f"🔧 Операция: {operation}, порог: {threshold}")
    
    try:
        # Различные операции
        if operation == 'filter':
            # Фильтрация с помощью лямбды
            result = list(filter(lambda x: x > threshold, items))
            message = f"Элементы больше {threshold}"
            
        elif operation == 'map':
            # Преобразование с помощью лямбды
            result = list(map(lambda x: x * 2, items))
            message = f"Удвоенные элементы"  # noqa: F541
            
        elif operation == 'square':
            # Возведение в квадрат
            result = [x ** 2 for x in items]
            message = f"Квадраты элементов"  # noqa: F541
            
        elif operation == 'analyze':
            # Анализ данных
            result = {
                'sum': sum(items),
                'average': sum(items) / len(items),
                'min': min(items),
                'max': max(items),
                'count': len(items)
            }
            message = "Анализ данных"
            
        elif operation == 'chunks':
            # Разбиение на чанки (генератор)
            chunk_size = threshold
            result = [items[i:i+chunk_size] for i in range(0, len(items), chunk_size)]
            message = f"Разбито на части по {chunk_size} элементов"
            
        else:
            raise ValueError(f"Неизвестная операция: {operation}")
        
        if verbose:
            print(f"✅ {message}: {result}")
            print(f"📈 Тип результата: {type(result).__name__}")
        
        return result
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None

# Демонстрация работы функции
print("=" * 50)
print("1. Фильтрация")
demonstrate_python_features(operation='filter', threshold=5)

print("\n" + "=" * 50)
print("2. Удвоение")
demonstrate_python_features([1, 2, 3, 4, 5], operation='map')

print("\n" + "=" * 50)
print("3. Квадраты")
demonstrate_python_features(operation='square', threshold=3)

print("\n" + "=" * 50)
print("4. Анализ")
result = demonstrate_python_features([10, 20, 30, 40, 50], operation='analyze')

print("\n" + "=" * 50)
print("5. Разбиение на части")
demonstrate_python_features(list(range(1, 21)), operation='chunks', threshold=4)

print("\n" + "=" * 50)
print("6. С отключенным выводом")
demonstrate_python_features([1, 2, 3], operation='filter', threshold=2, verbose=False)

print("Очень интересно, пожалуй я ничего трогать небуду")