import os

def convert_text_to_p_tags(input_file, output_file):
    """
    Reads a plain text file and wraps each paragraph in <p> tags for the newspaper app.
    """
    if not os.path.exists(input_file):
        # Create a dummy input file if it doesn't exist for demonstration
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write("这是第一段内容。\n\n这是第二段内容，段落之间有空行。")
        print(f"已为您创建示例 {input_file}，请修改内容后重新运行。")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        content = content.replace('\r\n', '\n')
        # Split by one or more newlines
        paragraphs = [p for p in content.split('\n') if p.strip()]

    html_output = []
    for p in paragraphs:
        clean_p = p.strip()
        if clean_p:
            # Indented to match the index.html structure
            html_output.append(f'                <p>{clean_p}</p>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_output))

    print(f"--- 转换成功 ---")
    print(f"请打开 {output_file} 复制内容，粘贴到 index.html 的 <div class=\"reader-content\"> 标签内。")

if __name__ == "__main__":
    convert_text_to_p_tags('story.txt', 'output.html')
