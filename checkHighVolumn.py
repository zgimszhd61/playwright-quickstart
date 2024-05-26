def find_text_in_file(file_path, target_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if target_text in line:
                    print(line.strip().split("  --- ")[1])
                    # print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 使用示例
file_path = 'answerwithpaper.txt'  # 替换为你的文件路径
target_text = '万  '
find_text_in_file(file_path, target_text)
